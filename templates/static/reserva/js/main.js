// Div mãe
const tela = document.querySelector('.principal')
const form = document.querySelector('#form')

// Buttons
const btnAdicionar = document.getElementById('adicionar-espaco')
const adicionar = document.getElementById('input-cadastrar')

// Modals
const modal = document.getElementById('modal-cadastro')
const btnFechaModal = document.getElementById('modal-fechar')

// Inputs
const inputNome = document.getElementById('input-nome')
const inputImagem = document.getElementById('input-imagem')

var imagemCarregada = ''

let contador = 1

// Abrir Modal
btnAdicionar.addEventListener('click', () => {
    modal.classList.add('mostrar')
})

// Fechar Modal
btnFechaModal.addEventListener('click', () => {
  modal.classList.remove('mostrar')
})

// Adicionar Espaço
function adicionarEspaco() {
  var section = document.createElement("section");
  section.classList.add("espaco");
  section.setAttribute("name", `espaco-${contador}`)
  
  const h3 = document.createElement('h3')
  h3.classList.add("espaco-titulo")
  h3.textContent = inputNome.value

  const a = document.createElement("a")
  a.classList.add("espaco-link")
  a.href = "#"
  a.textContent = "Faça sua reserva"

  section.append(h3, a)

  tela.appendChild(section);
  modal.classList.remove('mostrar')
  contador++
}

form.addEventListener('submit', (event) => {
  event.preventDefault()
  adicionarEspaco()
});
  
  
  

