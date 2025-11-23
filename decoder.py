import halcon as ha

def setup_barcode_model():
    """Setup 1D barcode model with parameters"""
    handle = ha.create_bar_code_model([], [])
    
    # Set barcode parameters
    ha.set_bar_code_param(handle, 'num_scanlines', 150)
    ha.set_bar_code_param(handle, 'barcode_width_min', 10)
    ha.set_bar_code_param(handle, 'barcode_width_max', 300)
    ha.set_bar_code_param(handle, 'meas_thresh', 0.001)
    ha.set_bar_code_param(handle, 'meas_thresh_abs', 5)
    ha.set_bar_code_param(handle, 'orientation', -90)
    ha.set_bar_code_param(handle, 'majority_voting', 'true')
    ha.set_bar_code_param(handle, 'element_size_max', 64)
    ha.set_bar_code_param(handle, 'merge_scanlines', 'true')
    
    return handle

def setup_datamatrix_model():
    """Setup Data Matrix ECC 200 model"""
    handle = ha.create_data_code_2d_model('Data Matrix ECC 200', [], [])
    
    # Set parameters
    ha.set_data_code_2d_param(handle, 'default_parameters', 'maximum_recognition')
    ha.set_data_code_2d_param(handle, 'polarity', 'any')
    ha.set_data_code_2d_param(handle, 'module_size_min', 1)
    ha.set_data_code_2d_param(handle, 'module_size_max', 100)
    ha.set_data_code_2d_param(handle, 'module_gap_max', 'big')
    ha.set_data_code_2d_param(handle, 'finder_pattern_tolerance', 'any')
    ha.set_data_code_2d_param(handle, 'alternating_pattern_tolerance', 'high')
    ha.set_data_code_2d_param(handle, 'module_grid', 'any')
    ha.set_data_code_2d_param(handle, 'small_modules_robustness', 'high')
    ha.set_data_code_2d_param(handle, 'strict_model', 'no')
    ha.set_data_code_2d_param(handle, 'strict_quiet_zone', 'no')
    ha.set_data_code_2d_param(handle, 'candidate_selection', 'extensive')
    
    return handle

def setup_qrcode_model():
    """Setup QR Code model"""
    handle = ha.create_data_code_2d_model('QR Code', [], [])
    
    # Set parameters
    ha.set_data_code_2d_param(handle, 'default_parameters', 'maximum_recognition')
    ha.set_data_code_2d_param(handle, 'polarity', 'any')
    ha.set_data_code_2d_param(handle, 'model_type', 'any')
    ha.set_data_code_2d_param(handle, 'version_min', 1)
    ha.set_data_code_2d_param(handle, 'version_max', 40)
    ha.set_data_code_2d_param(handle, 'module_size_min', 1)
    ha.set_data_code_2d_param(handle, 'module_size_max', 100)
    ha.set_data_code_2d_param(handle, 'module_gap_max', 'big')
    ha.set_data_code_2d_param(handle, 'contrast_tolerance', 'any')
    ha.set_data_code_2d_param(handle, 'position_pattern_min', 2)
    ha.set_data_code_2d_param(handle, 'small_modules_robustness', 'high')
    ha.set_data_code_2d_param(handle, 'strict_model', 'no')
    ha.set_data_code_2d_param(handle, 'candidate_selection', 'all')
    
    return handle

def setup_gs1_datamatrix_model():
    """Setup GS1 DataMatrix model"""
    handle = ha.create_data_code_2d_model('GS1 DataMatrix', [], [])
    
    # Set parameters
    ha.set_data_code_2d_param(handle, 'default_parameters', 'maximum_recognition')
    ha.set_data_code_2d_param(handle, 'polarity', 'any')
    ha.set_data_code_2d_param(handle, 'module_size_min', 1)
    ha.set_data_code_2d_param(handle, 'module_size_max', 100)
    ha.set_data_code_2d_param(handle, 'module_gap_max', 'big')
    ha.set_data_code_2d_param(handle, 'finder_pattern_tolerance', 'any')
    ha.set_data_code_2d_param(handle, 'alternating_pattern_tolerance', 'high')
    ha.set_data_code_2d_param(handle, 'module_grid', 'any')
    ha.set_data_code_2d_param(handle, 'small_modules_robustness', 'high')
    ha.set_data_code_2d_param(handle, 'strict_model', 'no')
    ha.set_data_code_2d_param(handle, 'strict_quiet_zone', 'no')
    ha.set_data_code_2d_param(handle, 'candidate_selection', 'extensive')
    
    return handle

def decode_barcodes(image, barcode_handle):
    """Decode 1D barcodes from image"""
    results = {}
    
    # Code 39
    try:
        _, decoded = ha.find_bar_code(image, barcode_handle, 'Code 39')
        results['Code 39'] = decoded
        print(f"  Code 39: Found {len(decoded)} codes")
    except Exception as e:
        results['Code 39'] = []
        print(f"  Code 39: No codes found - {str(e)}")
    
    # Code 93
    try:
        _, decoded = ha.find_bar_code(image, barcode_handle, 'Code 93')
        results['Code 93'] = decoded
        print(f"  Code 93: Found {len(decoded)} codes")
    except Exception as e:
        results['Code 93'] = []
        print(f"  Code 93: No codes found - {str(e)}")
    
    # Code 128
    try:
        _, decoded = ha.find_bar_code(image, barcode_handle, 'Code 128')
        results['Code 128'] = decoded
        print(f"  Code 128: Found {len(decoded)} codes")
    except Exception as e:
        results['Code 128'] = []
        print(f"  Code 128: No codes found - {str(e)}")
    
    return results

def decode_2d_codes(image, datamatrix_handle, qrcode_handle, gs1_handle):
    """Decode 2D codes from image"""
    results = {}
    
    # Data Matrix ECC 200
    try:
        _, _, decoded = ha.find_data_code_2d(image, datamatrix_handle, [], [])
        results['Data Matrix ECC 200'] = decoded
        print(f"  Data Matrix: Found {len(decoded)} codes")
    except Exception as e:
        results['Data Matrix ECC 200'] = []
        print(f"  Data Matrix: No codes found - {str(e)}")
    
    # QR Code
    try:
        _, _, decoded = ha.find_data_code_2d(image, qrcode_handle, [], [])
        results['QR Code'] = decoded
        print(f"  QR Code: Found {len(decoded)} codes")
    except Exception as e:
        results['QR Code'] = []
        print(f"  QR Code: No codes found - {str(e)}")
    
    # GS1 DataMatrix
    try:
        _, _, decoded = ha.find_data_code_2d(image, gs1_handle, [], [])
        results['GS1 DataMatrix'] = decoded
        print(f"  GS1 DataMatrix: Found {len(decoded)} codes")
    except Exception as e:
        results['GS1 DataMatrix'] = []
        print(f"  GS1 DataMatrix: No codes found - {str(e)}")
    
    return results

def print_detailed_results(barcode_results, code2d_results):
    """Print detailed decoded results"""
    print("\n" + "="*50)
    print("DETAILED DECODING RESULTS")
    print("="*50)
    
    print("\n1D Barcode Results:")
    found_1d = False
    for code_type, decoded in barcode_results.items():
        if decoded:
            found_1d = True
            print(f"  {code_type}:")
            for i, data in enumerate(decoded, 1):
                print(f"    {i}: {data}")
    
    if not found_1d:
        print("  No 1D barcodes found")
    
    print("\n2D Code Results:")
    found_2d = False
    for code_type, decoded in code2d_results.items():
        if decoded:
            found_2d = True
            print(f"  {code_type}:")
            for i, data in enumerate(decoded, 1):
                print(f"    {i}: {data}")
    
    if not found_2d:
        print("  No 2D codes found")

def process_single_image(image):
    """Process a single image and return results"""
    # Initialize models
    barcode_handle = setup_barcode_model()
    datamatrix_handle = setup_datamatrix_model()
    qrcode_handle = setup_qrcode_model()
    gs1_handle = setup_gs1_datamatrix_model()
    
    try:
        print("\nStarting barcode and 2D code detection...")
        
        # Decode barcodes and 2D codes
        barcode_results = decode_barcodes(image, barcode_handle)
        code2d_results = decode_2d_codes(image, datamatrix_handle, qrcode_handle, gs1_handle)
        
        # Print detailed results
        print_detailed_results(barcode_results, code2d_results)
        
        return barcode_results, code2d_results
        
    except Exception as e:
        print(f"Error during processing: {str(e)}")
        return {}, {}
        
    finally:
        # Cleanup
        cleanup_models(barcode_handle, datamatrix_handle, qrcode_handle, gs1_handle)

def cleanup_models(barcode_handle, datamatrix_handle, qrcode_handle, gs1_handle):
    """Clean up all Halcon models"""
    try:
        ha.clear_bar_code_model(barcode_handle)
    except:
        pass
    
    try:
        ha.clear_data_code_2d_model(datamatrix_handle)
    except:
        pass
    
    try:
        ha.clear_data_code_2d_model(qrcode_handle)
    except:
        pass
    
    try:
        ha.clear_data_code_2d_model(gs1_handle)
    except:
        pass

def process_image_file(image_path):
    """Process image from file path"""
    try:
        print(f"Loading image: {image_path}")
        image = ha.read_image(image_path)
        return process_single_image(image)
    except Exception as e:
        print(f"Error loading image: {str(e)}")
        return {}, {}

def main():
    """Main function - process a single image"""
    # You can change this path to your image
    image_path = 'path/to/your/image.jpg'
    
    print("Barcode and 2D Code Decoder")
    print("=" * 40)
    
    process_image_file(image_path)

if __name__ == "__main__":
    main()
