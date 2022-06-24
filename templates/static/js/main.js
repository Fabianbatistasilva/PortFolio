console.log('entrou no home')

function redes_hover(local){
    let conteudoredes = local;
    console.log(conteudoredes)
    switch (conteudoredes) {
        case 'gmail_list':
            console.log('entrou aqui')
            let gmail = document.getElementById('gmail_id');
            gmail.innerHTML= 'currifabianbatista@gmail.com ';
            gmail.style.color='white';
            break;
        case 'git_list':
            let git =document.getElementById('git_id');
            git.innerHTML = 'Github <i class="fab fa-github"></i>';
            git.style.color='white';
            break;
        case 'linkedin_list':
            let linkedin =document.getElementById('linkedin_id');
            linkedin.innerHTML = 'Linkedin <i class="fab fa-linkedin"></i>';
            linkedin.style.color='white';
            break;
        case 'facebook_list':
            let facebook =document.getElementById('facebook_id');
            facebook.innerHTML = 'Facebook <i class="fab fa-facebook"></i>';
            facebook.style.color='white';
            break;
        case 'instagram_list':
            let instagram =document.getElementById('instagram_id');
            instagram.innerHTML = 'Instagram <i class="fab fa-instagram"></i>';
            instagram.style.color='white';
            break;
        case 'Telefone_list':
            let telefone =  document.getElementById('Telefone_id');
            telefone.innerHTML='(48) 99173-2178 ';
            telefone.style.color='white';
            break;    
        case 'localiza_list':
            let localiza =document.getElementById('localiza_id');
            localiza.innerHTML ='Palhoça (sc) ';
            localiza.style.color='white';
            break;
    }
}
function saiu_da_rede(local){
    let conteudoredes = local;
    console.log(conteudoredes)
    switch (conteudoredes) {
        case 'gmail_list':
            let gmail =document.getElementById('gmail_id');
            gmail.innerHTML = 'Gmail <i class="fa-solid fa-envelopes-bulk"></i>';
            gmail.style.color='black';
            break;
        case 'git_list':
            let git =document.getElementById('git_id');
            git.innerHTML = 'Github <i class="fab fa-github"></i>';
            git.style.color='black';
            break;
        case 'linkedin_list':
            let linkedin =document.getElementById('linkedin_id');
            linkedin.innerHTML = 'Linkedin <i class="fab fa-linkedin"></i>';
            linkedin.style.color='black';
            break;
        case 'facebook_list':
            let facebook =document.getElementById('facebook_id');
            facebook.innerHTML = 'Facebook <i class="fab fa-facebook"></i>';
            facebook.style.color='black';
            break;
        case 'instagram_list':
            let instagram =document.getElementById('instagram_id');
            instagram.innerHTML = 'Instagram <i class="fab fa-instagram"></i>';
            instagram.style.color='black';
            break;
        case 'Telefone_list':
            let telefone =document.getElementById('Telefone_id');
            telefone.innerHTML ='Telefone <i class="fa-solid fa-mobile-button"></i>';
            telefone.style.color='black';
            break;
        case 'localiza_list':
            let localiza =document.getElementById('localiza_id');
            localiza.innerHTML ='Localização <i class="fa fa-map-marker" aria-hidden="true"></i>';
            localiza.style.color = 'black';
            break;
    }
}