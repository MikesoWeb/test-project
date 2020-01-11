mport time

name = 'Маш'
name2 = 'Саш'
fin = name
with open("the_beautiful_garden.txt", "r+") as file:
        data = file.readlines()
            for i in data:
                        if fin in i:
                                        print('Поиск начался....')
                                                    time.sleep(1)
                                                                print("Совпадений найдено", i.count(fin))
                                                                            print('Обработка данных...')
                                                                                        fin_2 = name2
                                                                                                    x = i.replace(fin, fin_2)
                                                                                                                time.sleep(0.3)
                                                                                                                            print(x)

                                                                                                                                        file.writelines(x)
                                                                                                                                                elif fin not in i:
                                                                                                                                                                print('Пусто')
                                                                                                                                                                            file.write(i)


                                                                                                                                                                                        time.sleep(1)
                                                                                                                                                                                                    print('Программа завершена')

