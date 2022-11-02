--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Ср ноя 2 12:29:17 2022
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE texts;

-- Таблица: texts
CREATE TABLE texts (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT
);

INSERT INTO texts ( id, text ) VALUES ( 1, 'Университет Иннополис приглашает посетить Дни открытых дверей абитуриентов,\nувлечённых сферой ИТ, а также их родителей и педагогов.\nДля участия необходимо зарегистрироваться.' );
INSERT INTO texts ( id, text ) VALUES (2, 'когда увидишь мой смятый след,\nуслышишь выстрелы за спиной,\nпоймешь, что против меня весь свет,\nпоймешь, что мир на меня войной,\nоставь дела и запри в сундук,\nвели соседке кормить кота, рассеяв выдохом тишину, иди к знакомым тебе местам.');
INSERT INTO texts ( id, text ) VALUES (3, 'Отмщенье, государь, отмщенье!\nПаду к ногам твоим:\nБудь справедлив и накажи убийцу,\nЧтоб казнь его в позднейшие века\nТвой правый суд потомству возвестила,\nЧтоб видели злодеи в ней пример.');
INSERT INTO texts ( id, text ) VALUES (4, 'Если мотылек сядет на цветы,\nЗакачаются ли они?\nА он, соскучившись по мне,\nМой мотылек, мой кругляшок,\nМоя красивая птичка, мой соловей,\nЗапоет ли?\n');
INSERT INTO texts ( id, text ) VALUES (5, 'Сижу за решеткой в темнице сырой.\nВскормленный в неволе орел молодой,\nМой грустный товарищ, махая крылом,\nКровавую пищу клюет под окном,');
INSERT INTO texts ( id, text ) VALUES (6, 'Ну как же я забыл про тебя?\nТы ждёшь звонка день изо дня\nТвоя любовь не знает конца\nДо утра, до утра');
INSERT INTO texts ( id, text ) VALUES (7, 'Белая берёза\nПод моим окном\nПринакрылась снегом,\nТочно серебром.\n\nНа пушистых ветках\nСнежною каймой\nРаспустились кисти\nБелой бахромой.\n\nИ стоит берёза\nВ сонной тишине,\nИ горят снежинки\nВ золотом огне.');
INSERT INTO texts ( id, text ) VALUES (8, 'Жди меня, и я вернусь.\nТолько очень жди,\nЖди, когда наводят грусть\nЖелтые дожди,\nЖди, когда снега метут,\nЖди, когда жара,\nЖди, когда других не ждут,\nПозабыв вчера.\nЖди, когда из дальних мест\nПисем не придет,\nЖди, когда уж надоест\nВсем, кто вместе ждет.');
INSERT INTO texts ( id, text ) VALUES (9, 'Лучше пожалеть о том что сделал,\nчем о том, что не сделал.');
INSERT INTO texts ( id, text ) VALUES (10, 'О, как смеялись вы над нами,\nКак ненавидели вы нас\nЗа то, что тихими стихами\nМы громко обличили вас!\nНо мы — всё те же. Мы, поэты,\nЗа вас, о вас тоскуем вновь,\nХраня священную любовь,\nТвердя старинные обеты…');
INSERT INTO texts ( id, text ) VALUES (11, 'Ветер по морю гуляет\nИ кораблик подгоняет\nОн бежит себе в волнах\nНа поднятых парусах\nМимо острова крутого,\nМимо города большого;');
INSERT INTO texts ( id, text ) VALUES (12, 'Ночь, улица, фонарь, аптека,\nБессмысленный и тусклый свет.\nЖиви еще хоть четверть века —\nВсё будет так. Исхода нет.\nУмрешь — начнешь опять сначала\nИ повторится всё, как встарь:\nНочь, ледяная рябь канала,\nАптека, улица, фонарь.');
INSERT INTO texts ( id, text ) VALUES (13, 'Скажи-ка, дядя, ведь недаром\nМосква, спаленная пожаром,\nФранцузу отдана?\nВедь были ж схватки боевые,\nДа, говорят, еще какие!\nНедаром помнит вся Россия\nПро день Бородина!');
INSERT INTO texts ( id, text ) VALUES (14, 'Я считаю, что человек живет на планете, а не в государстве.');
INSERT INTO texts ( id, text ) VALUES (15, 'Я помню чудное мгновенье:\nПередо мной явилась ты,\nКак мимолетное виденье,\nКак гений чистой красоты.\n\nВ томленьях грусти безнадежной,\nВ тревогах шумной суеты,\nЗвучал мне долго голос нежный\nИ снились милые черты.');
INSERT INTO texts ( id, text ) VALUES (16, 'Разработка - это про деньги. Никому не нужны программы, которые стоят больше,\nчем бизнес может себе позволить. Даже если эта программа прекрасна.\nИ это главная причина избегать преждевременной оптимизации.');
INSERT INTO texts ( id, text ) VALUES (17, 'Ни одному пессимисту в истории не удалось раскрыть тайны звезд,\nдоплыть до неведомой земли или открыть новые\nгоризонты человеческого разума.');
INSERT INTO texts ( id, text ) VALUES (18, 'Больше всего работающего человека раздражает вид не работающего человека.');
INSERT INTO texts ( id, text ) VALUES (19, 'Надо любить жизнь больше, чем смысл жизни.');
INSERT INTO texts ( id, text ) VALUES (20, 'Я люблю людскую жизнь за её безграничные\nвозможности сделать её ярче');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;