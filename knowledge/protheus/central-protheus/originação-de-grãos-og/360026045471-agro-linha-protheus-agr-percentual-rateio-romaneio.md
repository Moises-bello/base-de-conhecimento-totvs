---
article_id: 360026045471
category: Originação de Grãos (OG)
content_hash: 941ec1d0af30e47761c25c028bda421c6e9b6862f253e02ed597ae018dce0751
fetched_at: '2026-06-28T22:45:42.645408+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Percentual rateio romaneio
type: support-article
updated_at: '2025-06-23T15:51:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026045471-Agro-Linha-Protheus-AGR-Percentual-rateio-romaneio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20521814437399)*** Tempo aproximado para leitura: **00:00:40 min****Dúvida**Ao incluir um romaneio, na rotina de **Romaneio sem Pesagem - OGA251**, e informar na pesagem uma quantidade **com casas decimais após a vírgula**, mesmo que seja a mesma quantidade informada no contrato de venda, o Sistema apresenta a seguinte Mensagem: **A Soma do Percentual de Rateio por Entidade/Contrato deve ser igual a 100%.**  
O que é necessário realizar para que seja possível informar quantidade com casas decimais no Romaneio sem Pesagem?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**É necessário que seja alterado o conteúdo do parâmetro **MV\_OGDECPS** que determina a quantidade de decimais no peso dos Romaneios.  
Se o conteúdo do parâmetro estiver zerado, logo que o percentual é informado na tela o gatilho é disparado, desconsiderando as casas decimais, arredondando o valor informado.  
  
**Saiba Mais**  
No link abaixo há mais informações sobre o parâmetro MV\_OGDECPS.  
[Parâmetro MV\_OGDECPS - Definir Quantidade de Decimais p/ Campos de Peso no Romaneio](http://tdn.totvs.com/pages/viewpage.action?pageId=268596595)
