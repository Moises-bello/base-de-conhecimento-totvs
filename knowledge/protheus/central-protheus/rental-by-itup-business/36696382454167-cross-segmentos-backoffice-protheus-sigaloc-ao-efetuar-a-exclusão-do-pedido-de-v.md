---
article_id: 36696382454167
category: Rental by ItUp Business
content_hash: af1bf04d434c705b3a6c5472bc0111ba9819986976580a2c71f14d870e7f87ad
fetched_at: '2026-06-28T22:36:20.478754+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Ao efetuar a exclusão do
  pedido de venda apresenta um aviso "Existe um pedido emitido com data superior"
type: support-article
updated_at: '2025-12-01T17:40:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36696382454167-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Ao-efetuar-a-exclus%C3%A3o-do-pedido-de-venda-apresenta-um-aviso-Existe-um-pedido-emitido-com-data-superior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36696382411543) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao excluir um pedido de venda gerado pelo módulo SIGALOC, é apresentado um aviso **"Existe um pedido emitido para o orçamento com data superior ao que você está tentando excluir."**  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Causa**  
Quando lidamos com múltiplos faturamentos automáticos no **SIGALOC**, é fundamental seguir uma ordem específica para exclusão desses faturamentos.

A exclusão deve ser feita da última para a primeira ocorrência. Isso se deve ao fato de que o **SIGALOC** realiza atualizações no ciclo de locação conforme cada faturamento é processado. Se a exclusão for feita fora dessa ordem, o sistema pode se desorganizar, resultando em dados inconsistentes e possíveis erros no ciclo de locação.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. **Identifique a ordem dos faturamentos**: Verifique a sequência cronológica dos faturamentos automáticos registrados.

**2. Exclua do último para o primeiro**: Comece a exclusão pelo faturamento mais recente e prossiga até o mais antigo. Isso garante que o sistema mantenha a integridade dos dados e atualizações do ciclo de locação.  
  
**Saiba Mais:** [***Estorno de faturamento e remessa***](https://tdn.totvs.com/display/public/PROT/Estorno+de+faturamento+e+remessa)
