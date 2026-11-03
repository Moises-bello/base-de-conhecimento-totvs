---
article_id: 36119357140887
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 7bced65f28a2bd231a3201825fe92519d4422be422d61f65b3669a268730c2a3
fetched_at: '2026-06-28T22:42:27.996331+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Não envia imagem no e-mail
type: support-article
updated_at: '2025-11-07T00:00:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36119357140887-Manufatura-Linha-Protheus-SIGAQNC-N%C3%A3o-envia-imagem-no-e-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36119404213143) Tempo aproximado para leitura: **00:00:40 min**  
  
**Dúvida**  
Na rotina **QNCA040 - Cadastro de Não Conformidades** ao enviar um *e-mail* de relatório, o *e-mail* recebido **não contém a imagem** do relatório em anexo. Como proceder?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Solução**  
Para solucionar essa questão, realize os seguintes passos:  
1. Mantenha a **rotina atualizada**. Atualização disponível em: [Expedição Contínua SIGAQNC - Controle de Não-Conformidades](https://tdn.totvs.com/pages/releaseview.action?pageId=566491913)  
2. Validar o *appserver.ini*, confirmando se está definida a chave como **StarPath =\system\** . Caso esteja como **StarPath =/system/** não enviará imagem em anexo no *e-mail*.
