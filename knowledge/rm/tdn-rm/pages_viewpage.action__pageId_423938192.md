---
content_hash: a8f312e47eb627ab1464db6cb5b8ad4a786395c74f6d8c625bd7ac7641f2a099
fetched_at: '2026-06-29T00:09:25.883441+00:00'
page_id: '423938192'
product: rm
source: tdn-rm
title: Conhecimento de Transporte Rodoviário de Cargas (CTRC)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938192
version: 6
---

O Conhecimento de Transporte Rodoviário de Cargas é o documento onde se encontra toda a informação inerente ao transporte de uma mercadoria.   
Utilizado pela unidade fiscalizadora para verificar a veracidade das mercadorias descritas na Nota Fiscal com as mercadorias Transportadas (descritas na NF de Conhecimento de Transporte).   
O TOTVS Gestão de Compras, Estoques e Faturamento está apto controlar tanto a emissão quanto o recebimento de documentos de conhecimento de transporte rodoviário.  
Os principais dados referentes a mercadoria transportada são:

* Dados do remetente e destinatário;
* local de coleta e entrega da mercadoria;
* peso;
* quantidades;
* Notas Fiscais relacionadas;
* e valores componentes do Frete.

**CTRC de Saída**: A emissão do CTRC normalmente ocorre nos movimentos de saída (2.2.XX), onde o usuário informa os dados pertinentes ao CTRC e vincula as notas fiscais das mercadorias a serem despachadas para o destinatário. A inclusão do movimento é feita normalmente enfatizando-se o preenchimento dos dados nas abas "Transporte" e "CTRC".   
   
**CTRC de Entrada**: No recebimento das cargas são inclusas duas movimentações distintas. Uma é referente à entrada do CTRC e outra referente à entrada das notas fiscais vinculadas ao CTRC correspondente. Tais movimentações devem ser parametrizadas respectivamente como: Cadastrar CTRC e Indicar CTRC.

**Cadastrar CTRC**: É na movimentação de entrada parametrizada como "cadastro de CTRC" que o usuário informa os dados referentes ao conhecimento de transporte da carga recebida.

**Indicar CTRC**: A movimentação parametrizada como "Indicar CTRC" recebe as notas fiscais das mercadorias contidas na carga. As notas fiscais referentes a um determinado CTRC de entrada devem ser vinculas nesta movimentação.

Informações Adicionais

* [Conhecimento de Transporte de Entrada](http://tdn.totvs.com/display/LRM/CTRC+-+Conhecimento+de+Transporte+de+Entrada)
* [Conhecimento de Transporte de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=4813132)
* [Alteração na Contabilização de Movimento Associado ao CTRC](http://tdn.totvs.com/pages/viewpage.action?pageId=423938374&moved=true)
