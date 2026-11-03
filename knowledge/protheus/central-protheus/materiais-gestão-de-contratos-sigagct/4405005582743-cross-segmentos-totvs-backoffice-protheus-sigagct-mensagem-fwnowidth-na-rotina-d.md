---
article_id: 4405005582743
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: dc85fdb8f7b6559e61b298759db556d01ccbc595e5c53cf7e61c2c88c5794230
fetched_at: '2026-06-28T22:37:23.908594+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Mensagem FWNOWIDTH
  na rotina de Medição CNTA121 ao selecionar a Planilha
type: support-article
updated_at: '2022-08-04T16:39:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405005582743-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Mensagem-FWNOWIDTH-na-rotina-de-Medi%C3%A7%C3%A3o-CNTA121-ao-selecionar-a-Planilha
---

**Dúvida**Ocorrência da Mensagem " FWNOWIDTH " na rotina de Medição CNTA121 ao selecionar a Planilha mencionando "Descrição" na mensagem

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405005272215/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

A mensagem de help FWNOWIDTH está relacionada a tentativa de inserção de uma informação em um campo, sendo que essa informação tem um tamanho maior do que o tamanho do campos comporta.  
  
Como ele acontece no momento da seleção da planilha onde são gatilhadas as informações dos itens e a mensagem menciona o campo "Descrição", muito possivelmente o tamanho do campo de Descrição do Item da Medição (**CNE\_DESCRI**) está com um tamanho menor que os campos de Descrição dos processo anteriores como o **B1\_DESC  (Cadastro de Produto)** e **CNB\_DESCRI (Item da Planilha no Cadastro do Contrato)** por exemplo.  
  
Dessa forma, orienta-se a verificação dos tamanhos dos campos de Descrição do Produto das tabelas SB1, CNB e também CNE e ajustando-os (principalmente o campo da CNE) no ambiente **(no Dicionário e Banco de Dados)** para estarem todos com o mesmo tamanho (o tamanho maior utilizado entre os campos).

***Obs:***   
Deve-se analisar na base de dados os tamanhos de campos ***tanto no Dicionário de Dados como também no Banco de Dados***, os quais devem estar compatíveis.

Caso necessário, orienta-se o apoio de um analista especialista em loco para a analise da base de dados.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
