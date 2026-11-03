---
article_id: 5456139463447
category: Faturamento - Cadastros
content_hash: 80a48a7d38e18bc55b8169d88e4a1e834c779896abfe67fd388133be1e467e80
fetched_at: '2026-06-28T22:38:35.381430+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -Sigafat - FWFORMCANCEL
  - SA1MASTER
type: support-article
updated_at: '2022-04-14T20:59:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5456139463447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-FWFORMCANCEL-SA1MASTER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao excluir um registro do cadastro de cliente utilizando a rotina crma980, gera o HELP: Fwformcancel - problema violação de integridade.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5455905566743/mceclip0.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -Sigafat - Todas as versões  
  
**Causa**Ajuste realizado nas funções de inclusão da tabela AO4 melhorando a chave de relacionamento entre tabelas.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote expedição continua conforme o release vigente utilizado: [SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)  
2. Via Vs-code, aplique o pacote em seu ambiente.  
3. Posteriormente, reinicie o smartclient e efetue o procedimento novamente.

Obs. sempre aplicar o pacotes primeiramente em ambiente de homologação  para validação, e posteriormente aplicar em ambiente de produção.

O pacote deve ser aplicado por um analista que tenha pelo conhecimento de uso do Vs-Code. Em caso de ambiente no Cloud Totvs, efetuar a abertura do ticket para a o Cloud e solicitar a aplicação.
