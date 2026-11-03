---
article_id: 28160709730199
category: Financeiro - Contas a Receber
content_hash: 4411ff6817a47d4287b16f1947e2f86839e4999f05bdf5d7606321e597838ee6
fetched_at: '2026-06-28T22:38:12.781641+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA060 - Estorno de
  Título em Carteira Descontada Valor Bruto
type: support-article
updated_at: '2024-11-29T21:32:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28160709730199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA060-Estorno-de-T%C3%ADtulo-em-Carteira-Descontada-Valor-Bruto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709693975) Tempo aproximado para leitura: **00:05:00 min****Dúvida**

Em determinadas situações, o estorno de títulos em carteira descontada ou o cancelamento de borderôs deve ser realizado com base no valor bruto do título a receber.

Para facilitar esse processo, foi implementada uma melhoria na rotina de transferência, permitindo que o usuário escolha se deseja realizar o estorno da transferência ou o cancelamento do borderô utilizando o valor bruto do título. Essa funcionalidade garante que os títulos em carteira descontada (situação 2) possam ser corretamente retornados para a carteira normal (situação 0).

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA060 - Todas as versões  
  
**Solução**

**Atualização → Contas a Receber → Transferências.**  
Incluir títulos a receber.

* **1º Estorno de transferência em valor líquido:**

Transferir o título para a situação 2 (Carteira Descontada), informando a taxa de desconto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664076951)

Verificar o **Extrato Bancário (FINR470)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664077719)

Estornar o título no valor líquido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28161412088471)

O valor apresentado na tela do estorno é o mesmo valor que foi transferido. Confirmar o estorno.

Verificar o **Extrato Bancário (FINR470)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709696663)

O valor estornado é o mesmo valor que foi transferido.

* **2º Estorno em valor bruto:**

Transferir o título para a situação 2 (Carteira Descontada), informando a taxa de desconto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664080663)

Estornar o título no valor bruto, marcando o check box do “Estorno Valor Bruto”.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664081431)

O valor apresentado na tela do estorno é o valor que foi transferido acrescido da taxa de transferência. Confirmar o estorno.

Verificar o **Extrato Bancário (FINR470).** O valor estornado é o bruto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664082199)

**Cancelamento de borderô em valor líquido:**

* **1º** **Cancelamento em valor líquido**

Gerar Borderô para a situação 2 (Carteira Descontada), informando a taxa de desconto. Confirmar a geração do borderô.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664083095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709702167)

Verificar o **Extrato Bancário (FINR470)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709706007)

Cancelar o borderô no valor líquido.  Responder, Sim, na Pergunta exibida após a tela de parâmetros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709706519)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709707287)

O valor apresentado na tela do estorno é o mesmo valor que foi transferido. Confirmar o estorno.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664088343)

Verificar o **Extrato Bancário (FINR470).** O valor estornado é o mesmo valor que foi transferido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709712791)

* **2º Cancelamento em valor bruto**

Gerar Borderô para a situação 2 (Carteira Descontada), informando a taxa de desconto. Confirmar a geração do borderô.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664091671)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28161307406999)

Cancelar o borderô no valor líquido. Responder **Não** na pergunta exibida após a tela de parâmetros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709713687)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664093335)

O valor apresentado na tela do cancelamento é o valor bruto do título. Confirmar o cancelamento do borderô.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160709715095)

Verificar o **Extrato Bancário (FINR470).** O valor do cancelamento é o valor bruto do borderô.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160664095767)

**Saiba mais**

[Transferências - FINA060 - Financeiro - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=271405699)
