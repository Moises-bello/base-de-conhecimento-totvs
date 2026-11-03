---
content_hash: f7e9d8567f0f5deeb0ca654b0df8b56538e25f912a6790f8eb7960416be1fba0
fetched_at: '2026-06-29T00:08:41.287468+00:00'
page_id: '286522533'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar Código"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286522533
version: 27
---

# Índice:

---

* Objetivo:
* Especificação:

# Objetivo:

---

     Este documento tem por objetivo especificar a atividade “Executar Código” disponível na Fórmula Visual.

# Especificação:

---

     A atividade “Executar Código” é uma atividade que permite que um código (que varia de Levantar uma Exceção à realizar rotinas de Selecionar Dados de Tabelas do Banco, entre outras ) seja executado. Devido a sua complexidade,esta atividade exige um nível de conhecimento avançado em Fórmula Visual e em codificação.

Para começarmos a utilizar a atividade, temos que conhecer os parâmetros que ele recebe.

| N° | Nome do Parâmetro | Descrição do Parâmetro | Obrigatoriedade |
| --- | --- | --- | --- |
| 1 | ExecuteCode | Código à ser executado | OBRIGATÓRIO |

**1)** Existem duas formas de preencher a Propriedade **ExecuteCode:**

**1.1)** Clicando no **Ícone Amarelo** ao lado da Propriedade **ExecuteCode**, ou no **botão [...]** que aparece ao lado da mesma propriedade, a tela abaixo irá aparecer.

**1.2)** Clicando duas vezes em cima da Propriedade **ExecuteCode,** um console de programação .Net irá aparecer abaixo do diagrama do **Workflow.**

A funcionalidade de **Executar Código** aparece também clicando:

**2)** Na parte branca do **Workflow**, através do Grupo **Manipuladores**:

Tanto para a Propriedade **Completed**, quanto para a Propriedade **Initialized,**existem duas formas de preenchê-las, são elas:

****2.1)****Clicando no Ícone Amarelo ao lado das Propriedades ****Initialized / Completed**,** ou no ****botão [...]****que aparece ao lado das mesmas propriedades, a tela abaixo irá aparecer.

| Initialized | Completed |
| --- | --- |
|  |  |

**2.2)** Clicando duas vezes em cima das Propriedades **Initialized / Completed,**um console de programação .Net irá aparecer abaixo do diagrama do**Workflow.**

| Initalized | Completed |
| --- | --- |
|  |  |

**3)** Na atividade **Se / Senão.**

**3.1)** No Grupo **Condições**Escolher Condição de Código

**3.2)** Existem duas formas de preencher a Propriedade **Condition:**

**3.2.1)** Clicando no **Ícone Amarelo** ao lado da Propriedade **Condition**, ou no **botão [...]** que aparece ao lado da mesma propriedade, a tela abaixo irá aparecer.

**3.2.2)**Clicando duas vezes em cima da Propriedade****Condition,****um console de programação .Net irá aparecer abaixo do diagrama do****Workflow.****

A diferença do console da Propriedade **Condition** é que ela já vem por padrão com a linha **args.Result = true;.**

Como é uma atividade que necessita definir uma condição, o resultado desse código deve ser um valor booleano (ou lógico), **true** ou **false.**

## **Exemplo de Utilização da Atividade**

**EXEMPLO 1:**

Iremos utilizar a atividade **"Executar Web Service"** em conjunto com a atividade **"Executar Código".**

**1)** Configure a atividade de **Web Service []**

**2)** Defina o Retorno como uma **Nova Propriedade** clicando no **botão [...]** à frente da Propriedade **Retorno**

**2.1)** A tela da Atividade ficará assim**:**

**3)** Vamos gerar uma exceção trazendo o retorno do **Web Service**

O Resultado é o mesmo das telas apresentadas abaixo:

**EXEMPLO 2:**

Iremos utilizar a atividade****"Executar Consulta SQL"****em conjunto com as atividades****"Executar Código"**** e **"Enviar E-mail"**.****

****1)**Configure a atividade de **Consulta SQL [[Utilizando a atividade "Consulta SQL"](http://tdn.totvs.com/pages/releaseview.action?pageId=146184324)]****

sql1Consulta SQL FVXML01true

****2)****Configure a atividade de **"Executar Código".**

c#1codeActivity1: ExecuteCodetrueOUTROS EXEMPLOS DE CÓDIGO

EXEMPLO (Geração de Erro com conteúdo de SQL de uma Atividade Consulta SQL e retornando um erro):

c#1codeActivity1: ExecuteCodetrue

EXEMPLO Geração de Erro com conteúdo de SQL de dentro da Atividade Executar Código e retornando um erro:

c#1codeActivity1: ExecuteCodetrue

****3)****Configure a atividade de **"Enviar E-mail" ****[[Utilizando a atividade "Enviar E-mail"](http://tdn.totvs.com/pages/releaseview.action?pageId=146184224)]****.**

**4)** Ao executar a **Fórmula Visual** o E-mail com o **XML** da **Nota Fiscal Eletrônica (Exemplo Utilizado)** será enviado aos destinatários configurados.

Caso a atividade **Executar Código** apresente limitações para o seu cenário, recomendamos utilizar a atividade **[Executar Código Fonte](https://tdn.totvs.com/x/xzfyHg)**, que foi desenvolvida justamente para atender esses casos.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou Superior

false

**Processo:** Atividade "Executar Código" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
