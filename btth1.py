saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
          """)

    choice = input('Mời bạn chọn chức năng (1-7): ')

    while not choice.isdigit():
        print('Lựa chọn không hợp lệ, vui lòng nhập lại')
        choice = input('Mời bạn chọn chức năng (1-7): ')

    choice = int(choice)

    match choice:

        # Chức năng 1
        case 1:

            if len(saving_accounts) == 0:
                print('Danh sách sổ tiết kiệm hiện đang trống')

            else:
                print('Danh sách sổ tiết kiệm:')

                stt = 1

                for item in saving_accounts:
                    print(
                        f"{stt}. Mã sổ: {item['account_id']} | "
                        f"Khách hàng: {item['customer_name']} | "
                        f"Số tiền gửi: {item['balance']} | "
                        f"Kỳ hạn: {item['term_months']} tháng | "
                        f"Lãi suất: {item['interest_rate']}%/năm | "
                        f"Trạng thái: {item['status']}"
                    )

                    stt += 1

        # Chức năng 2
        case 2:

            account_id = input(
                'Nhập mã sổ tiết kiệm: '
            ).strip().upper()

            is_exist = False

            for item in saving_accounts:
                if item["account_id"] == account_id:
                    is_exist = True
                    break

            if is_exist:
                print('Mã sổ tiết kiệm đã tồn tại!')
                continue

            customer_name = input(
                'Nhập tên khách hàng: '
            ).strip()

            if customer_name == "":
                print('Tên khách hàng không được để trống')
                continue

            balance = input(
                'Nhập số tiền gửi: '
            ).strip()

            term_months = input(
                'Nhập kỳ hạn gửi theo tháng: '
            ).strip()

            if (not balance.isdigit()
                or not term_months.isdigit()
                or int(balance) <= 0
                or int(term_months) <= 0):

                print('Số tiền gửi hoặc kỳ hạn không hợp lệ')
                continue

            interest_rate = input(
                'Nhập lãi suất năm: '
            ).strip()

            if not interest_rate.replace(".", "", 1).isdigit():
                print('Lãi suất không hợp lệ!')
                continue

            interest_rate = float(interest_rate)

            if interest_rate <= 0:
                print('Lãi suất không hợp lệ!')
                continue

            saving_accounts.append(
                {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": int(balance),
                    "term_months": int(term_months),
                    "interest_rate": interest_rate,
                    "status": "active"
                }
            )

            print('Mở sổ tiết kiệm thành công!')

        # Chức năng 3
        case 3:

            account_id = input(
                'Nhập mã sổ tiết kiệm cần cập nhật: '
            ).strip().upper()

            found = False

            for item in saving_accounts:

                if item["account_id"] == account_id:

                    found = True

                    if item["status"] == "closed":
                        print(
                            'Không thể cập nhật sổ tiết kiệm đã tất toán!'
                        )
                        break

                    customer_name = input(
                        'Nhập tên khách hàng mới: '
                    ).strip()

                    if customer_name == "":
                        print(
                            'Tên khách hàng không được để trống'
                        )
                        break

                    balance = input(
                        'Nhập số tiền gửi mới: '
                    ).strip()

                    term_months = input(
                        'Nhập kỳ hạn mới theo tháng: '
                    ).strip()

                    if (not balance.isdigit()
                        or not term_months.isdigit()
                        or int(balance) <= 0
                        or int(term_months) <= 0):

                        print(
                            'Số tiền gửi hoặc kỳ hạn không hợp lệ'
                        )
                        break

                    interest_rate = input(
                        'Nhập lãi suất năm mới: '
                    ).strip()

                    if not interest_rate.replace(".", "", 1).isdigit():
                        print('Lãi suất không hợp lệ!')
                        break

                    interest_rate = float(interest_rate)

                    if interest_rate <= 0:
                        print('Lãi suất không hợp lệ!')
                        break

                    item["customer_name"] = customer_name
                    item["balance"] = int(balance)
                    item["term_months"] = int(term_months)
                    item["interest_rate"] = interest_rate

                    print('Cập nhật thành công!')
                    break

            if not found:
                print('Không tìm thấy mã sổ tiết kiệm')

        # Chức năng 4
        case 4:

            account_id = input(
                'Nhập mã sổ tiết kiệm cần tất toán/xóa: '
            ).strip().upper()

            found = False

            for item in saving_accounts:

                if item["account_id"] == account_id:

                    item["status"] = "closed"

                    found = True

                    print('Tất toán sổ tiết kiệm thành công!')

                    break

            if not found:
                print('Không tìm thấy mã sổ tiết kiệm')

        # Chức năng 5
        case 5:

            account_id = input(
                'Nhập mã sổ tiết kiệm cần tính lãi: '
            ).strip().upper()

            found = False

            for item in saving_accounts:

                if item["account_id"] == account_id:

                    found = True

                    if item["status"] == "closed":
                        print(
                            'Không thể thao tác với sổ tiết kiệm đã tất toán'
                        )
                        break

                    interest = (
                        item["balance"]
                        * item["interest_rate"]
                        / 100
                        * item["term_months"]
                        / 12
                    )

                    total = item["balance"] + interest

                    print(
                        f"Tiền lãi dự kiến: {interest:,.0f} VNĐ"
                    )

                    print(
                        f"Tổng tiền nhận khi đến hạn: {total:,.0f} VNĐ"
                    )

                    break

            if not found:
                print('Không tìm thấy mã sổ tiết kiệm')

        # Chức năng 6
        case 6:

            account_id = input(
                'Nhập mã sổ tiết kiệm cần kiểm tra: '
            ).strip().upper()

            found = False

            for item in saving_accounts:

                if item["account_id"] == account_id:

                    found = True

                    if item["status"] == "closed":
                        print(
                            'Không thể thao tác với sổ tiết kiệm đã tất toán'
                        )
                        break

                    actual_months = input(
                        'Nhập số tháng thực gửi: '
                    ).strip()

                    if (not actual_months.isdigit()
                        or int(actual_months) <= 0):

                        print(
                            'Số tháng thực gửi không hợp lệ!'
                        )

                        break

                    actual_months = int(actual_months)

                    if actual_months < item["term_months"]:

                        applied_rate = 0.5

                        print('Khách hàng rút trước hạn')

                    else:

                        applied_rate = item["interest_rate"]

                        print(
                            'Khách hàng đủ điều kiện hưởng lãi đúng hạn'
                        )

                    interest = (
                        item["balance"]
                        * applied_rate
                        / 100
                        * actual_months
                        / 12
                    )

                    total = item["balance"] + interest

                    print(
                        f'Lãi suất áp dụng: {applied_rate}%/năm'
                    )

                    print(
                        f'Tiền lãi thực nhận: {interest:,.0f} VNĐ'
                    )

                    print(
                        f'Tổng tiền thực nhận: {total:,.0f} VNĐ'
                    )

                    break

            if not found:
                print('Không tìm thấy mã sổ tiết kiệm')

        # Chức năng 7
        case 7:
            print('Thoát chương trình!')
            break

        case _:
            print('Lựa chọn không hợp lệ, vui lòng nhập lại')
```
