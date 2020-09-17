import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# print(current_dir)

# current_dir = '/home/nikita/ML/project/FineTuning-YOLOv3-Custom/darknet/data/vehicles'
# g_colab_full_path ='/FineTuning-YOLOv3-Custom/darknet/data/vehicles'
current_dir = './darknet/data/vehicles'
g_colab_full_path ='/FineTuning-YOLOv3-Custom/darknet/data/vehicles'
print(current_dir)

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('vehicles-train.txt', 'w')
file_test = open('vehicles-test.txt', 'w')
counter = 1
index_test = round(100 / percentage_test)
#Google Colab
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1
