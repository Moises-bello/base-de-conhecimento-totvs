---
content_hash: a2f466a01cb104468060b7e3b03c1213a9d96a5d872dbc2ea0deeebcccd26f8e
fetched_at: '2026-06-28T21:35:29.575730+00:00'
page_id: '75270483'
product: fluig
source: tdn-fluig
title: Desenvolvimento de Formulários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=75270483
version: 223
---

# Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é descrever o desenvolvimento de formulários avançados no fluig, abordando algumas regras iniciais para dar uma base para outras  e .

# Pré-requisitos

---

Antes de iniciar o desenvolvimento de formulários, assista aos vídeos *how to* no item [Criação de formulários](http://tdn.totvs.com/x/fv4lE).

# Não utilize a declaração <!DOCTYPE> HTML

---

Ao publicar um formulário não recomendamos a utilização de declarações *<!DOCTYPE>*:

html/xml]]>

A utilização dessas pode impactar em algumas funcionalidades da definição de formulário ou do *Workflow* na utilização do navegador Microsoft® Internet Explorer®.

# Pré-requisitos

---

Antes de iniciar o desenvolvimento de formulários, assista aos vídeos *how to* no item [Criação de formulários](http://tdn.totvs.com/x/fv4lE).

# Desenvolvimento de Formulários

---

Para facilitar o desenvolvimento do formulários, você pode usar o

0.5falsesamplesfadetrue1Passo1

* Para a criação de uma definição de formulário, na visão *Explorador de pacotes (Package Explorer)* deve-se acessar a pasta *forms* do projeto fluig, clicar com o botão direito e no menu acessar *Novo (New) > Formulário*.

**Figura 1 - Novo Formulário.**

2Passo 2

* Na tela de criação de definição de formulário, basta preencher o nome desejado e clicar em concluir.

**Figura 2 - Nova Definição de Formulário.**

3Passo 3

* Ao concluir, um pacote referente à definição de formulário é criado na pasta *forms* e o editor de formulário fica disponível para edição.

**Figura 3 - Nova Definição de Formulário.**

4Passo 4

* A partir do editor, todo o conteúdo HTML é desenvolvido. No exemplo abaixo um formulário simples de cadastro foi desenvolvido:

**Figura 4 - Novo Formulário.**

# Exportando o formulário para o Fluig

---

Após o desenvolvimento, você pode enviar para o fluig o seu formulário. Para saber como e ter mais informações sobre as formas de armazenamento de dados, você pode consultar a nossa documentação sobre  e .

## Garantindo a criação dos campos

Apenas são considerados os campos dentro da tag <form> do html principal usando o atributo *name* do html. Caso tenha outros arquivos html que compõe o formulário ou criação de campos dinâmicos, estes podem não conseguir ser persistidos corretamente no banco de dados.

Caso necessário, você pode criar os campos como não visíveis para que o fluig entenda que existe aquele campo (ainda que depois será substituído pela sua customização)

## Boas práticas de desenvolvimento

Evite a inserção de scripts diretamente no arquivo html. Opte por usar um arquivo .js separado para isso e importe-o no seu html através da tag

jsExemplo de import de arquivo de script]]>

## Estrutura de pastas

O Fluig não tem suporte a estrutura de pastas no formulário. Por isso, mesmo que você organize seus arquivos em pastas, como no exemplo abaixo:

bashExemplo de estrutura de pastas

Para o fluig, o seu formulário será entendido assim:

bashExemplo de estrutura de pastas

Ainda que nenhum arquivo seja perdido, para evitar confusões nas declarações no formulário o ideal é criar os formulário com todos os arquivos na raiz. A exceção são os eventos de formulário
