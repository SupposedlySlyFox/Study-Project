const textHeader = ` You have 3 choices of commands: 
fight - For a match of luck between winning and losing.
rank - For knowing your rank.
exit - To leave the program.`;

let wins = 0

let action = "idle"

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function levelClass(wins) {
    if (wins <= 10) {
        return rank = "Iron"
    } else if (wins >= 11 && wins <= 20) {
        return rank = "Bronze"
    } else if (wins >= 21 && wins <= 50) {
        return rank = "Silver"
    } else if (wins >= 51 && wins <= 70) {
        return rank = "Gold"
    } else if (wins >= 71 && wins <= 80) {
        return rank = "Platinum"
    } else if (wins >= 81 && wins <= 90) {
        return rank = "Ascendent"
    } else if (wins >= 91 && wins <= 100) {
        return rank = "Imortal"
    } else {
        return rank = "Radiant"
    }
}

function fight(wins) {
    switch (getRandomInt(1, 2)) {
        case 1:
        winsGained = 1
        wins += winsGained
        console.log(`You won!`)
        end

        case 2:
        winsGained = 0
        wins += winsGained
        console.log(`You lost!`)
        end
    }
}

function main() {
    while (true) {
    print()
        action = gets().toLowerCase();
        if (action == "fight") {
            fight(wins);
        } else if (action == "rank") {
            console.log(levelClass(wins))
        } else if (action == "exit") {
            exit
        } else {
            console.log("you did nothing.")
        }
    }
}

main();
