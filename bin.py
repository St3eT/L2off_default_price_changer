import xml.etree.ElementTree as ET

def load_price_changes(xml_path):
    price_changes = {}
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for group in root.findall('group'):
        percent_str = group.get('percent')
        if percent_str is None:
            continue
        try:
            percent = float(percent_str)
        except ValueError:
            continue
        for item_elem in group.findall('item'):
            item_id = item_elem.get('id')
            if item_id:
                price_changes[item_id] = percent
    return price_changes

def adjust_prices(itemdata_path, price_changes, output_path, log_path):
    with open(itemdata_path, 'r', encoding='utf-16le') as f:
        lines = f.readlines()

    log_lines = []
    found_ids = set()
    changed_count = 0

    for i, line in enumerate(lines):
        # Look for "item_begin" and "item_end" in line to process items individually
        if 'item_begin' in line and 'item_end' in line:
            # Try to find the ID
            parts = line.split('\t')
            item_id = None
            for part in parts:
                if part.strip().isdigit():
                    item_id = part.strip()
                    break
            if item_id is None:
                log_lines.append(f"ERROR: No item ID found on line {i+1}")
                continue

            found_ids.add(item_id)
            if item_id in price_changes:
                percent = price_changes[item_id]

                # Find and replace default_price=...
                import re
                m = re.search(r'default_price=(\d+)', line)
                if m:
                    original_price = int(m.group(1))
                    new_price = int(original_price * (1 + percent / 100))

                    # Replace in line
                    new_line = re.sub(r'default_price=\d+', f'default_price={new_price}', line)

                    lines[i] = new_line
                    changed_count += 1

                    sign = '+' if percent > 0 else ''
                    log_lines.append(f"ID {item_id}, original price: {original_price:,}, new price: {new_price:,}, percent change: {sign}{percent}%")
                else:
                    log_lines.append(f"ERROR: default_price not found for item ID {item_id} on line {i+1}")

    # Check for IDs in XML that were not found in itemdata
    for xml_id in price_changes.keys():
        if xml_id not in found_ids:
            log_lines.append(f"WARNING: Item ID {xml_id} from XML not found in itemdata.txt")

    with open(output_path, 'w', encoding='utf-16le') as f:
        f.writelines(lines)

    with open(log_path, 'w', encoding='utf-8') as f:
        for l in log_lines:
            f.write(l + '\n')

    print(f"Processed {len(price_changes)} items, changed {changed_count} items.")

if __name__ == "__main__":
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))
    itemdata_file = os.path.join(base_dir, 'itemdata.txt')
    price_changes_file = os.path.join(base_dir, 'price_changes.xml')
    output_file = os.path.join(base_dir, 'itemdata_new.txt')
    log_file = os.path.join(base_dir, 'log.log')

    price_changes = load_price_changes(price_changes_file)
    adjust_prices(itemdata_file, price_changes, output_file, log_file)
