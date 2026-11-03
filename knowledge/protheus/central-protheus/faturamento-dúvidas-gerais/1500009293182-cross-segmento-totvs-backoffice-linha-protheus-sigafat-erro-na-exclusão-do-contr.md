---
article_id: 1500009293182
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: ee727dccc3b3f8e9d03868f1e2c62fc59f2a0eb5f8b6398113be72ea12772cbb
fetched_at: '2026-06-28T22:38:28.555305+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Erro na exclusão
  do contrato de parceria - Alias does nota exist NLP
type: support-article
updated_at: '2023-07-05T16:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009293182-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-na-exclus%C3%A3o-do-contrato-de-parceria-Alias-does-nota-exist-NLP
---

**Ocorrência**

Ao tentar excluir um contrato de parceria (FATA400), ocorre o erro:

**Alias does not exist NLP on FT400GRAVA(FATA400.PRX) 11/02/2021 14:20:21 line : 1195**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Causa**O erro ocorreu por falta de uma proteção na rotina fata400, onde foi criado uma nova opção em outras ações do contrato de parceria, que  só poderá ser utilizada, quando o ambiente tiver em seu dicionário a tabela **NLP** e quando o módulo for **67 - SIGAAGRO.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o link e baixe o pacote de expedição contínua do módulo Faturamento, conforme o seu release: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**  
2. Via Vs-Code, aplique o pacote em seu ambiente.  
3. Reinicie o smartclient e refaça o processo de exclusão do contrato.

Obs. Para a aplicação de pacote, requer conhecimento da ferramenta VS\_Code, em caso de dúvidas sobre a ferramenta, contate a equipe de FrameWork.
