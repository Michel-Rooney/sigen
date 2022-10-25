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
const allInputs = document.querySelectorAll('input')

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

  const aEditar = document.createElement("a")
  const aDeletar = document.createElement("a")


  aEditar.classList.add("espaco-link")
  aDeletar.classList.add("espaco-link")

  aEditar.href = "#"
  aDeletar.href = "#"

  aEditar.textContent = "Editar Espaço"
  aDeletar.textContent = "Remover Espaço"

  section.append(h3, aEditar, aDeletar)

  tela.appendChild(section);
  modal.classList.remove('mostrar')
  contador++

}

form.addEventListener('submit', (event) => {
  event.preventDefault()
  adicionarEspaco()
});
  
  
  

