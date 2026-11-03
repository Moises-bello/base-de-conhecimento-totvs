---
article_id: 360036460133
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7e38c742cc3572bd6fff49baaeceb02de0e652a77e02cbf5db264415856bc802
fetched_at: '2026-06-28T22:42:42.212670+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - É possível não apresentar a mensagem
  alertando sobre o prazo de entrega das OPs intermediárias e SCs
type: support-article
updated_at: '2021-11-30T17:41:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036460133-Manufatura-Linha-Protheus-SIGAPCP-%C3%89-poss%C3%ADvel-n%C3%A3o-apresentar-a-mensagem-alertando-sobre-o-prazo-de-entrega-das-OPs-intermedi%C3%A1rias-e-SCs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**Ao abrir uma **OP - Ordem de Produção** através do **MATA650 - Ordem de Produção** é apresentada a mensagem que as **OPs** e **SCs - Solicitações de Compra** serão abertas com datas previstas anteriores a database.

![KCS_-_IMAGEM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047873233/KCS_-_IMAGEM.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A mensagem é apresentada quando o parâmetro **MV\_PRZESTR** está habilitado.   
  
**Solução**Para que a mensagem não seja mais apresentada, altere o conteúdo do **MV\_PRZESTR - Na inclusão da OP (MATA650), verifica a existência de componentes na estrutura que poderão gerar OPs intermediárias ou SCs anteriores a database?** para **.F.**.
