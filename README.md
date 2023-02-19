<!-- Banner -->
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<h1 align="center"><b>TRUY VẤN THÔNG TIN ĐA PHƯƠNG TIỆN<br>(MULTIMEDIA INFORMATION RETRIEVAL)</b></h>

[![Status](https://img.shields.io/badge/status-working-brightgreen?style=flat-square)](https://github.com/pahopu/CS336_ImageSearch_Project2)
[![GitHub contributors](https://img.shields.io/github/contributors/pahopu/CS336_ImageSearch_Project2?style=flat-square)](https://github.com/pahopu/CS336_ImageSearch_Project2/graphs/contributors)
[![Status](https://img.shields.io/badge/language-python-green?style=flat-square)](https://github.com/pahopu/CS336_ImageSearch_Project2)

## BẢNG MỤC LỤC
* [Giới thiệu môn học](#giới-thiệu-môn-học)
* [Thông tin các thành viên](#thông-tin-về-các-thành-viên-nhóm)
* [Thông tin đồ án](#thông-tin-đồ-án)
* [Các bước cần thiết](#các-bước-cần-thiết)
* [Chuẩn bị dataset](#chuẩn-bị-dataset)

## GIỚI THIỆU MÔN HỌC
* **Tên môn học:** Truy vấn thông tin đa phương tiện - Multimedia Information Retrieval
* **Mã môn học:** CS336
* **Mã lớp:** CS336.N11.KHCL
* **Năm học:** HK1 (2022 - 2023)
* **Giảng viên:** PGS.TS. Ngô Đức Thành

## THÔNG TIN VỀ CÁC THÀNH VIÊN NHÓM

| STT    | MSSV          | Họ và Tên                |Vai trò    | Github                                          | Email                   |
| :----: |:-------------:| :-----------------------:|:---------:|:-----------------------------------------------:|:-------------------------:
| 1      | 20520278      | Phạm Hoàng Phúc          |Trưởng nhóm|[pahopu](https://github.com/pahopu)              |20521446@gm.uit.edu.vn   |
| 2      | 20520313      | Nguyễn Hồng Anh Thư      |Thành viên |[thuwpink](https://github.com/thuwpink)          |20520278@gm.uit.edu.vn   |
| 3      | 20521446      | Huỳnh Nguyễn Vân Khánh   |Thành viên |[hnvkhanh](https://github.com/hnvkhanh)          |20521663@gm.uit.edu.vn   |
| 4      | 20521546      | Lê Tấn Lộc               |Thành viên |[leetnlok](https://github.com/leetnlok)          |20521663@gm.uit.edu.vn   |

## THÔNG TIN ĐỒ ÁN
* **Tên đồ án:** Hệ thống truy vấn thông tin bằng hình ảnh - Content-Based Information Retrieval System
* **Ngôn ngữ lập trình:** Python, HTML, CSS, JavaScript
* **Input:** 1 bức ảnh (có thể crop)
* **Output:** 1 tập những bức ảnh được xem là liên quan đến bức ảnh đầu vào

## CÁC BƯỚC CẦN THIẾT
Sử dụng Git Bash để có thể khởi chạy project.

### 1. Clone project
Clone project repository bằng câu lệnh dưới đây.

```bash
git clone https://github.com/pahopu/CS336_ImageSearch_Project2.git
```

### 2. Cài đặt thư viện
Cài đặt các thư viện cần thiết cho project với câu lệnh dưới đây.

```bash
cd CS336_ImageSearch_Project2
python3 -m pip install -r requirements.txt
```

## CHUẨN BỊ DATASET
* Ở đây, chúng ta có thể sử dụng 2 bộ dataset là Oxford Buildings và Paris Buildings để thực hiện truy vấn.
* Đường dẫn tải dataset và groundtruth sẽ được gắn ở phần chi tiết bên dưới.

### Tải dataset
Trước hết, chúng ta phải điền [form](https://docs.google.com/forms/d/e/1FAIpQLSeIWlksO7O2TxeftwR8vzEZ9ivPj29TuB_Zv_9glda9a1_rLQ/viewform) để được cung cấp **tên đăng nhập** và **mật khẩu** để tải các bộ dataset nói trên.

#### 1. Oxford Buildings
* Ta tải các ảnh trong dataset Oxford Buildings tại [đây](https://thor.robots.ox.ac.uk/datasets/oxford-buildings/oxbuild_images-v1.tgz).
* Sau đó, giải nén và đặt nó vào trong thư mục ```datasets/oxbuild/images```
* Cấu trúc như sau:
```
CS336_ImageSearch_Project2
            └───datasets
                   └───oxbuild
                          └───images
                                │all_souls_000000.jpg
                                │all_souls_000001.jpg
                                │all_souls_000002.jpg
                                |all_souls_000003.jpg
                                |...
```

* Ta cũng cần phải tải các file groundtruth tại [đây](https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/gt_files_170407.tgz).
* Giải nén và đặt nó trong thư mục ```datasets/oxbuild/groundtruth```
* Cấu trúc như sau:
```
CS336_ImageSearch_Project2
            └───datasets
                   └───oxbuild
                          └───groundtruth
                                   │all_souls_1_good.txt
                                   │all_souls_1_junk.txt
                                   │all_souls_1_ok.txt
                                   │all_souls_1_query.txt
                                   |...
```

#### 2. Paris Buildings
* Đối với bộ dataset này, nó được chia ra làm 2 phần. Ta có thể tải tại đây:
   * [paris_part1](https://thor.robots.ox.ac.uk/datasets/paris-buildings/paris_1-v1.tgz)
   * [paris_part2](https://thor.robots.ox.ac.uk/datasets/paris-buildings/paris_2-v1.tgz)
* Sau đó, giải nén cả 2 và đặt chúng cùng vào trong thư mục ```datasets/paris/images```
* Cấu trúc như sau:
```
CS336_ImageSearch_Project2
            └───datasets
                   └───paris
                         └───images
                               │paris_defense_000000.jpg
                               │paris_defense_000002.jpg
                               │paris_defense_000004.jpg
                               |paris_defense_000005.jpg
                               |...
```

* Ta cũng cần phải tải các file groundtruth tại [đây](https://www.robots.ox.ac.uk/~vgg/data/parisbuildings/paris_120310.tgz).
* Giải nén và đặt nó trong thư mục ```datasets/paris/groundtruth```
* Cấu trúc như sau:
```
CS336_ImageSearch_Project2
            └───datasets
                   └───paris
                         └───groundtruth
                                  │defense_1_good.txt
                                  │defense_1_junk.txt
                                  │defense_1_ok.txt
                                  │defense_1_query.txt
                                  |...
```
