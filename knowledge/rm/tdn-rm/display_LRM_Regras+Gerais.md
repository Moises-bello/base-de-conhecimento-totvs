---
content_hash: 85f5ee8c60b798a56f1fd108a72a0ea67df3b08f06750e572773bf6e01fc2d86
fetched_at: '2026-06-29T00:09:23.270940+00:00'
page_id: '422546089'
product: rm
source: tdn-rm
title: Regras Gerais
type: documentation
url: https://tdn.totvs.com/display/LRM/Regras+Gerais
version: 6
---

Abaixo as consistência para a geração dos dados da rotina.

**Lançamentos Normais**

Serão considerados Lançamentos Fiscais de acordo com as seguintes validações:

1. Coligada de contexto;
2. Identificação da Filial selecionada na tela de geração da rotina;
3. Data Inicial e Final selecionada na tela de geração da rotina;
4. Será validado a flag "Fiscal" marcada no cadastro do CFOP;
5. Lançamento Fiscal com o status diferente de Cancelado, Estorno e Extemporâneo.

De acordo com o manual da rotina DOT, não deverão ser considerados os seguintes códigos de CFOP:   
5.664, 6.664, 1.664, 2.664, 5.663, 6.663, 1.663, 2.663, 1.406, 2.406, 1.551, 2.551, 3.551, 5.552, 6.552, 1.552, 2.552, 5.554, 6.554, 1.554, 2.554, 5.555, 6.555, 1.555, 2.555, 1.257, 2.257, 1.407, 2.407, 1.556, 2.556, 3.556, 5.557, 6.557, 1.557, 2.557, 1.653, 1.253 e 2.653.  
***Observação***: Lançamentos com os CFOP's 1.9XX, 2.9XX, 3.9XX, 5.9XX, 6.9XX e 7.9XX não serão selecionados.

**Lançamentos de Serviços**

Serão considerados Lançamentos Fiscais de acordo com as seguintes validações:

1. Coligada de contexto;
2. Identificação da Filial selecionada na tela de geração da rotina;
3. Data Inicial e Final selecionada na tela de geração da rotina;
4. Será validado a flag "Fiscal" desmarcada no cadastro do CFOP;
5. Lançamento Fiscal com o status diferente de Cancelado, Estorno e Extemporâneo.

Lançamentos de Saída Interna de Naturezas Fiscais referente a serviços com incidência do ICMS como energia elétrica, comunicação, transporte e água canalizada.  
**Observação:**

* **TAG <VALR\_AQZ\_PESSOA\_FISICA>** - Entradas PF ou Não Contribuinte

Serão tratados os Lançamentos Fiscais de entrada de dentro do Estado do Espírito Santo. Será somado o valor da mercadoria informado nos itens dos lançamentos (quantidade \* preço) – desconto e produto selecionado = P (produto).  
Neste caso, o Cliente/Fornecedor não poderá ser Contribuinte de ICMS ou sua categoria deverá ser estar definida como Pessoa Física no cadastro de Cliente/Fornecedor.  
O cálculo será desmembrado por código do município do Lançamento Fiscal e acrescentado ao Quadros de Detalhamentos Item 3, preenchendo o valor de mercadoria.

* **TAG <VALR\_PROD\_RURAL\_PROPRIA>** - Entradas do Estado do Espírito Santo

Neste caso serão levados em consideração os lançamentos de entrada cujo CFOP seja do grupo 1.xxx e possua o campo Origem/Destino marcado como Dentro do Estado. Além disso no cadastro do Cliente/Fornecedor do lançamento deve possuir o ramo de atividade Produtor Rural selecionado.  
Será somado o valor da mercadoria informado nos itens dos lançamentos (quantidade \* preço) – desconto e produto selecionado = P (produto).

**Descrição dos campos do Quadro A, B, C e D**

As TAG dos Quadros A, B, C e D serão obrigatórias as suas criações, mesmo sendo zeradas ou vazias.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **CAMPO** | **DESCRIÇÃO** | **ORIGEM DOS DADOS** |
| 01 | <NUM\_INSCEST> | Inscrição estadual deverá ser importada com a sua máscara (999.999.99-9). | Inscrição Estadual informada no cadastro da Filial. |
| 02 | <DATA\_INICIO\_DECLARACAO> |  | Gerado de acordo com o Data Inicial informada na tela de geração da rotina. |
| 03 | <DATA\_FIM\_DECLARACAO> |  | Gerado de acordo com o Data Final informada na tela de geração da rotina. |
| 04 | <CODG\_MUNICIPIO> | Município o qual o contribuinte está localizado. | Município informado no cadastro da Filial. |
| 05 | <CODG\_APRESENTACAO> | Códigos válidos de acordo com o Anexo II. | Campo gerado conforme informado na tela de geração da Rotina. |
| 06 | <VALR\_ESTOQUE\_INICIAL> | Estoque inicial. | Valor gerado conforme o informado na tela de geração da Rotina, sub pasta "Outros Dados". |
| 07 | <VALR\_COMPRA\_DEVOL\_TRANSF> | Compras, transferências e devoluções do Estado (exceto campos 3 e 4);  Campo 3 - Entradas de Produtor Rural;  Campo 4 - Compras de Pessoa Física ou não contribuinte do ICMS Estado. | Somatório do valor contábil de todas as operações de entrada dentro do estado, onde o Cliente/Fornecedor seja contribuinte do ICMS e o CFOP seja do grupo 1.XXX. |
| 08 | <VALR\_PROD\_RURAL\_PROPRIA> | Entrada de Produtor Rural própria. | Entrada de Produtor Rural própria. |
| 09 | <VALR\_AQZ\_PESSOA\_FISICA> | Compras pessoa física ou não contribuinte do ICMS Estado. | Soma do valor contábil das operações de entrada de operação interna, onde o Cliente/Fornecedor não seja contribuinte do ICMS e o CFOP seja do grupo 1.XXX. |
| 10 | <VALR\_COMPRA\_FORA\_EST> | Compras, transferências e devoluções de operações interestaduais. | Soma do valor contábil das operações de entrada de operação interestaduais onde o CFOP seja do grupo 2.XXX. |
| 11 | <VALR\_COMPRA\_EXTERIOR> | Compras, transferências e devoluções do Exterior. | Soma do valor contábil das operações de importação onde o CFOP do lançamento seja do grupo 3.XXX. |
| 12 | <VALR\_VENDA\_DEVOLUCAO> | Vendas, transferências e devoluções internas. | Soma do valor contábil de todas as saídas de dentro do estado com o CFOP 5.XXX. |
| 13 | <VALR\_VENDA\_FORA\_ESTADO> | Vendas, transferências, e devoluções interestaduais. | Soma do valor contábil de todas as saídas interestaduais com o CFOP 6.XXX. |
| 14 | <VALR\_VENDA\_EXTERIOR> | Vendas para o exterior. | Soma do valor contábil de todas as operações de saída internas com o CFOP 7.XXX. |
| 15 | <VALR\_ESTOQUE\_FINAL> | Estoque final. | De acordo com o valor informado na tela de geração da rotina. |
| 16 | <VALR\_ENERGIA\_ELETRICA> | Valor total da receita resultante da geração e da distribuição de energia elétrica. | Soma do valor contábil de todas as operações de saída de energia elétrica (código modelo de documento 06) e CFOP específico de energia elétrica. |
| 17 | <VALR\_TRANSPORTE> | Correspondente as operações de prestação de serviço de transporte de passageiros e cargas por meio rodoviário, ferroviário, aquaviário e dutoviário. | Soma do valor contábil de todas as operações de saída com código modelo de documento = 07, 08, 8b, 09, 10, 11, 13, 14, 15, 16, 17, 20, 57 e CFOP especifico de transporte. |
| 18 | <VALR\_COMUNICACAO> | Correspondente a prestação de serviço de comunicação inclusas na competência de tributação do ICMS. | Soma do valor contábil de todas as operações de saída com código modelo de documento 21 e 22 e CFOP específico. |
| 19 | <VALR\_EXTRACAO\_PETROLEO> | Extração de petróleo.  Será informado o valor, no ano base, correspondente às operações relativas à extração de petróleo. | Campo não é gerado pela aplicação. |
| 20 | <VALR\_AGUA> | fornecimento de água tratada para os municípios dentro do Estado do Espírito Santo. | Soma do valor contábil de todas as operações de saída com código de modelo de documento igual a 29. |
| 21 | <VALR\_OUTRAS\_ATIVIDADES> | Valores correspondente às operações, no ano base, e não incluídas nos itens anteriores, promovidas por contribuintes com sistema de inscrição centralizada, nas hipóteses previstas na legislação de regência do ICMS ou através de regime especial. Excepcionalmente, o valor do resultado das operações, realizadas no ano base 2009, com gás natural canalizado será informado neste campo. | Tipo de Documento igual à 28. |
| 22 | <VALR\_OUTROS\_SER\_TRANS> | Correspondente aos serviços de transporte contratados de pessoas físicas (transportadores autônomos) ou de empresas de transportes estabelecidas em outras unidades da federação, nos quais o contribuinte contratante assume a responsabilidade pelo recolhimento do imposto devido. | Gerado de acordo com o Valor de Serviço de Transporte informado na tela de geração da rotina. |
| 23 | <MEMO\_OBS> | Informações Complementares.  Destina-se à prestação de informações complementares, nos casos em que as informações prestadas nos campos anteriores não sejam suficientes. | Gerado sem Informação |
