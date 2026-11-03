---
article_id: 4405084221207
category: RH - Férias
content_hash: bd3c5e24fe08c42272f9cccbf05ccf2bccff9a4cfce94ed62d0002585c73c5bc
fetched_at: '2026-06-28T22:43:58.319731+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: 'RH - Linha Protheus - GPE - No cálculo de Férias está apresentando o Log:
  Tabela de Imposto de Renda (Tabela S002) não cadastrada'
type: support-article
updated_at: '2025-08-13T19:11:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405084221207-RH-Linha-Protheus-GPE-No-c%C3%A1lculo-de-F%C3%A9rias-est%C3%A1-apresentando-o-Log-Tabela-de-Imposto-de-Renda-Tabela-S002-n%C3%A3o-cadastrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32036200366103) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Ao calcular Férias, é apresentado Log de Ocorrências com mensagem: **Tabela de Imposto de Renda (Tabela S002) não cadastrada**, porém para o ano do cálculo de Férias há registro na tabela S002-Imposto de Renda.**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Essa mensagem pode ser apresentada no log através de 2 inconsistências, em cadastros de períodos e no cadastro da manutenção de tabela S002. 

1. Na rotina **Períodos**, para o período em aberto do cálculo de Férias que está sendo efetuada, no roteiro FER, a coluna **Data Pagamento** está preenchida com um ano que **não consta** na **tabela S002** e **diferente do período selecionado**, note no exemplo abaixo que a coluna Data de Pagamento esta preenchida com o ano de 2023 (05/01/2023), sendo que o Período é 12/2022:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11300403917975)

Ajuste a coluna **Data de Pagamento** para a **data correta** de acordo com o **Período** em questão, no exemplo abaixo, a coluna **Data de Pagamento** foi ajustada de acordo com o **Período selecionado** (ano).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11300368603415)

2. Na rotina **Manutenção de tabelas**, as informações referente ao ano de férias gozadas não está cadastrado. No exemplo abaixo, o cálculo será realizado em Dezembro de 2022, porém os dias de férias gozadas será de 05/01/2023 à 03/02/2023. Repare que na tabela S002 não temos o registro de 2023.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11300868626327)

Ajuste a tabela S002 inserindo uma nova linha com as informações referente ao ano de férias gozadas. No exemplo abaixo, foi inserida uma nova linha com as informações de 2023 a coluna **Ano/Mês Ini** está preenchida com **202301** e a coluna **Ano/Mês Fim** preenchida com **202312.**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11301017294615)

**Observação:** Esse incidente pode ocorrer referente as tabelas S001, S002 e S004, pois anualmente essas tabelas sofrem ajustes de dados para o próximo ano.

**Saiba Mais**[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052262653-RH-Linha-Protheus-GPE-Como-efetuar-o-cadastro-de-per%C3%ADodo?source=search)  
[RH - Linha Protheus - GPE - Tabelas que sofrem alterações de um ano para o outro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000152881-RH-Linha-Protheus-GPE-Tabelas-que-sofrem-altera%C3%A7%C3%B5es-de-um-ano-para-o-outro?source=search)  
[RH - Linha Protheus - GPE - O que conferir quando não é executado o cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063018633-RH-Linha-Protheus-GPE-O-que-conferir-quando-n%C3%A3o-%C3%A9-executado-o-c%C3%A1lculo-das-f%C3%A9rias?source=search)  
[RH - Linha Protheus - GPE - Como criar e informar uma verba sem Identificador de cálculo nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002304442-RH-Linha-Protheus-GPE-Como-criar-e-informar-uma-verba-sem-Identificador-de-c%C3%A1lculo-nas-f%C3%A9rias?source=search)
