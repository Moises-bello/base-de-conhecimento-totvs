---
article_id: 39556560809751
category: Meu RH - Gestão de Comunicados e Push Notification
content_hash: a57812ac7dc4ad0b229241898f2f3df71e8a50ec1d62dd8097c93fe8cbba5a1b
fetched_at: '2026-06-28T22:47:26.548240+00:00'
product: rm
section_id: 37779496229783
source: central-rm
title: RH - RM - Meu RH - Erro ao criar um novo Comunicado String or binary data would
  be truncated
type: support-article
updated_at: '2026-04-09T12:51:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39556560809751-RH-RM-Meu-RH-Erro-ao-criar-um-novo-Comunicado-String-or-binary-data-would-be-truncated
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39556560799383) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao criar um novo comunicado no RM para ser enviado aos usuários do Meu RH, retorna o erro **String or binary data would be truncated in table 'xxxxx.dbo.PCOMMUNICATEATTACHMENT', column 'ATTACHMENTNAMENAME**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39625474633239)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH – Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o sistema está tentando gravar um texto (nome do anexo) maior do que o tamanho permitido na coluna ATTACHMENTNAMENAME da tabela PCOMMUNICATEATTACHMENT.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Ajuste o nome do arquivo para que possua no máximo 50 caracteres;
2. Utilize nomes reduzidos e abreviados para poder economizar na quantidade de caracteres caso seja um título muito grande
3. Realize novamente o envio do anexo após o ajuste

Analisando a tabela **PCOMMUNICATEATTACHMENT**a coluna **ATTACHMENTNAMENAME possui o tamanho de 50 caracteres** e retornará o erro caso seja excedido esse valor.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39556560800023)
