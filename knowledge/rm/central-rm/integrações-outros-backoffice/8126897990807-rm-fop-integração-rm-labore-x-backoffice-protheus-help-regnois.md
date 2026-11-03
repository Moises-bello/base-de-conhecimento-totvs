---
article_id: 8126897990807
category: Integrações Outros BackOffice
content_hash: 65fd9803b05631949a1f5cd61563604e27527157e737b1137a79e005c73343f0
fetched_at: '2026-06-28T22:46:42.135369+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RM - FOP - Integração RM Labore x BackOffice Protheus - HELP: REGNOIS'
type: support-article
updated_at: '2025-02-03T19:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8126897990807-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-HELP-REGNOIS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:57 min****Ocorrência**Ao realizar alguma integração entre o **RM x Protheus**, é retornado o erro **AJUDA: REGNOIS.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Essa incidência acontece pois os não há o registro de alguma informação que está sendo enviada na integração não existe no destino.  
  
**Solução**O erro que é retornado ao tentar incluir ou alterar algum registro quando se utiliza a integração **RM x Protheus.**  
   
Quando tentamos inserir no **Protheus** por exemplo, com as mesmas informações que estão preenchidas no **RM**, irá retornar o mesmo erro como na print abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/Jk1YnhYJaBjTQqvJ8BxlMiFFF/?name=image.png)  
   
Isso ocorre pois**algum registro que o RM está enviando não existe no Protheus**, por exemplo:  
  
Enviamos o funcionário com **Centro de Custo** de código 25 com origem no **RM**, mas no **Protheus** no cadastro de **Centro de Custo** existe só até o registro 24.  
Dado o cenário acima é retornado o erro **REGNOIS,** direcionando a um entendimento por abreviatura como registro não existente.  
  
Para solucionar o incidente, deve-se verificar o XML do erro através do artigo [RH - RM - FOP - Integração RM Labore x BackOffice Protheus: Obtenção o XML mensagem de Resposta e Transformada no RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036176914) e identificando o campo no XML, será possível realizar o cadastro no ambiente destino.
