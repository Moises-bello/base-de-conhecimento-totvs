---
article_id: 360026451971
category: ADVPL - Classe e Função
content_hash: d3a5114448cd7a0921ea3fd2550be7d65bd3e2347b323727ca3be4c56357af37
fetched_at: '2026-06-28T22:40:15.571311+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como solicitar confirmação
  de leitura atraves da Classe TMailMessage
type: support-article
updated_at: '2022-01-05T14:45:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026451971-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-solicitar-confirma%C3%A7%C3%A3o-de-leitura-atraves-da-Classe-TMailMessage
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como solicitar a confirmação de Leitura de um e-mail através da Classe TmailMessage?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Existe uma tag  ( Disposition-Notification-To ) que pode ser incluída no *Header* da mensagem para que seja solicitação a confirmação de leitura. Segundo parâmetro é o e-mail de onde foi disparado.  
Exemplo:

```
 oMessage := TMailMessage():New()  
 oMessage:AddCustomHeader( "Disposition-Notification-To", "rodrigo.abcdfg@empresa.com.br" )
```

Observação: Não é possível forçar o receptor enviar a confirmação, visto que está tarefa é do servidor de E-mails.   
 **Saiba Mais**[TMailMessage](http://tdn.totvs.com/display/tec/Classe+TMailMessage)
