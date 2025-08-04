# 🎯 Item Price Adjuster for Lineage 2 Offline (L2OFF)

**Effortlessly tweak your Lineage 2 Offline (L2OFF) item prices with precision and style!**

---

## 🚀 What is this?

**Item Price Adjuster** is a simple yet powerful Python tool designed specifically for **Lineage 2 Offline (L2OFF)** server admins and developers to modify `default_price` values in your game’s `itemdata.txt`. Whether you want to increase or decrease prices by a certain percentage for groups of items, this script handles it smoothly — even if your data is encoded in UTF-16LE BOM!

---

## 💡 Features

- 🔍 Parses your L2OFF `itemdata.txt` file (UTF-16LE BOM encoded) line-by-line  
- 📊 Applies price adjustments based on a clean, easy-to-edit XML config  
- ✅ Supports grouping multiple item IDs under one percentage change  
- 📝 Logs every change with clear, formatted info:  
  `ID 123456, original price: 1,000, new price: 1,050, percent change: +5%`  
- ⚠️ Warns if XML contains item IDs not found in your `itemdata.txt`  
- 🎯 Outputs a new `itemdata_new.txt` and detailed `log.info`  
- 🔄 Easy-to-run `.bat` file for Windows convenience

---

## 🛠️ How to use

1. **Prepare your files:**  
   - Put your `itemdata.txt` and the provided `price_changes.xml` (included in this project as a default template with example IDs and values) in the same folder as the script. The default `price_changes.xml` looks like this:

   ```xml
   <price_changes>
       <group percent="5"> <!-- Group of items whose default_price will be INCREASED by 5% -->
           <item id="111111111" />
       </group>
       <group percent="-10"> <!-- Group of items whose default_price will be DECREASED by 10% -->
           <item id="222222222" />
       </group>
   </price_changes>
   ```

2. **Edit `price_changes.xml`**  
   - Modify the example groups and item IDs inside `price_changes.xml` to fit your needs, adjusting percentages accordingly.

3. **Run the script:**  
   - Double-click `run.bat` (Windows) or run `python bin.py` manually.

4. **Check results:**  
   - `itemdata_new.txt` will contain updated prices  
   - `log.info` will show detailed logs of all changes and warnings

---

## 🎉 Why use this?

Forget tedious manual edits or error-prone scripts. This tool gives **Lineage 2 Offline (L2OFF)** server admins and modders a clean, auditable, and repeatable workflow for your item economy — perfect for smooth price tuning on your server.

---

## 📄 License

MIT License – feel free to modify and share!

---

## 🤝 Contributions?

Pull requests and ideas welcome! Let’s keep this tool evolving.

---

## 📬 Contact

Need help? Have a cool idea? Just ping me!

---

Enjoy your perfectly priced **Lineage 2 Offline (L2OFF)** server economy! 🎮💰
