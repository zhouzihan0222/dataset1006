import os
import glob

def delete_files(directory, extensions):
    for ext in extensions:
        files = glob.glob(os.path.join(directory, f'*{ext}'))
        for file in files:
            os.remove(file)
            print(f"Deleted: {file}")

# 基础路径
base_path = '.'

# 处理 train1 到 train5
for i in range(1, 6):
    # 删除 train{i}/images 中的文件
    train_images_path = os.path.join(base_path, f'train{i}', 'images')
    print(train_images_path)
    delete_files(train_images_path, ['v.jpg', 'vh.jpg'])

    # 删除 train{i}/labels 中的文件
    train_labels_path = os.path.join(base_path, f'train{i}', 'labels')
    delete_files(train_labels_path, ['v.txt', 'vh.txt'])

# 处理 valid1 到 valid5
for i in range(1, 6):
    # 删除 valid{i}/images 中的文件
    valid_images_path = os.path.join(base_path, f'valid{i}', 'images')
    delete_files(valid_images_path, ['h.jpg', 'v.jpg', 'vh.jpg'])

    # 删除 valid{i}/labels 中的文件
    valid_labels_path = os.path.join(base_path, f'valid{i}', 'labels')
    delete_files(valid_labels_path, ['h.txt', 'v.txt', 'vh.txt'])

# 处理 test 目录
test_images_path = os.path.join(base_path, 'test', 'images')
delete_files(test_images_path, ['h.jpg', 'v.jpg', 'vh.jpg'])

test_labels_path = os.path.join(base_path, 'test', 'labels')
delete_files(test_labels_path, ['h.txt', 'v.txt', 'vh.txt'])

print("File deletion completed.")