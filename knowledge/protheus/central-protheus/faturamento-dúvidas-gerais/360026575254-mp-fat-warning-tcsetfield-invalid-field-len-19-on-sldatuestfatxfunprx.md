---
article_id: 360026575254
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 19d19611813cec4ea327ddc0dd8bf2b710764f05fda7d54f7dad2f75280be27a
fetched_at: '2026-06-28T22:38:31.106271+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP - FAT - WARNING - TCSetField - Invalid field len: 19  on SLDATUEST(FATXFUN.PRX)'
type: support-article
updated_at: '2021-04-28T15:54:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026575254-MP-FAT-WARNING-TCSetField-Invalid-field-len-19-on-SLDATUEST-FATXFUN-PRX
---

**Ocorrência**Sistema gera errorlog, como corrigir?  
***WARNING - TCSetField - Invalid field len: 19 on SLDATUEST(FATXFUN.PRX)***

**Ambiente**

Microsiga Protheus –  A partir da versão 11.80.  
   
**Solução**

A função **SldAtuEst**avalia os saldo por Almoxarifado, Lote e Localização. Houve alguma alteração de tamanho de campo em relação aos campos de quantidade ou controle de estoque ,principalmente nas tabelas **SB8**e **SBF.**  
  
A variável **nSize** especifica a quantidade total de dígitos de um campo "N", e seu valor deve estar entre **1** e **18**. Caso o valor não esteja nesse intervalo, será apresentada a mensagem de erro fatal: "**WARNING - TCSetField - Invalid field len: *nSize***".  
  
Para tratar ajuste o dicionário de dados com relação as tabelas SB8 e SBF e realize a atualização do ambiente com o pacote acumulado disponível no portal, posteriormente, realize novos testes.

**Saiba Mais:****[MP - ADVPL - TCSetField](http://tdn.totvs.com/display/tec/TCSetField)**  
**[Portal Download Pacotes](https://suporte.totvs.com/portal/p/10098/download#000006)**
