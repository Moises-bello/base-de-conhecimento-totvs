---
content_hash: b342b042d0cdfd242e2581a2c5a70c4a801fe02b4b1c0c61306670453bfbbb4d
fetched_at: '2026-06-29T00:09:22.724848+00:00'
page_id: '422546012'
product: rm
source: tdn-rm
title: Detalhamento de Combustível (Grupo Encerrante)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546012
version: 5
---

**Cadastros**

Para a geração das tag do grupo "encerrante" serão necessários os seguintes cadastros:

* Dados de combustível no [TOTVS Gestão de Estoques, Compras e Faturamento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948835)  em Cadastros | Mais... | [Combustível](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938172);
* Tributo do tipo "CIDE"  no [TOTVS Gestão Fiscal](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948859) através do menu Cadastros | [Tributos](http://tdn.totvs.com.br/display/LRM/Tributos);
* Código ANP no cadastro do produto em Anexos | [Dados Fiscais do Produto](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938199) | Tributação.

***Observação**:* Os dados informados nos cadastros devem ser alimentados de acordo com as necessidades do cliente.

Na criação do movimento será necessário selecionar o código do produto vinculado ao Volume de Venda e no Bico da Bomba.

Na geração do XML da NF-e serão geradas as TAGS no grupo LA11 - Encerrante através dos campos informados no Volume de Venda:  
 **TAG <<nBico>> -** Informação do campo identificador do Bico   
 **TAG** **<<nBomba>>** - Informação do campo identificador da Bomba  
 **TAG** **<<vEncIni>>** -   Informação do campo Valor da leitura inicial  
 **TAG** **<<vEncFin>>** -   Informação do campo Valor da leitura final

A **TAG** **<<nTanque>>** será preenchida com o Local de Estoque selecionado no movimento.

Lembrando que estes campos seguirão as regras de tamanho e quantidade definidos no manual do contribuinte.
