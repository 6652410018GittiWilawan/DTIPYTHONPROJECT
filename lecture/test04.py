stu_id = input('ป้อน STUDENT ID: ')
stuName = input('ป้อน STUDENT NAME: ')
stu_brith_year = input('ป้อน STUDENT Birth Year: ')
print('---------------------')
print(f'ยินดีต้อนรับ {stu_id} {stuName} สู่ SAU')
print(f'คุณเกิดปี {stu_brith_year} แปลว่าคุณอายุ {2023 - int(stu_brith_year)} ปี')
print("ใช้ , ----------------------------------")
print('ยินดีต้อนรับ ',stu_id,stuName, 'สู่ SAU')
print('คุณเกิดปี' ,stu_brith_year, 'แปลว่าคุณอายุ',2023 - int(stu_brith_year),'ปี')
print("ใช้ + ----------------------------------")
print('ยินดีต้อนรับ '+stu_id+''+stuName+' สู่ SAU' )
print('คุณเกิดปี' +stu_brith_year+'' 'แปลว่าคุณอายุ'+str(2023 - int(stu_brith_year))+'ปี')
print("ใช้เมธอด format ----------------------------------")
print('ยินดีต้อนรับ {} {} สู่ SAU'.format(stu_id,stuName))
print('คุณเกิดปี {} แปลว่าคุณอายุ {} ปี'.format(stu_brith_year, 2023 - int(stu_brith_year)))