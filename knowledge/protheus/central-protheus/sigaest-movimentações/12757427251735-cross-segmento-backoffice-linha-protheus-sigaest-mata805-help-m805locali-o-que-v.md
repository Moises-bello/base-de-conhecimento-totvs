---
article_id: 12757427251735
category: SIGAEST - MOVIMENTAÇÕES
content_hash: cacd01a63ef1a2386f92ba8d6de3bbc2dc158de87034d4fd17b09de850e62567
fetched_at: '2026-06-28T22:38:57.185052+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA805 - HELP M805LOCALI
  o que verificar ao exibir esse help?
type: support-article
updated_at: '2025-03-12T12:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12757427251735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA805-HELP-M805LOCALI-o-que-verificar-ao-exibir-esse-help
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O que devo verificar no ambiente ao exibir o ***HELP M805LOCALI***?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12757565570199)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**O Help **M805LOCALI** pode ser exibido nas seguintes situações:

***- 1º -*** O campo **B1\_LOCALIZ** estar configurado igual a **"Não"** controla Endereço. Alterar o campo para **"Sim"**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12757870458903)

***- 2º -*** O parâmetro **MV\_LOCALIZ** estiver configurado igual a "**N"**, Esse parâmetro deve esta configurado igual a **"S"**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12757983957271)

***- 3º -*** Caso utilizar o parâmetro **MV\_ARQPROD** igual a **SBZ** deve verificar na rotina de ***INDICADORES DE PRODUTOS (MATA019)*** se esta indicando o Produto para Controlar Endereço **(BZ\_LOCALIZ)** na Filial que esta tentando alterar o controle do produto. *[Clique aqui e veja a FAQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060937474-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-alterar-B1-LOCALIZ-com-SB1-compartilhada-e-MV-LOCALIZ-MV-ARQPROD-?source=search)* sobre o parâmetro MV\_ARQPROD.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12758103762199)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12758229810455)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
