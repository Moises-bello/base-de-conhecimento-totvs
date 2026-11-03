---
article_id: 360041427293
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: ce4568fa22d8a9f0f293afe45071c99ff1a04ab127fba5511abc14078e36cdbe
fetched_at: '2026-06-28T22:39:20.454771+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração para
  Nota Fiscal de devolução com valor (Cálculo) do ICMS ST igual a Nota Fiscal de origem
type: support-article
updated_at: '2021-07-13T17:29:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041427293-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-Nota-Fiscal-de-devolu%C3%A7%C3%A3o-com-valor-C%C3%A1lculo-do-ICMS-ST-igual-a-Nota-Fiscal-de-origem
---

**Dúvida**Qual a configuração para Nota Fiscal de devolução com valor (Cálculo) do ICMS ST igual a Nota Fiscal de origem?  
   
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para notas fiscais de devolução foi implementado o parâmetro MV\_DEVRET=T (Trata se na Nota Fiscal de Devolução o valor do ICMS retido deve ser igual ao ICMS Ret. da Nota Fiscal de origem).

Em casos de devolução parcial é necessário configurar o campo  F4\_DEVPARC=Sim no Cadastro de Tipo de Entrada e Saída.
