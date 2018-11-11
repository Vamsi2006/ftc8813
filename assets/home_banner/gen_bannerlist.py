# Requires Python 3
# Use this script to generate the list of banner images
# (pages/includes/banner_images.json) so that the webpage knows which images are
# available.
import glob

def main():
    with open('../../pages/includes/banner_images.json', 'w') as f:
        f.write('[\n')
        print('[')
        for file in glob.glob('*.jpg'):
            f.write('  "assets/home_banner/' + file + '",\n')
            print('  "assets/home_banner/' + file + '",')
        f.write(']\n')
        print(']')

main()
