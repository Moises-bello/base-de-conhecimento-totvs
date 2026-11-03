---
content_hash: 4443790fe2df24d8901407010c4517abf7def58b10752e56c9ee06d935e68cb0
fetched_at: '2026-06-29T00:11:56.693279+00:00'
page_id: '868236620'
product: rm
source: tdn-rm
title: Alto contraste de cores na MDI
type: documentation
url: https://tdn.totvs.com/display/LRM/Alto+contraste+de+cores+na+MDI
version: 4
---

# Índice

---

.\*ndice

# Objetivo

---

Instruir o usuário a configurar um ambiente de aplicação com as cores alteradas para um alto contraste.

# Arquivos

---

Para configurar a MDI como alto contraste, é necessário colocar um arquivo, com o nome **style.json** na pasta base de onde o arquivo RM.exe a ser utilizado está (por exemplo: *C:/TOTVS/RM.Net*).

Existem duas opções de alto contraste homologadas pela TOTVS. Ao escolher dentre elas, baixe o arquivo à sua direita.

### Opção 1

30px

150

### Opção 2

30px

150

*Caso esta opção seja escolhida, o arquivo deve ser renomeado para **style.json***

Qualquer alteração de valores nos arquivos disponibilizados acima é de responsabilidade única e exclusiva do usuário. Apenas os arquivos acima são homologados pela TOTVS.

# Configurando

---

### Posicionado o arquivo

Com o arquivo baixado, garanta que seu nome é **style.json**, e então coloque-o na pasta base de onde o arquivo RM.exe a ser utilizado está (por exemplo: C:/TOTVS/RM.Net).

### Configurando o atalho do RM.exe

Então deve ser criado um atalho do arquivo RM.exe.

Neste atalho, ao clicar com o botão direito, deve ser selecionada a opção Propriedades:

No final campo **Destino**, deve ser adicionado o texto "*/thf=style.json*":

Deve então confirmar a alteração clicando em **OK**.

### Abrindo o RM através do atalho

Para que os efeitos sejam aplicados, o RM deve ser aberto através do atalho.

Ao abri-lo desta maneira, e realizar o login, a MDI abrirá da forma demonstrada nos prints acima.

### Voltando ao estilo padrão

Caso telas tenham sido abertas com o estilo de ao contraste, estas mesmas telas reterão o estilo da grid de alto contraste.

Para reverter este comportamento, e retornar ao layout padrão do RM, é necessário utilizar a funcionalidade de Voltar Layout Padrão:

---
