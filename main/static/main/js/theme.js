const switchBtn = document.querySelector('.theme-btn')

switchBtn.addEventListener('click', () => {
    const htmlTag = document.getElementsByTagName('html')
    let themeAttr = htmlTag[0].getAttribute("data-bs-theme")
    if(themeAttr == 'dark') {
        htmlTag[0].setAttribute("data-bs-theme", 'light')
        switchBtn.innerText = 'Темная тема'
    } else {
        htmlTag[0].setAttribute("data-bs-theme", 'dark')
        switchBtn.innerText = 'Светлая тема'
    }
})