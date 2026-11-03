---
article_id: 6214979985175
category: eSocial - Middleware
content_hash: f3ba75952cf9ed075ca119d1014208bf325b11ec2d3ce542c2415caeb3569556
fetched_at: '2026-06-28T22:47:05.572569+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: RH - RM - FOP - eSocial - Middleware - Como exportar XML de retorno do Governo
type: support-article
updated_at: '2026-06-05T17:53:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6214979985175-RH-RM-FOP-eSocial-Middleware-Como-exportar-XML-de-retorno-do-Governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23966275394071) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar a exportação de arquivos XML de retorno do governo no Middleware?  
  
**Ambiente**  
TOTVS RH - TOTVS RH - (Linha RM) - Folha de Pagamento - eSocial - A partir da release 12.1.33.255 e superiores  
  
**Solução**  
Após enviar os **Eventos S-1200, S-2299, S-2399, S-1210, S-1299,** sendo assim que aceitos, os totalizadores são retornados em seus respectivos registros. 

* S-5001 - Informações das contribuições sociais consolidadas por trabalhador - Retorno do S-1200, S-2299 ou S-2399;
* S-5002 - Imposto de Renda Retido na Fonte  - Retorno do S-1210;
* S-5003 - Informações do FGTS por Trabalhador - Retorno do S-1200 ou S-2299 ou S-2399
* S-5011 - Informações das contribuições sociais consolidadas por contribuinte - Retorno do S-1299;
* S-5012 - Imposto de Renda Retido na Fonte Consolidado por Contribuinte - Retorno do S-1299;
* S-5013 - Informações do FGTS consolidadas por contribuinte - Retorno do S-1299.

Para exportar o XML deverá seguir os passos abaixo:    
• Exportar **Totalizador individualmente**  
Na fila de eventos localize o evento que deseja exportar XML, clique na aba **Retorno da Integração  Salvar XML**.

![33333.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6269894696087)

• Exportar os **Totalizadores** em **Lote**  
É possível realizar a exportação em lote do XML de retorno do eSocial dos eventos periódicos. Para isso, acesse o menu  **eSocial |****Outros Processos | Exportar XML.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6216830392087)

**Importante**  
Após a entrada da Simplificação, os valores IRRF não serão retornadas através de evento S-5012. A verificação será possível através da DCTF(PGD) e pela DIRF.

***NOTA ORIENTATIVA S-1.0 01/2021:***

![](https://totvssuporte.zendesk.com/attachments/token/L2zZ3GBkDbDRj8C8RZ5ho6KgM/?name=inline-1511860906.png)​![](https://totvssuporte.zendesk.com/attachments/token/nKKH6S5dSXDFs2FG7WE1ncqiR/?name=inline-1783747739.png)

**Saiba Mais**  
[RH - RM - FOP - eSocial - Retorno do evento totalizador S-5012](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409648810391-RH-RM-FOP-eSocial-Retorno-do-evento-totalizador-S-5012)
