from app import app, db, Mess, Hostel

# ------------------ SEED MESS ------------------
def seed_mess():
    messes = [
        {
            "name": "Sanjog Pure Veg Mess",
            "description": "Affordable pure vegetarian mess near VIT Bibwewadi.",
            "images": "sanjog_menu_.jpg,sanjog_inside_.jpg",
            "address": "Bibwewadi, Pune (near VIT)",
            "google_map_link": "https://www.google.com/maps?q=Hotel+Sanjog+Bibwewadi+Pune&output=embed",
            "contact": "9422854285"
        },
        {
            "name": "Rasmadhuri Pure Veg Mess",
            "description": "Home-style pure veg meals, known for fresh thali and variety.",
            "images": "rasmadhuri_inside_.jpg,rasmadhuri_menu_.jpg",
            "address": "Bibwewadi, Pune (near VIT)",
            "google_map_link": "https://www.google.com/maps?q=Rasamadhuri+Canning+and+Foods+Bibwewadi+Pune&output=embed",
            "contact": "Not Available"
        },
        {
            "name": "Ruchira Pure Veg Mess",
            "description": "Known for simple thali, fresh vegetables, and hygienic cooking.",
            "images": "ruchira_inside_.jpg,ruchira_menu_.jpg",
            "address": "Bibwewadi, Pune (near VIT)",
            "google_map_link": "https://www.google.com/maps?q=Ruchira+Poli+Bhaji+Centre+Bibwewadi+Pune&output=embed",
            "contact": "9527680036"
        },
        {
            "name": "VIT College Canteen (Fruit Centre)",
            "description": (
                "VIT College Fruit Canteen, popularly known as the Fruit Centre, is located "
                "inside the VIT Bibwewadi College campus near 'SHARAD ARENA(Auditorium)'. "
                "It serves fresh fruit juices, milkshakes, snacks, chapati-bhaji "
                "and light meals at student-friendly prices."
            ),
            "images": "vit_fruit_canteen_menu.jpg,vit_fruit_canteen_outside.jpg",
            "address": "VIT Bibwewadi College Campus, Pune",
            "google_map_link": "https://www.google.com/maps?q=VIT+College+Canteen+Bibwewadi+Pune&output=embed",
            "contact": "Available at counter"
        },
        {
            "name": "VIT Main Canteen (Katel Caterers)",
            "description": (
                "VIT Main Canteen, operated by Katel Caterers, is located inside the "
                "VIT Bibwewadi College campus. It is the primary canteen serving a wide "
                "variety of food options including snacks, South Indian dishes, parathas, "
                "rice thalis, Chinese items, sandwiches, juices, and milkshakes. "
                "It is a popular daily dining spot for students due to affordable pricing "
                "and large menu variety."
            ),
            "images": "vit_canteen_menu1.jpg,vit_canteen_menu2.jpg,vit_canteen_outside.jpg",
            "address": "VIT Bibwewadi College Campus, Pune",
            "google_map_link": "https://www.google.com/maps?q=VIT+College+Canteen+Bibwewadi+Pune&output=embed",
            "contact": "Available at counter"
        }
    ]

    for data in messes:
        existing = Mess.query.filter_by(name=data["name"]).first()
        if existing:
            existing.description = data["description"]
            existing.images = data["images"]
            existing.address = data["address"]
            existing.google_map_link = data["google_map_link"]
            existing.contact = data["contact"]
        else:
            db.session.add(Mess(**data))

    db.session.commit()
    print("✅ Mess data inserted/updated")


# ------------------ SEED GIRLS HOSTELS ------------------
def seed_girls_hostels():
    hostels = [
        {
            "name": "Purandar Girls Hostel",
            "category": "girls",
            "description":
                "Purandar Girls Hostel is a well-maintained residential hostel for female students. "
                "It offers clean rooms, individual beds, cupboards, study space, and a secure environment.",
            "images": "purandar_room.jpg,purandar_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=Purandhar+Hostel+Kondhwa+Budruk+Pune&output=embed",
            "contact": "8483812848"
        },
        {
            "name": "Mauli Girls Hostel",
            "category": "girls",
            "description":
                "Mauli Girls Hostel provides safe and comfortable accommodation for female students. "
                "It offers clean rooms, a peaceful environment, and is located near VIT Bibwewadi.",
            "images": "mauli_room.jpg,mauli_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=Mauli+Girls+Hostel+Katraj+Pune&output=embed",
            "contact": "8390164777"
        },
        {
            "name": "Sharda Girls Hostel",
            "category": "girls",
            "description":
                "Sharda Girls Hostel is a clean and secure residential hostel designed especially for female students.",
            "images": "sharda_room.jpg,sharda_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=New+Sharada+Girls+VIT+Hostel+Katraj+Pune&output=embed",
            "contact": "8087551771"
        },
        {
            "name": "My Hostel Room Aurora Girls Hostel",
            "category": "girls",
            "description":
                "My Hostel Room Aurora offers a homely and peaceful living environment for college students.",
            "images": "hostel_room_aurora_room.jpg,hostel_room_aurora_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=MyHostelRoom+Aurora+Dhankawadi+Pune&output=embed",
            "contact": "8007005599"
        },
        {
            "name": "Girls Hostel/PG",
            "category": "girls",
            "description":
                "Girls Hostel/PG is a well-organized hostel providing safe accommodation for female students.",
            "images": "girls_hostel_pg_room.jpg,girls_hostel_pg_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=Girls+Hostel+near+VIT+VIIT+College+Katraj+Pune&output=embed",
            "contact": "9604703291"
        }
    ]

    for data in hostels:
        existing = Hostel.query.filter_by(name=data["name"]).first()
        if existing:
            existing.category = data["category"]
            existing.description = data["description"]
            existing.images = data["images"]
            existing.address = data["address"]
            existing.google_map_link = data["google_map_link"]
            existing.contact = data["contact"]
        else:
            db.session.add(Hostel(**data))

    db.session.commit()
    print("✅ Girls hostel data inserted/updated")


# ------------------ SEED BOYS HOSTELS ------------------
def seed_boys_hostels():
    hostels = [
        {
            "name": "Shree Pandurang Niwas Hostel",
            "category": "boys",
            "description":
                "Shree Pandurang Niwas Hostel provides safe and affordable accommodation for male students.",
            "images": "pandurang_room.jpg,pandurang_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=Shree+Pandurang+Niwas+Hostel+Katraj+Pune&output=embed",
            "contact": "9970112113"
        },
        {
            "name": "Aashirwad Boys Hostel",
            "category": "boys",
            "description":
                "Aashirwad Boys Hostel is a well-maintained residential hostel designed for college students.",
            "images": "aashirwad_room.jpg,aashirwad_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=Aashirwad+Bibwewadi+Pune&output=embed",
            "contact": "9933456600"
        },
        {
            "name": "Shrinivas Boys Hostel",
            "category": "boys",
            "description":
                "Shrinivas Boys Hostel offers a safe and calm student-friendly environment.",
            "images": "shrinivas_room.jpg,shrinivas_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=Shrinivas+Boys+Hostel+VIT+Bibwewadi+Pune&output=embed",
            "contact": "8308823822"
        },
        {
            "name": "Sumadhu Boys Hostel",
            "category": "boys",
            "description":
                "Samadhu Boys Hostel is a clean and comfortable hostel for male students.",
            "images": "sumadhu_room.jpg,sumadhu_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=Sumadhu+Boys+Hostel+Katraj+Pune&output=embed",
            "contact": "Not Available"
        },
        {
            "name": "Shree Gajanan Boys Hostel",
            "category": "boys",
            "description":
                "Shree Gajanan Boys Hostel offers safe and comfortable accommodation for male students.",
            "images": "gajanan_room.jpg,gajanan_building.jpg",
            "address": "Bibwewadi, Pune (near VIT College)",
            "google_map_link": "https://www.google.com/maps?q=Shree+Gajanan+Boys+Hostel+Kondhwa+Budruk+Pune&output=embed",
            "contact": "Not Available"
        }
    ]

    for data in hostels:
        existing = Hostel.query.filter_by(name=data["name"]).first()
        if existing:
            existing.category = data["category"]
            existing.description = data["description"]
            existing.images = data["images"]
            existing.address = data["address"]
            existing.google_map_link = data["google_map_link"]
            existing.contact = data["contact"]
        else:
            db.session.add(Hostel(**data))

    db.session.commit()
    print("✅ Boys hostel data inserted/updated")


# ------------------ RUN SEED ------------------
if __name__ == "__main__":
    with app.app_context():
        seed_mess()
        seed_girls_hostels()
        seed_boys_hostels()
        print("🎉 All seed data inserted successfully")