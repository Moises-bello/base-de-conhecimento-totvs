---
article_id: 8277765533079
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 2644362258c275eabf11b6ac1456b27c84ac87eb4037015f1751740fbb312222
fetched_at: '2026-06-28T22:42:00.865675+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos - Como gerar
  o registro 0205 quando há alteração no código do produto?
type: support-article
updated_at: '2022-08-19T12:14:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8277765533079-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-0205-quando-h%C3%A1-altera%C3%A7%C3%A3o-no-c%C3%B3digo-do-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o registro **0205** quando há alteração no código do produto?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**O registro **0205** é gerado quanto há alteração na **Descrição** ou na **Codificação do Produto**. Quando o código do produto é alterado não é possível replicar essa alteração diretamente no campo **Código - B1\_COD** do **Cadastro de Produtos** considerando a arquitetura e estrutura do **Protheus**.  
   
Uma vez criado o **Cadastro de Produto** e informado o **código** na sua inclusão não há uma forma segura de alteração desta informação, visto que, o código de produto é chave de busca e amarração para diversas rotinas de **Estoque, Compras, Faturamento, Fiscal, entre outros.**  
   
Dessa forma, para gerar o registro **0205** quando o código do produto sofrer alterações realize o seguinte processo:

1 - Ative o parâmetro **MV\_HISTTAB (.T.)** para que sejam gerados dados na tabela **AIF**

2 - Crie um novo **Cadastro de Produto** com as mesmas características do que está sendo alterado

3 - Na novo produto criado. aba **Outros** localize o campo **Cod Ant - B1\_CODANT** e informe o código antigo do produto 

4 - Gere uma movimentação e após o **Sped Fiscal**

**Importante:**

O registro **0205** só será gerado quando houver movimentação com o produto e não quando a alteração for realizada, ou seja, se a alteração ocorrer em um mês e a movimentação só ocorrer em período posterior, o registro **0205** só será gerado no mês da movimentação, conforme trecho abaixo do guia prático do Sped Fiscal

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8277719022999/mceclip0.png)
