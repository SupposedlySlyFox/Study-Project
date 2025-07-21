const textHeader = ` You have 3 choices of commands: 
mine - For mining and getting xp.
rank - For knowing your rank.
exit - To leave the program.`;

let xp = 0

let action = "idle"

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function levelClass(xp) {
    if (xp <= 1000) {
        return rank = "Iron"
    } else if (xp >= 1001 && xp <= 2000) {
        return rank = "Bronze"
    } else if (xp >= 2001 && xp <= 5000) {
        return rank = "Silver"
    } else if (xp >= 5001 && xp <= 7000) {
        return rank = "Gold"
    } else if (xp >= 7001 && xp <= 8000) {
        return rank = "Platinum"
    } else if (xp >= 8001 && xp <= 9000) {
        return rank = "Ascendent"
    } else if (xp >= 10001 && xp <= 10000) {
        return rank = "Imortal"
    } else {
        return rank = "Radiant"
    }
}

function mine(xp) {
    switch (getRandomInt(1, 5)) {
        case 1:
        xpGained = 10
        xp += xpGained
        console.log(`You got copper! +${xpGained}xp!`)
        end

        case 2:
        xpGained = 100
        xp += xpGained
        console.log(`You got iron! +${xpGained}xp!`)
        end

        case 3:
        xpGained = 250
        xp += xpGained
        console.log(`You got gold! +${xpGained}xp!`)
        end

        case 4:
        xpGained = 500
        xp += xpGained
        console.log(`You got platinum! +${xpGained}xp!`)
        end

        case 5:
        xpGained = 1000
        xp += xpGained
        console.log(`You got a magic stone! +${xpGained}xp!`)
        end
    }
}

function main() {
    while (true) {
    print()
        action = gets().toLowerCase();
        if (action == "mine") {
            mine(xp);
        } else if (action == "rank") {
            console.log(levelClass(xp))
        } else if (action == "exit") {
            exit
        } else {
            console.log("you did nothing.")
        }
    }
}

main();
