---
content_hash: 7f07f35baa6659d1115bd89011f22c2ab385d573aa2cd1091b9275787fe5eab8
fetched_at: '2026-06-29T00:10:52.974514+00:00'
page_id: '573515441'
product: rm
source: tdn-rm
title: Atualização de Valores no Encerramento da Parcial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=573515441
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**

## **01. VISÃO GERAL**

Ao executar a rotina de encerramento de parcial, os preços dos itens da mesma são atualizados conforme as vigências das respectivas tabelas (Brasíndice, Simpro), preços fixos e maior preço.

A configuração de preço que será usada é a definida nas condições contratuais, caso seja uma Material e haja uma tabela de materiais configurada essa será usada para calcular o preço.

Entretanto caso não haja tabela de materiais será usado a tabela de medicamentos para calculo do preço do material.

Caso o convênio possua alguma configuração de preço especifica para algum plano (Tabela de preço diferenciada) essa configuração terá prioridade no calculo de preço:

Por exemplo, dado que um convênio utilize a tabela de preço "Tabela Básica de MATMED" tanto para materiais quanto para medicamentos, mas para o plano "Enfermaria" utilize a tabela brasindice para medicamentos e a mesma para materiais "Tabela Básica de MATMED". Veja como fica a configuração:

Olhando para a configuração do medicamento "DIPIRONA SOD. 500MG COMP." vemos que ele possui dois valores na "Tabela Básica de MATMED" possui o valor 2,00 R$, já na tabela "Brasindice" possui o valor 7,47 R$. Vide imagens:

Ao lançar o mesmo medicamento, com o mesmo paciente usando planos diferentes é calculado o preço usando a tabela diferenciada:

Praticar o maior preço lançado para MATMED. Ao encerrar a conta ou até mesmo na rotina de Atualização de Valores, caso esteja parametrizado que será praticado o maior preço lançado para MATMED, o sistema pegará o maior preço de cada matmed lançado na conta e atualizará o preço dos demais itens de mesmo código. Essa atualização não ocorre quando ocorrer um dos seguintes cenários:

* Para itens cujo preço foi alterado via processo "Altera preço de OPME"
* Para itens lançados na aba Especial
* Para itens que possuem [vínculo com Nota fiscal](https://tdn.totvs.com/display/LRM/Processo+de+Material+Consignado) associada ao item da requisição de OPME do paciente

Processo "Altera preço de OPME"

]]>
