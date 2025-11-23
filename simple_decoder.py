import halcon as ha

def setup_models():
    """Setup all models in one function"""
    # Barcode model
    barcode_handle = ha.create_bar_code_model([], [])
    ha.set_bar_code_param(barcode_handle, 'num_scanlines', 150)
    ha.set_bar_code_param(barcode_handle, 'barcode_width_min', 10)
    ha.set_bar_code_param(barcode_handle, 'barcode_width_max', 300)
    
    # DataMatrix model
    datamatrix_handle = ha.create_data_code_2d_model('Data Matrix ECC 200', [], [])
    ha.set_data_code_2d_param(datamatrix_handle, 'default_parameters', 'maximum_recognition')
    
    # QR Code model
    qrcode_handle = ha.create_data_code_2d_model('QR Code', [], [])
    ha.set_data_code_2d_param(qrcode_handle, 'default_parameters', 'maximum_recognition')
    
    return barcode_handle, datamatrix_handle, qrcode_handle

def cleanup_models(barcode_handle, datamatrix_handle, qrcode_handle):
    """Cleanup models"""
    ha.clear_bar_code_model(barcode_handle)
    ha.clear_data_code_2d_model(datamatrix_handle)
    ha.clear_data_code_2d_model(qrcode_handle)

def decode_single_image(image_path):
    """Simple function to decode a single image"""
    try:
        # Read image
        image = ha.read_image(image_path)
        print(f"Processing: {image_path}")
        
        # Setup models
        barcode_handle, datamatrix_handle, qrcode_handle = setup_models()
        
        # Decode 1D barcodes
        print("\n1D Barcodes:")
        for barcode_type in ['Code 39', 'Code 93', 'Code 128']:
            try:
                _, decoded = ha.find_bar_code(image, barcode_handle, barcode_type)
                if decoded:
                    print(f"  {barcode_type}: {decoded}")
            except:
                print(f"  {barcode_type}: None")
        
        # Decode 2D codes
        print("\n2D Codes:")
        try:
            _, _, datamatrix_decoded = ha.find_data_code_2d(image, datamatrix_handle, [], [])
            if datamatrix_decoded:
                print(f"  Data Matrix: {datamatrix_decoded}")
        except:
            print("  Data Matrix: None")
        
        try:
            _, _, qrcode_decoded = ha.find_data_code_2d(image, qrcode_handle, [], [])
            if qrcode_decoded:
                print(f"  QR Code: {qrcode_decoded}")
        except:
            print("  QR Code: None")
        
        # Cleanup
        cleanup_models(barcode_handle, datamatrix_handle, qrcode_handle)
        
    except Exception as e:
        print(f"Error: {str(e)}")

# Usage example
if __name__ == "__main__":
    # Change this to your image path
    image_path = "path/to/your/image.jpg"
    decode_single_image(image_path)
