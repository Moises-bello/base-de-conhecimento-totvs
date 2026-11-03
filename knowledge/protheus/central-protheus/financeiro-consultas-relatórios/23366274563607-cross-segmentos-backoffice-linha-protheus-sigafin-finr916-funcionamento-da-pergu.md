---
article_id: 23366274563607
category: Financeiro - Consultas / Relatórios
content_hash: 564c3bad3a175c239030302ba795b7630e261f24737b7b885f583464929fed0b
fetched_at: '2026-06-28T22:37:58.506255+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR916 - Funcionamento
  da pergunta "Bandeira - Software Express ? " do relatório
type: support-article
updated_at: '2024-05-09T13:47:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23366274563607-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR916-Funcionamento-da-pergunta-Bandeira-Software-Express-do-relat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23366303451415) Tempo aproximado para leitura: **00****:05:00 min** **Dúvida**Qual o conceito da pergunta MV\_PAR02 do relatório FINR916 e como adicionar mais códigos de bandeiras?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões  
  
**Solução**

É possível realizar inclusão de novas bandeiras na pergunta **MV\_PAR02** do relatório **FINR916**.

Segue explicação como adicionar mais códigos de bandeiras.

Esse filtro só ira funcionar para operadora Software Express.

No momento que informar o código na **pergunta 2**, ele ira amarrar com o campo **FIF\_CODRED**( **Tabela onde fica as importações**).

Para cadastrar o código da operadora e apresentar na consulta padrão, deve incluir na **tabela genérica G3**, conforme exemplo abaixo:

Lembrando que para que funcione esse novo cadastro, a operadora deve ser **Software Express**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23366274546839)

Para incluir novas bandeiras, acesse:

**SIGACFG > Base de dados > Dicionário de dados > Tabelas genéricas > Procure pela tabela G3**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23366303454487)

Após isso, clique no botão incluir e configure da forma que necessita, no exemplo abaixo foi criado a bandeira **"TESTE"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23366274548631)

Saiba mais: [FINR916- Relatório de Conciliação - Pagamentos e Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=655196758)
