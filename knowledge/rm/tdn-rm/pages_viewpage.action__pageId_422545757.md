---
content_hash: ec2c0395c82f130f336e6635398dbe5e4877c04655d97c3725282adc9205feda
fetched_at: '2026-06-29T00:09:20.980358+00:00'
page_id: '422545757'
product: rm
source: tdn-rm
title: Portaria CAT 17/99
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545757
version: 6
---

A [PORTARIA CAT Nº 17 de 05-03-99](http://info.fazenda.sp.gov.br/NXT/gateway.dll/legislacao_tributaria/portaria_cat/pcat171999.htm) estabelece disciplina para o complemento e o ressarcimento do imposto retido por sujeição passiva por substituição previstos nos artigos 244, 248 e 249 do Regulamento do ICMS, aprovado pelo Decreto 33.118/91, com a redação dada pelo Decreto 43.853.

O Contribuinte Substituído poderá adotar a sistemática da [Portaria CAT 17/99](http://info.fazenda.sp.gov.br/NXT/gateway.dll/legislacao_tributaria/portaria_cat/pcat171999.htm) abrangendo, no máximo, as operações realizadas a partir de 01/01/1999, devendo:

1. Elaborar uma relação do estoque das mercadorias recebidas com retenção do imposto existente no dia imediatamente anterior ao da adoção dessa portaria;
2. Emitir Controle de Estoque das mercadorias sujeitas à Substituição Tributária;
3. Emitir Demonstrativo de Apuração juntamente com o Livro de Saídas;
4. Efetuar os lançamentos de ajustes previstos (no caso de ressarcimento, o contribuinte deverá adotar uma das modalidades definidas: NF de Ressarcimento, Pedido de Ressarcimento ou Pedido de Liquidação de Débitos Fiscais);
5. Geração de arquivo magnético;
6. Registrar os lançamentos de ajustes na GIA/SP – Registros 26 e 27.

**Parametrização**

* Criação de um Parâmetro por Filial para armazenara Data de Início do Controle de Estoque Fiscal:
* Este parâmetro está disponível na etapa "03.02.01 – Apuração de ICMS" -> "Apur. ICMS por Filial" -> "Etapa 2 – Apuração do ICMS 2/2";
* Como default, este Parâmetro será preenchido com a Data de Fechamento de Estoque mais um dia;
* Este parâmetro não poderá ser alterado para uma data anterior ou igual à Data de Fechamento do Estoque.
* Criação de campos nos Dados Fiscais por UF (Anexo do Produto):
* Foi criado um campo no anexo de Dados Fiscais por UF do Produto, para indicar se este produto é tributado pelo ICMS-ST na Unidade da Federação.
* Foi criado um outro campo no anexo de Dados Fiscais por UF do Produto, para indicar a partir de quando este produto passou a ser tributado pelo ICMS-ST na Unidade da Federação. Este campo somente é habilitado caso o campo anterior esteja marcado e, neste caso, seu preenchimento é obrigatório. Essa data deve ser anterior à Data de Início do controle de Estoque Fiscal de todas as filiais da coligada.
* Criação de tabela para armazenar os dados de Estoque Fiscal:
* Foi criada uma tabela para que sejam armazenados os dados de Estoque Fiscal de ICMS-ST (DESTOQUEFISCAL). Esta tabela será preenchida a partir do processo descrito abaixo.
* Somente produtos com o parâmetro Exige Inventário Fiscal marcado serão selecionados.

**Processo**  
 Na tela do processo deverão ser informados os seguintes dados:

* Filial para execução do Processo;
* Data de adoção desta Portaria;
* Esta data será apresentada de forma desabilitada, sem que possa ser alterada, e será preenchida com o parâmetro Data de Início do Controle de Estoque Fiscal.
* Data do Inventário;
* Esta data será apresentada de forma desabilitada, sem que possa ser alterada, e será preenchida com a data de Fechamento do Estoque (Data de adoção da Portaria – 1).
* Relatório do Gerador a ser executado;

Quando iniciado, o processo executará os seguintes passos:

* Selecionará os produtos que sejam tributados pelo ICMS ST, cuja data de início da tributação pelo ICMS ST seja igual ou anterior à Data do Inventário, e que possuam saldo em estoque nesta data;
* Se o produto não for tributado pelo ICMS-ST o mesmo não será considerado;
* Se a data de início da tributação pelo ICMS-ST for posterior à data do inventário o produto não será considerado;
* Se o produto não possuir saldo em estoque na data do inventário o mesmo também não será considerado;
* Se o Saldo Físico do produto estiver desatualizado o mesmo também não será considerado. Deverá ser executado primeiramente o processo de re-geração de Saldos e Custos;
* Para cada um destes produtos, irá calcular a Base de Cálculo e o Valor do ICMS ST.
* Para o cálculo da Base de Cálculo do ICMS-ST do produto serão percorridos os Movimentos de entrada com data igual ou anterior à Data do Inventário e acumulados os valores de Base de Cálculo do ICMS-ST do item do Movimento até que seja atingida a quantidade existente em estoque. Não serão considerados para este cálculo os Movimentos cancelados.
* Se os passos acima foram executados com sucesso, será executado o Gerador de Relatórios, passando como parâmetros a Filial informada na tela do processo, além do relatório selecionado pelo usuário.
* Durante a execução do processo será criado um Log no diretório de arquivos temporários com os Produtos que, por alguma razão, não foram considerados no relatório.

***Importante*:**De modo a manter os valores calculados consistentes, ao adotar esta portaria o usuário deverá primeiramente "fechar" seu Estoque. A Data de Início do controle de Estoque Fiscal deverá ser um dia após a Data de Fechamento do Estoque e não deverá ser alterada para uma data anterior ou igual a esta. Já a Data de Fechamento de Estoque pode ser alterada, mas sempre que o for não poderá ser menor que a data anterior da Data de Início do controle de Estoque Fiscal.

   1.   **Relatório Inicial – Relação do Estoque das Mercadorias**

A relação de estoque das mercadorias recebidas com retenção do ICMS-ST irá marcar o início do controle do estoque fiscal de ICMS-ST. Para que seja gerada esta relação foi disponibilizado no sistema um processo, que deverá ser executado a partir do menu Rotinas Legais -> Rotinas Estaduais -> Apuração de ICMS. Deverá ser selecionado o estado de SP e a rotina "Port. CAT 17/99 – Relatório Inicial".  
 Para utilizar esse relatório deverá importar o relatório nº 12.02.01.001 – CONTROLE ESTOQUE – MERCADORIAS COM SUBSTITUIÇÃO TRIBUTÁRIA

**Dados do relatório**

* Identificação da mercadoria: código do produto (TPRD.CODIGOPRD)
* Quantidade: saldo do produto (DESTOQUEFISCAL.SALDO)
* Unidade utilizada na contagem: unidade do produto (DESTOQUEFISCAL.CODUNDCONTROLE
* Valor total da base de cálculo de retenção: Base de cálculo do ST (DESTOQUEFISCAL.BCICMSST)
* Alíquota interna: alíquota interna informada no cadastro do produto (TPRDCODFISCAL.ALIQINTICMS)

 2.**Controle de Estoque das mercadorias sujeitas à Substituição Tributária;**

Esta relação será gerada a partir de um relatório do Gerador de Relatórios (Planilha). Este relatório será chamado pelo menu Rotinas Legais -> Rotinas Estaduais -> Apuração de ICMS. Deverá ser selecionado o estado de SP e a rotina "Port. CAT 17/99 – Controle Estoque - Planilha", que antes da execução do relatório, irá popular a tabela DESTOQUEFISCAL com as entradas e saídas dos produtos.  
 Para utilizar esse relatório deverá importar o relatório nº 12.02.01.002 – Controle Estoque - Merc. Enquad. Subst. Tribut. - PLANILHA  
 Este processo deverá conter os seguintes dados de entrada:

* Filial para execução do Processo;
* Data de Início para seleção das Movimentações e geração do Relatório.
* Data de Fim para seleção das Movimentações e geração do Relatório.
* Relatório do Gerador (Planilha) a ser executado;

Quando iniciado, o processo deverá executar os seguintes passos:

* Apagar todos os registros da tabela DESTOQUEFISCAL que tenham o campo SEQUENCIAL maior do que 1 e o campo DATAMOVIMENTO igual ou maior que a Data de Início, informada na tela do processo;
* Selecionar os Movimentos/Itens que atendam os seguintes critérios:
* Movimentos com "Data do Movimento" compreendida no intervalo de Datas informado na tela do processo;
* Itens de Movimento cujo produto seja tributado pelo ICMS-ST;
* Movimentos que afetem o Saldo 2;
* Para cada um destes Itens selecionados deverá ser incluída uma linha na tabela DESTOQUEFISCAL. O preenchimento de alguns dos dados desta tabela deverá ser da seguinte maneira:
* Sequencial: Autoincremento, calculado via código, para os campos CODCOLIGADA; CODFILIAL;IDPRD
* Código da Unidade Controle: Unidade de Controle do Produto
* Tipo da Operação de Saída: Este campo será preenchido somente para os movimentos de saída, com os seguintes valores:
* **N** (Fato gerador não realizado): Caso o CFOP do Item seja "5.927";
* **F** (Saída para consumidor ou usuário final): Caso o Cliente/Fornecedor associado ao Movimento não seja Contribuinte do ICMS;
* **I** (Saída com isenção ou não incidência): Caso o Tipo de ICMS do CFOP associado ao Item de Movimento seja "Isento" ou "Não Incidência";
* **O** (Saída para outros estados): Caso o CFOP associado ao Item de Movimento seja Interestadual (6.XXX);
* **C** (Saída para comercialização subseqüente): Caso não caia em nenhuma das situações anteriores.
* Quantidade comercializada: Quantidade do Item movimentado, ajustada de acordo com o fator de conversão entre a Unidade do Movimento e Unidade de Controle do Produto;
* Saldo do Produto: Atualizado de acordo com o valor existente no registro anterior e o campo "Quantidade comercializada" do registro atual. Se o Movimento for de Entrada o valor deve ser somado, se o Movimento for de Saída o valor deve ser subtraído;
* Base de Cálculo do ICMS-ST da Operação: Base de Cálculo do Tributo ICMS-ST do Item Movimentado. Se não existir Tributo ICMS-ST no Item de Movimento, este valor será calculado de acordo com o "Valor Líquido do Item" (Quantidade \* Preço Unitário – Descontos + Despesas);
* Valor do ICMS-ST da Operação: Valor do Tributo ICMS-ST do Item Movimentado. Se não existir Tributo ICMS-ST no Item de Movimento, este valor será zerado;
* Base de Cálculo do ICMS-ST Acumulado: Atualizado de acordo com o valor existente no registro anterior e o campo "Base de Cálculo do ICMS-ST da Operação" do registro atual. Se o Movimento for de Entrada o valor deve ser somado, se o Movimento for de Saída o valor deve ser subtraído;
* Valor do ICMS-ST Acumulado: Atualizado de acordo com o valor existente no registro anterior e o campo "Valor do ICMS-ST da Operação" do registro atual. Se o Movimento for de Entrada o valor deve ser somado, se o Movimento for de Saída o valor deve ser subtraído;

**Dados do relatório:**

* Deve ser gerada uma folha para cada mercadoria e período de apuração;
* Calculado pela média ponderada móvel;
* As operações de devolução ou retorno devem ser lançadas nas colunas próprias, porém, com valor negativo para anular a operação anterior;
* As notas fiscais emitidas para remessa e retorno de mercadorias para venda fora do estabelecimento não devem ser lançadas. Para tanto, devem ser movimentadas em Tipo de Movimento que não afeta estoque;
* Coluna 1 - DATA: data do evento (entrada, saída, baixa, etc);
* Colunas 2 a 5 – Nota Fiscal, Série, Quantidade e B.C. do ICMS ST, respectivamente: para registro dos documentos que acobertaram as operações de entrada da mercadoria no estabelecimento;
* Colunas 6 a 8 – Nota Fiscal, Série e Quantidade, respectivamente: para registros dos documentos que acobertaram as operações de saída das mercadorias do estabelecimento;
* Colunas 9 a 14 – devem ser informadas a seguintes bases de cálculo (coluna 8 \* coluna 9):
* Coluna 9 – Valor Unitário: valor da BC do ICMS ST por unidade da mercadoria (deve corresponder ao valor lançado na coluna 18 da linha anterior);
* Coluna 10 - Saída para consumidor ou usuário final: informar a BC do ICMS ST das operações destinadas a consumidor ou usuário final.
* Coluna 11 - Fato gerador não realizado: informar a BC do ICMS ST no caso de baixa no estoque como perda, roubo/furto, deterioração, etc.
* Coluna 12 - Saída com isenção ou não incidência: informar a BC do ICMS ST no caso de operações realizadas amparadas pela isenção ou não-incidência.
* Coluna 13 - Saída para outros estados: informar a BC do ICMS ST no caso de operações realizadas destinadas a outras unidades da federação.
* Coluna 14 - Saída para comercialização subseqüente: informar baixas de estoque.
* Colunas 15 e 16 – devem ser informados os valores de confronto das BC para fins de levantamento do complemento ou ressarcimento do imposto. Nessas duas colunas teremos os valores efetivos da saída:
* Coluna 15 – BC efetiva na saída a consumidor ou usuário final: deve ser informada a BC das saídas realizadas ao consumidor final e a BC de saídas amparadas pela isenção ou não incidência;
* Coluna 16 - B.C. efetiva da entrada nas demais hipóteses: deve ser informada a BC da operação própria do substituto caso a mercadoria tenha sido recebida diretamente dele, ou, o valor da operação própria que seria devida pelo substituído.
* Colunas 17 a 19 – devem ser informados os valores referentes ao saldo em estoque da mercadoria:
* Coluna 17 – Quantidade: informar a quantidade remanescente da mercadoria em estoque (deve corresponder ao valor do saldo da linha anterior + entradas - saídas);
* Coluna 18 – Valor Unitário: informar o valor da BC do ICMS ST por unidade da mercadoria. Esse valor será (coluna 19 / coluna 17);
* Coluna 19 – Valor total: deve ser informado o valor total da BC do ICMS ST de toda a mercadoria em estoque. Esse valor será (saldo da linha anterior + BC total das entradas – BC total das saídas).

3. **Demonstrativo de Apuração**

Gerado pela totalização dos valores do Controle de Estoque de todas as mercadorias tributadas pela substituição tributária, com valores individualizados por alíquota. Deve ser emitido no final do Livro de Saída.  
 O Demonstrativo da Apuração esta junto com a Planilha, ou seja, para utilizar esse relatório deverá importar o relatório nº 12.02.01.002 – Controle Estoque - Merc. Enquad. Subst. Tribut. – PLANILHA e na ultima pagina estará sendo impresso todas as informações.

4. **Geração de arquivo magnético**

De acordo com o layout disponível na portaria. Os dados são os mesmos do Controle de Estoque e do Demonstrativo.  
 Para utilizar esse relatório deverá importar o relatório nº 12.02.01.003 – Controle Estoque - Merc. Enquad. Subst. Tributária – TEXTO, e gerar via Gerador o arquivo texto conforme parâmetros do Relatório.

**Dados do Layout**

**Registro Tipo 01 - MESTRE DO ESTABELECIMENTO**   
 Esse registro será gerado com os dados da Filial para a qual se está gerando o arquivo. Os dados serão extraídos do Cadastro de Filial.

**Registro Tipo 02 - MOVIMENTAÇÃO DE MERCADORIAS POR NOTA FISCAL**   
 Esse registro será gerado com as movimentações efetuadas na tabela DESTOQUEFISCAL que, por sua vez, é alimentada com as movimentações de estoque das mercadorias tributadas por ST (TRIBUTADOICMSST = 1). Deve ser gerado um registro para cada movimentação registrada no período informado na tela da rotina.  
 Deve ser gerado, também, um registro para informação do saldo inicial, transportado do período anterior. Ver item 7.1.13 do Layout  
 **Campo 09** - Código complementar da operação - Deverá criar um campo complementar alfanumérico de tamanho "dois" no item do movimento para identificação dessa informação: CODIGOCOMPLOPERACAO. Para informações sobre esse campo verificar no Layout da Portaria item 7.1.16.  
 **Campo 10** – Quantidade: DESTOQUEFISCAL.QUANTIDADE  
 **Campo 11** - Valor total da base de calculo da retenção: DESTOQUEFISCAL.BCICMSSTACUMULADO  
 **Campo 12** - Valor de confronto: DESTOQUEFISCAL.BCICMSST  
 **Campo 14** – Chassi - Não aderência  
 **Campo 15** - Base de calculo do substituto nas operações com veículos ou motos - Não aderência

**Registro Tipo 03 – M - MESTRE: IDENTIFICADOR DO EQUIPAMENTO**  
 Esse registro será gerado com os dados da redução Z  
 Esse registro será gerado quando o Código do Modelo do Documento for "2B", "2C" ou "2D" com as informações da redução Z.  
 Registro Tipo 03 – A - ANALÍTICO: Identificador diário das situações tributárias por equipamento  
 Esse registro deve ser gerado com os totalizadores da Redução Z.  
 Campo 05 - Situação Tributária / Alíquota: TTRIBUTACAOECF.TIPO.  
 Se TIPO = Tributado, informar o campo ALIQUOTA

**Registro Tipo 03 - P - MERCADORIA: Movimentação diária por produto e por equipamento**   
 Os itens devem ser totalizados por dia/equipamento.

**Registro Tipo 04 - CÓDIGO DA MERCADORIA**

**Registro Tipo 05 - ALÍQUOTA DE ICMS**   
 Esse registro será gerado considerando a alíquota informada como sendo única no período informado na geração do arquivo. As datas inicial e final serão as datas informadas na tela da rotina.

**Registro Tipo 06 - TOTALIZAÇÃO DO ARQUIVO**
