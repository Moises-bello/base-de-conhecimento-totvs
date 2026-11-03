---
article_id: 360046095773
category: Controle de Não Conformidades (SIGAQNC)
content_hash: da95af76353b5299c263bf48686c897b7b5e12cbf6bb404d185f3228bdb31445
fetched_at: '2026-06-28T22:42:27.978065+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Help QNCDIRDCNE
type: support-article
updated_at: '2021-05-19T10:44:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046095773-Manufatura-Linha-Protheus-SIGAQNC-Help-QNCDIRDCNE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:40 min**  
**Ocorrência**Ao incluir uma **FNC - Ficha de Não Conformidade** na rotina **QNCA040 - Cadastro de FNC** é apresentado o *help* **QNCDIRDCNE**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**O *help* **QNCDIRDCNE** indica que o diretório definido no parâmetro **MV\_QNCPDOC - Define o diretório onde contem os arquivos dos Documentos** para o **Documento Anexo** não existe.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Configurar o parâmetro com o valor **\SYSTEM\DOCS**;  
2. Criar uma pasta com o nome **DOCS** dentro do diretório **\protheus\_data\system**.
