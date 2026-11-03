---
article_id: 12158196499991
category: Administração de Pessoal
content_hash: d8e08dbb687022bc66c303fb2972c7cd366592fd2c1f95e81098047e48fb71c4
fetched_at: '2026-06-28T22:47:01.259075+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - Eventos: cadastro de outros itens do nome de totalizador'
type: support-article
updated_at: '2025-01-21T19:54:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12158196499991-RH-RM-FOP-Eventos-cadastro-de-outros-itens-do-nome-de-totalizador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:07 min****Dúvida**No módulo Folha de Pagamento, como cadastrar outros itens para seleção do campo Totalizador localizado no cadastro de eventos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O cadastro de novos itens para as opções exibidas no campo **Totalizador** é realizado através da tabela dinâmica **INT33**, conforme abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12157702990487)  
  
É necessário parametrizar a opção **Sistema** no canto superior esquerdo como **Folha de pagamento.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12157809160599)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12157884005399)**

Após, realize a busca diretamente pelo código **INT33** ou pela descrição, como foi feito no exemplo acima. Localizada a tabela, basta clicar sobre a mesma e será exibida a janela com seus dados. Para cadastrar um novo item, é necessário acessar a aba **Itens da tabela** e selecionar a opção **Incluir**, onde será apresentada a janela abaixo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12157948077079)

Dessa forma, a informação será apresentada para seleção no campo **Totalizador**.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12158031114903)
