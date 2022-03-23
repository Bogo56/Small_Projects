// Data
const account1 = {
    owner: 'Jonas Schmedtmann',
    movements: [200, 450, -400, 3000, -650, -130, 70, 1300],
    interestRate: 1.2, // %
    username: "js",
    pin: 1111,
  };
  
  const account2 = {
    owner: 'Jessica Davis',
    movements: [5000, 3400, -150, -790, -3210, -1000, 8500, -30],
    interestRate: 1.5,
    username: "jd",
    pin: 2222,
  };
  
  const account3 = {
    owner: 'Steven Thomas Williams',
    movements: [200, -200, 340, -300, -20, 50, 400, -460],
    interestRate: 0.7,
    username: "st",
    pin: 3333,
  };
  
  const account4 = {
    owner: 'Sarah Smith',
    movements: [430, 1000, 700, 50, 90],
    interestRate: 1,
    username: "ss",
    pin: 4444,
  };
  
  const accounts = [account1, account2, account3, account4];


// ELEMENTS

let greeting = document.querySelector(".greeting")
const inputUser = document.querySelector("#username")
const inputPIN = document.querySelector("#PIN")
const logButton = document.querySelector(".log_button")
const date = document.querySelector(".label1 p")
const balance = document.querySelector("#balance")
const operationType = document.querySelectorAll(".info1 .type")
const operationDate = document.querySelectorAll(".info1 .date")
const operationAmount = document.querySelectorAll(".info2 .amount")
const summaryInfo = document.querySelector(".numbers p")
const transferTo = document.querySelector("#transfer-to")
const transferAmount = document.querySelector("#transfer-amount")
const confUser = document.querySelector("#confirm-user")
const confPIN = document.querySelector("#confirm-PIN")
const loanAmount = document.querySelector("#loan-amount")
const sendBtn1 = document.querySelector(".send_button.transfer")
const sendBtn2 = document.querySelector(".send_button.loan")
const sendBtn3 = document.querySelector(".send_button.close")
const screen = document.querySelector(".content")
const sortBtn = document.querySelector(".sort")

let loggedUser;
const today = new Date()
date.textContent = `As of ${today.getMonth()+1}/${today.getDate()}/${today.getFullYear()}, ${today.getHours()}:${today.getMinutes()}` 

logButton.addEventListener("click",(e) =>{
    e.preventDefault()
    let checkUser = accounts.find( account => account.username === inputUser.value)
    if (checkUser === loggedUser){
        alert("Already logged in")
    }
    else if (checkUser?.pin === parseInt(inputPIN.value)){
        loggedUser = checkUser
        screen.style.opacity = 100;
        updateUI()
        startCounting()
        sortBtn.addEventListener("click",sortMovements())
    }else{alert("Wrong Username or Password")}
})


sendBtn1.addEventListener("click", (e) => {
e.preventDefault()
 const receiver = accounts.find(user => user.username === transferTo.value) 
 const sendAmount = parseInt(transferAmount.value)
 if(receiver 
    && transferAmount.value > 10 
    && loggedUser.balance > sendAmount + 50)
    {
        loggedUser.movements.push(-sendAmount)
        receiver.movements.push(sendAmount)
        updateUI()
    }else{
        alert("Transfer could not be executed")
    }
} )

sendBtn2.addEventListener("click", (e) => {
    e.preventDefault()
    const loan = parseInt(loanAmount.value)
    if(loan < loggedUser.balance/2){
        loggedUser.movements.push(loan)
        updateUI()
    }else{
        alert("Not eligable for a loan")
    }
})

sendBtn3.addEventListener("click", (e) => {
    e.preventDefault()
    const user = confUser.value
    const pin = parseInt(confPIN.value)
    if(loggedUser.username === user && loggedUser.pin === pin){
        let index = accounts.findIndex(account => account.username === user)
        accounts.splice(index,1)
        screen.style.opacity = 0;
        loggedUser = {owner:""}
        updateUI()
    }else{
        alert("Invalid Credentials")
    }
})

let updateUI = () => {
    document.querySelector(".greeting").textContent = `Good Afternoon, ${loggedUser.owner}!`
    updateMovements()
    updateSummary()
    updateBalance()
}

let updateMovements = (movements = loggedUser.movements) => {
    document.querySelector('.history').innerHTML = ""
    movements.forEach(amount => {
    let type = amount < 0 ? "Withdrawal" : "Deposit"
    let color = type === "Withdrawal" ? "bg-red" : "bg-green"
    let html = `<div class="movement">
                    <div class = "info1">
                        <p class="type ${color}">${type}</p>
                        <p class="date">${today.getMonth()+1}/${today.getDate()}/${today.getFullYear()}</p>
                    </div>
                    <div class = "info2">
                        <p class ="amount">${amount}</p>
                    </div>
                </div>`
                document.querySelector(".history")
                .insertAdjacentHTML("afterbegin",html)
})
};

let updateSummary = () => {
    let depositsAmount = loggedUser.movements
    .filter((el)=> el > 1)
    .reduce((acc,value) => acc+value,0)
    let withdrawalAmount = loggedUser.movements
    .filter((el)=> el < 1)
    .reduce((acc,value) => acc+value,0)
    let interest = loggedUser.interestRate/100 * depositsAmount
    document.querySelectorAll(".sum.green")[0].textContent = depositsAmount
    document.querySelectorAll(".sum.green")[1].textContent = interest
    document.querySelectorAll(".sum.red").forEach(el => {
        el.textContent = Math.abs(withdrawalAmount)
    })
}

let updateBalance = () => {
    loggedUser.balance = loggedUser.movements.reduce ((acc,value) => acc+value)
    balance.textContent = `$${loggedUser.balance}.00`
}

let sortMovements = () => {
    let sorted = true
    return () => {
        if(sorted){
            let movementsSorted = [...loggedUser.movements].sort((a,b) => a-b)
            updateMovements(movementsSorted)
            sorted = !sorted
        }else{
            updateMovements(loggedUser.movements)
            sorted = !sorted
        }
    }
}

const startCounting  = ()=>{
let timeLeft = document.querySelector("span")
let totalTime = 150
let lastUser = loggedUser
let minutes;
let seconds;
let counter = setInterval(() => {
    if (totalTime === 0){
        clearInterval(counter)
        screen.style.opacity = 0;
        loggedUser = {owner:""}
        updateUI()
    }
    else if (lastUser !== loggedUser){
        clearInterval(counter)
    }
    minutes = Math.floor(totalTime/60)
    seconds = `${totalTime % 60}`.padStart(2,"0")
    timeLeft.textContent = `${minutes}:${seconds}`
    totalTime--
},1000)
}