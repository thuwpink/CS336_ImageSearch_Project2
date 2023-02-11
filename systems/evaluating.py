from image_search_system import ImageSearch_System as ISS

if __name__ == '__main__':
    # Name of dataset and method
    dataset_name = 'oxbuild'
    method = 'VGG16'

    # Create Image Search System object
    IS = ISS(dataset_name, method)

    # Evaluating system
    IS.evaluating()