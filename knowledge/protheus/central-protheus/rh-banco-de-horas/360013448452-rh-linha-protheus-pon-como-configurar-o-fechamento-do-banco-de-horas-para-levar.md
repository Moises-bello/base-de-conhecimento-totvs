---
article_id: 360013448452
category: RH - Banco De Horas
content_hash: 5cc405dd0a34fdd288a100d28ec03fbe533cb88803c9f3a218aa035b745f62af
fetched_at: '2026-06-28T22:44:54.159474+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON -  Como configurar o fechamento do banco de horas,
  para levar apenas as horas excedentes para a folha de pagamento
type: support-article
updated_at: '2025-11-07T19:29:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013448452-RH-Linha-Protheus-PON-Como-configurar-o-fechamento-do-banco-de-horas-para-levar-apenas-as-horas-excedentes-para-a-folha-de-pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33773034847255) Tempo aproximado para leitura: 01:00:00 min  
  
Dúvida**Como configurar o fechamento do banco de horas, para levar apenas as horas excedentes para a folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para demonstrar como o sistema efetua esse procedimento, será utilizado um exemplo onde o Banco de Horas do funcionário permite até 30 horas de banco o restante deve ser pago na folha de pagamento.  
  
- Funcionário tem saldo de 28,00 horas e 38,00 horas valorizadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607049285015)

Acessar a rotina: **Miscelânea> Fechamentos> Banco de Horas**, e deixar os parâmetros conforme imagem abaixo:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607008539031)

Desta forma o sistema efetuará a baixa somente do saldo acima do limite de 30 horas. Levando para o **Resultado** e posteriormente para a **Folha de Pagamento** o valor das horas excedentes.

**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
