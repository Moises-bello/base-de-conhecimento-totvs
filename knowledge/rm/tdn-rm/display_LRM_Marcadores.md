---
content_hash: a4b4602263bc96888aa37281c0c230e9036929ce81d1a559beecf51773dac541
fetched_at: '2026-06-29T00:08:48.477376+00:00'
page_id: '325847848'
product: rm
source: tdn-rm
title: Marcadores
type: documentation
url: https://tdn.totvs.com/display/LRM/Marcadores
version: 10
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão do que é e como funciona os marcadores no RM Reports.

# Introdução:

---

       Os marcadores tem como objetivo literalmente marcar alguns campos do texto definidos pelo usuário, para que ao gerar o relatório eles sejam mais facilmente encontrados.

      Eles funcionam como um Índice, quando clicado no marcador ele direciona diretamente para onde o campo está.

      Por exemplo:

       Um relatório que trás uma ficha de registro de todos os funcionários da empresa, e para fins de conferência, deseja-se saber as alterações de salário de cada um dos funcionários.

       Desta forma, basta colocar um marcador no campo "Alterações de Salário", para que na pré-visualização ou ao gerar o relatório, ao clicar no marcador ele direcione diretamente para o campo.

# Como criar:

---

***Passo a passo para configurar os marcadores:***

falseInstalação em N camadas (App Server)1º Passo:

Primeiramente, é necessário "ativar" os marcadores em seu relatório. Para isso, basta informar o nome de seu marcador na Grade de Propriedades do Relatório.

Basta selecionar a caixa de texto do "Marcador" e digitar o nome desejado. Conforme imagem abaixo:

2º Passo:

Em seguida, selecione o campo que você deseja marcar. Acesse a Grade de Propriedades do campo selecionado e no campo "Marcador" digite por qual nome esse campo será identificado.

O campo "Marcador Pai" é opcional, caso o usuário deseje estabelecer marcadores em diferentes níveis, caso nada seja selecionado, todos os marcadores serão criados no mesmo nível.

O campo "Marcador Pai" caso preenchido, deve selecionar qual será o campo representando o nível superior ao marcador.

Repita o 2° Passo em todos os campos em que se deseja colocar um marcador.

# Vizualização:

---

       Como exemplo, utilizaremos um marcador no campo "Alterações de Salário".

       A cada vez que é clicado no marcador "Salário" criado, ele direciona diretamente para o campo, conforme imagem abaixo:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.19 ou Superior

false

**Processo:** Marcadores

falsefalse

**Status:** Finalizado

false

**Data:** 26/12/2017

false

**Autores:**
