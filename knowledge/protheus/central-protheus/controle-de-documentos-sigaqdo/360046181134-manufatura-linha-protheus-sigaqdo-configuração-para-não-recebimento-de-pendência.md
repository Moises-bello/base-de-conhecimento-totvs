---
article_id: 360046181134
category: Controle de Documentos (SIGAQDO)
content_hash: 7cff0817d715d4cdc4cad4b21cbf37a9fcecc25780fc52e51d7ea55c0750321f
fetched_at: '2026-06-28T22:42:28.977516+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Configuração para não recebimento de
  Pendência de Leitura
type: support-article
updated_at: '2021-05-11T19:49:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046181134-Manufatura-Linha-Protheus-SIGAQDO-Configura%C3%A7%C3%A3o-para-n%C3%A3o-recebimento-de-Pend%C3%AAncia-de-Leitura
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Como configurar o cadastro de documentos para o usuário não receber a **Pendência de Leitura**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**A configuração para o usuário não receber a **Pendência de Leitura** pode ser feita no cadastro de documentos, rotina **QDOA050 - Cadastro de Documentos** ou na distribuição do documento, rotina **QDOA110 - Distribuição de Documentos**. É necessário remover a bolinha vermelha existente no início da linha. Além disso, quando parâmetro **MV\_DISQDZ - Distribuidor do documento recebe pendência de leitura?** estiver ativo, indica que o usuário que realizar a distribuição do documento, também irá receber a **Pendência de leitura**.
