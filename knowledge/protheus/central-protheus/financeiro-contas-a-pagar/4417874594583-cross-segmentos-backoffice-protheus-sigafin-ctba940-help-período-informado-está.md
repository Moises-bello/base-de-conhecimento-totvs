---
article_id: 4417874594583
category: Financeiro - Contas a Pagar
content_hash: d89eb383871462177f80a73737245f0540b10aa3222519806cdd8169e07897fd
fetched_at: '2026-06-28T22:38:09.819803+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - BackOffice Protheus - SIGAFIN - CTBA940 - Help: Período
  informado está abaixo da data limite de Conciliação Bancária'
type: support-article
updated_at: '2025-06-10T17:30:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417874594583-Cross-Segmentos-BackOffice-Protheus-SIGAFIN-CTBA940-Help-Per%C3%ADodo-informado-est%C3%A1-abaixo-da-data-limite-de-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32719332412951) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar conciliação do movimento financeiro, é apresentado a mensagem "Período informado está abaixo da data limite de Conciliação Bancária"  
  
![KCS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417892232087)  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Essa mensagem ocorre, pois o parâmetro **MV\_DATAREC** está com data maior que a data de conciliação informada.   
  
**Solução**Ajustar o parâmetro **MV\_DATAREC** para uma data menor que o período de conciliação.

O parâmetro **MV\_DATAREC** define qual data limite para realização de reconciliação bancária.  
**Exemplo:**   
**Conciliação** 01/12/2021  
Parâmetro deve estar com conteúdo 30/11/2021 (data abaixo do período informado).   
  
**Saiba mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6070721>
