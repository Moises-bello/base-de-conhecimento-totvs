---
article_id: 1500006008562
category: ADVPL - Classe e Função
content_hash: 2793238a2f3fc16a044af055ab31b671d19b7583811aff71feae9f9f6beff2b4
fetched_at: '2026-06-28T22:40:18.108993+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TmailManager: total
  de mensagens'
type: support-article
updated_at: '2022-06-14T17:20:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006008562-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TmailManager-total-de-mensagens
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como podemos capturar o total de mensagens de uma pasta (marcadores) com a classe **TmailManager**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.  
  
**Solução**Temos o método **GetNumMsgs*()*** que  trás o número total de mensagens existentes na caixa entrada. Nos métodos **GetAllFolderList**e **GetFolderList**, na 3° posição do *array*, trás o total de mensagens do pasta em questão.  
  
**Saiba mais**  
[TMailManager:GetNumMsgs](https://tdn.totvs.com/display/tec/TMailManager%3AGetNumMsgs)  
[TMailManager:GetAllFolderList](https://tdn.totvs.com/display/tec/tMailManager%3AGetAllFolderList)  
[TMailManager:GetFolder](https://tdn.totvs.com/display/tec/TMailManager%3AGetFolder)
