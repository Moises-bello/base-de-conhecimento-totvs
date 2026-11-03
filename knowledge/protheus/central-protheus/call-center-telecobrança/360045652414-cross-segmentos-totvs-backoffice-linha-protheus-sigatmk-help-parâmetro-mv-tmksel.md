---
article_id: 360045652414
category: Call Center - Telecobrança
content_hash: 9396aa4df1bac67142688b52067749674b14ea950b0269eea11983e0dddd6cdd
fetched_at: '2026-06-28T22:41:28.649691+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Help parâmetro
  MV_TMKSELV habilitado
type: support-article
updated_at: '2022-06-22T17:19:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045652414-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Help-par%C3%A2metro-MV-TMKSELV-habilitado
---

**Ocorrência**

Ao acessar a rotina de **Pré atendimento** o sistema informa que: "O **parâmetro MV\_TMKSELV** está **habilitado** para buscar os **títulos mais antigos** de **maior valor** na solicitação de novo pré-atendimento, mas o **dicionário de dados** não foi **ajustado**."  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-A partir da versão 11.80.  
  
**Causa**

Ao habilitar o parâmetro o sistema necessita que sejam criados os campos **K1\_SALDO** e **K1\_SALDEC** na tabela **SK1** do sistema, precisa também do **índice 5** da tabela **SK1**.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Atualize o **Dicionário de Dados** e execute o **UPDDISTR** para atualização das tabelas (este processo precisa ser realizado por analista especialista);

2. Outra opção é **realizar a criação dos campos** e do **índice** via **configurador**, seguindo as configurações da documentação: **<https://tdn.totvs.com/pages/releaseview.action?pageId=6787683>**
