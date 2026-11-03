---
article_id: 360045359514
category: Faturamento - Cenários de Venda
content_hash: dab3d993b7d2dce56f4747d78b343459273a2a8f7f7c29af913ce29b8392976f
fetched_at: '2026-06-28T22:38:33.887085+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus)  - FAT - Uso do campo Preço
  Máximo DA1_PRCMAX da Tabela de Preço
type: support-article
updated_at: '2023-01-30T21:13:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045359514-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Uso-do-campo-Pre%C3%A7o-M%C3%A1ximo-DA1-PRCMAX-da-Tabela-de-Pre%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao inserir um Produto na Tabela de Preço(**OMSA010)** e preencher o campo Preço Maximo (**DA1\_PRCMAX)**,na inclusão do Pedido de Vendas (**MATA410)**, o sistema aceita incluir Pedido com valor maior que o informado no campo **DA1\_PRCMAX**.  Porque não está fazendo nenhuma trava?  
   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  - Faturamento - A partir da versão 11.80  
  
**Solução**O campo **DA1\_PRCMAX**somente é utilizado pela rotina **MATA926,** não tem nenhum efeito na rotina de**Pedido de Vendas MATA410. .**

É um campo para uso de processamento do **SPEDFISCAL**: **[Manual Utilização SPEDFISCAL](http://tdn.totvs.com.br/pages/viewpage.action?pageId=238035285)**

**Saiba Mais:****[Documentação Tabela de Preços](https://tdn.totvs.com/pages/releaseview.action?pageId=224453270)**
