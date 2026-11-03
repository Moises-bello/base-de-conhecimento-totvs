---
article_id: 360044510893
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 16243ebedc891e8db2b5f8480d0ee005735b1b396a3406b4a4004a4339871c9b
fetched_at: '2026-06-28T22:39:20.465665+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Considerar a tabela
  SFT para apuração do ICMS ST
type: support-article
updated_at: '2021-07-13T17:28:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044510893-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Considerar-a-tabela-SFT-para-apura%C3%A7%C3%A3o-do-ICMS-ST
---

**Dúvida**MP - FIS - CONSIDERAR A TABELA SFT PARA APURAÇÃO DO ICMS ST  
  
**Ambiente**  
Protheus – Fiscal – A partir da versão 11.80]  
  
**Solução**

Para considerar a tabela SFT para a apuração do icms st, configurar o parâmetro

MV\_RESF3FT = .T.

Usar dessa forma para operações com o mesmo CFOP porém com itens diferentes do conteúdo do campo FT\_CREDST

exemplo:

6910 - CST = 41 - FT\_credst = 4

6910 - CST = 10 - FT\_credst = 2

Dessa forma será considerado o campo de forma correta.
