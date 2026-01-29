const form = document.getElementById("form")
const darkModeBtn = document.getElementById('darkModeBtn')

darkModeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

form.addEventListener("submit", function(event){
    event.preventDefault()

    let userId = event.target.id.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userPhone = event.target.phone.value
    let userGender = event.target.gender.value
    let userEmail = event.target.email.value

    if(userId.length < 6){
        alert("아이디가 너무 짧습니다. 6자 이상 입력해 주세요.")
        return
    }
    
    if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다.")
        return
    }

    // 가입 성공 시 화면
    document.body.innerHTML = ""
    document.write(`<p>${userId}님 환영합니다.</p><br>
        <p>등록된 성명: ${userName}</p><br>
        <p>전화번호: ${userPhone}</p><br>
        <p>성별: ${userGender}</p><br>
        <p>이메일: ${userEmail}</p>`)
})

