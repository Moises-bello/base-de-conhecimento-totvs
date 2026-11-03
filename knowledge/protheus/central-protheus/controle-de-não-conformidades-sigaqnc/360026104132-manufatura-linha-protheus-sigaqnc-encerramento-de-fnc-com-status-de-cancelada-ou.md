---
article_id: 360026104132
category: Controle de Não Conformidades (SIGAQNC)
content_hash: b58fd39210e5184d8dfe3cc15151646f1c4850faf13fbd394a7799962cbecd81
fetched_at: '2026-06-28T22:42:27.931656+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Encerramento de FNC com status de Cancelada
  ou Não Procede
type: support-article
updated_at: '2021-09-08T12:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026104132-Manufatura-Linha-Protheus-SIGAQNC-Encerramento-de-FNC-com-status-de-Cancelada-ou-N%C3%A3o-Procede
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Na rotina **Ficha de Ocorrência e de Não Conformidade - QNCA040**, como encerro uma **FNC - Ficha de Não Conformidade** quando o status da mesma é **Cancelada** ou **Não Procede**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Solução**Para encerrar as **FNCs** com status **Cancelada** ou **Não Procede**, deve ser preenchido o campo **Dt. Con. Real - Data de Conclusão Real** do Cadastro da **FNC** na rotina **QNCA040**.  
  
**Importante**Para os demais status, a **FNC** é encerrada automaticamente quando o **Plano de Ação** vinculado à **FNC** é **encerrado**. O parâmetro **MV\_QNEAPLA** **- Baixa do Plano de Ação Automática** define se o encerramento do **Plano de Ação** será feito automaticamente após a finalização da última etapa ou se deverá ser encerrado manualmente.
