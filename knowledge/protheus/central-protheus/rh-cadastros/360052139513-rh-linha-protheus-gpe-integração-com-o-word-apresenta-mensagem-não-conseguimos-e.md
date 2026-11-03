---
article_id: 360052139513
category: RH - Cadastros
content_hash: c3611a73391d18c94c77dee6455a480aad648e984ad7a4eac76dd7d710faac95
fetched_at: '2026-06-28T22:43:25.930570+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: 'RH - Linha Protheus - GPE - Integração com o Word apresenta mensagem: Não
  conseguimos encontrar seu arquivo. É possível que ele tenha sido movido, renomeado
  ou excluído'
type: support-article
updated_at: '2025-07-15T16:37:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052139513-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-com-o-Word-apresenta-mensagem-N%C3%A3o-conseguimos-encontrar-seu-arquivo-%C3%89-poss%C3%ADvel-que-ele-tenha-sido-movido-renomeado-ou-exclu%C3%ADdo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26832678356887)** Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Na **Integração com Word** o sistema apresenta mensagem **Microsoft Word - Infelizmente, não conseguimos encontrar seu arquivo. É possível que ele tenha sido movido, renomeado ou excluído?**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10316900920087)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre quando realmente o arquivo modelo .dot foi corrompido ou quando está no servidor **linux** e contém em seu nome, algum **caractere especial** e/ou **letras maiúsculas,** como no exemplo abaixo onde o nome está: CT\_TESTE\_ADMINISTRATIVO.dot.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10316919897879)  
  
**Solução**Se o documento estiver corrompido, deve ser refeito e inserido no servidor novamente. Caso seja linux, altere o nome do arquivo dentro do servidor, **retirando os caracteres especiais** e **deixando todas as letras minúsculas**, isso é uma exigência do Linux de aceitar apenas dessa forma. Segue exemplo de como deve ficar:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10317015143319)

Após o ajuste, gere novamente o documento.

**Saiba Mais**[RH - Linha Protheus - GPE - Configuração para Impressão de Documentos no Word (GPEWORD)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwggIPXSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMTU2NTQ3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1wYXJhLUltcHJlc3MlQzMlQTNvLWRlLURvY3VtZW50b3Mtbm8tV29yZC1HUEVXT1JELQY7CFQ6DnNlYXJjaF9pZEkiKTU4MjhmOTlhLTY1NzctNDgzMy04YTBkLWZkZDAyMjIyODQ5ZAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDEdQRVdPUkQGOwhUOhJyZXN1bHRzX2NvdW50aRM%3D--51bca6bb1a43ad15f786c9a6454be2607678d9b3)  
[RH - Linha Protheus - GPE - Como gerar documentos na rotina Imprime Modelos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXXaDGBQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MjI4NTM3NDU5NDMtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8taW1wcmltaXItYXJxdWl2by1Nb2RlbG8tbm8tR1BFV09SRC0GOwhUOg5zZWFyY2hfaWRJIik1ODI4Zjk5YS02NTc3LTQ4MzMtOGEwZC1mZGQwMjIyMjg0OWQGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxHUEVXT1JEBjsIVDoScmVzdWx0c19jb3VudGkT--c9c45e5f3301d0fefcee9ec8f5af128d19582644)  
[Artigos Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)  
[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
