console.log('hey');
document.addEventListener("DOMContentLoaded", ()=>{
    const risk_free_rate = document.querySelector("#risk_free_rate");
    const beta_of_investment = document.querySelector('#beta_of_investment');
    const market_rise = document.querySelector("#market_rise");
    const calculate = document.querySelector(".calculate");
    const result = document.querySelector(".result");
    const resultHtml = `
        <div cl
    `
    let data ={}
    async function postData(url='', data){
        // Default options are marked with *
        const response = await fetch(url, {
            method: 'POST',
            credentials:'same-origin',
            headers :{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        console.log(response.json())
        return response.json();
    }
    
    risk_free_rate.addEventListener('blur',(e)=>{
        console.log(e.currentTarget.value)
        data['risk_free_rate'] = e.currentTarget.value
    })
    beta_of_investment.addEventListener('blur',(e)=>{
        console.log(e.currentTarget.value)
        data['beta_of_investment'] = e.currentTarget.value
    })    
    market_rise.addEventListener('blur',(e)=>{
        console.log(e.currentTarget.value)
        data['market_rise'] = e.currentTarget.values
    })  
    calculate.addEventListener("click",(e)=>{
        postData('/calculate', data).then( data => console.log(data))   
    }
  )
})



