---
article_id: 38185829431447
category: Financeiro - Compensação Contas a Receber
content_hash: db0dd4f84c124e4bff4c0db251f1d0b5dd0d9ad9ea7c24dd92a710d2a0f0eaf3
fetched_at: '2026-06-28T22:37:40.457139+00:00'
product: protheus
section_id: 35056224784407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA330 - É possível
  compensar títulos de filiais diferentes ?
type: support-article
updated_at: '2026-06-01T20:04:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38185829431447-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA330-%C3%89-poss%C3%ADvel-compensar-t%C3%ADtulos-de-filiais-diferentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38185829415447) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
O sistema permite realizar a compensação de títulos de filiais diferentes ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da 12.1.2210.  
  
**Solução**  
Para conseguir realizar a compensação de títulos entre filiais:

* Na tela de seleção dos registros, clique no botão filiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38185829416855)

* Irá apresentar a tela abaixo, devendo clicar em SIM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38185829417367)

* Após isso, deverá selecionar as filiais nas quais deseja realizar o filtro dos registros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38185829417879)

* Após escolher as filiais, basta clicar em OK na próxima tela.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38185829418135)

* Com isso, o sistema irá apresentar os registros para selecionar e seguir com a compensação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38185829418775)

Após clicar em **OK**, pressione **F12** para acessar os parâmetros da rotina. Em seguida, ajuste os seguintes parâmetros:

* considera Loja? "Não"
* Considera Cliente? "Não"
* Do cliente? Deixar em branco
* Até o cliente? Adicionar ZZZZZ
* Considera Filiais abaixo? "Sim"
* Da Filial? Deixar em branco
* Até Filial? Adicionar ZZZZZ

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40891931102103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40891947810455)

**Saiba mais**

[Compensação contas a receber- FINA330 - Financeiro P12](https://tdn.totvs.com/pages/viewpage.action?pageId=505768648)
