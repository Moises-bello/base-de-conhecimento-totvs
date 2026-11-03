---
content_hash: 7413da765796926d137894353602ec093c70830a0684d1c07dc3dfe1b41eb8a2
fetched_at: '2026-06-29T00:09:21.199147+00:00'
page_id: '422545863'
product: rm
source: tdn-rm
title: Crédito e Débito Extemporâneo (Outras Informações)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545863
version: 4
---

**Crédito Extemporâneo**

**1)** Uma NF de entrada foi registrada em período anterior de forma incorreta, sem o preenchimento do crédito correspondente:  
 Neste caso o contribuinte deverá incluir um Lançamento de Outros Créditos referente ao Crédito Extemporâneo. Este Lançamento de Outros Créditos deverá compor o Registro de Apuração do ICMS no campo referente a Outros Créditos.  
 **2)** Uma NF de entrada deixou de ser registrada em período anterior:  
 Neste caso o contribuinte deverá incluir esta nota fiscal no Registro de Entrada com Valor Contábil e Outros ICMS preenchidos. O Valor ICMS deverá se encontrar zerado. Além disso, devem ser preenchidos os dados do cabeçalho da NF e a coluna observações deverá receber o valor do crédito extemporâneo e o motivo.  
    
 **Débito Extemporâneo**

**1)** Uma NF de saída foi registrada em período anterior de forma incorreta, sem o preenchimento do débito correspondente:  
 Para esta situação, deve-se apenas gerar uma guia de ICMS correspondente ao valor do débito. Mesmo que o período em que a nota foi registrada tenha sido encerrado com saldo credor superior ao débito, o contribuinte deverá pagar a guia. Neste caso funciona como uma punição pela informação indevida.  
 **2)** Uma NF de saída deixou de ser registrada em período anterior:  
 Para esta situação uma guia também deverá ser paga com o valor do débito.  
 A nota deverá ser informada no Registro de Saídas atual com os dados do cabeçalho, o Valor Contábil e Outros ICMS. Em Observações deverão ser informados o valor do débito extemporâneo e o motivo. A data do Registro de Saída deve receber a data de emissão, referente ao mês em que a nota foi emitida, exemplo: NF emitida em setembro, porém foi informada no registro de saída de dezembro. A data é a de setembro.   
 Notas Fiscais de Entrada e Saída (Extemporâneas) devem ser informadas nos livros fiscais com as datas originais, exemplo:

**Entrada:** emissão em 15/07/2005 e entrada no estabelecimento em 20/07/2005. Se a NF não foi para o Registro de Entradas de Julho / 2005 e pretendemos registrá-la em Setembro / 2005, a Data Entrada deverá ser 20/07/2005 e a Data Emissão 15/07/2005. Nas observações serão informados o motivo do lançamento extemporâneo e o valor.

**Saída:** emissão em 15/07/2005 e saída também em 15/07/2005. Se a NF não foi para o Registro de Saídas de Julho / 2005 e pretendemos registrá-la em Setembro / 2005, a Data Emissão no livro deverá ser 15/07/2005. Nas observações serão informados o motivo do lançamento extemporâneo e o valor.  
 Inclusão de Lançamentos Extemporâneos  
 Para Inserir Lançamento Extemporâneo clique no botão na tela de Lançamentos Fiscais.  
 Este botão será visível somente para filiais do Estado de MG e SP.  
 Esse lançamento fiscal extemporâneo terá o STATUSLF "X"  
 Na janela de edição de Lançamentos foi acrescentado o campo Data LF.  
 Este campo será habilitado para edição somente nos Lançamentos Fiscais de Status Extemporâneo.  
 Para Lançamentos Fiscais Normais, o campo Data LF será preenchido pelo sistema, ou seja, Entrada (= Data Entrada/Saída) e Saída (= Data Emissão).  
 Na inclusão de Lançamentos Fiscais extemporâneos, o campo deverá ser informado pelo usuário e deverá se encontrar dentro do período do lote corrente.  
 Se o usuário não trabalha com lotes, deverá existir período aberto para a Data LF informada. Neste tipo de Lançamento Fiscal, a Data Entrada/Saída deverá ser de período anterior à Data LF.  
    
 ***Atenção!***Na apuração não serão considerados os Lançamentos Extemporâneos, visto que a orientação é que os mesmos sejam cadastrados sem valor do ICMS, ou seja, lançando em Outros ICMS; além disso, a orientação é que os créditos extemporâneos sejam lançados em Outros Créditos e os débitos pagos através de guias. Por isso não poderão ser considerados na apuração.  
 Nas rotinas de cálculo do CIAP não estaremos desconsiderando lançamentos extemporâneos, visto que os bens associados aos mesmos devem ser controlados;  
 A geração automática de guias de recolhimento com base nos lançamentos fiscais também não estará considerando estes lançamentos.
