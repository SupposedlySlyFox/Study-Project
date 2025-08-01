rpgclass = {
  "mage": {"age": 30, "health": 75, "mana": 50, "inventory": {"staff": {"durability": 40, "quantity": 1, "damage": 15}, "Manafied robe": {"quantity": 1}}, "level": 1},
  "warrior": {"age": 35, "health": 125, "mana": 10, "inventory": {"sword": {"durability": 35, "quantity": 1, "damage": 35}, "robe": {"quantity": 1}}, "level": 1},
  "monk": {"age": 45, "health": 100, "mana": 10, "inventory": {"potion": {"quantity": 1, "effectHP": 25}, "robe": {"quantity": 1}}, "level": 1},
  "ninja": {"age": 25, "health": 100, "mana": 25, "inventory": {"katana": {"durability": 30, "quantity": 1, "damage": 25}, "robe": {"quantity": 1}}, "level": 1}
}

let classUser = "mage"

function classUsage() {
  switch(classUser) {
    case "mage":
      return "staff"
    case "warrior":
      return "sword" 
    case "monk":
      return "fists"
    case "ninja":
      return "katana"
  }
}

class RPG {

  constructor(classUser, weapon){
    this.classUser = classUser
    this.weapon = weapon
  }

  attack() {
    let weapon = classUsage();
    console.log(`You, as a ${this.classUser}, attacked using ${this.weapon}`);

    const weaponData = rpgclass[classUser]["inventory"][classUsage()];

    if (weaponData && weaponData.damage) {
      console.log(`You have dealt ${weaponData.damage} damage`);
    } else {
      console.log(`You used your ${this.weapon} to attack the enemy, but no damage has been dealt.`);
    }
  }
}
RPG.attack();
