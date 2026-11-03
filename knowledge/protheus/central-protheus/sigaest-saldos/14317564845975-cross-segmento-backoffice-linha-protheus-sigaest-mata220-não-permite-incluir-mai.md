---
article_id: 14317564845975
category: SIGAEST - SALDOS
content_hash: 693ff96a0208a188bbc9d5055cfe3b953ad16de826243dff18bd46701201d9e0
fetched_at: '2026-06-28T22:39:14.882010+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA220 - Não permite
  incluir mais de um Lote nos Saldos Iniciais
type: support-article
updated_at: '2023-05-03T10:53:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14317564845975-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA220-N%C3%A3o-permite-incluir-mais-de-um-Lote-nos-Saldos-Iniciais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Na rotina de ***Saldos Iniciais (MATA220)*** não permite incluir mais de uma linha informando um Lote diferente. Ao digitar seta para baixo não inclui uma nova linha. Ao clicar em Salvar exibe o ***HELP A220QTLOTE*** e não conclui a inclusão. Obrigando informar todo o saldo inicial em apenas um Lote. É possível incluir o Saldo Inicial em mais de um Lote? Como proceder?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14317731498007)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14317767485335)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Para esse cenário alterar o parâmetro **MV\_A390QTD** para **.F.**. ***Obs.:*** Caso desejar pode-se manter o parâmetro igual a .T., incluindo todo o Saldo Inicial do produto para um Lote específico, em seguida utilizar a rotina TRANSFERÊNCIAS MÚLTIPLAS (MATA261) destinando saldo aos Lotes desejados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14317926218647)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14317962995095)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre SALDOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)

[SIGAEST - Como ativar o controle de Lote/Rastro para produtos com saldo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-ativar-o-controle-de-Lote-Rastro-para-produtos-com-saldo-)
