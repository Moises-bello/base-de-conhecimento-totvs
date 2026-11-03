---
article_id: 360051926213
category: Gestão de Transportes (TMS)
content_hash: 889cfb1225e873ea1c7e3fc25948bcddb854f4907ffa3eb4a2bbb9a6e8cd2d71
fetched_at: '2026-06-28T22:45:33.382609+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Subfaixa Tabela de Frete
type: support-article
updated_at: '2023-02-24T19:46:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051926213-Log%C3%ADstica-Linha-Protheus-TMS-Subfaixa-Tabela-de-Frete
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**Como funciona o conceito de **Subfaixa** na **Tabela de Frete** no **TOTVS Logística TMS**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**A utilização de **subfaixas** na tabela de frete aumenta a flexibilidade na maneira de cobrar os serviços de transporte prestados. Os **Componentes de Frete - TMSA030** podem ser definidos em **Faixas - DT3\_FAIXA** e em outros fatores que farão parte da **Tabela de Frete - TMSA010**, conforme configuração. As faixas podem ser divididas em **S****ubfaixas - DT3\_FAIXA2**, com um tipo diferente da faixa principal.   
  
Por exemplo, o valor de um **Componente de Frete** pode ser calculado sobre o **Calc. Sobre - DT3\_FAIXA** = **01 - Peso Mercadoria**e cobrado sobre **Subfaixa - DT3\_FAIXA2 = 08 - Km.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079910814/mceclip0.png)

Este conceito pode ser utilizado nas rotinas **Tabela de Frete - TMSA010**, **Tabela de Tarifas - TMSA080** e **Ajuste de Tabela de Frete - TMSA011**.  
  
Para os **Componentes de Frete** **com****S****ubfaixa,** no cadastro da **Tabela de Frete - TMSA010**, os campos **Fração** **- DT1\_INTERV** e **Valor** **- DT1\_VALOR** não são apresentados. Para visualizá-los, clique em **Outras Ações/Subfaixa.**
