---
article_id: 26409869350679
category: Materiais - Compras (SIGACOM)
content_hash: 1225704e3e5f0c01bf988d4090587a14e6e539c059fbd14c62f4538845f34fee
fetched_at: '2026-06-28T22:41:13.022559+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Mensagem Nota Fiscal
  - Este Documento Possui OPs Vinculadas (BN).
type: support-article
updated_at: '2024-09-16T19:01:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26409869350679-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Mensagem-Nota-Fiscal-Este-Documento-Possui-OPs-Vinculadas-BN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26409869327639) Tempo aproximado para leitura: **00:05:SS min** **Dúvida**

Ao confirmar o lançamento da Nota Fiscal, a seguinte mensagem é exibida: "Este documento possui OPs vinculadas (BN).  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS- Versão 12  
  
**Solução**

Foi criada uma proteção para permitir que a quantidade inserida seja maior que o saldo da OP  <https://tdn.totvs.com/pages/releaseview.action?pageId=854372039> ,apresentando uma tela de validação que informa a quantidade da OP no saldo quando incluímos a nota fiscal de entrada. Para prosseguir é necessário dar um duplo clique na tela, com a quantidade à apontar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26409884385303)

**Simulação para Gerar a mensagem**

**1. Ordem de Produção:** quantidade 5850,00

**2.** **Tolerância de Recebimento** : Porcentagem 5% Quantidade | 20 % Preço

**3. Solicitação de Compras**: Manualmente, informando a OP na linha do item

**4. P****edido de Compras ->**Outras Ações: Solicitação de Compras.

**5. Nota Fiscal de Entrada:** Quantidade 5855,00 (quantidade superior à Ordem de Produção).

Neste momento foi realizado o Bloqueio por tolerância

**6. Liberação da Nota Fiscal.**

Ao classificar a nota, será gerada a mensagem, onde informa que não é possível incluir nota fiscal com valor superior à Ordem de Produção.

**Saiba mais :**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
