---
content_hash: a99aadc8d2aa0bcaa94bf5053f18bc7b62ccb387deee60832670e48a41a5ac9d
fetched_at: '2026-06-29T00:09:20.649073+00:00'
page_id: '422545732'
product: rm
source: tdn-rm
title: Gerar FECP
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+FECP
version: 6
---

Este processo estará visível somente para as filiais do estado do Rio de Janeiro que estejam parametrizadas para gerar FECP. Executado somente para os tributos ICMS e ICMS ST

Somente serão considerados itens que não estão vinculados aos produtos informados no filtro de Parâmetro de processo.

O sistema considera a vigência do Processo FECP para selecionar os produtos que devem ser excluídos.

falseCadastros necessários para geração do FECP0stepBySteplefttrue1Ativar o cálculo do FECPAtivar o cálculo do FECP

Ative o cálculo do FECP nos parâmetros da apuração do ICMS:

Imagem2Filial do RJSelecionar uma filial do RJ

Para a geração do FECP RJ uma filial do Rio de Janeiro deve estar selecionada:

Imagem3Período de Apuração de ICMSCadastrar um período de apuração para o tributo ICMS

Cadastre um período de apuração para o tributo ICMS:

Imagem4Cadastrar Parâmetro de ProcessoCadastrar parâmetro de processo

Cadastre um parâmetro de processo para o FECP com um intervalo que abranja a data do período de apuração de ICMS cadastrado anteriormente.

ImagemfalseGeração do FECP0geracaoleftProcesso de geração do FECP

Acesse o menu Outros Débitos/Créditos e acione o processo de geração do FECP, informando a alíquota para o cálculo.

Imagem1Informações do Cálculo para ICMSInformações do Cálculo para ICMS

**Débito internas**: Somar valores de saídas internas com saídas interestaduais e subtrair entradas internas. O valor obtido será usado para criar um lançamento de outros débitos/créditos para o tributo e períodos selecionados com o tipo Outros Débitos e subtipo FECP - Débitos Op. Internas e classificação informada na tela de geração do processo.

**Débito importação**: O valor de importação será usado para criar um lançamento de outros débitos/créditos para o tributo e períodos selecionados com o tipo Outros Débitos e subtipo FECP - Débitos Op. Importação e a classificação informada na tela de geração do processo.

**Diferencial de alíquota**: O valor de diferencial de alíquota será usado para criar um lançamento de outros débitos/créditos para o tributo e períodos selecionados com tipo Outros Débitos e subtipo FECP - Débitos Op. Dif. Alíquota e a classificação informada na tela de geração do processo.

**Dedução**: o valor de débito internas será usado para criar um lançamento de outros débitos/créditos para o tributo e períodos selecionados com o tipo Dedução e subtipo FECP - Dedução Op. Internas e a classificação informada na tela de geração da rotina.  
Onde:

* **Saídas internas**: Soma dos valores dos lançamentos de saída (somatório do campo Base Tributada ICMS dos itens) com a natureza do tipo **5**. Multiplicar o valor pela Alíquota.
* **Saídas interestaduais**: Soma dos valores dos lançamentos de saída (somatório do campo Base Tributada ICMS dos itens), natureza do tipo **6** e emitente contribuinte. Multiplicar o valor pela Alíquota.
* **Entradas internas**: Soma dos valores dos lançamentos de entrada (somatório do campo Base Tributada ICMS dos itens) e natureza do tipo **1**. Multiplicar o valor pela Alíquota.  
  ***Importação***: Soma dos valores dos lançamentos de entrada da coligada, filial e período (somatório do campo Base Tributada ICMS dos itens), natureza do tipo **3**. Multiplicar o valor pela Alíquota.
* **Diferencial de alíquota**: Soma dos valores dos lançamentos de entrada da coligada, filial e período (somatório do campo Base tributada de ICMS dos itens) e natureza com Tipo Operação Tributária como Diferencial de Alíquota.  
  ***Observação*:** Os lançamentos da coligada, filial e período, com status Normal ou Estorno, documento que não acoberta cupom fiscal, e item com produto não parametrizados no processo Produtos não considerados no Cálculo FECP.
2Informações do Cálculo para ICMS STFECP Interestadual

Para o valor de Internas ST somado ao valor de Entradas Interestaduais ST será criado um lançamento de outros débitos/créditos para o ICMS ST e período selecionado com tipo Outros Débitos e subtipo FECP - Débitos Op. Sub. Tributária e a classificação informada na tela de geração do processo; e outro tipo Deduções com subtipo FECP - Deduções Op. Sub. Tributária e a classificação informada na tela de geração do processo, onde:

**Internas ST**: Selecionar os valor dos lançamentos de saída (somatório dos campos Base Tributada ICMS, Base ICMS ST e Isento ICMS dos itens agrupados pelo tipo do ICMS da natureza), natureza 5 com tipo de operação Situação Tributária e tipo Isento ou Tributo sem retenção de ICMS ST que some o valor de ICMS ST ao valor contábil. O valor será a soma para todos os itens pela regra seguinte:

* Se tipo **Isento**: Base ICMS ST - Isentos de ICMS
* Se tipo **Tributado**: Base ICMS ST - Base Tributada ICMS

O resultado deve ser multiplicado pela Alíquota.

**Entrada Interestadual ST**: Selecionar os valores dos lançamentos de entrada (somatório dos campos Base Tributada ICMS ST e Isento ICMS dos itens agrupado pelo tipo do ICMS da natureza), natureza 2 com tipo de operação Situação Tributária, e tipo Isento, ou Outros com retenção de ICMS ST que não some o valor de ICMS ST ao valor contábil, ou Outros que some o valor de ICMS ST ao valor contábil e tipo de natureza diferente de Ativo, ou Tributado com o tipo de natureza diferente de Ativo. O valor será a soma para todos os itens pela regra seguinte:

* Se tipo **Isento**: Base ICMS ST - Isento ICMS
* Se tipo **Tributado**: Base ICMS ST - Base Tributada ICMS

O resultado deve ser multiplicado pela Alíquota.

3ExemploExemplo

Criado um Lançamento Fiscal de Saída para um cliente fornecedor do estado da Bahia. Sua situação tributária foi configurada com uma natureza do tipo 6, e o Valor Base ICMS do item da situação de R$3.000.

Imagens

Foi incluído também um Lançamento Fiscal de Entrada para um cliente fornecedor do estado da Rio de Janeiro. Com situação tributária configurada com uma natureza do tipo 5, e o Valor Base ICMS do item da situação de R$1.000.

Ao executar o processo de geração do FECP RJ são geradas dois lançamentos. Um do tipo "Débito" e subtipo "FECP - Débitos Op. Internas" e outro do tipo "Deduções" e subtipo "FECP - Dedução - Op. Internas".

O valor dos lançamentos é definido como R$40:

2% do Valor Base ICMS do lançamento de saída (R$60)

Subtraído de

2% do Valor Base ICMS do lançamento de entrada (R$20)

ImagensInformações

A partir da versão 12.1.33 é possível informar os itens que devem ser desconsiderados do cálculo utilizando o cadastro de Parâmetros de Processos na nova MDI.

Para mais informações acesse seguinte link:

[Parâmetros de Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588)
