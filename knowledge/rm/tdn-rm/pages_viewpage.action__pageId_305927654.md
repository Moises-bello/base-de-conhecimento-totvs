---
content_hash: 1d8673283cd4684a469a8746b017aa3fe76bc51e7ff32816bc3a5cd83d89336d
fetched_at: '2026-06-29T00:08:43.716160+00:00'
page_id: '305927654'
product: rm
source: tdn-rm
title: Utilizando a atividade "Localizar Registro na Tabela"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=305927654
version: 4
---

# Índice:

---

* Objetivo:
* Especificação:

# Objetivo

---

     Este documento tem por objetivo especificar a atividade “Localizar Registro na Tabela” disponível na Fórmula Visual.

# Especificação

---

     A atividade “Localizar Registro na Tabela” é uma atividade que permite que um registro especifico de uma tabela específica seja localizada. No exemplo que será utilizado abaixo iremos, ao editarmos um usuário, enviar um e-mail informando que o usuário "X" foi modificado.

Para começarmos a utilizar a atividade, temos que conhecer os parâmetros que ele recebe.

| N° | Nome do Parâmetro | Descrição do Parâmetro | Obrigatoriedade |
| --- | --- | --- | --- |
| 1 | KeyFields | Campos que serão utilizados como chave de pesquisa (separados por vírgula) | GreenOBRIGATÓRIO |
| 2 | Tabela | Tabela cujo registro será localizado | GreenOBRIGATÓRIO |

**1)** Primeiramente iremos preencher a tabela à qual o registro será localizado (recuperado).

Clique no **Ícone Amarelo** ao lado da Propriedade **Tabela**, ou no **botão [...]** que aparece ao lado da mesma propriedade, a tela abaixo irá aparecer.

**2)** Agora devemos preencher a Propriedade **KeyFields**

Como escolhemos a tabela **PFUNC (Funcionários)**devemos informar suas chaves primárias, separadas por vírgula:

* CODCOLIGADA
* CHAPA

**3)** Agora iremos preencher os **parâmetros** que foram criados **dinamicamente** à partir da propriedade **KeyFields (CHAPA e CODCOLIGADA)**

| N° | Nome do Parâmetro | Descrição do Parâmetro | Obrigatoriedade |
| --- | --- | --- | --- |
| 1 | CODCOLIGADA | Valor da Coligada que será utilizada para recuperar um registro específico | GreenOBRIGATÓRIO |
| 2 | CHAPA | Valor da Chapa do Funcionário que será utilizada para recuperar um registro específico | GreenOBRIGATÓRIO |

****4)****Clicando no Ícone Amarelo ao lado da Propriedade **CODCOLIGADA,** ou no ****botão [...]****que aparece ao lado da mesma propriedade, a tela abaixo irá aparecer.

******5)******Clicando no **Ícone Amarelo**ao lado da Propriedade****CHAPA,****ou no ******botão [...]******que aparece ao lado da mesma propriedade, a tela abaixo irá aparecer.

**6)** Ao término da configuração da Atividade "**Localizar Registro na Tabela**", vamos configurar agora a atividade **"Enviar E-mail"**[**[Utilizando a Atividade Enviar E-mail](http://tdn.totvs.com/pages/releaseview.action?pageId=146184224)**]

**6.1)** Na imagem acima, foi preenchido:

| Nº | Propriedade | Valor | Descrição / (Valor Amigável) |
| --- | --- | --- | --- |
| 1 | Assunto | Activity=rmsFindRecordActivity1, Path=Fields["NOME"].AsString | Coluna NOME da tabela PFUNC |
| 2 | Destinatários | Matriz String[] | Conjunto de endereços de e-mail |
| 3 | Remetente | Company | O Remetente do e-mail será a própria empresa (COLIGADA do contexto) |
| 4 | Texto do e-mail | Foi realizado alteração no funcionário objeto desse e-mail | Texto que será apresentado no Corpo do e-mail |

O E-mail enviado será como a imagem abaixo:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou Superior

false

**Processo:** Atividade "Executar Código Fonte" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
