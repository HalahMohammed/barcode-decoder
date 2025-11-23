import halcon as ha
import os
from typing import Dict, List, Tuple, Optional

class BarcodeDecoder:
    """
    Main class for decoding 1D barcodes and 2D codes using Halcon.
    """
    
    def __init__(self, enable_1d=True, enable_2d=True):
        self.enable_1d = enable_1d
        self.enable_2d = enable_2d
        self.models = {}
        self._initialize_models()
    
    def _initialize_models(self):
        """Initialize all code recognition models"""
        if self.enable_1d:
            self.models['barcode'] = self._setup_barcode_model()
        
        if self.enable_2d:
            self.models['datamatrix'] = self._setup_datamatrix_model()
            self.models['qrcode'] = self._setup_qrcode_model()
            self.models['gs1_datamatrix'] = self._setup_gs1_datamatrix_model()
    
    def _setup_barcode_model(self):
        """Setup 1D barcode model with optimized parameters"""
        handle = ha.create_bar_code_model([], [])
        
        # Configuration parameters
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
    
    def _setup_datamatrix_model(self):
        """Setup Data Matrix ECC 200 model"""
        handle = ha.create_data_code_2d_model('Data Matrix ECC 200', [], [])
        self._configure_datamatrix_params(handle)
        return handle
    
    def _setup_qrcode_model(self):
        """Setup QR Code model"""
        handle = ha.create_data_code_2d_model('QR Code', [], [])
        self._configure_qrcode_params(handle)
        return handle
    
    def _setup_gs1_datamatrix_model(self):
        """Setup GS1 DataMatrix model"""
        handle = ha.create_data_code_2d_model('GS1 DataMatrix', [], [])
        self._configure_datamatrix_params(handle)
        return handle
    
    def _configure_datamatrix_params(self, handle):
        """Common configuration for DataMatrix models"""
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
    
    def _configure_qrcode_params(self, handle):
        """Configuration for QR Code model"""
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
    
    def decode_image(self, image_path: str) -> Dict:
        """
        Decode all supported codes from an image.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Dictionary containing decoded results for all code types
        """
        try:
            image = ha.read_image(image_path)
            results = {}
            
            if self.enable_1d:
                results['1d_barcodes'] = self._decode_1d_barcodes(image)
            
            if self.enable_2d:
                results['2d_codes'] = self._decode_2d_codes(image)
            
            return results
            
        except Exception as e:
            return {'error': f"Failed to process image: {str(e)}"}
    
    def _decode_1d_barcodes(self, image) -> Dict:
        """Decode 1D barcodes from image"""
        results = {}
        barcode_handle = self.models['barcode']
        
        # Supported 1D barcode types
        barcode_types = ['Code 39', 'Code 93', 'Code 128']
        
        for barcode_type in barcode_types:
            try:
                _, decoded = ha.find_bar_code(image, barcode_handle, barcode_type)
                results[barcode_type] = decoded
            except Exception as e:
                results[barcode_type] = [f"Error: {str(e)}"]
        
        return results
    
    def _decode_2d_codes(self, image) -> Dict:
        """Decode 2D codes from image"""
        results = {}
        
        # Data Matrix ECC 200
        try:
            _, _, decoded = ha.find_data_code_2d(image, self.models['datamatrix'], [], [])
            results['Data Matrix ECC 200'] = decoded
        except Exception as e:
            results['Data Matrix ECC 200'] = [f"Error: {str(e)}"]
        
        # QR Code
        try:
            _, _, decoded = ha.find_data_code_2d(image, self.models['qrcode'], [], [])
            results['QR Code'] = decoded
        except Exception as e:
            results['QR Code'] = [f"Error: {str(e)}"]
        
        # GS1 DataMatrix
        try:
            _, _, decoded = ha.find_data_code_2d(image, self.models['gs1_datamatrix'], [], [])
            results['GS1 DataMatrix'] = decoded
        except Exception as e:
            results['GS1 DataMatrix'] = [f"Error: {str(e)}"]
        
        return results
    
    def process_directory(self, directory_path: str) -> Dict[str, Dict]:
        """
        Process all images in a directory.
        
        Args:
            directory_path: Path to directory containing images
            
        Returns:
            Dictionary with filenames as keys and decoding results as values
        """
        results = {}
        
        try:
            # Get supported image files
            image_files = ha.list_files(directory_path, ['files', 'follow_links', 'recursive'])
            image_files = ha.tuple_regexp_select(image_files, [
                '\\.(tif|tiff|gif|bmp|jpg|jpeg|jp2|png|pcx|pgm|ppm|pbm|xwd|ima|hobj)$', 
                'ignore_case'
            ])
            
            for image_file in image_files:
                print(f"Processing: {image_file}")
                results[image_file] = self.decode_image(image_file)
                
        except Exception as e:
            print(f"Error processing directory: {str(e)}")
        
        return results
    
    def print_results(self, results: Dict):
        """Print formatted decoding results"""
        if '1d_barcodes' in results:
            print("\n1D Barcode Results:")
            for code_type, decoded in results['1d_barcodes'].items():
                print(f"  {code_type}:")
                for i, data in enumerate(decoded, 1):
                    print(f"    {i}: {data}")
        
        if '2d_codes' in results:
            print("\n2D Code Results:")
            for code_type, decoded in results['2d_codes'].items():
                print(f"  {code_type}:")
                for i, data in enumerate(decoded, 1):
                    print(f"    {i}: {data}")
    
    def cleanup(self):
        """Clean up Halcon models"""
        for model_name, handle in self.models.items():
            try:
                if 'barcode' in model_name:
                    ha.clear_bar_code_model(handle)
                else:
                    ha.clear_data_code_2d_model(handle)
            except Exception as e:
                print(f"Warning: Failed to clean up {model_name}: {str(e)}")

def main():
    """Example main function"""
    decoder = BarcodeDecoder()
    
    try:
        # Process directory of images
        image_dir = 'C:/Users/halah/Downloads/codes/bar_code/Images QR/images QR'
        results = decoder.process_directory(image_dir)
        
        # Print results
        for filename, result in results.items():
            print(f"\n{'='*50}")
            print(f"Results for: {filename}")
            print(f"{'='*50}")
            decoder.print_results(result)
            
    finally:
        decoder.cleanup()

if __name__ == "__main__":
    main()
