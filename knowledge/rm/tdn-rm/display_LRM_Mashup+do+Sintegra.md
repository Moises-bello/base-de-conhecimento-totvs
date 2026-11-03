---
content_hash: 186c8d455a1127ec561436caecfcb779b228bbdd47609e828af8765b0834a1d5
fetched_at: '2026-06-29T00:05:55.371653+00:00'
page_id: '142803038'
product: rm
source: tdn-rm
title: Mashup do Sintegra
type: documentation
url: https://tdn.totvs.com/display/LRM/Mashup+do+Sintegra
version: 20
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão de como funciona o Mashup do Sintegra.

# Introdução:

---

       Quanto aos empecilhos relatados no Mashup do Sintegra.

       O Sintegra de Minas Gerais está fora do ar mesmo, por isso não esta em funcionamento. Quanto ao Sergipe, o site foi alterado. Para descobrir o que aconteceu, utilizamos o MashupStudio para comparar o que o Mashup envia e o que a página está fazendo.

falseServidor de JobExecução do Mashup

Primeiramente, deve-se executar o Mashup por dentro do MashupStudio, assim ele irá gerar um log do que aconteceu.

Análise do Log

Analisando o log, é possível ver que a requisição "**requestSE**" está dando erro "**404**". Em seguida, ao navegar na página por dentro do MashupStudio, é visto que a URL da requisição foi alterada e foi acrescentado um novo parâmetro.

Requisições

**Requisição do Mashup:**

**Página requisitada:**

* **<https://security.sefaz.se.gov.br/SIC/sintegra/consulta.jsp>**

**Parâmetros requisitados**:

* AppName = SIC
* Transld = T21297
* cdCnpj = 06090988000103
* cdPessoaContribuinte =
* ds = idea

**Requisição da Página:**

**Página requisitada:**

* **<https://security.sefaz.se.gov.br/SIC/sintegra/consulta.jsp>**

**Parâmetro requisitado:**

* cdImagem a mais, mudando então, a URL da requisição no Workflow.

Adição de Parâmetro

Adicionando o parâmetro nos PostData:

Mapeamento do Parâmetro

  A origem deste parâmetro foi mapeada na primeira Página de requisição, lendo do HTML:

 

falseObservação:

Este retorno foi mapeado para uso interno do Mashup.

Para maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX

false

**Processo:** Mashup do Sintegra

falsefalse

**Status:** Finalizado

false

**Data:** 07/04/2014

false

**Autores:**
