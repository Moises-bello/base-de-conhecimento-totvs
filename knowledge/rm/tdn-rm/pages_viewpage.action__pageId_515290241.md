---
content_hash: 067cfef62e4963ba5237361c660ef01b54122122c63bc888760421d60e439d16
fetched_at: '2026-06-29T00:10:26.872419+00:00'
page_id: '515290241'
product: rm
source: tdn-rm
title: Cotação - WebServices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515290241
version: 5
---

Segue um Fluxo com os Status possíveis na Cotação e cada processo responsável por alterá-los.

---

É possível realizar operações em cotações a partir de chamadas via Web Service.

Os Serviços disponíveis para serem chamados são:

**Assistente de Cotação**

**Nome do Método: ExecuteWithXmlParams**

**Nome do Processo: CmpAssistenteCotacaoProc**

Esse processo cria uma nova cotação. Em parametrizações normais, a cotação será criada com o Status **Composição.**

**Comunicar Fornecedores**

**Nome do Método: ExecuteWithXmlParams**

**Nome do Processo: CmpCotacaoComunicarFornecedoresProc**

Esse processo envia - por e-mail, impresso, ou para a Web - as cotações para os fornecedores inclusos na mesma.  O Status da cotação será alterado para **Aguardando Resposta Fornecedores.**

**Alterar Cotação**

**Nome do Método: SaveRecord**

**Nome do DataServer: CmpCotacaoData**

Por esse DataServer é possível alterar alguns dados da Cotação. Ele deve ser usado inclusive para Registrar os Orçamentos retornados pelos fornecedores.

Essa alteração será consistida exatamente como se fosse realizada pela tela. 

**OBS: Não se deve alterar o Status da Cotação por esse processo.**

**Calcular Quadro Comparativo**

**Nome do Método: ExecuteWithXmlParams**

**Nome do Processo: CmpCotCalculoQuadroComparativoProc**

Esse processo executa o cálculo do Quadro Comparativo para definir os vencedores da Cotação. O Status da cotação será alterado para **Negociação da Melhor Oferta.**

****Gerar Ordem de Compra****

**Nome do Método: ExecuteWithXmlParams**

**Nome do Processo: CmpOrdemCompraProc**

Esse processo gera a Ordem de Compra para os itens enviados no XML.

Se gerada a Ordem de Compra para todos os itens da Cotação, seu Status será alterado para **Pedido de Compra.**Caso não se gere para todos os itens, o Status será alterado para **Ordem de Compra Parcialmente Gerada.**
