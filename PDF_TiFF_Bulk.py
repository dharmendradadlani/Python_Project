from pdf2image import convert_from_path
import os

# Folders
input_folder = r"C:\Users\Dharmendra Dadlani\Desktop\Contracts\PDF"
output_folder = r"C:\Users\Dharmendra Dadlani\Desktop\Contracts\TiFF"
poppler_path = r"C:\poppler\Library\bin"  # Change to where you extracted Poppler

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop over all PDFs in the input folder
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_folder, file_name)
        print(f"Converting: {pdf_path}")

        # Convert all pages of the PDF to images
        images = convert_from_path(pdf_path, dpi=300, fmt='tiff', poppler_path=poppler_path)

        # Output TIFF file path (multi-page)
        output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.tiff")

        # Save as a single multi-page TIFF
        images[0].save(
            output_path,
            save_all=True,
            append_images=images[1:],
            compression="tiff_deflate"
        )

        print(f"✅ Saved multi-page TIFF: {output_path}")

print("🎉 All conversions complete.")