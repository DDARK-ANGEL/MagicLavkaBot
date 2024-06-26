import random
import sqlite3 as sq

def randomMagic():
    var = ['огонь', 'вода', 'земля', 'молния', 'воздух', 'тьма', 'свет']
    return random.choice(var)


def refPay(id, sum):
    conn = sq.connect('main_db.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT ref FROM referal WHERE user_id = {id}')
    inviter_id = cursor.fetchone()[0]

    if not inviter_id == 'NULL':
        cursor.execute(f'SELECT balance FROM users WHERE user_id = {inviter_id}')
        inviter_bal = cursor.fetchone()[0]

        cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (inviter_bal + sum, inviter_id))
    conn.commit()
    conn.close()

    return inviter_id


def randomItem(id):
    conn = sq.connect('main_db.db')
    cursor = conn.cursor()

    cursor.execute('''
               CREATE TABLE IF NOT EXISTS inventory (
                   id INTEGER,
                   item TEXT,
                   count INTEGER
                   )''')
    conn.commit()

    items = {'bronze': 6000, 'silver': 3000, 'gold': 500, 'platinum': 300, 'diamond': 184, 'money': 16}

    total_weight = sum(items.values())
    random_value = random.randint(1, total_weight)

    if random_value <= 16:
        res = 'money'
    elif random_value <= 184 and random_value > 16:
        res = 'diamond'
    elif random_value <= 300 and random_value > 184:
        res = 'platinum'
    elif random_value <= 500 and random_value > 300:
        res = 'gold'
    elif random_value <= 3000 and random_value > 500:
        res = 'silver'
    elif random_value <= 6000 and random_value > 3000:
        res = 'bronze'
    

    bronze = ['носки бронзовые', 'рубашка бронзовая']
    silver = ['шапка серебряная', 'тапок серебряный']
    gold = ['золотая корона', 'золотой сапог']
    platinum = ['платина 1', 'платина 2']
    diamond = ['алмаз 1', 'алмаз 2']
    money = ['0.1 ton']

    sha = ['bronze', 'silver', 'gold', 'platinum', 'diamond', 'money']
    
    if res == 'bronze':
        random_item = random.choice(bronze)
    if res == 'silver':
        random_item = random.choice(silver)
    if res == 'gold':
        random_item = random.choice(gold)
    if res == 'platinum':
        random_item = random.choice(platinum)
    if res == 'diamond':
        random_item = random.choice(diamond)
    if res == 'money':
        random_item = random.choice(money)

    cursor.execute(f'SELECT count FROM inventory WHERE id = ? AND item = ?', (id, random_item))
    kol = cursor.fetchone()

    if kol is None:
        cursor.execute('INSERT INTO inventory VALUES (?, ?, 1)', (id, random_item))
        conn.commit()
    else:
        cursor.execute(f'UPDATE inventory SET count = ? WHERE id = ? AND item = ?', (kol[0] + 1, id, random_item))
        conn.commit()
    conn.close()

    return random_item