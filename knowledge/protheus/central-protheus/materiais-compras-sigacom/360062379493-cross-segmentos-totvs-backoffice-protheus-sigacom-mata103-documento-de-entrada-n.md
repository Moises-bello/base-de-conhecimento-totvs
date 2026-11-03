---
article_id: 360062379493
category: Materiais - Compras (SIGACOM)
content_hash: a1dfba111b7cb2733f1de70c368f71bad80210c51d54080dd4b8e8d6b78cc131
fetched_at: '2026-06-28T22:41:20.082046+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA103 Documento de
  Entrada na Segunda Moeda / Moeda 2
type: support-article
updated_at: '2025-04-04T13:50:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062379493-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA103-Documento-de-Entrada-na-Segunda-Moeda-Moeda-2
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31164016035863)***Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**É possivel efetuar a inclusão de Documentos de Entrada, diretamente na segunda moeda?

**Ambiente**Microsiga Protheus - Compras/Estoque - Versão 12

**Solução**

A inclusão de documentos fiscais é efetuada sempre em moeda corrente (R$) isto por conta de controle de estoque e contábil, ou seja, o valor unitário será mantido em reais.  Caso exista pedido de compra cadastradoa na Moeda 2, o documento de entrada sempre será na moeda 1 real que é convertido o item da NF, porém pode-se gerar o titulo no contas a pagar na moeda 2, só que por padrão, o sistema só fará essa conversão mediante preenchimento da cotação da moeda no cadastro de moedas do sistema, e, sempre considerando a data de emissão da nota de entrada.

Por padrão, o sistema para gerar o título a pagar na moeda 2, ele vai buscar a taxa da moeda na data de emissão da nota.  
Dentro do documento de entrada na aba duplicatas ele vai sugerir a moeda 1, porém você pode alterar para 2, e aí o sistema vai converter o valor do título a pagar, considerando a taxa da moeda cadastrada no sistema, considerando a data de emissão da nota.  
Se houver a troca da moeda na inclusão da nota, na aba duplicatas, o título será gerado em moeda 2.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31164016037655)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
