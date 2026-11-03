---
article_id: 4416695706007
category: Faturamento - Cadastros
content_hash: f136560aa27225e0392eb87ee1f83d3665e2f34020c641616dcb6da83d2fa91a
fetched_at: '2026-06-28T22:38:35.349330+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - variable is
  not an object  on PICCLI(MATV030.PRX)
type: support-article
updated_at: '2024-02-27T19:25:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416695706007-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-variable-is-not-an-object-on-PICCLI-MATV030-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao clicar em outras ações, referências do **cadastro do cliente** (**mata030**) ou em consulta **posição do cliente (Finc010)**, outras ações visualizar, gera o erro:

**variable is not an object  on PICCLI(MATV030.PRX) 30/09/2021 15:05:37 line : 1214**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**Foi alterada a função **PicCli()** onde foi incluída uma validação para que não ocorra o errorlog: "Erro no parâmetro FWFormModel: A operação (SetOperation)" no momento do usuário tentar visualizar ou excluir um cliente, utilizando o cadastro em MVC com o parâmetro **MV\_MVCSA1 = .T.**

Consequentemente, o ajuste também efetua a correção o erro variable is not an object  on PICCLI(MATV030.PRX),  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote de expedição contínua correspondente ao seu release:  [SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)  
2. Via Vs-Code, aplique o pacote para atualização do ambiente.

3. Reinicie o Smartclient e efetue o processo novamente.

**obs. Aplicação de pacote requer que o analista tenha conhecimentos de estrutura Protheus e vs-code .**
