---
article_id: 37153386600983
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f6576e4fe2fc01daf1394adcae1a39bb532933736f74a8a795b7c3352633c876
fetched_at: '2026-06-28T22:38:55.515281+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Excluir do Documento
  apresenta Help para estornar o endereçamento.
type: support-article
updated_at: '2026-01-20T12:27:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37153386600983-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Excluir-do-Documento-apresenta-Help-para-estornar-o-endere%C3%A7amento
---

Ao excluir um documento de entrada com produto que começou a controlar endereço após a entrada, o Protheus exige selecionar endereços válidos com saldos para estorno, conforme mensagem nativa do sistema. Esse procedimento surgiu na atualização de novembro do pacote de expedição contínua. O processo envolve alterar o controle de endereço do produto, ajustar saldos na rotina MATA805 e, ao excluir a nota, selecionar o endereço para estornar o endereçamento e a nota corretamente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37153405867799) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao excluir um documento de entrada, com um produto que não controla endereço e depois começou a controlar endereço, na exclusão da nota apresenta um HELP como proceder ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153405869847)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A mensagem apresentada na exclusão do documento de entrada "Identificamos um ou mais itens que passaram a controlar localização após a entrada deste Documento de Entrada. Para prosseguir com estorno/exclusão do documento, **É OBRIGATÓRIO**, selecionar o endereços válidos e com saldos a serem estornados. É uma mensagem nativa do Protheus.  Começou apresentar na nova atualização do pacote de expedição continua do mês de Novembro atualizando o fonte **BACKOFFICE.STOCK.ANALYSISDELETEORREVERSAL.TLP**.

Segue o cenário para ocorrer a mensagem:

1. Incluir um documento de entrada sem controlar endereço.
2. Realizar a entrada do documento.
3. Acessar o cadastro do produto clicando em alterar, mudar o campo de endereço para o produto controlar endereço e dar o saldo para o endereçamento na rotina MATA805.
4. Acessar a rotina MATA805 para dar o saldo do produto, para o endereço que deseja.
5. Ao excluir a nota controlar endereço, apresentará o HELP padrão do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153386591127)

Selecionar o endereço disponível para fazer o estorno do endereçamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153405870615)

Ao selecionar o endereço disponível já faz o endereçamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153405872023)

Iniciando o estorno do endereçamento e o estorno da nota.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153386594327)

Excluindo a nota e estornando o endereçamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153386594967)

Consulta F4 do produto demostrando os saldos estornados como o nativo do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153386596119)

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
