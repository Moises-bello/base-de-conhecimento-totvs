---
article_id: 360026398251
category: Financeiro - Contas a Receber
content_hash: 66b512bd5b935b1d4e3a99fa8c5980396f60cc5378ad5e8f0110acb8552089ac
fetched_at: '2026-06-28T22:38:15.054107+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA450 -  Retenção de PCC na baixa para Compensação Entre Carteiras
type: support-article
updated_at: '2021-06-11T00:28:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026398251-MP-SIGAFIN-FINA450-Reten%C3%A7%C3%A3o-de-PCC-na-baixa-para-Compensa%C3%A7%C3%A3o-Entre-Carteiras
---

**Dúvida**Na rotina **Compensação Entre Carteiras** (**FINA450**), quando um **título a pagar** possui retenção de **PIS**, **COFINS** e **CSLL** na baixa (**MV\_BX10925** = 1) e esteja configurado para que a retenção seja realizada através da compensação (**MV\_CC10925** = 2), é possível determinar se o **valor a pagar** exibido na tela de seleção será o **líquido** (subtrai o **PCC**) ou o **bruto** (valor do título).  
   
 **Ambiente**Microsiga Protheus – Financeiro – FINA450 - A partir da versão 11.8  
  
**Solução**Para realizar a retenção dos impostos **PIS ,COFINS e CSLL** na rotina **Compensação Entre Carteiras** (**FINA450**) é necessário configurar os parâmetros conforme abaixo:  
**MV\_BX10925 = 1 (retenção do PCC na baixa)****MV\_CC10925 = 2 (habilita a retenção do PCC na compensação entre carteiras)**

**Observações:**  
Na tela de seleção dos títulos, para que a coluna **Valor Paga**r seja exibida com o **valor líquido** do título, ou seja, descontando o valor da retenção do **PCC**, é necessária a configuração abaixo:  
**MV\_BP10925 = 2 (Considera o valor líquido).**

**Importante:**Não recomendamos a alteração do parâmetro **MV\_BX10925**, pois no momento da implantação do ***Protheus***, é definido como a empresa irá tratar o imposto.
