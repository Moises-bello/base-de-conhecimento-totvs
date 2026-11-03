---
content_hash: 3cc2af3c7e4ba6642caba24140a467cde500c368cf54b28445fa800f1d70b83b
fetched_at: '2026-06-29T00:09:23.781373+00:00'
page_id: '422546120'
product: rm
source: tdn-rm
title: Geração do Bloco 8
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546120
version: 17
---

**title**

BLOCO8left80018001

**Abertura do Bloco 8 - Dados de Pernambuco**

Abertura do Bloco. Informa se há conteúdo ou não no Bloco.

80208020

**Informações Complementares - Quadro de Cálculo do Valor Adicionado**

Indica se há valores informados ou não no quadro do valor adicionado. Torna obrigatório o registro 8050.  
O objetivo deste registro e filhos é demonstrar o cálculo do valor adicionado previsto no [inciso I do parágrafo único do art. 158 da Constituição Federal, e conforme disposto pela Lei Complementar 63/90 em art. 3º, § 1º](http://www.planalto.gov.br/ccivil_03/LEIS/LCP/Lcp63.htm), colacionados abaixo:  
CF:  
*Art. 158. Pertencem aos Municípios...IV - 25% do produto da arrecadação do ICMS. Parágrafo único. As parcelas de receita pertencentes aos Municípios, mencionadas no inciso IV, serão creditadas conforme os seguintes critérios:*  
*I - 3/4, no mínimo, na proporção do valor adicionado nas operações relativas à circulação de mercadorias e nas prestações de serviços, realizadas em seus territórios;*  
*Art. 161. Cabe à lei complementar:*  
*I - Definir valor adicionado para fins do disposto no art. 158, parágrafo único, I;*  
*LC 63/90:*  
*Art. 3º 25% do produto da arrecadação do ICMS serão creditados, pelos Estados, aos respectivos Municípios, conforme os seguintes critérios:*  
*§ 1o O valor adicionado corresponderá, para cada Município:*  
*I - Ao valor das mercadorias saídas, acrescido do valor das prestações de serviços, no seu território, deduzido o valor das mercadorias entradas, em cada ano civil;*  
*II - Nas hipóteses de tributação simplificada a que se refere o parágrafo único do art. 146 da Constituição Federal, e, em outras situações, em que se dispensem os controles de entrada, considerar-se-á como valor adicionado o percentual de 32% (trinta e dois por cento) da receita bruta.*  
*§ 2º Para efeito de cálculo do valor adicionado serão computadas;*  
*I - As operações e prestações que constituam fato gerador do imposto, mesmo quando o pagamento for antecipado ou diferido, ou quando o crédito tributário for diferido, reduzido ou excluído em virtude de isenção ou outros benefícios, incentivos ou favores fiscais;*  
*II - As operações imunes do imposto, conforme as alíneas a e b do inciso X do § 2º do art. 155, e a alínea d do inciso VI do art. 150, da Constituição Federal...*

80308030

**Detalhamento por Município das Operações e Prestações**

Registra o cálculo do valor adicionado por município, para situações específicas.  
Para o "Total Geral" devem ser selecionados todos os lançamentos de entrada e saída cuja UF do lançamento seja igual à UF da Filial declarante, desconsiderando os seguintes CFOPs:

* CFOPs de entrada expurgados: 1.111, 1.113, 1.406, 1.551, 1.552, 1.553, 1.554, 1.555, 1.601, 1.602, 1.603, 1.604, 1.919, 1.922, 1.923, 1.924, 1.925, 1.933, 2.111, 2.113, 2.406, 2.551, 2.552, 2.553, 2.554, 2.555, 2.603, 2.919, 2.922, 2.923, 2.924, 2.925, 2.933, 3.551, 3.553.
* CFOPs de saída expurgados: 5.111, 5.112, 5.113, 5.114, 5.412, 5.551, 5.552, 5.553, 5.554, 5.555, 5.601, 5.602, 5.603, 5.919, 5.922, 5.923, 5.924, 5.925, 5.929, 5.932, 5.933, 6.111, 6.112, 6.113, 6.114, 6.412, 6.551, 6.552, 6.553, 6.554, 6.555, 6.603, 6.919, 6.922, 6.923, 6.924, 6.925, 6.929, 6.932, 7.551, 7.553.

Estes mesmos lançamentos devem ser totalizados por município x operação x detalhe da operação. Devem ser gerados, no máximo, três registros para cada município.

80408040

**QVA - Ajustes de Valores por CFOP**

Registra os ajustes e os expurgos dos valores por CFOP. Devem ser selecionados todos os lançamentos fiscais associados a CFOP "Fiscal" que estejam dentro do período da escrituração. Estes lançamentos devem ser totalizados por CFOP (Campo 05).

80508050

**QVA - Cálculo do Valor Adicionado**

Registra o cálculo do valor adicionado, no modo geral. Neste registro devem ser gerados o valor contábil total das operações de entrada e de saída, deduzidos do valor contábil das operações de expurgo, conforme detalhado no registro 8040.

81008100

**Informações Complementares - Quadro de Aquisição de Bens**

Indica se há valores informados ou se documenta a ausência de valores no quadro de aquisição de bens.

81108110

**QVA - Aquisição de Bens para Uso/Consumo ou Ativo Fixo**

Registra a aquisição de bens para uso/consumo ou ativo fixo.  
Seleciona os lançamentos de entrada do período da escrituração, associados a CFOP "Fiscal" aplicando os filtros de CFOP's relacionados abaixo e agrupando por UF de origem (Campo 02). Relação de CFOP’s de cada campo:

* Campo 03 \[VL\_EEL\] - Energia Elétrica: 1.251 à 1.257 | 2.251 à 2.257 | 3.251
* Campo 04 \[VL\_COM\] - Comunicação: 1.301 à 1.306 | 2.301 à 2.306 | 3.301
* Campo 05 \[VL\_ATV\] - Ativo Fixo: 1.406, 1.551 | 2.406, 2.551 | 3.551
* Campo 06 \[VL\_OUT\] - Uso e Consumo: 1.407, 1.556 | 2.407, 2.556 | 3.556
81608160

**Informações Complementares - Quadro de Controle do Crédito Acumulado**

Indica se há valores informados ou se documenta a ausência de valores no quadro de controle do crédito acumulado (não é gerado).

81658165

**QCA - Controle do Crédito Acumulado**

Registra o controle do crédito acumulado (não é gerado).

81708170

**QCA - Crédito Acumulado no Período**

Registra o crédito acumulado no período (não é gerado).

81758175

**QCA - Utilização de Crédito Acumulado**

Registra a utilização de crédito acumulado (não é gerado).

81808180

**QCA - Compensação de Débito**

Registra a compensação de débito (não é gerado).

83008300

**Informações Complementares - Quadro do Consumo Continuado**

Indica se há valores informados ou se documenta a ausência de valores no quadro de consumo continuado.

83108310

**QCC - Consumo Continuado**

Registra o consumo continuado de determinados tipos de mercadorias ou serviço.  
Este registro será gerado para os Lançamentos de Saídas com os seguintes CFOP's e/ou modelos de documento:

* Energia elétrica - CFOPs: 5.251, 5.252, 5.253, 5.254, 5.255, 5.256, 5.257, 5.258, 6.251, 6.252, 6.253, 6.254, 6.255, 6.256, 6.257, 6.258 e 7.251.
* Gás canalizado - modelo 28 e CFOPs: 5.101, 5.401, 5.651, 5.652, 5.653, 5.654, 5.655, 5.656, 5.667, 6.651, 6652, 6.653, 6.654, 6.655, 6.656, 6.667, 7.651, 7.654 e 7.667.
* Água canalizada - modelo 29 e CFOPs: 5.101 e 6.101.
* Comunicação - CFOPs: 5.301, 5.302, 5303, 5.304, 5.305, 5.306, 5.307, 6.301, 6.302, 6.303, 6.304, 6.305, 6.306, 6.307 e 7.301.

Os lançamentos devem ser agrupados em função do Indicador do Fornecimento e da Classe de Consumo informada no Lançamento Fiscal.

85008500

**Guia de Apuração dos Incentivos Fiscais e Financeiros GIAF**

Informa se há conteúdo ou documento vazio.

85058505

**GIAF - Benefícios Fiscais**

Registra informações de cadastro dos benefícios fiscais. Deve gerar um registro para cada Benefício que cuja validade de encontra dentro do período da escrituração.

85108510

**GIAF - Alterações do Benefício**

Registra alterações do benefício. Deve ser gerado um registro para cada Decreto de alteração registrado no Anexo do Cadastro de Benefícios Fiscais.

85158515

**Sub Apurações Por Benefício**

Registra quais as sub apurações de um tipo de benefício. Deve ser gerado um registro para cada sub apuração cadastrada para os Benefícios Fiscais vigentes de acordo com o período da escrituração.

85258525

**GIAF - ITEM INCENTIVADO (PI) por Benefício**

Registra o item incentivado (PI) por benefício. Deve ser gerado um registro para cada Produto associado a sub apuração. A origem das informações desse registro é o Cadastro do Produto/Serviço.

85308530

**GIAF - Lançamento com Item Incentivado**

Registra o lançamento com item incentivado. Devem ser selecionados todos os lançamentos de entrada e saída associados a CFOP "Fiscal" no período da escrituração, cujo Código do Modelo de Documento associado seja "01" e "55". A origem das informações desse registro é o Lançamento Fiscal.

85358535

**GIAF - Itens Incentivados no Lançamento**

Registra os itens incentivados do documento. Deve ser gerado um registro para cada item constante no Lançamento Fiscal selecionado para geração do Registro 8530. A origem das informações desse registro é o Lançamento Fiscal e seus Itens.

85408540

**GIAF - Valores Parciais**

Registra os valores parciais do lançamento com item incentivado. Os lançamentos selecionados para o registro 8530 devem ser totalizados por CFOP, alíquota do ICMS e Indicador de sub apuração (campos 03, 05 e 07). A origem das informações é o Lançamento Fiscal.

85458545

**GIAF - Apuração Incentivada**

Registra as sub apurações incentivadas. Deve ser gerado um registro 8545 e seus filhos para cada sub apuração do período a que se refere a escrituração.

85508550

**GIAF - Consolidação por CFOP das Operações Incentivadas**

Registra consolidação por CFOP das operações incentivadas. Os mesmos lançamentos selecionados para geração do registro 8530 devem ser totalizados, para cada sub apuração, por CFOP (Campo 03). A origem das informações é o Lançamento Fiscal.

85558555

**GIAF - Totalização das Operações Incentivadas**

Registra totalização das operações incentivadas. Neste registro serão selecionados os mesmos lançamentos da geração do registro 8530, porem a totalização destes se dará pela origem/destino da operação. A origem das informações é o Lançamento Fiscal.

85608560

**GIAF - Saldos da Apuração Incentivada**

Registra os resultados da apuração incentivada. Esse registro será gerado a partir do Detalhamento da sub apuração.

85658565

**GIAF - Ajustes da Apuração Incentivada**

Registra os ajustes da apuração incentivada. Esse registro será gerado com os lançamentos de outros débitos/créditos associados à sub apuração, agrupados por Código de Ajuste.

85708570

**GIAF 1 - Prodepe Indústria (Crédito Presumido)**

Registra o valor do incentivo Prodepe Indústria (crédito presumido). Este registro deve ser gerado quando o Indicador do enquadramento do Benefício Fiscal associado a sub apuração for "Indústria (crédito presumido)".

85808580

**GIAF 3 - Prodepe Importação (Diferimento na Entrada e Crédito Presumido na Saída Subsequente)**

Registra o valor do incentivo Prodepe Importação (diferimento na entrada e crédito presumido na saída subsequente). Este registro deve ser gerado quando o Indicador do enquadramento do Benefício Fiscal associado a sub apuração for "Importação (diferimento/crédito presumido)".

85858585

**GIAF 3 - Prodepe Importação (Saídas Internas por Faixa de Alíquota) GIAF 3**

Registra etapas do incentivo Prodepe Importação (saídas internas por faixa de alíquota).  
Gerar um registro para cada Faixa de incentivo.

85908590

**GIAF 4 - Prodepe Central de Distribuição (Entradas/Saídas) GIAF 4**

Registra o valor do incentivo Prodepe Central de Distribuição (entradas/saídas).  
Este registro deve ser gerado quando o Indicador do enquadramento do Benefício Fiscal associado a sub apuração for "Central de distribuição (entradas/saídas)".

89908990

**Encerramento do Bloco 8 - Dados de Pernambuco**

Encerra o bloco, indicando a quantidade de linhas nele contidas. Este registro já é gerado pela rotina.
