---
article_id: 4416677034647
category: Escrita Fiscal - CIAP
content_hash: 192b377a79f316e7cada042301751fcf729fe8b95c34e057c9b199162694ed7f
fetched_at: '2026-06-28T22:39:33.811999+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como criar cadastro
  CIAP quando é apresentada mensagem de crédito incorreto ou já apropriado? 
type: support-article
updated_at: '2021-12-21T19:40:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416677034647-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-criar-cadastro-CIAP-quando-%C3%A9-apresentada-mensagem-de-cr%C3%A9dito-incorreto-ou-j%C3%A1-apropriado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como criar cadastro CIAP quando é apresentada mensagem de crédito incorreto ou já apropriado?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

|  |  |
| --- | --- |
| **Produto:** | Microsiga Protheus |
| **Versões:** | Todas |
| **Ocorrência:** | Como criar cadastro CIAP quando é apresentada mensagem de crédito incorreto ou já apropriado? |
| **Passo a passo:** | Nestes casos, para que o bem seja incluído na manutenção CIAP, mesmo com NF de entrada lançada incorretamente e inserida informações para o Sped Fiscal corretamente, deve ser feito o seguinte procedimento:  1) Inclua um novo campo na tabela SF9 através do Configurador, por exemplo:  Campo: F9\_ITEMNF2 Tipo: Caracter Tamanho: 4 Decimal: 0 Formato: @! Contexto: Real Título: Item NF (Sped Fiscal) Texto: Incluir item nf entrada Modo de Edição: INCLUI Nível: 1  2) Altere a informação no parâmetro **MV\_F9ITEM,** para que na geração do Sped Fiscal seja verificado o item da nota fiscal a partir do novo campo criado, e não pelo campo padrão constante na SF9, exemplo de conteúdo: F9\_ITEMNF2  Caso não possua este parâmetro, seguem configurações:  Nome da Variável: MV\_F9ITEM Tipo: Caracter Conteúdo: <definido pelo cliente> Descrição: Indica qual campo da tabela SF9 é considerado para indicar o item da nota de entrada. Por padrão, este campo será criado com conteúdo F9\_ITEMNFE. Caso tenha necessidade, pode ser criado um campo na tabela SF9 através do configurador para informar o número do item de entrada e informar o novo campo neste parâmetro.  3) Inclua o bem na Manutenção CIAP, informando o código do item no novo campo criado, deixando em branco o campo F9\_ITEMNFE. |
