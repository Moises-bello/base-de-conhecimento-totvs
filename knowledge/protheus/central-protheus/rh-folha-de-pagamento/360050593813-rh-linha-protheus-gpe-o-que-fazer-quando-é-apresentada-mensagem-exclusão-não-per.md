---
article_id: 360050593813
category: RH - Folha de Pagamento
content_hash: 78de6eff74103d9f03d8e05d28e447b803aadff1b589ceec6620f5c858c6b219
fetched_at: '2026-06-28T22:44:16.039763+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: 'RH - Linha Protheus - GPE - O que fazer quando é apresentada mensagem: "Exclusão
  não permitida pois a verba foi encontrada na tabela SRC" ao tentar excluir uma verba'
type: support-article
updated_at: '2024-09-10T19:02:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050593813-RH-Linha-Protheus-GPE-O-que-fazer-quando-%C3%A9-apresentada-mensagem-Exclus%C3%A3o-n%C3%A3o-permitida-pois-a-verba-foi-encontrada-na-tabela-SRC-ao-tentar-excluir-uma-verba
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26278240241687) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Ao tentar excluir uma verba gerada ou lançada na rotina Lançamento por Verbas ou Lançamento por Funcionários, sistema apresenta a mensagem "Exclusão não permitida pois a verba foi encontrada na tabela SRC", o que deve ser feito?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**Para conseguir excluir a verba, deve ser realizado o cancelamento de cálculo pela rotina Cancelamento de Cálculo (GPEM160) através do caminho >Miscelânea >Cálculos >Cancelamento de Cálculo, os parâmetros devem ser preenchidos de acordo com a verba a ser cancelada, abaixo exemplo:  
  
Se a verba foi **gerada** (coluna Origem em Lançamento por Verbas ou Lançamentos por Funcionários com G), a pergunta Tipo de Cancelamento deve ficar GERADOS conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076420333)  
  
Se a verba foi **informada** (coluna Origem em Lançamento por Verbas ou Lançamentos por Funcionários com I), a pergunta Tipo de Cancelamento deve ficar INFORMADOS conforme exemplo abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076424553)  
  
Após o cancelamento do cálculo da verba, o sistema permitirá a exclusão da mesma pela rotina Lançamento por Verba ou Lançamento por Funcionários.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
