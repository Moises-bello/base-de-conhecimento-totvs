---
article_id: 360058399074
category: RH - Fechamentos
content_hash: 7f8de5176723e33cd5e89a5ec4c7cf91989c4c0b53b05e549078e2704378679a
fetched_at: '2026-06-28T22:44:48.893883+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Fechamento de Banco de Horas para funcionário com
  saldo final credor, devedor ou ambos
type: support-article
updated_at: '2025-06-13T17:19:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058399074-RH-Linha-Protheus-PON-Fechamento-de-Banco-de-Horas-para-funcion%C3%A1rio-com-saldo-final-credor-devedor-ou-ambos
---

**Dúvida**Como fechar o BH para funcionário com saldo final credor, devedor ou ambos  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**No Fechamento de Banco de Horas, Acessando a rotina Miscelanea-Fechamentos-Banco de Horas, temos uma pergunta 'Resultado?'  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101016713)  
  
Abaixo demonstro a funcionalidade de cada opção do parâmetro 'Resultado?',são três opções: Credor, Devedor ou Saldo.  
  
Quando utilizado o parâmetro 'Resultado?' igual à Credor, apenas os funcionários com saldo final positivo terão o fechamento realizado, veja exemplo prático:  
  
Antes do fechamento temos dois funcionários um com saldo negativo e outro com positivo.   
Funcionário com saldo negativo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31943354394391)  
  
Com saldo Positivo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31943348874775)  
  
Veja que quando executei o fechamento do BH utilizando o parâmetro 'Resultado?' igual à Credor, ficou o BH da seguinte forma:  
  
o Funcionário que estava com saldo negativo não foi dado baixa:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31943354410007)  
  
Já o funcionário que estava com saldo positivo foi dado baixa:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31943348885143)  
  
Caso selecionarmos o parâmetro 'Resultado?' igual à Devedor, somente terão o banco de horas fechados, os funcionários com saldo final negativo. Veja exemplo prático:  
  
O funcionário com saldo negativo foi dado a baixa:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31943354415767)  
  
Já o funcionário com saldo positivo não foi dado a baixa:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31943354421399)  
  
Por fim, se a opção estiver como Saldo, todos os funcionários terão o fechamento de banco de horas realizado após o processamento.  
  
**Saiba mais:**[MP - PON - Limita Descontos no Fechamento de Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060213973-MP-PON-Limita-Descontos-no-Fechamento-de-Banco-de-Horas?source=search)  
[RH - Linha Protheus - PON - Como efetuar o fechamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas?source=search)
