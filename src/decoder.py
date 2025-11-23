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
    except Exception as e:
        results['Code 39'] = [f"Error: {str(e)}"]
    
    # Code 93
    try:
        _, decoded = ha.find_bar_code(image, barcode_handle, 'Code 93')
        results['Code 93'] = decoded
    except Exception as e:
        results['Code 93'] = [f"Error: {str(e)}"]
    
    # Code 128
    try:
        _, decoded = ha.find_bar_code(image, barcode_handle, 'Code 128')
        results['Code 128'] = decoded
    except Exception as e:
        results['Code 128'] = [f"Error: {str(e)}"]
    
    return results

def decode_2d_codes(image, datamatrix_handle, qrcode_handle, gs1_handle):
    """Decode 2D codes from image"""
    results = {}
    
    # Data Matrix ECC 200
    try:
        _, _, decoded = ha.find_data_code_2d(image, datamatrix_handle, [], [])
        results['Data Matrix ECC 200'] = decoded
    except Exception as e:
        results['Data Matrix ECC 200'] = [f"Error: {str(e)}"]
    
    # QR Code
    try:
        _, _, decoded = ha.find_data_code_2d(image, qrcode_handle, [], [])
        results['QR Code'] = decoded
    except Exception as e:
        results['QR Code'] = [f"Error: {str(e)}"]
    
    # GS1 DataMatrix
    try:
        _, _, decoded = ha.find_data_code_2d(image, gs1_handle, [], [])
        results['GS1 DataMatrix'] = decoded
    except Exception as e:
        results['GS1 DataMatrix'] = [f"Error: {str(e)}"]
    
    return results

def print_results(barcode_results, code2d_results, filename=None):
    """Print decoded results"""
    if filename:
        print(f"\n{'='*60}")
        print(f"RESULTS FOR: {filename}")
        print(f"{'='*60}")
    
    print("\n1D Barcode Results:")
    for code_type, decoded in barcode_results.items():
        print(f"  {code_type}:")
        if decoded:
            for i, data in enumerate(decoded, 1):
                print(f"    {i}: {data}")
        else:
            print("    No codes found")
    
    print("\n2D Code Results:")
    for code_type, decoded in code2d_results.items():
        print(f"  {code_type}:")
        if decoded:
            for i, data in enumerate(decoded, 1):
                print(f"    {i}: {data}")
        else:
            print("    No codes found")

def print_processing_summary(results_summary):
    """Print summary of all processed images"""
    print("\n" + "="*60)
    print("PROCESSING SUMMARY")
    print("="*60)
    
    total_images = len(results_summary)
    total_1d_codes = 0
    total_2d_codes = 0
    
    for filename, (barcode_results, code2d_results) in results_summary.items():
        print(f"\n{filename}:")
        
        # Count 1D barcodes
        for code_type, decoded in barcode_results.items():
            if decoded and not any(str(d).startswith('Error:') for d in decoded):
                count = len(decoded)
                total_1d_codes += count
                print(f"  {code_type}: {count} code(s)")
        
        # Count 2D codes
        for code_type, decoded in code2d_results.items():
            if decoded and not any(str(d).startswith('Error:') for d in decoded):
                count = len(decoded)
                total_2d_codes += count
                print(f"  {code_type}: {count} code(s)")
    
    print("\n" + "="*60)
    print(f"Total Images Processed: {total_images}")
    print(f"Total 1D Barcodes Found: {total_1d_codes}")
    print(f"Total 2D Codes Found: {total_2d_codes}")
    print("="*60)

def cleanup_models(barcode_handle, datamatrix_handle, qrcode_handle, gs1_handle):
    """Clean up all Halcon models"""
    try:
        ha.clear_bar_code_model(barcode_handle)
    except Exception as e:
        print(f"Warning: Failed to clean up barcode model: {str(e)}")
    
    try:
        ha.clear_data_code_2d_model(datamatrix_handle)
    except Exception as e:
        print(f"Warning: Failed to clean up datamatrix model: {str(e)}")
    
    try:
        ha.clear_data_code_2d_model(qrcode_handle)
    except Exception as e:
        print(f"Warning: Failed to clean up QR code model: {str(e)}")
    
    try:
        ha.clear_data_code_2d_model(gs1_handle)
    except Exception as e:
        print(f"Warning: Failed to clean up GS1 model: {str(e)}")

def process_single_image(image_path):
    """Process a single image and print results"""
    # Initialize models
    barcode_handle = setup_barcode_model()
    datamatrix_handle = setup_datamatrix_model()
    qrcode_handle = setup_qrcode_model()
    gs1_handle = setup_gs1_datamatrix_model()
    
    try:
        # Read and process image
        image = ha.read_image(image_path)
        print(f"Processing: {image_path}")
        
        # Decode barcodes and 2D codes
        barcode_results = decode_barcodes(image, barcode_handle)
        code2d_results = decode_2d_codes(image, datamatrix_handle, qrcode_handle, gs1_handle)
        
        # Print results
        print_results(barcode_results, code2d_results, image_path)
        
        return barcode_results, code2d_results
        
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")
        return None, None
        
    finally:
        # Cleanup
        cleanup_models(barcode_handle, datamatrix_handle, qrcode_handle, gs1_handle)

def process_image_directory(directory_path):
    """Process all images in a directory"""
    # Initialize models (reused for all images)
    barcode_handle = setup_barcode_model()
    datamatrix_handle = setup_datamatrix_model()
    qrcode_handle = setup_qrcode_model()
    gs1_handle = setup_gs1_datamatrix_model()
    
    results_summary = {}
    
    try:
        # Get supported image files
        image_files = ha.list_files(directory_path, ['files', 'follow_links', 'recursive'])
        image_files = ha.tuple_regexp_select(image_files, [
            '\\.(tif|tiff|gif|bmp|jpg|jpeg|jp2|png|pcx|pgm|ppm|pbm|xwd|ima|hobj)$', 
            'ignore_case'
        ])
        
        # Process each image
        for image_file in image_files:
            try:
                image = ha.read_image(image_file)
                print(f"\nProcessing: {image_file}")
                
                # Decode barcodes and 2D codes
                barcode_results = decode_barcodes(image, barcode_handle)
                code2d_results = decode_2d_codes(image, datamatrix_handle, qrcode_handle, gs1_handle)
                
                # Store results
                results_summary[image_file] = (barcode_results, code2d_results)
                
                # Print results for this image
                print_results(barcode_results, code2d_results, image_file)
                
            except Exception as e:
                print(f"Error processing {image_file}: {str(e)}")
                results_summary[image_file] = ({'Error': [str(e)]}, {'Error': [str(e)]})
        
        # Print summary
        print_processing_summary(results_summary)
        return results_summary
        
    except Exception as e:
        print(f"Error processing directory: {str(e)}")
        return {}
        
    finally:
        # Cleanup
        cleanup_models(barcode_handle, datamatrix_handle, qrcode_handle, gs1_handle)

def main():
    """Main decoding function - exactly as in your original code"""
    # Initialize models
    barcode_handle = setup_barcode_model()
    datamatrix_handle = setup_datamatrix_model()
    qrcode_handle = setup_qrcode_model()
    gs1_handle = setup_gs1_datamatrix_model()
    
    # Get image files
    image_files = ha.list_files('C:/Users/halah/Downloads/codes/bar_code/Images QR/images QR', 
                              ['files', 'follow_links', 'recursive'])
    image_files = ha.tuple_regexp_select(image_files, 
                                       ['\\.(tif|tiff|gif|bmp|jpg|jpeg|jp2|png|pcx|pgm|ppm|pbm|xwd|ima|hobj)$', 
                                        'ignore_case'])
    
    # Process all images
    for image_file in image_files:
        try:
            image = ha.read_image(image_file)
            print(f"\nProcessing: {image_file}")
            
            # Decode barcodes and 2D codes
            barcode_results = decode_barcodes(image, barcode_handle)
            code2d_results = decode_2d_codes(image, datamatrix_handle, qrcode_handle, gs1_handle)
            
            # Print results
            print_results(barcode_results, code2d_results)
            
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")
    
    # Cleanup
    cleanup_models(barcode_handle, datamatrix_handle, qrcode_handle, gs1_handle)

if __name__ == "__main__":
    main()
