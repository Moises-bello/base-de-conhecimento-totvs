---
content_hash: 6eadf0832e41a523040bf4cd91a1fd25dd7ccb099a429011093c4d10b1882f11
fetched_at: '2026-06-29T00:09:45.468284+00:00'
page_id: '433251901'
product: rm
source: tdn-rm
title: Controle de Créditos Fiscais de Tributos Retidos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433251901
version: 3
---

**Controle dos Valores Retido na Fonte**

O cadastro será usado para armazenar os registros de valores retidos na fonte, onde devem ser informados na aba identificação o Código do Tributo, Período (Mês e Ano) e a Natureza de Retenção. Na aba "Valores" são informados os valores Totais da Retenção, Retenção de Compensação, Retenção Deduzido, Retenção Restituição e o Saldo da Retenção, os campos de valores são somente leitura para o usuário. No anexo são informados os valores das compensações onde é selecionado o tipo de compensação, cadastrado o Período (Mês e Ano) e valor da Compensação.  
Estes valores são totalizados e armazenados no campo somente leitura do Controle dos Valores Retido na Fonte então é calculado o Saldo da Retenção.  
O processo vinculado ao cadastro de controle dos valores retido na fonte gera automaticamente registros no cadastro principal com base nos lançamentos baixados no mês do Período da Retenção do sistema TOTVS Gestão Financeira "Calculo do Saldo da Retenção" O Saldo da Retenção será calculado com base: (Valor Total da Retenção) - (Valor da retenção Mediante a declaração de compensação) -(Valor da Retenção do Pedido de restituição) - (Valor da Retenção Deduzida).
