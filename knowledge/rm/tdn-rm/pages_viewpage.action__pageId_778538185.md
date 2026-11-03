---
content_hash: ab1234470ecc886aea7fe5cdd9898c5f58a443c5d18285b4add0719b78869e3b
fetched_at: '2026-06-29T00:11:37.495655+00:00'
page_id: '778538185'
product: rm
source: tdn-rm
title: Versões inferiores a 12.1.2310
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=778538185
version: 3
---

Versão disponível

Esta funcionalidade está disponível a partir da versão 12.1.2205

# Descrição

A apuração do concurso de bolsa ocorre no momento em que é realizada a classificação do candidato.

Durante a classificação, o sistema valida a pontuação/classificação do candidato com o range cadastrado para o concurso de bolsa vinculado ao processo seletivo ou área de interesse ofertada.

Se a pontuação/classificação satisfazer a regra estabelecida no range, então o sistema classifica o candidato para o concurso de bolsa.

**Classificação por nota**

Na classificação por nota, a regra do concurso de bolsa só será aplicada quando a área ofertada possuir uma única etapa ou no caso de mais de uma etapa, será aplicada na última etapa de classificação que define os candidatos como classificados para chamada.

**Classificação Manual**

Na classificação manual, ao clicar em "**Validar**", se o sistema identificar que existe concurso de bolsa cadastrado e  candidatos aptos para o concurso de bolsa, então será apresentada duas novas colunas ( "Concurso Bolsa" e "Valor") com as informações da bolsa a ser concedida para o candidato na matricula.

**Classificados concurso bolsa**

Todo candidato apto a receber a bolsa através do concurso de bolsa será armazenado na tabela SPSCLASSICADOSCONCURSOBOLSA.

**Como consultar se o candidato esta apto a receber a bolsa através do concurso?**

I***nscrição do candidato***

***Visualização "Classificados concurso bolsa"***

Esta visão mostrar todos os candidatos classificados para o concurso de bolsa, através desta tela será possível conferir todas as informações utilizadas para a apuração.

Esta tela pode ser acessada através do anexo dos seguintes cadastros: *processo seletivo, área de interesse ofertada, concurso de bolsa.*

* Ao executar o processo "Cancelar classificação do candidato" as bolsas apuradas através do concurso de bolsa serão removidas do candidato.
* Se um candidato possuir uma bolsa pelo concurso de bolsa, e durante uma nova classificação os critérios (pontuação /classificação) não satisfazer o range cadastrado para o concurso bolsa, o sistema irá remover a bolsa concedida na classificação anterior.
* O concurso de bolsa não será processado para os candidatos que a chamada já foi realizada.

Na central do candidato é possível o candidato visualizar o resultado da apuração da bolsa.

Para maiores informações acesse
