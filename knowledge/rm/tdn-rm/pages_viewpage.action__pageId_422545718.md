---
content_hash: 73ac488e47b7287ea7aa87b4a7aef00612e0685f0ed11a8a93c27cee8f466ede
fetched_at: '2026-06-29T00:09:20.612648+00:00'
page_id: '422545718'
product: rm
source: tdn-rm
title: Estornar Contabilidade (Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545718
version: 3
---

Através deste processo o usuário poderá estornar a contabilidade dos lançamentos fiscais dos lançamentos que já estão integrados ao lote zero.  
Nesta tela o usuário informa o lote contábil de estorno, histórico padrão e data de estorno.  
*****Observações*:****Ao selecionar um histórico as contas contábeis geradas através do estorno são associadas a este histórico. Caso não selecione nenhum Histórico Padrão, a contabilização de estorno será gerada com o Histórico Padrão original. Os históricos que esteja com a opção "Complemento não permitido" marcado no [TOTVS Gestão Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=198948832), não serão visualizados.  
O campo Data do Estorno será preenchido com a data do sistema, mas o usuário terá a opção de alterá-la caso necessário. O estorno será gerado na data informada pelo usuário, o usuário ainda poderá considerar a data de contabilização como a data de estorno.  
O sistema não irá efetuar o estorno de lançamentos em que estiverem nas seguintes condições:

* Lançamentos Fiscais pertencentes a Período Fiscal com status de ENCERRADO e Lotes Fiscais com status LIBERADO
* Lançamento CANCELADO ( No momento do CANCELAMENTO, o sistema já excluí a contabilização do lançamento gravando-o como "Não Contábil"
* Lançamentos que não tenham sido integrados ao lote 0 ( zero ) do [TOTVS Gestão Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=198948832).
