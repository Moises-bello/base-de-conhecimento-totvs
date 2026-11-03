---
content_hash: 9548da1390f61e7f20cfb931156e32f054ce86f3f44fb4f644dfedcd89c4ddfb
fetched_at: '2026-06-29T00:09:23.984647+00:00'
page_id: '422546181'
product: rm
source: tdn-rm
title: Bloco C (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546181
version: 35
---

## Documentos Fiscais – I - Mercadorias (ICMS/IPI)

registroslefttrueC001Registro C001

**Registro C001 – Abertura do bloco C**  
Este registro informa se houve movimentação no bloco C.

c010Registro C010

**Registro C010 – Identificação do estabelecimento**  
Gerado para cada filial que possui movimentação no período da escrituração.

c100Registro C100

**Registro C100 – Documento – Nota Fiscal (01), Nota Fiscal Avulsa (1B),  Nota Fiscal de Produtor (04), NF-e (55) e NFC-e (65)**

Para a geração deste registro são selecionados Lançamentos Fiscais que estejam associados a naturezas do tipo Fiscal e aos código modelo de documento 01, 1b, 04, 55 e 65.  
***Observação:*** Quando estiver parametrizado um lançamento fiscal cujo modelo de documento for 55 (NF-e) e possuir CFPS preenchido na natureza de operação, será gerado o registro A100. No momento não estão sendo geradas as devoluções neste registro. A geração desta informação já está sob análise.

Em relação aos parâmetros "**Não Gerar Valores para Notas Sem Direito a Crédito (PIS/COFINS)**" e "**Não Gerar Operações Sem Direito a Crédito (PIS/COFINS)**", o sistema terá o seguinte comportamento:

Os valores de CST devem ser preenchidos separadas por (;) Ponto e Virgula para a primeira opção os registros serão gerados porem sem os valores de PIS/COFINS e para a

segunda opção nem mesmo os registros serão gerados.

Observação: Retirado o CST 49 da lista de CSTs utilizados na opção "Gerar Operações sem direito a crédito" pois o mesmo deve ser utilizado em operações de saída.

O campo 15(VL\_ABAT\_NT), será gerado quando o valor do ICMS Desonerado estiver preenchido na Situação Tributaria do Lançamento Fiscal. Para isso a Regra de ICMS da Natureza de Operação deve estar parametrizada com a flag "ICMS Desonerado" marcada e a flag "ICMS Deson. Não afeta Valor Contábil" desmarcada.

Veja mais sobre a geração deste Registro (C100) quando houver caso de Devolução por Recusa:

<https://tdn.totvs.com/x/rxpZIw>

c110Registro C110**Registro C110 – Complemento do Documento – Informação Complementar do Documento Fiscal (Códigos 01, 1B, 04 e 55)**  
Este registro só será gerado se o lançamento declarado no registro C100 possuir o campo [INFCOMPLDOCFISCAL](http://tdn.totvs.com.br/pages/viewpage.action?pageId=190518894) e este estiver preenchido.c111Registro C111**Registro C111 – Processo Referenciado**  
Este registro só será gerado se o lançamento declarado no registro C100 possuir algum processo referenciado. Esta informação pode ser associada na guia - pasta Outros Dados | Processo judicial.c120Registro C120**Registro C120 – Complemento do Documento – Operações de Importação (Códigos 01,55)**  
Este registro só será gerado se o lançamento declarado no registro C100 estiver associado a um CFOP iniciado com 3. Os itens do lançamento deverão possuir os tributos PIS e COFINS Importação.c170Registro C170

**Registro C170 – Complemento do Documento – Itens do Documento (Códigos 01, 1B, 04 e 55)**  
Neste registro é gerada uma linha para cada item do documento fiscal. A tributação do PIS e da COFINS deverá estar nos itens para que este registro seja corretamente gerado. Este registro será gerado inclusive para documentos com Situação Especial (COD\_SIT = 8), diferente do comportamento da EFD ICMS\IPI.

**Campo 04 DESCR\_COMPL -** é gerado de acordo com a Observação do Item do Lançamento Fiscal. A partir da versão 12.1.2205, será considerado o valor do campo "Descrição do produto do fornecedor" para lançamentos de Entrada.  
  
Regras de geração:  
  
**1 -** Caso o campo não seja preenchido o valor continua sendo gerado de acordo com a Observação do Item.  
  
**2 -** Caso ambos os campos estejam preenchidos será considerado o campo Descrição do produto do fornecedor.

O campo pode ser informado no módulo de Faturamento e escriturado para o módulo Fiscal, para mais detalhes sobre o preenchimento no movimento [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=574890054)Campo Descrição do Produto do FornecedorDisponível nos Lançamentos de Entrada a partir da versão 12.1.2205.  
Campo Observação

**Campo 19 (IND\_APUR) -** é preenchido de acordo com a periodicidade do IPI, podendo ser mensal (valor 0) ou Decendial (Valor 1). Para parametrizar a periodicidade do IPI e mais detalhes, consulte a página .  
  
**Campo 38(VL\_ABAT\_NT) -** será gerado quando o valor do ICMS Desonerado estiver preenchido no Item do Lançamento Fiscal. Para isso a Regra de ICMS da Natureza de Operação deve estar parametrizada com a flag "ICMS Desonerado" marcada e a flag "ICMS Deson. Não afeta Valor Contábil" desmarcada.

Os campos **Campo 28 (QUANT\_BC\_PIS), Campo 29 (ALIQ\_PIS\_QUANT), Campo 34 (QUANT\_BC\_COFINS) e Campo 35 (ALIQ\_COFINS\_QUANT)** serão gerados no arquivo da EFD Contribuições, quando usado o CST "**03 -** **Operação Tributável com Alíquota por Unidade de Medida de Produto**".

c175Registro C175**Registro C175 – Registro Analítico do Documento (Código 65)**  
Este registro demonstra a totalização dos documentos fiscais da NFC-e (Código 65), totalizados por CST PIS, CST COFINS, CFOP, alíquota de PIS e alíquota da COFINS.c380Registro C380**Registro C380 – Nota Fiscal de Venda a Consumidor (código 02) – Consolidação dos Documentos Emitidos.**  
Para a geração deste registro são selecionados Lançamentos Fiscais de saída que estejam associados a CFOP do tipo fiscal e que estejam associados ao código modelo de documento 02.C381Registro C381**Registro C381 – Detalhamento da Consolidação – PIS/PASEP**C385Registro C385**Registro C385 – Detalhamento da Consolidação – COFINS**  
Para cada Lançamento Declarado no registro C380 será gerada uma linha do registro C381 e uma do registro C385 com as informações do PIS e da COFINS. Estes tributos são carregados dos itens dos Lançamentos Fiscais.C395Registro C395**Registro C395 – Notas Fiscais de Venda a Consumidor (códigos 02, 2D, 2E e 59)**  
São selecionados para a geração deste registro os Lançamentos Fiscais de entrada que estejam associados a CFOP do tipo fiscal e possuam os código modelo de documento 02, 2D, 2E e 59.C396Registro C396**Registro C396 – Itens do documento (Código 02, 2D, 2E e 59) – Aquisições/Entradas com crédito**  
Para cada documento declarado no registro C395 será gerada uma ou mais linhas com as informações de seus itens. Para a correta geração deste registro é necessário que os tributos PIS e COFINS estejam corretamente gravados nos itens do Lançamento Fiscal.c400Registro C400**Registro C400 – Equipamento ECF (Códigos 02 e 2D)**  
Para a geração deste registro serão selecionadas as informações dos equipamentos de ECF que emitiram Cupons Fiscais no período da escrituração.c405Registro C405**Registro C405 – Redução Z (Códigos 02 e 2D)**  
Para a geração deste registro serão selecionados os lançamentos de saída associados a CFOP do tipo fiscal e que possuam código modelo de documento 2D: Redução Z.c481Registro C481**Registro C481 – Resumo Diário de Documentos emitidos por ECF – PIS/PASEP (Códigos 02 e 2D)**c485Registro C485**Registro C485 – Resumo Diário de Documentos emitidos por ECF – COFINS (Códigos 02 e 2D)**  
Para cada Redução Z declarada no registro C405 será gerada uma linha para cada item que ela possuir com as informações do PIS e da COFINS incidentes.c489Registro C489**Registro C489 – Processo Referenciado**  
Este registro só será gerado somente se a Redução Z possuir algum processo judicial referenciado.c500Registro C500

**Registro C500 refere-se a Nota Fiscal/Conta de Energia Elétrica (Código 06), Nota Fiscal de Energia Elétrica**  
**Eletrônica – NF3e (Código 66), Nota Fiscal/Conta de fornecimento D’água Canalizada (Código 29), Nota Fiscal/Consumo Fornecimento de Gás (Código 28) e NF-e (Código 55) – Documentos de Entrada / Aquisição com Crédito**

"Neste registro serão informadas pela pessoa jurídica as operações sujeitas à apuração de créditos de PIS/Pasep e de Cofins, na forma da legislação tributária, referentes a:

* energia elétrica, consumida nos estabelecimentos da pessoa jurídica (art. 3º, III, das Leis nº 10.637/02 e nº10.833/03);
* água canalizada ou gás, utilizados como insumo na fabricação de produtos destinados à venda ou na prestação de serviços (art. 3º, II, das Leis nº 10.637/02 e nº 10.833/03).

A partir de 01/01/2020, se o campo COD\_MOD for igual a ”66” ou “55” o campo CHV\_DOCe é obrigatório."

###### \*[(**Guia\_Pratico\_EFD\_Contribuicoes\_Versao\_1\_33 - 16\_12\_2019;**página 164)](http://sped.rfb.gov.br/estatico/21/752D4028C877B5B71F3B1A850C32317A36B5AC/Guia_Pratico_EFD_Contribuicoes_Versao_1_33%20-%2016_12_2019.pdf#page=164)

c501Registro C501

**Registro C501 – Complemento da Operação – PIS/PASEP**

Neste registro devem ser detalhadas as informações relativas à apuração do crédito de PIS/Pasep, referentes ao   
documento fiscal escriturado no Registro Pai C500. Deve ser escriturado um registro C501 para cada item   
(fornecimento d´água canalizada, de energia elétrica ou de gás) cuja operação dê direito a crédito, pelo seu valor total   
ou parcial.

Caso em relação a um mesmo item venha a ocorrer tratamentos tributários diversos (mais de um CST), deve a pessoa   
jurídica informar um registro C501 para cada CST.

c505Registro C505**Registro C505 – Complemento da Operação – COFINS**  
Para cada nota declarada no registro C500 serão geradas um ou mais linhas com as informações do PIS e da COFINS incidentes. Estes registros  são agrupados por CST, Natureza da Base de Crédito e Alíquota do Tributo.c509Registro C509**Registro C509 – Processo Referenciado**  
Este registro só será gerado se o documento declarado no registro C500 possuir algum processo judicial associado.c600Registro C600

**Registro C600 – Consolidação Diária de Notas Fiscais/Contas Emitidas de Energia Elétrica (Código 06), Nota Fiscal de Energia Elétrica Eletrônica – NF3e (Código 66), Nota Fiscal/Conta de Fornecimento D'água Canalizada (Código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) (Empresas Obrigadas ou não Obrigadas ao Convenio ICMS 115/03) – Documentos de Saída**

"Este registro deve ser apresentado pelas pessoas jurídicas que auferem receita da venda de energia elétrica, água canalizada e gás, informando a consolidação diária de Notas Fiscais/Conta de Energia Elétrica (código 06 da Tabela Documentos Fiscais do ICMS), Nota Fiscal de Energia Elétrica Eletrônica – NF3e (código 66 da Tabela de Guia Prático da EFD   
Documentos Fiscais do ICMS – a partir das escriturações de janeiro/2020), Notas Fiscais de Fornecimento D’Água (código 29 da Tabela Documentos Fiscais do ICMS) e Notas Fiscais/Conta de Fornecimento de Gás (código 28 da Tabela Documentos Fiscais do ICMS), independente se a pessoa jurídica está ou não obrigada ao Convênio ICMS 115/2003.

Notas fiscais eletrônicas, modelo 55, referentes à fornecimento de energia elétrica também devem ser consolidadas neste registro.

OBS: Caso a pessoa jurídica queira demonstrar na escrituração os registros representativos das receitas de suas atividades, de acordo com cada natureza, tipo ou forma de reconhecimento, poderá segregar os diversos tipos de receitas, nos registros C601 (PIS/Pasep) e C605 (Cofins), segregando as receitas em contas contábeis específicas, gerando registros C601 e C605 específicos para cada conta contábil correspondente.".

###### \*(**[Guia\_Pratico\_EFD\_Contribuicoes\_Versao\_1\_33 - 16\_12\_2019; página 171](http://sped.rfb.gov.br/estatico/21/752D4028C877B5B71F3B1A850C32317A36B5AC/Guia_Pratico_EFD_Contribuicoes_Versao_1_33%20-%2016_12_2019.pdf#page=171))**

c601Registro C601**Registro C601 – Complemento da Consolidação Diária – Documentos de Saídas – PIS/PASEP**c605Registro C605**Registro C605 – Complemento da Consolidação Diária – Documentos de Saídas – COFINS**  
Para cada nota declarada no registro C600 serão geradas um ou mais linhas com as informações do PIS e da COFINS incidentes. Estes registros  são agrupados por CST, Natureza da Base de Crédito e Alíquota do Tributo.c609Registro C609**Registro C609 – Processo Referenciado**  
Este registro só será gerado se o documento declarado no registro C600 possuir algum processo judicial associado.c860Registro C860**Registro C860 – Identificação do Equipamento SAT-CF-e**  
Tem por objetivo identificar o equipamento SAT-CF-e. Não pode haver mais de um registro.c870Registro C870**Registro C870 – Resumo Diário de Documentos Emitidos por Equipamento SAT-CF-e (código 59) - PIS/PASEP e COFINS**  
Serão selecionados lançamentos com código modelo de documento 59.c880Registro C880**Registro C880 – Resumo Diário de Documentos Emitidos por Equipamento SAT-CF-e (código 59) - PIS/PASEP e COFINS Apurado por Unidade de Medida de Produto**  
Este registro é gerado para demonstrar o equipamento SAT-CF-e da receita consolidada e da apuração das contribuições sociais por unidade de medida de produto.c890Registro C890**Registro C890 – Processo Referenciado**  
Registro específico para a pessoa jurídica informar a existência de processo administrativo ou judicial. Será consistido o Processo Judicial informado na Situação Tributária do Lançamento Fiscal.c990Registro C990**Registro C990 – Encerramento do Bloco C**  
Este registro é gerado automaticamente pela rotina com a quantidade de linhas do bloco C.
