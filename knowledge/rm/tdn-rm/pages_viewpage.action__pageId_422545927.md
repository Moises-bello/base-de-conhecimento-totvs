---
content_hash: 7aba2af2fa99b757710b12bcb27636e65e2813bbbb4598b1bfc035b3a14d68e8
fetched_at: '2026-06-29T00:09:21.905668+00:00'
page_id: '422545927'
product: rm
source: tdn-rm
title: Bloco M (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545927
version: 109
---

true1left

## Apuração da Contribuição e Crédito do PIS/Pasep e da Cofins

Também são demonstrados neste bloco as informações de deferimento dos tributos.                                                                                                                                                                        Acesse o link  e veja como configurar a geração dos registros M100/M500, M105/M505, M200/M600, M205/M605 e M210/M610.

m001Registro M001

**Registro M001 — Abertura do Bloco M**

Este registro informa se houve movimentação no bloco M.

m100Registro M100

**Registro M100 — Crédito de PIS/Pasep Relativo ao Período**

Este registro tem por finalidade realizar a consolidação do crédito relativo à contribuição para o PIS/PASEP apurado no período. Deve ser gerado um registro M100 especifico para cada tipo de crédito apurado (vinculados à receita tributada, vinculados à receita não tributada e vinculados à exportação), conforme a Tabela de tipos de créditos “Tabela 4.3.6”, bem como para créditos de operações próprias e créditos transferidos por eventos de sucessão.

Para a geração deste registro serão selecionados os Registros  A100/A170, C100/C170, C500/C501, F100, gerados no Período de Apuração em anexo Detalhamento da Apuração, com CST correspondente a crédito ou Código do Tipo da Operação:

* 0 – Operação Representativa de Aquisição, Custos, Despesa ou Encargos, ou Receitas, Sujeita à Incidência de Crédito de PIS/Pasep  (CST 50 a 66).

Para gravar os dados na Detalhamento da Apuração, é necessário encerrar o Período de Apuração;

InformaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento Apuração10Passo 1Encerrando do Período de ApuraçãoDados gravados no anexo Detalhamento da Apuração

O Cálculo no encerramento do Período de Apuração continua considerando os Parâmetros de Processo.

1Passo 2Gerador de SaídasObservação

O Registro M100 não será gerado quando o Código indicador da incidência tributaria no período for igual a **"2 - Com incidência no regime cumulativo"**.

3Passo 3

Após o detalhamento da apuração ser preenchido, basta executar a rotina EFD-Contribuições para o registro M100 apresentar os dados;

Exemplo do registro M100 geradoLayout do Registro

Registro agrupado pelos campos COD\_CRED e IND\_CRED\_ORI.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG |  | Fixo M100 |
| 02 | COD\_CRED | Código de Tipo de Crédito apurado no período, conforme a Tabela 4.3.6. | Campo deve ser gerado internamente conforme a consistência feita na tabela 4.3.6 |
| 03 | IND\_CRED\_ORI | Indicador de Crédito Oriundo de: 0 – Operações próprias 1 – Evento de incorporação, cisão ou fusão | Fixo 0 A opção 1 - Evento de Incorporação, Cisão ou Fusão Não será gerado neste momento. |
| 04 | VL\_BC\_PIS | Valor da base de cálculo do tributo | Campo gerado com o valor da Base de Cálculo do PIS/COFINS do Período de Apuração\Sub pasta Detalhamento da Apuração |
| 05 | ALIQ\_PIS | Alíquota do PIS/PASEP (em percentual) | Campo gerado com a alíquota constante no Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 06 | QUANT\_BC\_PIS | Quantidade – Base de cálculo PIS | Não será gerado neste momento. |
| 07 | ALIQ\_PIS\_QUA NT | Alíquota do PIS (em reais) | Não será gerado neste momento. |
| 08 | VL\_CRED | Valor total do crédito apurado no período | Gerado com o valor do Imposto PIS/COFINS do Período de Apuração\Sub Pasta Detalhamento da Apuração. |
| 09 | VL\_AJUS\_ACRE S | Valor total dos ajustes de acréscimo | Não será gerado neste momento. |
| 10 | VL\_AJUS\_REDU C | Valor total dos ajustes de redução | Não será gerado neste momento. |
| 11 | VL\_CRED\_DIF | Valor total do crédito diferido no período | Não será gerado neste momento. |
| 12 | VL\_CRED\_DISP | Valor Total do Crédito Disponível relativo ao Período (08 + 09 – 10 – 11) =(VL\_CRED + VL\_AJUS\_ACRES - VL\_AJUS\_REDUC - VL\_CRED\_DIF) | Totalizador. Calculado pela rotina |
| 13 | IND\_DESC\_CRE D | Indicador de opção de utilização do crédito disponível no período:                         0 – Utilização do valor total para desconto da contribuição apurada no período, no Registro M200;                                                                                                         1 – Utilização de valor parcial para desconto da contribuição apurada no período, no Registro M200. | Gerado fixo “0 – Utilização do valor total para desconto da contribuição apurada no período, no Registro.                                                                                            A opção “1” não será implementada neste momento. |
| 14 | VL\_CRED\_DESC | Valor do Crédito disponível, descontado  da contribuição apurada no próprio período.                                                                                                              Se IND\_DESC\_CRED=0, informar o valor total do Campo 12; Se IND\_DESC\_CRED=1, informar o valor parcial do Campo 12. | Valor do Crédito disponível, descontado da contribuição apurada no próprio período. Esta informação será gerada conforme o conteúdo do campo 13.                                                                                                                 Se for 0  (utilização do valor total) será gravado neste campo o valor apurado no campo 12 – Valor do Crédito disponível.                                                                                        Para a Opção 1 (utilização parcial) não será gerado neste momento. |
| 15 | SLD\_CRED | Saldo de créditos a utilizar em períodos futuros (12 – 14) | Não será gerado neste momento |

m105Registro M105

**Registro M105 — Detalhamento da Base de Calculo do Crédito Apurado no Período – PISPasep**

Neste registro será informada a composição da base de cálculo de cada tipo de crédito (M100), conforme as informações constantes nos documentos e operações com CST geradores de créditos, escriturados nos Blocos “A”, “C”  e “F”. Os valores representativos de Bases de Cálculo  escriturados nestes registros serão transferidos para o Registro PAI M100 (Campos 04 e 06), que especifica e escritura os diversos tipos de créditos da escrituração.

Deve ser escriturado um registro M105 para cada CST recuperado dos registros dos Blocos “A”, “C” e “F”, vinculado ao tipo de crédito informado no Registro M100.

Para a geração deste registro serão selecionados os Registros A100/A170, C100/C170, C500/C501, F100 gerados no Período de Apuração\ Sub Pasta Detalhamento da Apuração

Para gravar os dados na Detalhamento da Apuração, é necessário encerrar o Período de Apuração;

ObservaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento da Apuração10Passo 1Encerrando do Período de ApuraçãoDados gravados no anexo Detalhamento da Apuração1Passo 2

Após o detalhamento da apuração ser preenchido, basta executar a rotina EFD-Contribuições para o registro M105 apresentar os dados;

Exemplo do registro M105 geradoLayout do Registro

Registro agrupado pelo NAT\_BC\_CRED e CST.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG | Texto fixo contendo "M105" | Fixo M105 |
| 02 | NAT\_BC\_CRED | Código da Base de Cálculo do Crédito apurado no período, conforme a Tabela 4.3.7. | Gerado conforme do Campo Natureza do Crédito  do Período de Apuração\Sub Pasta Detalhamento da Apuração. NATBCCREDITO.DDETALHAMENTOAPURACAOPISCOFINS |
| 03 | CST\_PIS | Código da Situação Tributária referente ao crédito de PIS/Pasep (Tabela 4.3.3) vinculado ao tipo de crédito escriturado em M100. | Gerado com o CST do Período de Apuração\Sub Pasta Detalhamento da Apuração CST.DDETALHAMENTOAPURACAOPISCOFINS. |
| 04 | VL\_BC\_PIS\_TOT | Valor Total da Base de Cálculo escriturada nos documentos e operações (Blocos “A”, “C”, “D” e “F”), referente ao CST\_PIS informado no Campo 03. | Gerado com a base de cálculo do Período de Apuração\Sub Pasta Detalhamento da Apuração BASEDECALCULO.DDETALHAMENTOAPURACAOPISCOFINS |
| 05 | VL\_BC\_PIS\_CUM | Parcela do Valor Total da Base de Cálculo informada no Campo 04, vinculada a receitas com incidência cumulativa.Campo de preenchimento específico para a pessoa jurídica sujeita ao regime cumulativo e não-cumulativo da contribuição (COD\_INC\_TRIB = 3 do Registro 0110) | Neste momento este campo não será gerado. |
| 06 | VL\_BC\_PIS\_NC | Valor Total da Base de Cálculo do Crédito, vinculada a receitas com incidência não-cumulativa (Campo 04 – Campo 05). | Gerado com a base de cálculo do Tributo dos Itens dos Lançamentos Fiscais de Entrada, Lançamentos Financeiros a receber e dados carregados do TOTVS Gestão de Patrimônio que possuam  código de contribuição apurada (tabela 4.3.5 EFD) igual a 01, 02, 03, 04 e 71. Este campo deverá ser criado conforme especificação dos registros M200 e M600. |
| 07 | VL\_BC\_PIS | Valor da Base de Cálculo do Crédito, vinculada ao tipo de Crédito escriturado em M100. Para os CST\_PIS = “50”, “51”, “52”, “60”, “61” e “62”: Informar o valor do Campo 06 (VL\_BC\_PIS\_NC); Para os CST\_PIS = “53”, “54”, “55”, “56”, “63”, “64” “65” e “66” (Crédito sobre operações vinculadas a mais de um tipo de receita): Informar a parcela do valor do Campo 06 (VL\_BC\_PIS\_NC) vinculada especificamente ao tipo de crédito escriturado em M100.  O valor deste campo será transportado para o Campo 04 (VL\_BC\_PIS) do registro M100. | Gerado com o Valor do Campo 06 (VL\_BC\_\_NC) vinculada especificamente ao tipo de crédito escriturado em M100.  O valor deste campo será transportado para o Campo 04 (VL\_BC\_PIS) do registro M100. |
| 08 | QUANT\_BC\_PIS\_TOT | Quantidade Total da Base de Cálculo do Crédito apurado em Unidade de Medida de Produto, escriturada nos documentos e operações (Blocos “A”, “C”, “D” e “F”), referente ao CST\_PIS informado no Campo 03 | Não será gerado no momento |
| 09 | QUANT\_BC\_PIS | Parcela da base de cálculo do crédito em quantidade (campo 08) vinculada ao tipo de crédito escriturado em M100. Para os CST\_PIS = “50”, “51” e “52”: Informar o valor do Campo 08 (QUANT\_BC\_PIS); Para os CST\_PIS = “53”, “54”, “55” e “56” (crédito vinculado a mais de um tipo de receita): Informar a parcela do valor do Campo 08 (QUANT\_BC\_PIS) vinculada ao tipo de crédito escriturado em M100.  O valor deste campo será transportado para o Campo 06 (QUANT\_BC\_PIS) do registro M100. | Não será gerado no momento |
| 10 | DESC\_CRED | Descrição do crédito |  |

Registro M200

**Registro M200 — Consolidação da Contribuição para o PIS/Pasep do Período**

Neste registro serão consolidadas as contribuições sociais apuradas no período da escrituração, nos regimes não cumulativo e cumulativo, bem como procedido ao desconto dos créditos não cumulativos apurados no próprio período, dos créditos apurados em períodos anteriores, dos valores retidos na fonte e de outras deduções previstas em Lei, demonstrando em seu final os valores devidos a recolher.

A apuração do bloco M200 é realizado pelos valores dos registros dos bloco A, C e F.

Para a geração deste registro, serão utilizadas as informações contidas na aba **Valores Apuração Pis/Cofins** dentro do **Período de Apuração PIS**.

ObservaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento Apuração01Passo 1Encerrando do Período de ApuraçãoValores Apuração Pis/Cofins2Passo 2

Após os **Valores Apuração Pis/Cofins** serem preenchidas, basta executar a rotina EFD-Contribuições para o registro M200 apresentar os dados;

Exemplo do registro M200 geradoLayout do registro

Gerado um registro por arquivo SPED.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG | Texto Fixo M 200 | Fixo M200 |
| 02 | VL\_TOT\_CONT\_NC\_PER | Valor total da contribuição Não Cumulativa do Período (recuperado do campo 13 do Registro M210), quando o campo "COD CONT" = 01,02,03,04,32 E 71) | Gerado com a soma do Valor do Imposto do Período de Apuração no Detalhamento da Apuração que possuam o tipo de contribuição igual a 01, 02, 03, 04, 32 e 71, considerando as consistências do Item 1.Valor a ser Transportado do Campo 13 do Registro M210 |
| 03 | VL\_TOT\_CRED\_DESC | Valor do Crédito Descontado, Apurado no Próprio Período da Escrituração (recuperado do campo 14 do Registro M100 | Valor a ser transportado do campo 14 do registro M100 |
| 04 | VL\_TOT\_CRED\_DESC\_ANT | Valor do Crédito Descontado, Apurado em Período de Apuração Anterior (recuperado do campo 13 do Registro 1100) | Este campo não gerado neste momento. |
| 05 | VL\_TOT\_CONT\_NC\_DEV | Valor Total da Contribuição Não Cumulativa Devida (02 – 03 - 04) | Campo calculado pela rotina. |
| 06 | VL\_RET\_NC | Valor Retido na Fonte Deduzido no Período | Este campo não será gerado neste momento |
| 07 | VL\_OUT\_DED\_NC | Outras Deduções no Período | Este campo não será gerado neste momento |
| 08 | VL\_CONT\_NC\_REC | Valor da Contribuição Não Cumulativa a Recolher/Pagar (05 – 06 - 07) | Campo calculado pela rotina. |
| 09 | VL\_TOT\_CONT\_CUM\_PER | Valor Total da Contribuição Cumulativa do Período (recuperado do campo 13 do Registro M210, quando o campo “COD\_CONT” = 31, 32, 51, 52, 53, 54 e 72) | Gerado com a soma do Valor do Imposto do Período de Apuração\Sub Pasta Detalhamento da Apuração  que possuam o tipo de contribuição igual a 31, 32, 51, 52, 53, 54 e 72,.Valor a ser Transportado do Campo 13 do Registro M210 |
| 10 | VL\_RET\_CUM | Valor Retido na Fonte Deduzido no Período | Este campo não será gerado neste momento |
| 11 | VL\_OUT\_DED\_CUM | Outras Deduções no Período | Este Campo não será gerado neste momento |
| 12 | VL\_CONT\_CUM\_REC | Valor da Contribuição Cumulativa a Recolher/Pagar (09 - 10 – 11) | Campo calculado pela rotina. |
| 13 | VL\_TOT\_CONT\_REC | Valor Total da Contribuição a Recolher/Pagar no Período (08 + 12) | Campo calculado pela rotina. |

m205Registro M205

**Registro M205 — Contribuição para o PIS/Pasep a Recolher–Detalhamento por Código de Receita**

Neste registro será informado, por código de receita (conforme códigos de débitos informados em DCTF), o detalhamento da contribuição a recolher informada nos campos 08 (regime não cumulativo) e 12 (regime cumulativo) do Registro Pai M200.

Para a geração deste registro são selecionadas todas as guias DARF incluídas no anexo do Período de Apuração PIS.

ObservaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento Apuração11Passo 1Encerrando do Período de ApuraçãoGeração de Guias AutomaticamenteGuia DARF Gerada

No cadastro da Guia, utilizamos o campo "Código da Obrigação", na aba Outros Dados para identificar o código da contribuição a recolher e fazer o agrupamento da apuração.

Podendo ser:

* "08" para regime não cumulativo
* "12" para regime cumulativo.

É necessário respeitar o tamanho do campo de dois dígitos, para validação no PVA.

2Passo 2

Após encerrar o Período de Apuração e executar a rotina, o arquivo deve ser gerado conforme exemplo abaixo.

Exemplo do arquivo gerado com o registro M205Layout do Registro

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG | Texto Fixo M 205 | Fixo M205 |
| 02 | NUM\_CAMPO | Informar o número do campo do registro “M200” (Campo 08 (contribuição não cumulativa) ou Campo 12 (contribuição cumulativa)), objeto de detalhamento neste registro | Informar o número do campo do registro “M200” (Campo 08 (contribuição não cumulativa) ou Campo 12 (contribuição cumulativa)), objeto de detalhamento neste registro.DGUIAPERIODO.CODIGOOBRIGACAO |
| 03 | COD\_REC | Informar o código da receita referente à contribuição a recolher, detalhada neste registro. | Informar o código da receita referente à contribuição a recolher, detalhada neste registro.Gerado conforme o Código da Receita da guia DGUIAPERIODO.CODRECEITA |
| 04 | VL\_DEBITO | Valor do débito correspondente ao código do Campo 03, conforme informação na DCTF. | Valor do débito correspondente ao código do Campo 03, conforme informação na DCTF. Gerado com o Valor Paga informado na Guia - Sup Pasta Valores DGUIAPERIODO.VALORPAGO |

m210Registro M210

**Registro M210 — Detalhamento da Contribuição para o PIS/Pasep do Período**

Este registro será gerado através do Anexo Detalhamento da Apuração de Período filtrando os registros com Tipo de Operação "Operações Sujeitas a Contribuições" e "Operações Não Sujeitas a Contribuições".

ObservaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento Apuração11Passo 1Encerrando do Período de ApuraçãoDados gravados no anexo Detalhamento da Apuração2Passo 2

Após encerrar o Período de Apuração e executar a rotina, o arquivo deve ser gerado conforme exemplo abaixo.

Exemplo do registro M210 geradoLayout do Registro

Registro agrupado pelo Campo COD\_CONT (conforme a Tabela 4.3.5) e campo ALIQ\_PIS

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG | Texto Fixo M 210 | Fixo M210 |
| 02 | COD\_CONT | Código da contribuição social apurada no período, conforme a Tabela 4.3.5. | Gerado conforme Código da contribuição social apurada do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 03 | VL\_REC\_BRT | Valor da Receita Bruta | Gerado conforme o Valor da Operação do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 04 | VL\_BC\_CONT | Valor da Base de Cálculo da Contribuição antes de ajustes | Gerado com o valor da Base de Cálculo do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 05 | VL\_AJUS\_ACRES\_BC\_PIS | Valor do total dos ajustes de acréscimo da base de cálculo da contribuição a que se refere o Campo 04 | Este Campo não será gerado neste momento |
| 06 | VL\_AJUS\_REDUC\_BC\_PIS | Valor da Base de Cálculo da Contribuição, após os ajustes. (Campo 07 = Campo 04 + Campo 05 - Campo 06) | Este Campo não será gerado neste momento |
| 07 | VL\_BC\_CONT\_AJUS | Alíquota do PIS/PASEP (em percentual) | (VL\_BC\_CONT  + VL\_AJUS\_ACRES\_BC\_PIS - VL\_AJUS\_REDUC\_BC\_PIS ) |
| 08 | ALIQ\_PIS | Alíquota do PIS (em reais) | Gerado com o valor da Alíquota do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 09 | QUANT\_BC\_PIS | Quantidade – Base de cálculo PIS | Este Campo não será gerado neste momento |
| 10 | ALIQ\_PIS\_QUANT | Alíquota do PIS (em reais) | Este Campo não será gerado neste momento |
| 11 | VL\_CONT\_APUR | Valor total da contribuição social apurada | Gerado conforme o Valor do Imposto do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 12 | VL\_AJUS\_ACRES | Valor total dos ajustes de acréscimo da contribuição social apurada | Este Campo não será gerado neste Momento |
| 13 | VL\_AJUS\_REDUC | Valor total dos ajustes de redução da contribuição social apurada | Este Campo não será gerado neste Momento |
| 14 | VL\_CONT\_DIFER | Valor da contribuição a diferir no período | Este Campo não será gerado neste Momento |
| 15 | VL\_CONT\_DIFER \_ANT | Valor da contribuição diferida em períodos anteriores | Este Campo não será gerado neste Momento |
| 16 | VL\_CONT\_PER | Valor Total da Contribuição do Período (11 + 12 – 13 – 14+15) | (VL\_CONT\_APUR  + VL\_AJUS\_ACRES -  VL\_AJUS\_REDUC - VL\_CONT\_DIFER + VL\_CONT\_DIFER\_ANT) |

m230Registro M230**Registro M230 — Informações adicionais de Diferimento**m300Registro M300**Registro M300 — Contribuição da PIS/PASEP diferida em períodos anteriores — Valores a pagar no período**m350Registro M350

**Registro M350 — PIS/PASEP — Folhas de Salário**  
Neste registro é gerado o Valor Total da Folha de Salários (Proventos) subtraído o Valor dos Eventos parametrizado no aplicativo [TOTVS](http://tdn.totvs.com.br/display/LRM/TOTVS+Folha+de+Pagamento)Gestão de Folha de Pagamento, onde o sistema calcula internamente o Valor Total da Contribuição Social sobre a Folha de Salários considerando a alíquota fixa de 1%.

**Parametrização do Aplicativo Gestão de Folha (RM Labore)**

Acesse: **Opções | Parâmetros | RM Labore ->  Outros Parâmetros - - Eventos Exclusão Base PIS**. Preencher com os eventos necessários a serem Excluídos da Base de Cálculo do PIS.

REGISTRO M350: PIS/PASEP – FOLHA DE SALÁRIOS

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo | "M350" |
| 02 | VL\_TOT\_ | Valor Total da Folha de Salários | Gerado com os dados do Aplicativo Gestão de Folha (RM Labore) Total de todos os proventos da Folha de pagamento – Valor por ser Conferido através do Relatório da Folha Analítica. |
| 03 | VL\_EXC\_BC | Valor Total das Exclusões à Base de Cálculo | Gerado com o Valor dos Eventos parametrizado no Aplicativo Gestão de Folha (RM Labore). |
| 04 | VL\_TOT\_BC | Valor Total da Base de Cálculo | Calculado Internamente (VL\_TOT(02) – VL\_EXC\_BC(03)) |
| 05 | ALIQ\_PIS\_FOL | Alíquota do PIS/PASEP – Folha de Salários | Conforme o Layout do EFD o valor é fixo em "1%" |
| 06 | VL\_TOT\_CONT\_FOL | Valor Total da Contribuição Social sobre a Folha de Salários | Calculado Internamente (VL\_TOT\_BC \* ALIQ\_PIS\_FOL) |

m400Registro M400**Registro M400 — Receitas Isentas, Não alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota zero ou de Vendas com Suspensão PIS/PASEP**m410Registro M410**Registro M410 — Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão — Alíquota zero ou de Vendas com Suspensão — PIS/PASEP**m500Registro M500

**Registro M500 — Crédito de Cofins Relativo Ao Período**

Este registro tem por finalidade realizar a consolidação do crédito relativo à Cofins apurado no período. Deve ser gerado um registro M500 especifico para cada tipo de crédito apurado (vinculados à receita tributada, vinculados à receita não tributada e vinculados à exportação), conforme a Tabela de tipos de créditos “Tabela 4.3.6”, bem como para créditos de operações próprias e créditos transferidos por eventos de sucessão.

Para a geração deste registro serão selecionados os Registros  A100/A170, C100/C170, C500/C505, F100, gerados no Período de Apuração em anexo Detalhamento da Apuração, com CST correspondente a crédito ou Código do Tipo da Operação:

* 0 – Operação Representativa de Aquisição, Custos, Despesa ou Encargos, ou Receitas, Sujeita à Incidência de Crédito de PIS/Pasep ou Cofins (CST 50 a 66).

Para gravar os dados na Detalhamento da Apuração, é necessário encerrar o Período de Apuração;

ObservaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento Apuração10Passo 1Encerrando do Período de ApuraçãoDados gravados no anexo Detalhamento da Apuração

O Cálculo no encerramento do Período de Apuração continua considerando os Parâmetros de Processo.

2Passo 2Gerador de SaídasObservação

O Registro M500 não será gerado quando o Código indicador da incidência tributaria no período for igual a **"2 - Com incidência no regime cumulativo"**.

3Passo 3

Após o detalhamento da apuração ser preenchido, basta executar a rotina EFD-Contribuições para o registro M500 apresentar os dados;

Exemplo do registro M500 geradoLayout do Registro

Registro agrupado pelos campos COD\_CRED e IND\_CRED\_ORI.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG |  | Fixo M500 |
| 02 | COD\_CRED | Código de Tipo de Crédito apurado no período, conforme a Tabela 4.3.6. | Campo deve ser gerado internamente conforme a consistência feita na tabela 4.3.6 |
| 03 | IND\_CRED\_ORI | Indicador de Crédito Oriundo de: 0 – Operações próprias 1 – Evento de incorporação, cisão ou fusão | Fixo 0. A opção 1 - Evento de Incorporação, Cisão ou Fusão Não será gerado neste momento. |
| 04 | VL\_BC\_PIS | Valor da base de cálculo do tributo | Campo gerado com o valor da Base de Cálculo do PIS/COFINS do Período de Apuração\Sub pasta Detalhamento da Apuração |
| 05 | ALIQ\_PIS | Alíquota do COFINS  (em percentual) | Campo gerado com a alíquota constante no Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 06 | QUANT\_BC\_COFINS | Quantidade – Base de cálculo COFINS | Não será gerado neste momento. |
| 07 | ALIQ\_COFINS\_QUA NT | Alíquota do COFINS  (em reais) | Não será gerado neste momento. |
| 08 | VL\_CRED | Valor total do crédito apurado no período | Gerado com o valor do Imposto PIS/COFINS do Período de Apuração\Sub Pasta Detalhamento da Apuração. |
| 09 | VL\_AJUS\_ACRE S | Valor total dos ajustes de acréscimo | Não será gerado neste momento. |
| 10 | VL\_AJUS\_REDU C | Valor total dos ajustes de redução | Não será gerado neste momento. |
| 11 | VL\_CRED\_DIF | Valor total do crédito diferido no período | Não será gerado neste momento. |
| 12 | VL\_CRED\_DISP | Valor Total do Crédito Disponível relativo ao Período (08 + 09 – 10 – 11) =(VL\_CRED + VL\_AJUS\_ACRES - VL\_AJUS\_REDUC - VL\_CRED\_DIF) | Totalizador. Calculado pela rotina |
| 13 | IND\_DESC\_CRE D | Indicador de opção de utilização do crédito disponível no período:                                                             0 – Utilização do valor total para desconto da contribuição apurada no período, no Registro M600;       1 – Utilização de valor parcial para desconto da contribuição apurada no período, no Registro M600. | Gerado fixo “0 – Utilização do valor total para desconto da contribuição apurada no período, no Registro.                                                                                A opção “1” não será implementada neste momento. |
| 14 | VL\_CRED\_DESC | Valor do Crédito disponível, descontado  da contribuição apurada no próprio período.                                                                                                              Se IND\_DESC\_CRED=0, informar o valor total do Campo 12; Se IND\_DESC\_CRED=1, informar o valor parcial do Campo 12. | Valor do Crédito disponível, descontado da contribuição apurada no próprio período. Esta informação será gerada conforme o conteúdo do campo 13.                       Se for 0  (utilização do valor total) será gravado neste campo o valor apurado no campo 12 – Valor do Crédito disponível.                                                                           Para a Opção 1 (utilização parcial) não será gerado neste momento. |
| 15 | SLD\_CRED | Saldo de créditos a utilizar em períodos futuros (12 – 14) | Não será gerado neste momento |

m505Registro M505

**Registro M505 — Detalhamento da Base de Calculo do Crédito Apurado no Período – Cofins**

Neste registro será informada a composição da base de cálculo de cada tipo de crédito (M500), conforme as informações constantes nos documentos e operações com CST geradores de créditos, escriturados nos Blocos “A”, “C”, “D” e “F”. Os valores representativos de Bases de Cálculo escriturados nestes registros serão transferidos para o Registro PAI M500 (Campos 04 e 06), que especifica e escritura os diversos tipos de créditos da escrituração.

Deve ser escriturado um registro M505 para cada CST recuperado dos registros dos Blocos “A”, “C”, “D” e “F”, vinculado ao tipo de crédito informado no Registro M500.

Para a geração deste registro serão selecionados os Registros A100/A170, C100/C170, C500/C505, F100 gerados no Período de Apuração\ Sub Pasta Detalhamento da Apuração.

Para gravar os dados na Detalhamento da Apuração, é necessário encerrar o Período de Apuração;

ObservaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento Apuração10Passo 1Encerrando do Período de ApuraçãoDados gravados no anexo Detalhamento da Apuração

O Cálculo no encerramento do Período de Apuração continua considerando os Parâmetros de Processo.

1Passo 2

Após o detalhamento da apuração ser preenchido, basta executar a rotina EFD-Contribuições para o registro M505 apresentar os dados;

Exemplo do registro M505 geradoLayout do Registro

Registro agrupado pelo NAT\_BC\_CRED e CST.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG | Texto fixo contendo "M505" | Fixo M505 |
| 02 | NAT\_BC\_CRED | Código da Base de Cálculo do Crédito apurado no período, conforme a Tabela 4.3.7. | Gerado conforme do Campo Natureza do Crédito  do Período de Apuração\Sub Pasta Detalhamento da Apuração. NATBCCREDITO.DDETALHAMENTOAPURACAOPISCOFINS |
| 03 | CST\_COFINS | Código da Situação Tributária referente ao crédito de COFINS (Tabela 4.3.3) vinculado ao tipo de crédito escriturado em M105. | Gerado com o CST do Período de Apuração\Sub Pasta Detalhamento da Apuração CST.DDETALHAMENTOAPURACAOPISCOFINS. |
| 04 | VL\_BC\_COFINS\_TOT | Valor Total da Base de Cálculo escriturada nos documentos e operações (Blocos “A”, “C”, “D” e “F”), referente ao CST\_PIS informado no Campo 03. | Gerado com a base de cálculo do Período de Apuração\Sub Pasta Detalhamento da Apuração BASEDECALCULO.DDETALHAMENTOAPURACAOPISCOFINS |
| 05 | VL\_BC\_COFINS\_CUM | Parcela do Valor Total da Base de Cálculo informada no Campo 04, vinculada a receitas com incidência cumulativa.Campo de preenchimento específico para a pessoa jurídica sujeita ao regime cumulativo e não-cumulativo da contribuição (COD\_INC\_TRIB = 3 do Registro 0110) | Neste momento este campo não será gerado. |
| 06 | VL\_BC\_COFINS\_NC | Valor Total da Base de Cálculo do Crédito, vinculada a receitas com incidência não-cumulativa (Campo 04 – Campo 05). | Valor Total da Base de Cálculo do Crédito, vinculada a receitas com incidência não cumulativa (Campo 04 - Campo 05). |
| 07 | VL\_BC\_COFINS | Valor da Base de Cálculo do Crédito, vinculada ao tipo de Crédito escriturado em M105. Para os CST\_PIS = “50”, “51”, “52”, “60”, “61” e “62”: Informar o valor do Campo 06 (VL\_BC\_PIS\_NC); Para os CST\_PIS = “53”, “54”, “55”, “56”, “63”, “64” “65” e “66” (Crédito sobre operações vinculadas a mais de um tipo de receita): Informar a parcela do valor do Campo 06 (VL\_BC\_PIS\_NC) vinculada especificamente ao tipo de crédito escriturado em M100.  O valor deste campo será transportado para o Campo 04 (VL\_BC\_PIS) do registro M100. | Gerado com o Valor do Campo 06 (VL\_BC\_PIS\_NC) vinculada especificamente ao tipo de crédito escriturado em M 500.  O valor deste campo será transportado para o Campo 04 (VL\_BC\_PIS) do registro M500. |
| 08 | QUANT\_BC\_COFINS\_TOT | Quantidade Total da Base de Cálculo do Crédito apurado em Unidade de Medida de Produto, escriturada nos documentos e operações (Blocos “A”, “C”, “D” e “F”), referente ao CST\_PIS informado no Campo 03 | Não será gerado no momento |
| 09 | QUANT\_BC\_PIS | Parcela da base de cálculo do crédito em quantidade (campo 08) vinculada ao tipo de crédito escriturado em M100. Para os CST\_PIS = “50”, “51” e “52”: Informar o valor do Campo 08 (QUANT\_BC\_PIS); Para os CST\_PIS = “53”, “54”, “55” e “56” (crédito vinculado a mais de um tipo de receita): Informar a parcela do valor do Campo 08 (QUANT\_BC\_PIS) vinculada ao tipo de crédito escriturado em M100.  O valor deste campo será transportado para o Campo 06 (QUANT\_BC\_PIS) do registro M100. | Não será gerado no momento |
| 10 | DESC\_CRED | Descrição do crédito | Descrição do Crédito |

Registro M600

**Registro M600 — Consolidação da Contribuição para a Seguridade Social - Cofins do Período**

Neste registro serão consolidadas as contribuições sociais apuradas no período da escrituração, nos regimes não cumulativo e cumulativo, bem como procedido ao desconto dos créditos não cumulativos apurados no próprio período, dos créditos apurados em períodos anteriores, dos valores retidos na fonte e de outras deduções previstas em Lei, demonstrando em seu final os valores devidos a recolher.

A apuração do bloco M600 é realizado pelos valores dos registros dos bloco A, C e F.

Para a geração deste registro, serão utilizadas as informações contidas na aba **Valores Apuração Pis/Cofins** dentro do **Período de Apuração COFINS**.

ObservaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento Apuração01Passo 1Encerrando do Período de ApuraçãoValores Apuração Pis/Cofins2Passo 2

Após os **Valores Apuração Pis/Cofins** serem preenchidas, basta executar a rotina EFD-Contribuições para o registro M600 apresentar os dados.

Exemplo do registro M600 geradoLayout do registro

Gerado um registro por arquivo SPED.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG | Texto Fixo M 600 | Fixo M600 |
| 02 | VL\_TOT\_CONT\_ NC\_PER | Valor Total da Contribuição Não Cumulativa do Período (recuperado do campo 13 do Registro M610, quando o campo “COD\_CONT” = 01, 02, 03, 04, 32 e 71) | Gerado com a soma do Valor do Imposto do Período de Apuração no Detalhamento da Apuração que possuam o tipo de contribuição igual a 01, 02, 03, 04, 32 e 71, considerando as consistências do Item 1. Valor a ser Transportado do Campo 13 do Registro M610 |
| 03 | VL\_TOT\_CRED\_ DESC | Valor do Crédito Descontado, Apurado no Próprio Período da Escrituração (recuperado do campo 14 do Registro M500) | Valor a ser transportado do campo 14 do registro M500 |
| 04 | VL\_TOT\_CRED\_ DESC\_ANT | Valor do Crédito Descontado, Apurado em Período de Apuração Anterior (recuperado do campo 13 do Registro 1500) | Este campo não gerado neste momento. |
| 05 | VL\_TOT\_CONT\_ NC\_DEV | Valor Total da Contribuição Não Cumulativa Devida (02 - 03 - 04) | Campo calculado pela rotina. |
| 06 | VL\_RET\_NC | Valor Retido na Fonte Deduzido no Período | Este campo não será gerado neste momento |
| 07 | VL\_OUT\_DED\_N C | Outras Deduções no Período | Este campo não será gerado neste momento |
| 08 | VL\_CONT\_NC\_R EC | Valor da Contribuição Não Cumulativa a Recolher/Pagar (05 - 06 - 07) | Campo calculado pela rotina. |
| 09 | VL\_TOT\_CONT\_ CUM\_PER | Valor Total da Contribuição Cumulativa do Período (recuperado do campo 13 do Registro M610, quando o campo “COD\_CONT” = 31, 32, 51, 52, 53, 54 e 72) | Gerado com a soma do Valor do Imposto do Período de Apuração\Sub Pasta Detalhamento da Apuração  que possuam o tipo de contribuição igual a 31, 32, 51, 52, 53, 54 e 72,. Valor a ser Transportado do Campo 13 do Registro M610 |
| 10 | VL\_RET\_CUM | Valor Retido na Fonte Deduzido no Período | Este Campo não será gerado neste momento |
| 11 | VL\_OUT\_DED\_C UM | Outras Deduções no Período | Este Campo não será gerado neste momento |
| 12 | VL\_CONT\_CUM\_ REC | Valor da Contribuição Cumulativa a Recolher/Pagar (09 - 10 - 11) | Campo calculado pela rotina. |
| 13 | VL\_TOT\_CONT\_ REC | Valor Total da Contribuição a Recolher/Pagar no Período (08 + 12) | Campo Calculado pela rotina. |

m605Registro M605

**Registro M605 — Cofins a Recolher – Detalhamento por Código de Receita**

Neste registro será informado, por código de receita (conforme códigos de débitos informados em DCTF), o detalhamento da contribuição a recolher informada nos campos 08 (regime não cumulativo) e 12 (regime cumulativo) do Registro Pai M600.

Para a geração deste registro são selecionadas todas as guias DARF incluídas no anexo do Período de Apuração COFINS.

Observação

Este Registro só será gerado a partir da **Versão 12.1.2406**.

Detalhamento Apuração11Passo 1Encerrando do Período de ApuraçãoGeração de Guias AutomaticamenteGuia DARF Gerada

No cadastro da Guia, utilizamos o campo "Código da Obrigação", na aba Outros Dados para identificar o código da contribuição a recolher e fazer o agrupamento da apuração.

Podendo ser:

* "08" para regime não cumulativo
* "12" para regime cumulativo.

É necessário respeitar o tamanho do campo de dois dígitos, para validação no PVA.

2Passo 2

Após encerrar o Período de Apuração e executar a rotina, o arquivo deve ser gerado conforme exemplo abaixo.

Exemplo do arquivo gerado com o registro M605Layout do Registro

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |  |
| 01 | REG | Texto Fixo M 605 | Fixo M605 |  |
| 02 | NUM\_CAMPO | Informar o número do campo do registro “M600” (Campo 08 (contribuição não cumulativa) ou Campo 12 (contribuição cumulativa)), objeto de detalhamento neste registro | Informar o número do campo do registro “M600” (Campo 08 (contribuição não cumulativa) ou Campo 12 (contribuição cumulativa)), objeto de detalhamento neste registro. DGUIAPERIODO.CODIGOOBRIGACAO |  |
| 03 | COD\_REC | Informar o código da receita referente à contribuição a recolher, detalhada neste registro. | Informar o código da receita referente à contribuição a recolher, detalhada neste registro. Gerado conforme o Código da Receita da guia DGUIAPERIODO.CODRECEITA |  |
| 04 | VL\_DEBITO | Valor do débito correspondente ao código do Campo 03, conforme informação na DCTF. | Valor do débito correspondente ao código do Campo 03, conforme informação na DCTF. Gerado com o Valor Paga informado na Guia - Sup Pasta Valores DGUIAPERIODO.VALORPAGO |  |

m610Registro M610**Registro M610 — Detalhamento da Contribuição para a Seguridade Social - Cofins do Período**  

Este registro será gerado através do Anexo Detalhamento da Apuração de Período filtrando os registros com Tipo de Operação "Operações Sujeitas a Contribuições" e "Operações Não Sujeitas a Contribuições"

ObservaçãoEste Registro só será gerado a partir da **Versão 12.1.2406**.Detalhamento Apuração11Passo 1Encerrando do Período de ApuraçãoDados gravados no anexo Detalhamento da Apuração2Passo 2

Após encerrar o Período de Apuração e executar a rotina, o arquivo deve ser gerado conforme exemplo abaixo.

Exemplo do registro M610 geradoLayout do Registro

Registro é agrupado pelos campos COD\_CONT e ALIQ\_COFINS.

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem dos dados |
| 01 | REG | Texto Fixo M 610 | Fixo M610 |
| 02 | COD\_CONT | Código da contribuição social apurada no período, conforme a Tabela 4.3.5 | Gerado conforme Código da contribuição social apurada do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 03 | VL\_REC\_BRT | Valor da Receita Bruta | Gerado conforme o Valor da Operação do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 04 | VL\_BC\_CONT | Valor da Base de Cálculo da Contribuição, antes de ajustes | Gerado com o valor da Base de Cálculo do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 05 | VL\_AJUS\_ACRES\_BC\_COFINS | Valor do total dos ajustes de acréscimo da base de cálculo da contribuição a que se refere o Campo 04 | Este Campo não será gerado neste momento |
| 06 | VL\_AJUS\_REDUC\_BC\_COFINS | Valor do total dos ajustes de redução da base de cálculo da contribuição a que se refere o Campo 04 | Este Campo não será gerado neste momento |
| 07 | VL\_BC\_CONT\_AJUS | Valor da Base de Cálculo da Contribuição, após os ajustes. (Campo 07 = Campo 04 + Campo 05 - Campo 06) | (VL\_BC\_CONT  + VL\_AJUS\_ACRES\_BC\_PIS - VL\_AJUS\_REDUC\_BC\_PIS ) |
| 08 | ALIQ\_COFINS | Alíquota da Cofins (em percentual) | Gerado com o valor da Alíquota do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 09 | QUANT\_BC\_COF INS | Quantidade – Base de cálculo Cofins | Este Campo não será gerado neste momento |
| 10 | ALIQ\_COFINS\_QUANT | Alíquota da Cofins (em reais) | Este Campo não será gerado neste momento |
| 11 | VL\_CONT\_APUR | Valor total da contribuição social apurada | Gerado conforme o Valor do Imposto do Período de Apuração\Sub Pasta Detalhamento da Apuração |
| 12 | VL\_AJUS\_ACRES | Valor total dos ajustes de acréscimo da contribuição social apurada | Este Campo não será gerado neste Momento |
| 13 | VL\_AJUS\_REDUC | Valor total dos ajustes de redução da contribuição social apurada | Este Campo não será gerado neste Momento |
| 14 | VL\_CONT\_DIFER | Valor da contribuição a diferir no período | Este Campo não será gerado neste Momento |
| 15 | VL\_CONT\_DIFER \_ANT | Valor da contribuição diferida em períodos anteriores | Este Campo não será gerado neste Momento |
| 16 | VL\_CONT\_PER | Valor Total da Contribuição do Período (11 + 12 –13 – 14+15) | (VL\_CONT\_APUR  + VL\_AJUS\_ACRES -  VL\_AJUS\_REDUC - VL\_CONT\_DIFER + VL\_CONT\_DIFER\_ANT) |

m630Registro M630**Registro M630 — Informações adicionais de Diferimento**m700Registro M700**Registro M700 — COFINS diferida em períodos anteriores — Valores a pagar no período**m800Registro M800**Registro M800 — Receitas Isentas, Não alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota zero ou de Vendas com Suspensão COFINS**  
Estes registros são gerados com as informações das receitas informadas nos blocos A, C, D e F cujos Tributos PIS e COFINS possuam os CST 04, 05, 06, 07, 08 ou 09.m810Registro M810**Registro M810 — Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão — Alíquota zero ou de Vendas com Suspensão — COFINS**  
Estes registros detalham as receitas isentas declaradas nos registros M400 e M800 agrupando-as por sua natureza.
