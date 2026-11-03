---
article_id: 35907946239127
category: Materiais - Compras (SIGACOM)
content_hash: 35b8653b8d1d53489fcd6f87062e56d2a352317e100db986f6602b107bc462e0
fetched_at: '2026-06-28T22:41:07.330758+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento – TOTVS Backoffice – Compras – NFC Failed to load program AVALCOT
type: support-article
updated_at: '2025-10-27T14:19:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35907946239127-Cross-Segmento-TOTVS-Backoffice-Compras-NFC-Failed-to-load-program-AVALCOT
---

⏱️ Tempo aproximado para leitura: 00:03:12 min

**Ocorrência**  
Ao gerar um pedido de compras via Novo fluxo de Compras é apresentado o erro "Failed to load program AVALCOT.PRW."

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Causa**  
Esse incidente ocorre, pois o programa AVALCOT.PRW não está compilado corretamente ou não consegue acessar algum recurso necessário, resultando em falha ao tentar carregá-lo no sistema.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a pasta onde o programa AVALCOT.PRW está localizado.
2. Abra o arquivo no ambiente de desenvolvimento ADVPL.
3. Verifique se existem erros de compilação no código.
4. Se necessário, faça correções no código.
5. Compile o programa novamente.
6. Após a recompilação, teste o programa para verificar se o erro persiste.

**Observação:**

Caso o fonte seja diferente, é necessário validar o nome do fonte e buscar direto nos seus programas para recompilar.

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
