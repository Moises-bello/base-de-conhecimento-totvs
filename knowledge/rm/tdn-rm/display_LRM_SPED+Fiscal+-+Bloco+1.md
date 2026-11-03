---
content_hash: 51576fedba756cd055422fe36aec2f90528cc758a2838b5a5e7afa7a6fa77843
fetched_at: '2026-06-29T00:09:22.721888+00:00'
page_id: '422546011'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco 1
type: documentation
url: https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+1
version: 95
---

Este Bloco é composto pelos registros:

BLOCO1left10101010

**Obrigatoriedade dos Registros do Bloco 1**

Este registro deverá ser apresentado por todos os contribuintes. Caso a resposta seja "S", o contribuinte está obrigado à apresentação do registro respectivo. Se houver dispensa de apresentação do registro pela unidade federada, a resposta para o campo específico do registro deverá ser "N". O registro será gerado a partir de 01/07/2012

11001100

**Registro de Informação Sobre Exportação.**

Será gerado de acordo com os lançamento de exportação direta ou indireta pelo exportador existentes no período de geração da rotina.

11051105

**Documentos Fiscais de Exportação**

Este registro deverá ser gerado para documentos fiscais vinculados a exportação.

11101110

**Operações de Exportação Indireta - Mercadorias de Terceiros**

Registro gerado para apresentar a origem das mercadorias adquiridas para a exportação. Será apresentado quando a exportação for do tipo "Indireta" e possuir lançamento de entrada referenciado ao mesmo.

120012001210121012501250

**Informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS**

Esse registro contém o somatório de todos os valores declarados no Registro 1255.

**Campo 02** (VL\_CREDITO\_ICMS\_OP) – Soma do campo “VL\_CREDITO\_ICMS\_OP\_MOT” dos registros 1255.

**Campo 03** (VL\_ICMS\_ST\_REST) – Soma do campo “VL\_ICMS\_ST\_REST\_MOT” dos registros 1255.

**Campo 04** (VL\_FCP\_ST\_REST) – Soma do campo “VL\_FCP\_ST\_REST\_MOT” dos registros 1255.

**Campo 05** (VL\_ICMS\_ST\_COMPL) – Soma do campo “VL\_ICMS\_ST\_COMPL\_MOT” dos registros 1255.

**Campo 06** (VL\_FCP\_ST\_COMPL) – Soma do campo “VL\_FCP\_ST\_COMPL\_MOT” dos registros 1255.

12551255

**Informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS por motivo**

Campo 02 (COD\_MOT\_REST\_COMPL) - Código do motivo da restituição ou complementação conforme Tabela 5.7

Campo 03 (VL\_CREDITO\_ICMS\_OP\_MOT) - Informar o valor total do ICMS operação própria que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito, para o mesmo “COD\_MOT\_REST\_COMPL” →  Somatório do Campo 12 dos Registros C185 e Campo 13 do Registro C181 multiplicados pelo campo QUANT\_CONV

Campo 04 (VL\_ICMS\_ST\_REST\_MOT) - Informar o valor total do ICMS ST que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito, para o mesmo  “COD\_MOT\_REST\_COMPL”  → Somatório do Campo 15 dos Registros C185 e Campo e Campo 18 do Registro C181 multiplicados pelo campo QUANT\_CONV

Campo 05 (VL\_FCP\_ST\_REST\_MOT) - Informar o valor total do FCP\_ST agregado ao valor do ICMS ST informado no campo “VL\_ICMS\_ST\_REST\_MOT” → Somatório do Campo 16 dos Registros C185 e Campo 19 do Registro C181

Campo 06 (VL\_ICMS\_ST\_COMPL\_MOT) Informar o valor total do débito referente ao complemento do imposto, nos casos previstos na legislação, para o mesmo “COD\_MOT\_REST\_COMPL” → Somatório dos campos 17 dos registros C185 e Campo 20 do Registro C181

Campo 07 (VL\_FCP\_ST\_COMPL\_MOT) - Informar o valor total do FCP\_ST agregado ao valor informado no campo “VL\_ICMS\_ST\_COMPL\_MOT” → Somatório dos campos 18 dos registros C185 e Campo 21 do Registro C181

Os campos de 03 a 07 do Registro 1255 serão gerados conforme valores existentes nos registros C185 e C181

13001300

**Movimentação de Combustíveis**

Este registro deve ser apresentado pelos contribuintes do ramo varejista de combustíveis (postos de combustíveis). Serão gerados se o "Tipo Operação com combustíveis" da Filial for "Posto Varejista" e somente se os Lançamentos Fiscais forem provenientes do [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835).

Documentação: 

13101310

**Movimentação Diária de Combustíveis por Tanque**

**Campo 01** - Sigla: REG - Descrição: Texto fixo contendo "1310"

**Campo 02** - Sigla: NUM\_TANQUE - Descrição: Tanque que armazena o combustível.

**Campo 03** - Sigla: ESTQ\_ABERT - Descrição: Estoque no início do dia, em litros.

**Campo 04** - Sigla: VOL\_ENTR - Descrição: Volume recebido no dia, em litros.

**Campo 05** - Sigla: VOL\_DISP - Descrição: Volume disponível (03 + 04), em litros.

**Campo 06** - Sigla: VOL\_SAIDAS - Descrição: Volume total das saídas, em litros.

**Campo 07** - Sigla: ESTQ\_ESCR - Descrição: Estoque escritural (05 − 06), em litros.

**Campo 08** - Sigla: VAL\_PERDA - Descrição: Valor da perda, em litros.

**Campo 09** - Sigla: VAL\_AJ\_GANHO - Descrição: Valor do ganho, em litros.

**Campo 10** - Sigla: FECH\_FISICO - Descrição: Volume aferido no tanque, em litros. Estoque de fechamento físico do tanque.

**Campo 11** - Sigla: CAP\_TANQUE - Descrição: Capacidade de armazenamento, em litros.

Este registro deve ser apresentado para informar a movimentação diária por tanque. Não pode haver mais de um registro com o mesmo número de tanque. Informações são geradas de acordo com serviço provido pela [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835).

**Obs:** Nos casos em que dois ou mais tanques de combustíveis estiverem interligados ou a saída deles passe por um único filtro de combustível, de forma que não seja possível identificar qual tanque alimentou um determinado “Bico”, os valores dos tanques deverão ser agrupados (somados), como se fossem um único tanque e informados em um único registro 1310. Neste caso, o campo NUM\_TANQUE deverá, sempre, conter o número de um dos tanques, que deve ser referenciado no  
registro 1370.

13201320

**Volume de Vendas**

Este registro tem por objetivo discriminar o volume das vendas no dia, considerando-se vendas todas as saídas promovidas a qualquer título. Informações são geradas de acordo com serviço provido pela [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835).

13501350

**Bombas**

Este registro deve ser apresentado para discriminar as bombas pertencentes ao varejista. Será gerado a partir de movimentações do cadastro de [Bomba](http://tdn.totvs.com/pages/viewpage.action?pageId=423938240) do [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835).

13601360

**Lacres da Bomba**

Este registro deve ser apresentado para discriminar as bombas pertencentes ao varejista. Será gerado a partir de movimentações do cadastro de [Lacre de Bomba](http://tdn.totvs.com/pages/viewpage.action?pageId=423937988) do [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835).

13701370

**Bicos da Bomba**

Este registro deve ser apresentado para discriminar as bombas pertencentes ao varejista. Será gerado a partir de movimentações do cadastro de [Bico de Bomba](http://tdn.totvs.com/pages/viewpage.action?pageId=423938239) do [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835).

13901390

**Controle de Produção da Usina**

Será gerado a partir do cadastro da Produção Diária da Usina localizado no [TOTVS Gestão Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=198948859) no menu Cadastros | Mais...

13911391

**Produção Diária da Usina**

Será gerado a partir dos Valores informados no Grupo de Valores do cadastro do Produção Diária da Usina localizado no [TOTVS Gestão Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=198948859) no menu Cadastros | Mais...

Novos registros gerados a partir de 2020:

Informações geradas conforme disposto nos novos campos do cadastro de Usina.

COD\_ITEM - Gerado conforme produto informado no cadastro de Usina.

TP\_RESIDUO - Gerado conforme tipo de Resídio selecionado no cadastro de Usina.

QTD\_RESIDUO - Gerado conforme informação preenchida no campo "Quantidade de resíduo produzido".

No layout 3.1.4 de 2023 foram incluídos os seguintes campos: no registro 1391:

* 21 - QTD\_RESIDUO\_ DDG;
* 22 - QTD\_RESIDUO\_ WDG;
* 23 - QTD\_RESIDUO\_ CANA.

Confira os detalhes na documentação da atualização do layout: 

14001400

**Informação Sobre Valores Agregados**

Este registro tem como objetivo fornecer informações para o cálculo do valor adicionado por Município, sendo utilizado para subsidiar cálculos de índices de participação.

Para este registro, serão selecionados:

* Lançamento de Entrada com natureza de operação cujo Tipo Nat DIPI seja igual a 21 - "Compras a Extrat. Prod. Agrop. e Pescadores", a categoria do cli/for seja pessoa física e seu ramo de atividade seja "Produtor Rural" (*Cliente/Fornecedor > Outros > Tributos > Ramo de Atividade*) ;
* Lançamentos de Saída com natureza de operação entre X.250 a X.399;
* Lançamentos cujo Tipo Nat DIPI seja igual a "Adicionado por Município".

Só serão selecionados lançamentos cuja UF de Serviço ou de Coleta seja a mesma UF da Filial (regra válida à partir do ano de 2015).

* **Município da Coleta preenchido +  Município do Serviço preenchido** = Gerar 1400 com o código  **Município do Serviço**
* **Município da Coleta NÃO preenchido +  Município do Serviço preenchido** = Gerar 1400 com o código  **Município do Serviço**
* **Município da Coleta preenchido +  Município do Serviço NÃO preenchido =**Gerar 1400 com o código  **Município de Coleta**
* **Município da Coleta NÃO preenchido +  Município do Serviço NÃO preenchido = Não gerar o 1400**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Texto fixo contendo "1400" | Valor fixo “1400” |
| 02 | COD\_ITEM\_IPM | Código do item (Tabela 5.9.1 de Itens UF Índice de Participação dos Municípios ou Tabela 5.9.2 de Itens UF\_ST Índice de participação dos Municípios) ou campo 02 do Registro 0200 |  |
| 03 | MUN | Código do Município de origem/destino |  |
| 04 | VALOR | Valor mensal correspondente ao município |  |

**1400 - Anual**  
  
A utilização do registro 1400 na modalidade anual se justifica pelo fato de que determinadas Unidades Federativas (UFs) têm exigido a geração de um registro adicional ao final do exercício, ou em situações específicas, como processos de cisão, fusão, entre outros eventos societários. Nesses casos, é necessária a apresentação da **totalização da Receita Bruta** em um único registro consolidado.

O Registro Anual deve ser gerado apenas quando exigido pela sua Unidade Federativa, caso exista a necessidade de geração do registro anual siga os passos da documentação abaixo:  
  
[Geração do Registro 1400 - Anual](https://tdn.totvs.com/display/LRM/Registro+1400+-+Anual)

15001500

**Nota Fiscal/Conta de Energia Elétrica Interestaduais (código 06)**

Serão selecionados Lançamentos Fiscais de Saída em operação interestaduais cujo o código modelo de documento seja igual a 06.

15101510

**Itens da Nota Fiscal/Conta de Energia Elétrica Interestaduais (código 06)**

Este registro tem por objetivo informar os itens das notas informadas no registro 1500.

16001600

**Total das Operações com Cartão de Crédito e/ou Débito**

* O registro será gerado considerado todas das VENDAS realizadas com Cartão de Credito ou Debito no período da Rotina, independente se foi “Baixado ou não”. Essa consistência estará considerando a “Data de Emissão” do Lançamento;

* O Lançamento fiscal deve ser proveniente do TOTVS Gestão de Estoques, Compras e Faturamentos escriturado para o TOTVS Gestão Fiscal;

* O Movimento deve ser integrado com o Financeiro, possuindo "Forma de Pagamento";

* Meios de pagamentos que não possuírem Cliente/Fornecedor, não serão gerados no Registro 1600. No Log da execução do processo de geração do SPED Fiscal, esses meios de pagamentos serão destacados.
* Será gerado apenas um Registro 1600 por Cliente/Fornecedor, sendo totalizado o valor de Crédito e Débito de cada Meio de Pagamento.InformaçõesPara datas anteriores a 01/01/2022 o registro será gerado e para datas posteriores a 31/12/2021 o registro não será gerado, conforme orientações do [Guia Prático EFD ICMS IPI - v 3.0.7](http://sped.rfb.gov.br/estatico/55/9CCACF05685E011D7100D6CF1AD79EFD60EDF0/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.7.pdf "Follow link")
16011601

**Operações com instrumentos de pagamento eletrônicos**

Este registro destina-se a identificar o valor total das operações realizadas pelo declarante por meio de instrumentos de pagamentos eletrônicos, discriminado por instituição financeira e de pagamento, integrante ou não do Sistema de Pagamento Brasileiro - SPB (Convênio ICMS n° 134/2016).

Deve-se consultar o contrato firmado entre a instituição e o informante do arquivo para se ratificar a existência da prestação do serviço, quando houver.

Deve ser informado o valor total destas operações, excluídos os estornos e cancelamentos. A obrigatoriedade deste registro deve ser verificada junto a cada um das unidades federativas.

##### **Consistências do sistema:**

* O registro será gerado considerado todas das VENDAS realizadas **(****exceto para os meios de pagamento dinheiro)** Cujo o meio de pagamento esteja parametrizado para geração do Registro 1601.   
  Veja: [Como parametrizar o Registro 1601 no meio de pagamento.](https://tdn.totvs.com/display/LRM/Meio+de+Pagamento)
* Será gerado para os tipos de transações: Crédito, Débito e Outros.
* O Lançamento fiscal deve ser proveniente do TOTVS Gestão de Estoques, Compras e Faturamentos, quando a data de geração do 1601 estiver parametrizada como "Emissão do movimento" o movimento deve ser escriturado para o TOTVS Gestão Fiscal, as demais datas com origem do financeiro não exigem que o movimento esteja escriturado para geração do registro 1601.
* O Movimento deve ser integrado com o Financeiro, possuindo "Forma de Pagamento";
* Meios de pagamentos que não possuírem Cliente/Fornecedor, ou não estejam devidamente parametrizados para o 1601 e dentro da vigência, não serão gerados no Registro 1601. No Log da execução do processo de geração do SPED Fiscal, esses meios de pagamentos serão destacados;
* Será gerado apenas um Registro 1601 por Cliente/Fornecedor, sendo totalizado o valor de cada Meio de Pagamento.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Texto fixo contendo "1601" | Valor fixo “1601” |
| 02 | COD\_PART\_IP | Código do participante (campo 02 do Registro 0150): identificação da instituição que efetuou o pagamento. | TFORMAPAGTO.CODCFO |
| 03 | COD\_PART\_IT | Código do participante (campo 02 do Registro 0150): identificação do intermediador da transação | TINTERMEDIADOR.CNPJ |
| 04 | TOT\_VS | Valor total bruto das vendas e/ou prestações de serviços no campo de incidência do ICMS, incluindo operações com imunidade do imposto | TPAGTO.VALOR (Soma o valor por código de tributo - ICMS) |
| 05 | TOT\_ISS | Valor total bruto das prestações de serviços no campo de incidência do ISS | TPAGTO.VALOR (Soma o valor por código de tributo - ISS) |
| 06 | TOT\_OUTROS | Valor total de operações deduzido dos valores dos campos TOT\_VS e TOT\_ISS. | Será gerado sob demanda |

InformaçõesO registro será gerado a partir de 01/01/2022, conforme orientações do [Guia Prático EFD ICMS IPI - v 3.0.7](http://sped.rfb.gov.br/estatico/55/9CCACF05685E011D7100D6CF1AD79EFD60EDF0/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.7.pdf "Follow link")17001700

**Documentos Utilizados**

Os dados serão buscados na tabela de AIDF para os documentos movimentados no período.

17101710

**Documentos Fiscais Cancelados e Inutilizados**

Neste registro devem ser informados os documentos cancelados/inutilizados no intervalo constante do Registro 1700.

18001800

**DCTA - Demonstrativo de Crédito do ICMS Sobre Transporte Aéreo**

**Registro não gerado**

19001900

#### **Indicador de Sub-apuração do ICMS**

Este registro tem por objetivo escriturar o ICMS de operações especificadas em legislação estadual como obrigadas a apurações em separado. Este registro deverá ser apresentado somente pelos contribuintes obrigados por legislação específica de cada UF.

Deve ser gerado um Registro para cada Sub-apuração informada nos Períodos de Apuração do ICMS e ICMSST considerando o Período da rotina.

Podem existir várias no período. Este registro é “filho” do Registro 0000 (nível 2).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1921” |
| 02 | IND\_APUR\_ICMS | Indicador de outra apuração do ICMS:   3 – APURAÇÃO 1;   4 – APURAÇÃO 2;   5 – APURAÇÃO 3;   6 – APURAÇÃO 4;   7 – APURAÇÃO 5;   8 – APURAÇÃO 6. | DSUBAPURACAOPERIODO.CODAPURACAO |
| 03 | DESCR\_COMPL\_OUT\_APUR | Descrição complementar de Outra Apuração do ICMS. | DSUBAPURACAOPERIODO.DESCRICAO |

19101910

#### **Período da Sub-apuração do ICMS**

Este registro tem por objetivo informar o(s) período(s) das apurações em separado do ICMS. Os períodos informados devem abranger todo o intervalo da escrituração fiscal, sem sobreposição ou omissão de datas ou períodos.

Este registro também deve ser gerado com as informações do Anexo de Sub-Apuração selecionadas para geração do 1900. Também podem conter vários registro no período. Registro “filho” do 1900 (nível 3).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1921” |
| 02 | DT\_INI | Data inicial da sub-apuração | DSUBAPURACAOPERIODO.DTINICIOPER |
| 03 | DT\_FIN | Data final da sub-apuração | DSUBAPURACAOPERIODO.DTFIMPER |

19201920

#### **Sub-apuração do ICMS**

Este registro tem por objetivo informar os valores relativos a apurações especificadas no registro 1900, que se referem aos valores do ICMS das operações próprias estornados do registro E110 por meio de ajustes decorrentes de documentos, nos campos 03 (VL\_AJ\_DEBITOS) e 07 (VL\_AJ\_CREDITOS), e por meio de ajustes de apuração nos campos 05 (VL\_ESTORNOS\_CRED) e 09 (VL\_ESTORNOS\_DEB).

A origem dos dados deste registro são os valores apurados para cada Sub-apuração no momento do encerramento. Este registro deve ser único no período por sub-apuração e deve conter os somatórios dos valores de todas as sub-apurações selecionadas no período. Registro Filho do 1910 (nível 4).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1921” |
| 02 | VL\_TOT\_TRANSF\_DEBITOS\_OA | Valor total dos débitos por “Saídas e prestações com débito do imposto” | DSUBAPURACAOPERIODO.TOTALDEBITOSSAIDA |
| 03 | VL\_TOT\_AJ\_DEBITOS\_OA | Valor total de “Ajustes a débito” | DSUBAPURACAOPERIODO.TOTALAJUSTESDEBITO |
| 04 | VL\_ESTORNOS\_CRED\_OA | Valor total de Ajustes “Estornos de créditos” | DSUBAPURACAOPERIODO.TOTALAJUSTESCREDESTORNO |
| 05 | VL\_TOT\_TRANSF\_CREDITOS\_OA | Valor total dos créditos por “Entradas e aquisições com crédito do imposto” | DSUBAPURACAOPERIODO.TOTALCREDITOSENTRADA |
| 06 | VL\_TOT\_AJ\_CREDITOS\_OA | Valor total de “Ajustes a crédito” | DSUBAPURACAOPERIODO.TOTALAJUSTESCREDITOS |
| 07 | VL\_ESTORNOS\_DEB\_OA | Valor total de Ajustes “Estornos de Débitos” | DSUBAPURACAOPERIODO.TOTALAJUSTESDEBESTORNO |
| 08 | VL\_SLD\_CREDOR\_ANT\_OA | Valor total de “Saldo credor do período anterior” | DSUBAPURACAOPERIODO.SALDOCREDORANTERIOR |
| 09 | VL\_SLD\_APURADO\_OA | Valor do saldo devedor apurado | DSUBAPURACAOPERIODO.SALDOAPURADO + DSUBAPURACAOPERIODO.TOTALDEDUCOES |
| 10 | VL\_TOT\_DED | Valor total de “Deduções” | DSUBAPURACAOPERIODO.TOTALDEDUCOES |
| 11 | VL\_ICMS\_RECOLHER\_OA | Valor total de "ICMS a recolher (09-10) | DSUBAPURACAOPERIODO.SALDOAPURADO |
| 12 | VL\_SLD\_CREDOR\_TRANSP\_OA | Valor total de “Saldo credor a transportar para o período seguinte” | Quando gerado saldo positivo (credor) no campo DSUBAPURACAOPERIODO.SALDOAPURADO. |
| 13 | DEB\_ESP\_OA | Valores recolhidos ou a recolher, extraapuração. | DSUBAPURACAOPERIODO.DEBITOSESPECIAIS |

19211921

**Ajuste/Benefício/Incentivo da Sub-apuração do ICMS**

**Este registro traz os detalhes dos lançamentos de ajustes que afetaram a sub-apuração**

Lançamentos de Outros Débitos/Créditos que tenham uma sub-apuração associada.

Podem existir vários no período. Esse registro é filho do 1920 (nível 5).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1921” |
| 02 | COD\_AJ\_APUR | Código do ajuste da SUB-APURAÇÃO e dedução, conforme a Tabela indicada no item 5.1.1. | DLDC.CODAJUSTESPED |
| 03 | DESCR\_COMPL\_AJ | Descrição complementar do ajuste da apuração. | DLDC.OBSERVACAO |
| 04 | VL\_AJ\_APUR | Valor do ajuste da apuração | DLDC.VALORLDC |

19221922

Este registro tem por objetivo detalhar os ajustes do registro 1921 quando forem relacionados a processos judiciais, fiscais ou a documentos de arrecadação.

Esse registro é filho do 1921 (nível 6).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1922” |
| 02 | NUM\_DA | Número do documento de arrecadação estadual, se houver | Não será gerado. Atualmente não é possível associar uma guia ao lançamento de outros débitos/créditos |
| 03 | NUM\_PROC | Número do processo ao qual o ajuste está vinculado, se houver | DPROCESSOJUDICIAL.NUMERO |
| 04 | IND\_PROC | Indicador da origem do processo:  0- SEFAZ;  1- Justiça Federal;  2- Justiça Estadual;  9- Outros | Primeiro carácter do campo DPROCESSOJUDICIAL.TIPO |
| 05 | PROC | Descrição resumida do processo que embasou o lançamento | DPROCESSOJUDICIAL.DESCRICAO |
| 06 | TXT\_COMPL | Descrição complementar | Não será gerado. |

19231923

#### **Informações Adicionais dos Ajustes da SubApuração do ICMS - Identificação dos Documentos Fiscais**

Este registro tem por objetivo identificar os documentos fiscais relacionados ao ajuste.

Esse registro é filho do 1921 (nível 6).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1923” |
| 02 | COD\_PART | Código do participante (campo 02 do Registro 0150): - do emitente do documento ou do remetente das mercadorias, no caso de entradas; - do adquirente, no caso de saídas | FCFO.CODCFO |
| 03 | COD\_MOD | Código do modelo do documento fiscal | FTDO.CODMODDOC |
| 04 | SER | Série do documento fiscal | DLAF.SERIEDOC |
| 05 | SUB | Subsérie do documento fiscal | DLAF.SUBSERIE |
| 06 | NUM\_DOC | Número do documento fiscal | DLAF.DOCINI |
| 07 | DT\_DOC | Data da emissão do documento fiscal | DLAF.DATAEMISSAO |
| 08 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | TPRODUTO.CODPRD |
| 09 | VL\_AJ\_ITEM | Valor do ajuste para a operação/item | Origem lançamento Outros Débitos e Créditos:  DLDCNF.VALORTOTAL  Origem Ajuste de Lançamento Fiscal:  DITEMAJUSTESPED. VALORICMSICMSST ou  DLAFAJUSTESPED.VALORICMSICMSST |
| 10 | CHV\_DOCe | Chave do Documento Eletrônico | DLAF.CHAVEACESSONFE |

19251925

#### **Informações Adicionais da Sub-apuração – Valores Declaratórios**

Este registro é gerado, para os Lançamentos de Outros Débitos/Créditos do Tipo “Não de aplica” e que possua uma sub-apuração associada. Podem ser gerados vários registros por período.

Esse registro é filho do 1920 (nível 5).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1925” |
| 02 | COD\_INF\_ADIC | Código da informação adicional conforme tabela a ser definida pelas SEFAZ, conforme tabela definida no item 5.2. | DLDC.CODAJUSTESPED |
| 03 | VL\_INF\_ADIC | Valor referente à informação adicional | DLDC.VALORLDC |
| 04 | DESCR\_COMPL\_AJ | Descrição complementar do ajuste | DLDC.OBSERVACAO |

19601960, 1970, 1975 e 1980

**Registro 1960: GIAF 1 - Guia de Informação e Apuração de Incetivos Fiscais e Financeiro: Indústria (Crédito Presumido)**

Este registro será gerado quando o Indicador do enquadramento do Benefício Fiscal associado à Sub-Apuração for “Indústria (crédito presumido)”.

**Registro 1970: GIAF 3 - Guia de Informação e Apuração de Incentivos Fiscais e Financeiros: Importação (Diferimento na Entrada e Crédito Presumido na Saída Subsequente)**

**Registro 1975: GIAF 3 - Guia de Informação e Apuração de Incentivos Fiscais e Financeiros: Importação (Saídas Internas por Faixa de Alíquota)**

Estes registros serão gerados quando o Indicador do enquadramento do Benefício Fiscal associado à Sub-Apuração for “Importação (diferimento/crédito presumido)"

**Registro 1980: GIAF 4 - Guia de Informação e Apuração de Incentivos Fiscais e Financeiros: Central de Distribuição (Entradas/Saídas)**Este registro será gerado quando o Indicador do enquadramento do Benefício Fiscal associado à Sub-Apuração for “Central de distribuição (entradas/saídas)”.

*Estes registros são gerados com informações extraídas do Período de Apuração do Tributo ICMS, na aba Prodepe Sub-Apuração. Somente para contribuintes domiciliados em Pernambuco.*

Informações Relacionadas

Para a correta geração dos registros devem ser observadas as instruções contidas no [Documento de Referência da SEF II](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546136).

Para mais detalhes leia o [O Documento Técnico DT SPED Fiscal - Registros 1010, 1960, 1970, 1975 e 1980 (GIAF)](http://tdn.totvs.com.br/pages/viewpage.action?pageId=440845930)
