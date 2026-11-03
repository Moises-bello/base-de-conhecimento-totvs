---
article_id: 4403476544791
category: Escrita Fiscal - Impostos - Funrural
content_hash: 87d39b28232f1f837afaec72f5ba6c2472d5ec44c087a4edd908fd6e6837baf4
fetched_at: '2026-06-28T22:39:28.163699+00:00'
product: protheus
section_id: 1500001549822
source: central-protheus
title: MP - FIS - Configuração Arredondamento Imposto Funrural
type: support-article
updated_at: '2021-06-30T11:27:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403476544791-MP-FIS-Configura%C3%A7%C3%A3o-Arredondamento-Imposto-Funrural
---

**Dúvida**  
Como configurar o arredondamento do imposto Funrural?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – Todas as versões  
  
**Solução**  
1- Para configurar o arredondamento do imposto **Funrural** é necessário configurar o parâmetro **MV\_RNDFUN**:

**MV\_RNDFUN =** Informe o critério de arredondamento do **FUNRURAL**. As opções validas são: .T. Arredonda e .F. Trunca.

2- O parâmetro **MV\_RNDFUN** é Utilizado em conjunto com o parâmetro **MV\_RNDSOBR**:

1. Sempre que o **RNDSOBR** estiver como Falso, não teremos o tratamento das sobras e consequentemente os valores serão truncados por item.
2. Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* também como Verdadeiro, será efetuado o tratamento de arredondamento por item.
3. Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* como falso, será efetuado o tratamento de arredondamento no total do imposto (truncando por item e considerando a sobra).

3- Segue abaixo a tabela explicando como funciona o arredondamento. OBS: Detalhe no campo "soma sobras" detalhando que o próximo item pode arredondar, por causa das sobras do item anterior.  
![](https://totvssuporte.zendesk.com/attachments/token/lEioBVn3nTHOfFZHKL5mKhG3z/?name=inline1583227458.png)

Mais informações nas documentações abaixo:

<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=336407064>

https://tdn.totvs.com/display/public/PROT/FIS00024\_Arredondamento\_de\_Impostos
