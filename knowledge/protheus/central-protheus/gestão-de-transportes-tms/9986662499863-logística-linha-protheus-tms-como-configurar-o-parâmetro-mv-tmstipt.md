---
article_id: 9986662499863
category: Gestão de Transportes (TMS)
content_hash: f6ea9c649c2aac19ef95a11d0743cbdded2ad4348d15276abe4fac63e436b63c
fetched_at: '2026-06-28T22:45:27.410666+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: 'Logística - Linha Protheus - TMS - Como configurar o parâmetro MV_TMSTIPT? '
type: support-article
updated_at: '2022-11-03T17:32:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9986662499863-Log%C3%ADstica-Linha-Protheus-TMS-Como-configurar-o-par%C3%A2metro-MV-TMSTIPT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Como configurar o parâmetro **MV\_TMSTIPT?****Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Segue abaixo orientações para configuração do parâmetro **MV\_TMSTIPT:**

1. Na tabela genérica - **SX5** deve existir o tipo **CTE.**  
   Exemplo:  
   X5\_TABELA=05  
   X5\_CHAVE=CTE
2. No parâmetro **MV\_TMSTIPT**, indicar a série e filtro, e caso tenha diversas séries deve indicar todas separando com ponto e virgula.  
   Exemplo:  
   **MV\_TMSTIPT:** 721=CTE;133=CTE

O parâmetro determina o tipo do título a receber, quando a geração da fatura for a partir da tabela **SE1**, ou seja quando o parâmetro **MV\_TMSMFAT = 1.**

**![Captura_de_tela_2022-11-03_142033.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/9986851995287)**
