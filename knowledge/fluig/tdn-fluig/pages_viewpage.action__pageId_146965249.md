---
content_hash: 60a33a41ff7c724d7361422e21672496ed3d3da6efa94f4fa006dcd46d04344c
fetched_at: '2026-06-28T21:35:18.043614+00:00'
page_id: '146965249'
product: fluig
source: tdn-fluig
title: Personalização de Temas de Formulários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146965249
version: 22
---

# Índice

true.\*ndicenone

# Personalização de Temas de Formulários

---

No editor de formulários, disponível no editor de processos, é possível selecionar um estilo personalizado para o formulário que está sendo criado.

Este estilo pode ser personalizado por qualquer usuário que possui permissão ao painel de controle.

Compatibilidade no modo escuro

Este recurso ainda não é compatível com o modo escuro lançado na atualização [Voyager 2.0](https://tdn.totvs.com/x/6HxjN). Para mais detalhes, consulte a documentação em: add link

Acompanhe, navegando nas abas a seguir, o passo a passo para a criação de um novo tema personalizado.

0.5falsesamplesfadetruePasso1Passo 1slide

* Acessar o **Painel de Controle** pelo menu lateral.

Passo2Passo 2slide

* Verifique no agrupador **Desenvolvimento** e após clique no item **Temas de Formulários**.

Passo3Passo 3slide

* Na tela é possível realizar o *download* de temas já cadastrados, definir se o tema está ou não está ativo (quando ativo, o tema é disponibilizado para seleção na edição de formulários) e tema padrão que é o tema pré selecionado ao criar um formulário. Para adicionar um tema novo, clique em **Adicionar**.

Passo4Passo 4slide

* Na tela para adicionar um estilo novo, é necessário preencher um código ao tema, a descrição do tema e selecionar o arquivo CSS para realizar o *upload*.

* Clique em **Salvar**. Após isto o tema está cadastrado e já pode ser utilizado no editor de formulários.

### Recomendações

Ao fazer o upload de temas é importante seguir as seguintes regras:

1. O tema deve possuir sempre uma regra por linha.
2. Todas as propriedades de cada classe tem que estar na mesma linha, não deve-se pular linha, para melhor interpretação do editor.
3. O arquivo *.css* deve possuir todas as linhas com seletores, não se deve possuir linhas em branco.
4. Todas as classes, elementos e identificadores podem ser modificados, desde que respeitando as regras acima.

É possível obter um exemplo de uma folha de estilos acessando a página de Temas, no Painel de Controle.

Abaixo estão cada uma das classes e estrutura de um formulário gerado a partir do editor.

| Classe | Descrição |
| --- | --- |
| .title-form-application | Classe do título do formulário |
| .form-field | DIV que enquadra todo campo do formulário |
| .form-input | DIV do campo |
| .required | Classe do asterisco em campos obrigatórios. |
| .paragraph-is-required | Mensagem de obrigatório |

Em alguns casos é necessário utilizar "**!important**", pois são classes que já são utilizadas pela plataforma e podem ser sobrescritas.

### HTML

O HTML gerado automaticamente pelo editor de formulários com apenas um campo, fica com a seguinte estrutura:

html/xmlFormuláriotrue

# Formulário

Todos os campos com \* são de preenchimento obrigatório.

Label textbox
**\***

]]>

### Exemplo

A seguir criaremos um tema com um estilo personalizado:

* Para este resultado, o seguinte CSS deve ser criado e cadastrado nos temas:

  cssexemplo.csstrue
* Toda personalização deve iniciar com a classe t + id. Assim, evita-se que as personalizações interfiram no estilo de outras páginas da plataforma., nesse exemplo, a classe é t3 pois o id do tema é 3.
