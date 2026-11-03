---
article_id: 28129642007703
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 084a0c84ac80ddd49f4ac64ea7291d0e8d02d850d2b340ad177f4c4fe07ae124
fetched_at: '2026-06-28T22:38:44.005449+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Bloquear ou fixar o pergunte
  de usuários no faturamento
type: support-article
updated_at: '2024-11-28T15:09:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28129642007703-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Bloquear-ou-fixar-o-pergunte-de-usu%C3%A1rios-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28129681432471) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como bloquear ou fixar o pergunte de algum usuário no faturamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

1 - Veja a janela com o pergunte que quer travar com algum valor ou restringir para algum determinado usuário.  
  
2 - Aperte no pergunte e veja o "nome dele":

![](https://totvssuporte.zendesk.com/attachments/token/D1DoXWnryTIZfcMgGLRD8h2pN/?name=image.png)  
No exemplo, é o MTA456, pergunte 01.  
  
3 - Vá no configurador, nesse caminho e inclua:

![](https://totvssuporte.zendesk.com/attachments/token/BFHv86wx7T0XAiwRd9SZai65g/?name=image.png)  
  
4 - Informe o grupo do pergunte e o usuário ou o grupo de usuário que terá um tratamento diferente para ele no cabeçalho:

![](https://totvssuporte.zendesk.com/attachments/token/VHLDxyIyoYqKDjXndDimsxxjJ/?name=image.png)  
Se o pergunte abaixo está "cinza/excluído", quer dizer que o usuário tem acesso. Ao desbloqueá-lo, o campo ficara "cinza" para o usuário, travado então.  
  
No teste, iremos "desbloquear" no configurador de pergunte para mudar o conteúdo dele para 4 (Todos os Bloq.), para assim travar a tela do pergunte do usuário em 4 (Todos os Bloq.), exemplo:

![](https://totvssuporte.zendesk.com/attachments/token/jSQYmqHio7P4oY0L3ZWuraTkH/?name=image.png)  
  
5 - Resultado:

![](https://totvssuporte.zendesk.com/attachments/token/yGQxPbpalw3klplR0id2dj9Cj/?name=image.png)

**OBSERVAÇÃO:** Dúvidas no processo acima, contate a Equipe Protheus Framework!

**Saiba mais:**

[FAT0320 - Permissões, acessos e privilégios no Protheus](https://tdn.totvs.com/x/tEZpMg)
