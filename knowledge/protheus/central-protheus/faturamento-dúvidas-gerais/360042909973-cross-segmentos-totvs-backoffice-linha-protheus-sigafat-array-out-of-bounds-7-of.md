---
article_id: 360042909973
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 2ec0de5e1a75facc20731404e8412e6cb43fba3eed8471ecf3c47dfa76ea41d1
fetched_at: '2026-06-28T22:38:29.940757+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - array out of
  bounds ( 7 of 5 ) on TRANSCANC(SPEDNFE.PRX)
type: support-article
updated_at: '2021-11-12T16:12:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042909973-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-array-out-of-bounds-7-of-5-on-TRANSCANC-SPEDNFE-PRX
---

**Ocorrência**

Ao realizar a exclusão do documento de saída (**MATA521**) com o parâmetro "**MV\_CANCNFE**" e o Job "**FatJobNFe**" habilitado o sistema apresenta o seguinte error.log:

**array out of bounds ( 7 of 5 ) on TRANSCANC(SPEDNFE.PRX) 20/12/2019 09:47:37 line : 12913**

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - A partir da release 12.1.17.

**Causa**

O problema estava relacionado ao ponto de entrada **FISCANNFE**  e quantidade de posições recebidas por seu array para ser tratado na exclusão dos documentos de saída (**MATA521**) e na transmissão da Nota fiscal eletrônica (**SPEDNEF**)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do **pacote de expedição contínua do módulo Faturamento**,  conforme a release de sistema :  **[SIGAFAT](https://tdn.totvs.com/x/Iw4dHw)** 

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;  
3.Posteriormente, inicialize o Smartclient e refaça o processo.

**Importante: Para que haja a correção do erro, o fonte mata521 - Exclusão da Nota de Saída,  precisa estar com data igual ou superior a 13/12/2019.**

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
