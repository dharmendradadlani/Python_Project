from pdf2image import convert_from_path

pdf_path = r"d:\Python-Files\Test.pdf"
tiff_path = r"d:\Python-Files\output.tiff"

images = convert_from_path(
    pdf_path,
    dpi=300,
    poppler_path=r"C:\poppler\Library\bin"  # or wherever pdfinfo.exe is
)

images[0].save(
    tiff_path,
    save_all=True,
    append_images=images[1:],
    compression="tiff_deflate"
)

print("✅ PDF converted to TIFF:", tiff_path)