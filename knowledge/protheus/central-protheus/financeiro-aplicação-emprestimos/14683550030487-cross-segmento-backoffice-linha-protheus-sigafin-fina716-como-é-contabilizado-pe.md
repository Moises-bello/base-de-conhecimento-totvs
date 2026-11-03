---
article_id: 14683550030487
category: Financeiro - Aplicação / Emprestimos
content_hash: e4c1e33ef93f1072f295711d94944b26ea9f59f9637affa10e139027b9877356
fetched_at: '2026-06-28T22:37:59.402289+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - Backoffice linha Protheus -  SIGAFIN - FINA716 Como é contabilizado
  pelo LP 582 e 585 na apropriação e no resgate dos rendimentos mês a mês de uma aplicação
  por cotas FAF
type: support-article
updated_at: '2024-06-03T20:35:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14683550030487-Cross-Segmento-Backoffice-linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-contabilizado-pelo-LP-582-e-585-na-apropria%C3%A7%C3%A3o-e-no-resgate-dos-rendimentos-m%C3%AAs-a-m%C3%AAs-de-uma-aplica%C3%A7%C3%A3o-por-cotas-FAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:15:00 min****Dúvida**Como é contabilizado pelo LP 582 e 585 na apropriação e no resgate dos rendimentos mês a mês de uma aplicação por cotas FAF  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12

**Solução**

**Passo 1** - Ter cadastrado os lançamentos padrões

**LP 582** - Lançamento padrão de apropriação, utilizando a sintaxe **EH\_VALJUR** para obter o valor de rendimento mensal

**LP 585** - Lançamento padrão de resgate, utilizando a sintaxe **EH\_VALJUR** para obter o valor de rendimento total

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683549639319)](https://centraldeatendimento.totvs.com/hc/article_attachments/14683549639319)

Caso necessite contabilizar o valor do rendimento ou do imposto de renda mês a mês utilize o parâmetro com o conteúdo [MV\_RENAPL4 = "2" (Mensal)](https://tdn.totvs.com/pages/releaseview.action?pageId=571786367)

**Passo 2** - Cadastre como no exemplo o contrato bancário no dia 13/01/2020

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683665350039)](https://centraldeatendimento.totvs.com/hc/article_attachments/14683665350039)

E atualizar a cotação do dia

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683669949207)](https://centraldeatendimento.totvs.com/hc/article_attachments/14683669949207)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683643038999)](https://totvssuporte.zendesk.com/hc/article_attachments/14683643038999)

**Passo 3** - Cadastre a aplicação **FAF** conforme imagem, insira o número do contrato bancário, no exemplo abaixo vou comprar 238,31106100 unidades de cotas, onde 1 cota possui o valor de R$ 339,89190287 no dia 13/01/2020

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683707245719)](https://totvssuporte.zendesk.com/hc/article_attachments/14683707245719)

**Passo 4** - No final do mês de Janeiro vou fazer a **apropriação**, logo atualizo o contrato bancário o valor de 1 unidade de cota no dia 31/01/2020

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683759013911)](https://totvssuporte.zendesk.com/hc/article_attachments/14683759013911)

**Passo 5** - Ao realizar a apropriação, será chamado o **LP 582 - Lançamento padrão de apropriação**, e gravado no contábil o valor de R$ 192,52

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683898650007)](https://totvssuporte.zendesk.com/hc/article_attachments/14683898650007)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683932096535)](https://totvssuporte.zendesk.com/hc/article_attachments/14683932096535)

**Passo 6** - No final do mês de Fevereiro é feito uma apropriação, atualizo o contrato bancário o valor de 1 unidade de cota no dia 28/02/2020

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683940641431)](https://totvssuporte.zendesk.com/hc/article_attachments/14683940641431)

**Passo 7** - Faço a apropriação, será chamado o **LP 582 - Lançamento padrão de apropriação,** e gravado no contábil o valor de R$ 428,19

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14683997443351)](https://totvssuporte.zendesk.com/hc/article_attachments/14683997443351)

**Passo 8** - No final do mês de Março faço o resgate, atualizo o contrato bancário o valor de 1 unidade de cota no dia 31/03/2022

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14684023027223)](https://totvssuporte.zendesk.com/hc/article_attachments/14684023027223)

**Passo 9** - Faço o resgate

**Importante:** Ao fazer o resgate o sistema também irá fazer uma apropriação

Então será chamado o **LP 582 - Lançamento padrão de apropriação**, e gravado no contábil o valor de R$ 428,19 (que é o rendimento exclusivo do mês de Março)

Chamado o **LP 585 - Lançamento padrão de resgate**, e gravado no contábil o valor de R$ 1.048,90 (que é a soma do rendimento total de todos os mês)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14684186126999)](https://totvssuporte.zendesk.com/hc/article_attachments/14684186126999)

**Passo 10** - Conferência na contabilidade dos valores

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14684161093655)](https://totvssuporte.zendesk.com/hc/article_attachments/14684161093655)

**Saiba mais:**

[Empréstimos - FINA716](https://tdn.totvs.com.br/pages/releaseview.action?pageId=684987254)  
[Valores utilizados neste documento e utilização do parâmetro MV\_RENAPL4](https://tdn.totvs.com/pages/releaseview.action?pageId=571786367)  
[Exemplo\_de\_Contabilização\_de\_Aplicação\_e\_Empréstimo](https://tdn.totvs.com/pages/releaseview.action?pageId=236430682)  
[Aplicações e Empréstimos - Financeiro P12](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=392500138)
