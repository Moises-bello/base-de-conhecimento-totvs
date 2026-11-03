---
article_id: 31351805490199
category: Gestão de Transportes (TMS)
content_hash: 816bf5f55c72b053e47ce503207c8810a96bc5623e0d2e1eb3c14a31d924a86c
fetched_at: '2026-06-28T22:45:29.319192+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Inclusão de CTe via Painel de Agendamentos
  não gatilha dados
type: support-article
updated_at: '2025-04-11T21:58:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31351805490199-Log%C3%ADstica-Linha-Protheus-TMS-Inclus%C3%A3o-de-CTe-via-Painel-de-Agendamentos-n%C3%A3o-gatilha-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31351805463063) Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Na rotina **TMSAF76 - Painel de Agendamentos**, ao incluir um documento na aba **Nfs Cliente**, não gatilha dados do agendamento para a digitação do documento.  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Causa**O gatilho das informações do agendamento depende do preenchimento do produto no agendamento na tabela **DF2 - Produtos por Agendamento**. Sem o produto preenchido no agendamento, não irá gatilhar nenhuma informação na inclusão de documentos.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

* Ao incluir ou copiar um agendamento, navegue no grid até o campo **Produto(s)**e clique no campo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31351805465495)

* Será exibida a tela de **Produtos por Agendamento**, onde deve preencher os produtos que serão transportados e suas devidas quantidades.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31351805466903)

Com os produtos preenchidos, clique em **Salvar** e continue o preenchimento e grave o agendamento.   
  
Quando for incluir um documento na aba **Nfs Cliente**, serão gatilhados os dados do agendamento para o documento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31351814036631)

Se não preencher o produto no agendamento, a inclusão de documentos virá em branco:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31351814039959)
