---
article_id: 17530001526935
category: Call Center - Telecobrança
content_hash: cdbeb4c2754d788956c49ec566173e2594fc9f13dc8490d4c389a6c15cdc028e
fetched_at: '2026-06-28T22:41:28.737801+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Help: TK274NOENC
  Este atendimento não poderá ser encerrado. Existem títulos que ainda não foram quitados'
type: support-article
updated_at: '2023-09-14T18:30:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17530001526935-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Help-TK274NOENC-Este-atendimento-n%C3%A3o-poder%C3%A1-ser-encerrado-Existem-t%C3%ADtulos-que-ainda-n%C3%A3o-foram-quitados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17530011736983) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao finalizar um atendimento na rotina TMKA271 o sistema apresenta o HELP " TK274NOENC " Este atendimento não poderá ser encerrado. Existem títulos que ainda não foram quitados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17529034222871)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center (SIGATMK) - Todas as versões.  
  
**Causa**

Esse incidente ocorre ao selecionar o status do campo "Status" (ACF\_STATUS) para (3- Encerrado), quando os títulos relacionados a esse atendimento estiverem em aberto. Não permitindo que o operador encerre o atendimento de telecobrança.    
  
**Solução**  
Para que o atendimento seja encerrado, o(s) título(s) devem estar pagos após receberem a baixa do financeiro, apresentando o conteúdo conforme o tipo de pagamento **(1- Pago, 2-Negociado ou 4-Baixa)** no campo "Status" (ACG\_STATUS).   
  
Outra alternativa para permitir o encerramento do atendimento seria selecionar a opção **(3- Cartório)** no campo "Status" (ACG\_STATUS).  
  
O conceito de cartório para essa opção seria indicar ao sistema um tipo de cobrança "externa", permitindo finalizar o atendimento em questão, indicando que o título será atribuído a outro tipo de cobrança (Cartório).  
  
**Saiba mais:**  
[Habilitar telecobrança no Call Center](https://tdn.totvs.com/pages/viewpage.action?pageId=239037537)
