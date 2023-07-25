# blacklist-scripts

---

* [Russian Text](#Russian)
* [English Text](#English)

---

# <a name="Russian">Russian README.</a>

Черный и белый списки Fail2Ban.

![Linux](./image/linux.svg "Linux") &nbsp;![Python-3](./image/python-3-icon.svg "Python-3")

## <a name="Oglavlenie">Оглавление</a>

1. [Установка.](#Setup)
2. [Обзор утилиты](#ShowUtilites)
3. [Об авторе.](#About)

---

## <a name="Setup">1. Установка.</a>

Для установки программы воспользуйтесь следующей командой:

```bash
cd ~
git clone https://github.com/maximalisimus/blacklist-scripts.git
cd blacklist-scripts
sudo make DESTDIR=/ install
```

Для контроля установки в **Makefile** предусмотрены некоторые переменные, которыми вы могли бы воспользоваться.

* **DESTDIR** - местоположение в системе, директория. По умолчанию задаётся корень системы.
* **POSTDIR** - установочная директория перед папкой с программой, т.е. родительская директория программы. По умолчанию равна **&laquo;etc&raquo;**. <u>Обязательно должна присутствовать. Не допускается устанавливать пустой.</u>
* **INSTALLDIR** - удалённый корень будущей системы. Используется для создания правильной символической ссылки в **&laquo;/usr/bin/&raquo;**.
* **TARGET** - название директории с самой программой.

Остальные переменные не рекомендуется менять каким-либо образом.

Если вам нужно изменить установочную директорию в системе - воспользуйтесь переменными *DESTDIR*, *POSTDIR* и *TARGET*. 

Например, я хочу установить программу в **&laquo;/opt/blacklist/&raquo;**.

```bash
sudo make DESTDIR=/ POSTDIR=opt TARGET=blacklist install
```

Если вам нужны фильтры для **NGINX** - установите их отдельно:

```bash
sudo make DESTDIR=/ install-filter
```

В данных предустановленных фильтрах для **Fail2ban** содержаться регулярные выражения для отдельного отслеживания всех ошибок самого *Nginx* как такового из файла **&laquo;/var/log/nginx/error.log&raquo;** или похожем, а также отслеживания статусных состояний &laquo;4xx ошибка в запросе&raquo; и &laquo;5xx ошибка сервера&raquo; из файла **&laquo;/var/log/nginx/access.log&raquo;** или похожем пользовательском.

Для установки действий **action**-ов для **Fail2ban**-а воспользуйтесь командой их установки:

```bash
sudo make DESTDIR=/ install-action
```

Также у черного списка имеются предустановленные **Jail**-правила, которые вы также можете установить, при таковой необходимости:

```bash
sudo make DESTDIR=/ install-jail
```

Если же вам нужны все предустановленные функции для **Fail2ban**-а (экшены, фильтры, правила), вы можете установить их одной командой:

```bash
sudo make DESTDIR=/ install-all
```

Или одновременной установки и самой программы и всех функций для **Fail2ban**-а (экшенов, фильтров, правил):

```bash
sudo make DESTDIR=/ all
```

Для удаления программы и / или дополнительных функций для **Fail2ban**-а в **Makefile** имеются соответствующие команды:

* uninstall - удалить пграмму,
* uninstall-action - удалить предустановленные экшены,
* uninstall-filter - удалить предустановленные фильтры,
* uninstall-jail - удалить предустановленные правила,
* uninstall-all - удалить все предустановленные функции **Fail2ban**-а.
* clear - удалить и саму программу и все предустановленные функции **Fail2ban**-а.

---

[К оглавлению](#Oglavlenie)

---

## <a name="ShowUtilites">2. Обзор утилиты.</a>

Помощь программы выглядит следующим образом (Параметры и ключи. Русифицикация.):

```bash
$ ./py-blacklist.py -h

usage: py-blacklist.py [-h] [-v] [-info] [-c COUNT] [-q QUANTITY]
                       [-wd WORKDIR] [-b BLACKLIST] [-w WHITELIST] [-personal]
                       [-e] [-run] [-fine] [-ipv6] [-nft]
                       [-nftproto {ip,ip6,inet}] [-table TABLE] [-chain CHAIN]
                       [-newtable] [-newchain] [-Deltable] [-Delchain]
                       [-cleartable] [-clearchain] [-con CONSOLE] [-cmd] [-sd]
                       [-logfile LOGFILE] [-nolog] [-limit] [-viewlog]
                       [-resetlog]
                       {systemd,service,black,white} ...

Черный и белый списки Fail2Ban в Python.

options:
  -h, --help            показать справку и выйти
  -v, --version         Версия.
  -info, --info         Информация об авторе.

Управление:
  Команды управления.

  {systemd,service,black,white}
                        команды помощи.
    systemd             Управление Systemd.
    service             Управление программой.
    black               Управление черными списками.
    white               Управление белыми списками.

Параметры:
  Настройки количества запретов.

  -c COUNT, --count COUNT
                        Количество блокировок, после которых адрес
                        добавляется в таблицы {IP,IP6,NF}TABLES (по умолчанию 0).
  -q QUANTITY, --quantity QUANTITY
                        Количество сохраняемых блокировок ip-адресов (по умолчанию
                        0).

Файлы:
  Работа с файлами.

  -wd WORKDIR, --workdir WORKDIR
                        Рабочая директория.
  -b BLACKLIST, --blacklist BLACKLIST
                        Входной файл черного списка.
  -w WHITELIST, --whitelist WHITELIST
                        Входной файл белого списка.

NFTABLES:
  Конфигурационные таблицы NFTABLES.

  -personal, --personal
                        Персональные настройки таблиц NFTABLES, 
                        независимо от введёных данных.
  -e, -exit, --exit     Завершение создание таблиц/цепочек в NFTABLES.
  -run, --run           Полный запуск таблиц NFTABLES из всех настроек.
                        Используйте осторожно!
  -fine, --fine         Полная очистка таблиц NFTABLES от всех настроек.
                        Используйте осторожно!
  -ipv6, --ipv6         Принудительный выбор протокола IPV6.
  -nft, --nftables      Выбер фреймворка NFTABLES (по умолчанию IP(6)TABLES).
  -nftproto {ip,ip6,inet}, --nftproto {ip,ip6,inet}
                        Выберите протокол NFTABLES, перед правилами 
                        (Автоматически для ipv4 "ip" или 
                        при ключе -ipv6 - "ip6").
  -table TABLE, --table TABLE
                        Выберите таблицу для NFTABLES (по умолчанию "filter").
  -chain CHAIN, --chain CHAIN
                        Выбор цепочки правил (по умолчанию "INPUT").
  -newtable, --newtable
                        Добавить новую таблицу в NFTABLES.
                        Используйте осторожно!
  -newchain, --newchain
                        Добавить новую цепочку в NFTABLES
                        Используйте осторожно!
  -Deltable, --Deltable
                        Удалить таблицы NFTABLES. 
                        Используйте осторожно!
  -Delchain, --Delchain
                        Удалить цепочку NFTABLES. 
                        Используйте осторожно!
  -cleartable, --cleartable
                        Очистить таблицу NFTABLES. 
                        Используйте осторожно!
  -clearchain, --clearchain
                        Очистить цепочку NFTABLES. 
                        Используйте осторожно!

Настройки:
  Конфигурация.

  -con CONSOLE, --console CONSOLE
                        Ввод имени консоли (по умолчанию "sh").
  -cmd, --cmd           Посмотреть команды и выйти без выполнения.
  -sd, --showdir        Показать рабочий каталог.
  -logfile LOGFILE, --logfile LOGFILE
                        Файл журнала.
  -nolog, --nolog       Не записывать события в журнал.
  -limit, --limit       Ограничьте размер файла журнала. Каждый день 
                        журнал будет стираться.
  -viewlog, --viewlog   Посмотреть журнал событий.
  -resetlog, --resetlog
                        Сброс файла журнала.
```

При этом, если не вводить никаких ключей пользователь автоматически перенаправляется на страницу помощи, причём в любом меню и под-меню.

По ключам **NFTABLES** необходимо сделать пояснение.

При введении ключа *-nft* вы начинаете работу с **NFTABLES**. Без него вы будете работать с **IPTABLES** и **IP6TABLES**.

При выборе ключа *-personal* и ключа *-nft* программа выбирет <u>предопределённые</u> таблицы и цепочки во фрейворке **NFTABLES**. При этом не имеет значения, что вы будете пытаться вводить соответствующим ключам. Все значения будут переопределены програмно.

Тоже самое касается ключей *-run* и *-fine*. Первый определяется вместо использования 2 ключей *-newtable* и *-newchain*. Ну т.е. когда используются оба последних ключа, проще указать один *-run* вместо 2 ключей. Для *-fine* соответственно будет аналогичное обращение ко всем функциям очистки и удаления таблиц и цепочек после завершения работы приложения.

Также такое обращение по указанным выше ключам будет автоматически применено в меню управления сервисом Systemd, т.е. учтено при создание сервиса и таймера.

Или вы можете использовать любые другие ключи без *-personal*, *-run* и *-fine* раздельно и не зависимо, например для мониторинга или создания определенных таблиц или цепочек.

При удалении и очистки таблиц и цепочек есть определённые ограничения, связанные со стандартными таблицами и цепочками системы в пакетах со слоем совместимости между **NFTABLES** и **IP(6)TABLES** Netfilter-а. Поэтому не удивляйтесь если таблица или цепочка не была удалена из системы или не была очищена. Это сделано только для безопасности. 

Но, есть одна маленькая хитрость. Вы можете с помощью ключей **-cmd**, **-fine** и **-e** посмотреть на все команды завершения, и использовать их на свой страх и риск. Или соответствующими ключами изменить наименование таблиц и / или цепочек и снова указать **-cmd**, **-fine** и **-e**, чтобы посмотреть на все команды завершения с изменёнными значениями и также использовать их на свой страх и риск.

Ещё одно пояснение касается выбора протокола **-ipv6**. Вообще при вводе ip-адресов протокол определяется автоматически и также автоматически корректируется. Однако, протокол можно принудительно поменять.

Рассмотрим меню Systemd.

```bash
$ ./py-blacklist.py systemd

Файл «blacklist@.service» и «blacklist@.timer» не найден!
Пожалуйста, введите «-create», чтобы создать системные файлы, перед тем как обращаться к функциям Systemd!

usage: py-blacklist.py systemd [-h] [-create] [-delete] [-status] [-istimer]
                               [-isservice] [-enable] [-disable] [-start]
                               [-stop] [-reload] [-starttimer] [-stoptimer]

options:
  -h, --help            Показать справку и выйти
  -create, --create     Создать «blacklist@.service» and «blacklist@.timer».
  -delete, --delete     Удалить «blacklist@.service» и «blacklist@.timer».
  -status, --status     Состояние «blacklist@.service».
  -istimer, --istimer   Проверить включен и запущен ли «blacklist@.timer».
  -isservice, --isservice
                        Проверить включен и запущен ли «blacklist@.service».
  -enable, --enable     Включить «blacklist@.timer».
  -disable, --disable   Выключить «blacklist@.timer».
  -start, --start       Запустить «blacklist@.service».
  -stop, --stop         Остановить «blacklist@.service».
  -reload, --reload     Перезапустить «blacklist@.service».
  -starttimer, --starttimer
                        Запустить «blacklist@.timer».
  -stoptimer, --stoptimer
                        Остановить «blacklist@.timer».
```
 
 Рассмотрим меню Service.
 
 ```bash
 $ ./py-blacklist.py service
 
 usage: py-blacklist.py service [-h] [-start] [-stop] [-nostop] [-reload]
                               [-show] [-link] [-unlink] [-name NAME]

Опции:
  -h, --help            Показать справку и выйти
  -start, --start       Запустить черный список.
  -stop, --stop         Остановить черный список.
  -nostop, --nostop     Остановка работы с черным списком без очистки
                        {IP,IP6,NF}TABLES.
  -reload, --reload     Перезапустить черный список.
  -show, --show         Показать состояние таблиц NETFILTER.
  -link, --link         Символическая ссылка на программу в «/usr/bin/».
  -unlink, --unlink     Удалить ссылку на программу в «/usr/bin/».
  -name NAME, --name NAME
                        Наименование символьной ссылки в «/usr/bin/». 
                        (по умолчанию "blacklist").
 ```
 
 По умолчанию в прогрумму встроен метод работы из любого каталога. Если вы не устанавливали программу с помощью **Makefile**, вам может потребоваться функция создания символьной ссылки на скрипт в **«/usr/bin/»** и также безопасного удаления этой символьной ссылки. В качестве бонуса можете даже изменить наименование символьной ссылки, чтобы вам было удобно обращаться к скрипту без указания полного пути и его наименования.

При запуске, остановке или перезапуске программы обработаны будут оба списка - и черный и белый. При этом белый список будет внесён в **Netfilter** с обязательными разрешающими правилами, а черный с запрещающими. 

Программу можно запускать многократно. В отличии от ручного управления с помощью команд через терминал, здесь имеется защита от повторного добавления ip-адреса и в таблицы **NetFilter**-а и в сами файлы списков.

Рассмотрим меню black.

```bash
 $ ./py-blacklist.py black

usage: py-blacklist.py black [-h] [-ban] [-unban] [-a] [-d] [-s] [-j] [-save]
                             [-o OUTPUT] [-empty] [-ip IP [IP ...]]
                             [-m MASK [MASK ...]]

Опции:
  -h, --help            Показать справку и выйти
  -ban, --ban           Заблокировать ip-адреса в {IP,IP6,NF}TABLES.
  -unban, --unban       Разблокировать ip-адреса в {IP,IP6,NF}TABLES.
  -a, --add             Добавить в черный список.
  -d, --delete          Удалить из черного списка.
  -s, --show            Посмотреть черный список.
  -j, --json            JSON формат просмотра.
  -save, --save         Сохранить.
  -o OUTPUT, --output OUTPUT
                        Выходной файл черного списка.
  -empty, --empty       Очистить черный список. Используйте осторожно!

Addressing:
  IP address management.

  -ip IP [IP ...], --ip IP [IP ...]
                        IP адреса.
  -m MASK [MASK ...], --mask MASK [MASK ...]
                        Маски сетей.
```

Рассмотрим меню white.

```bash
 $ ./py-blacklist.py white

usage: py-blacklist.py white [-h] [-ban] [-unban] [-a] [-d] [-s] [-j] [-save]
                             [-o OUTPUT] [-empty] [-ip IP [IP ...]]
                             [-m MASK [MASK ...]]

Опции:
  -h, --help            Показать справку и выйти
  -ban, --ban           Разрешить ip-адреса в {IP,IP6,NF}TABLES.
  -unban, --unban       Удалить разрешения из {IP,IP6,NF}TABLES.
  -a, --add             Добавить в белый список.
  -d, --delete          Удалить из белого списка.
  -s, --show            Посмотреть белый список.
  -j, --json            JSON формат просмотра.
  -save, --save         Сохранить.
  -o OUTPUT, --output OUTPUT
                        Выходной файл белого списка.
  -empty, --empty       Очистить белый список. Используйте осторожно!

Addressing:
  IP address management.

  -ip IP [IP ...], --ip IP [IP ...]
                        IP адреса.
  -m MASK [MASK ...], --mask MASK [MASK ...]
                        Маски сетей.
```

---

## <a name="about">3. Обо Мне</a>

<details>
	<summary>Подробнее ...</summary>
	
Автор данной разработки **Shadow**: [maximalisimus](https://github.com/maximalisimus).

Имя автора: **maximalisimus**: [maximalis171091@yandex.ru](mailto:maximalis171091@yandex.ru).

Дата создания: **25.07.2023**

</details>

---

[К оглавлению](#Oglavlenie)

---

# <a name="English">English README.</a>

Fail2Ban black and white lists.

![Linux](./image/linux.svg "Linux") &nbsp;![Python-3](./image/python-3-icon.svg "Python-3")

## <a name="EngOglavlenie">Table of contents</a>

1. [Installation.](#SetupEng)
2. [Utility Overview.](#ShowUtilitesEng)
3. [About the author.](#AboutEng)

---

## <a name="SetupEng">1. Installation</a>

To install the program, use the following command:

```bash
cd ~
git clone https://github.com/maximalisimus/blacklist-scripts.git
cd blacklist-scripts
sudo make DESTDIR=/ install
```

To control the installation, there are some variables in the **Makefile** that you could use.

* **DESTDIR** - location in the system, directory. By default, the root of the system is set.
* **POSTDIR** - the installation directory in front of the program folder, i.e. the parent directory of the program. By default, it is equal to **&laquo;etc&raquo;**. <u>Must be present. It is not allowed to set an empty one.</u>
* **INSTALLDIR** - the remote root of the future system. Used to create the correct symbolic link in **/usr/bin/**.
* **TARGET** - the name of the directory with the program itself.

It is not recommended to change the other variables in any way.

If you need to change the installation directory in the system, use the variables *DESTDIR*, *POSTDIR* and *TARGET*. 

For example, I want to install a program in **/opt/blacklist/**.

```bash
sudo make DESTDIR=/ POSTDIR=opt TARGET=blacklist install
```

If you need filters for **NGINX** - install them separately:

```bash
sudo make DESTDIR=/ install-filter
```

These preset filters for **Fail2ban** contain regular expressions for separate tracking of all errors of *Nginx itself* as such from the file **/var/log/nginx/error.log** or similar, as well as tracking the status states of "4xx error in the request" and "5xx server error" from the file **/var/log/nginx/access.log** or similar custom.

To install the **action**s for **Fail2ban**, use the command to install them:

```bash
sudo make DESTDIR=/ install-action
```

The blacklist also has pre-installed **Jail**-rules that you can also set, if necessary:

```bash
sudo make DESTDIR=/ install-jail
```

If you need all the preset functions for **Fail2ban** (actions, filters, rules), you can install them with one command:

```bash
sudo make DESTDIR=/ install-all
```

Or simultaneous installation of the program itself and all functions for **Fail2ban**-a (actions, filters, rules):

```bash
sudo make DESTDIR=/ all
```

To remove the program and/or additional functions for **Fail2ban**-and in **Makefile** there are appropriate commands:

* uninstall - remove the program,
* uninstall-action - remove pre-installed actions,
* uninstall-filter - remove pre-installed filters,
* uninstall-tool - remove preset rules,
* uninstall-all - remove all pre-installed functions **Fail2ban**-a.
* clear - delete both the program itself and all pre-installed functions **Fail2ban**-a.

---

[To the table of contents](#EngOglavlenie)

---

## <a name="ShowUtilitesEng">2. Utility Overview.</a>



---

[To the table of contents](#EngOglavlenie)

---

## <a name="AboutEng">3. About the author.</a>


<details>
	<summary>More detailed ...</summary>

The author of this development **Shadow**: [maximalisimus](https://github.com/maximalisimus).

Author's name: **maximalisimus**: [maximalis171091@yandex.ru](mailto:maximalis171091@yandex.ru).

Date of creation: **25.07.2023**

</details>

---

[To the table of contents](#EngOglavlenie)

---
