---
article_id: 10108982081687
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 09d1ea1d4b3511e5e00c14f8f79724cb61ed08fd1ea16c18172dbe0ce09c29cf
fetched_at: '2026-06-28T22:38:58.551353+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAEST - D1_OP em Branco Documento
  de Entrada
type: support-article
updated_at: '2022-11-09T14:03:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10108982081687-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAEST-D1-OP-em-Branco-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao informar a Ordem de Produção no campo D1\_OP em um documento de entrada, o sistema não está acatando a informação da OP.

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ESTOQUE/CUSTOS  
  
**Solução**

Para corrigir este problema acesse o módulo Configurador (SIGACFG) em Base de Dados > Dicionário > Gatilhos.  
Selecione o campo D1\_OP e clique para editar.  
Altere o contradomínio (X7\_CDOMIN) do gatilho de D1\_OP para D1\_ORDEM conforme abaixo e salve a alteração.

![D1_OP.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10108925300119)

**Saiba mais em :**

[Gatilho D1\_OP](https://tdn.totvs.com/x/t04hH)
