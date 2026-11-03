---
content_hash: 0dece9bf6754d523dc196a298b7fed5d0eadc8eb36540d7f58d046d7caefbdce
fetched_at: '2026-06-29T00:10:11.893273+00:00'
page_id: '453295119'
product: rm
source: tdn-rm
title: Espelhos ao serem convertidos não funcionam
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453295119
version: 10
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Este tutorial tem por objetivo esclarecer comportamentos pós conversão de relatórios Delphi para .Net quando possuem consultas SQL com passagem de parâmetro espelho.

# Cenário:

---

**Espelhos ao serem convertidos não funcionam.**

É comum que espelhos ao serem convertidos em expressões não exibam valores corretamente, sendo necessário ajustes manuais. Um exemplo simples quando o Espelho faz referência a um campo da consulta SQL. Considerando uma consulta hipotética de código TESTE contendo a query:

sql

Na versão Delphi temos o componente ***SQL#1*** que imprimi a ***CHAPA*** dessa consulta e um espelho para esse campo chamado ***ESPELHO#1***. Depois de convertido, o campo ***SQL#1*** receberá um componente de texto com nome genérico, por exemplo **"*Texto5*"**, ligado à fonte de dados ***PFUNC.CHAPA***. Já o ***ESPELHO#1*** será convertido em um controle expressão e com nome ***EXPRESSAO\_1***, por exemplo. Porém o conteúdo dessa expressão é **"*= ESP SQL\_1*"** e ao gerar o relatório a expressão não exibe valor.

falseSolução:

Para ajustar a expressão edite seu conteúdo de **"*= ESP SQL\_1*"** para o novo nome do controle **"*Relatório.Texto5*"**. Pode-se alterar o valor da expressão ao editá-la e clicar no menu *Parâmetros > Relatório (Campos do Relatório) > Texto5*. Encontrando o nome do controle selecione para que seja adicionado automaticamente ao conteúdo da expressão. Depois salve o relatório.

---

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Conversão Relatórios Delphi

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**

Gustavo Naves De Castro
