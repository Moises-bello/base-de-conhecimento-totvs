---
content_hash: bb5d0a8601225f9010fe918d78e95316d340c62b49fb44d5cce4643ca36f3288
fetched_at: '2026-06-29T00:09:21.780779+00:00'
page_id: '422545906'
product: rm
source: tdn-rm
title: Outras Informações - Apuração ISS Construção Civil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545906
version: 2
---

Nos parâmetros foi definido o campo Controla Saldo Deduções para controlar o saldo das deduções de material e/ ou das deduções da subempreitada. Este campo só se aplica se para a Filial for permitido Deduzir Material e/ou subempreitada e se a Filial Emite Livros de Construção Civil.  
 Uma vez habilitado este  parâmetro o sistema irá, no momento da apuração do período: calcular o total de material adquirido e subempreitada contratada no período, transferir o saldo do período anterior para o que se está encerrando, calcular os valores que foram deduzidos no lançamento fiscal no período , e os saldo a transportar para o período seguinte.   
 Este cálculo é realizado obra por obra e para obras no município da Filial.  
 Estes valores se encontram disponíveis na pasta Serviços por Projeto, subpasta Deduções do cadastro de Períodos.

OS campos disponibilizados na nova pasta são:

* Saldo Anterior de Materiais
* Saldo de Materiais
* Saldo Anterior de subempreitada
* Saldo de subempreitada

Esta PASTA somente estará visível se o parâmetro Controla Saldo de Deduções de Materiais e/ou subempreitada estiver habilitado.  
 O campo "Deduz Materiais" foi disponibilizado tanto para operações de Entrada quanto para operações de Saída.  
 Este campo será considerado na seleção de lançamentos fiscais referentes as deduções de Subempreitada e Materiais.  
 A regra de seleção dos lançamentos referente a operações que são possíveis de serem deduzidas da Base do ISS é a seguinte:  
 Dedução de Materiais: Lançamentos Fiscais vinculados a Naturezas de Operação cujo campo "Classificação Operação de Entrada = '01 ou 02'" ou cujo campo Deduz Materiais está habilitado.  
 Dedução subempreitada: Lançamentos Fiscais vinculados a Naturezas de Operação cujo campo "Classificação Operação de Entrada = '06,07, 08 ou 09'" ou cujo campo Deduz Subempreitada está habilitado.  
 Não foram considerados neste cálculo os lançamentos fiscais de SAÍDA, vinculados as Naturezas cujo campo Deduz Material está habilitado. Isso porque estas Notas não serão registradas no REMAS e pode gerar diferença no cálculo das deduções
