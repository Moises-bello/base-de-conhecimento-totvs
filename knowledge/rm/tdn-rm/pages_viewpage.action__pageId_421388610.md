---
content_hash: fcc8f0f4bc3822a0863416bc6836e26b7b2b13310c02d194c11cf33a2883ea2a
fetched_at: '2026-06-29T00:09:17.625812+00:00'
page_id: '421388610'
product: rm
source: tdn-rm
title: Importação de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388610
version: 31
---

**Layout de Importação de Lançamentos**

Para a importação de arquivo texto contendo dados para a inclusão de lançamentos no Totvs Gestão Financeira, é necessário seguir o seguinte layout:  
No arquivo texto deverá existir:

* Uma linha contendo os dados do lançamento;
* Linhas contendo dados do rateio por departamento, caso exista;
* Linhas contendo dados do rateio por centro de custo, caso exista;
* Linhas contendo dados da contabilização do lançamento, caso seja contábil;
* Linhas contendo dados do rateio gerencial da contabilização, caso exista;
* Linhas contendo dados dos campos complementares, caso exista;
* Linhas contendo dados dos tributos, caso tenha.

Estas linhas deverão ser identificadas com os prefixos apropriados, conforme explicado abaixo:

|  |  |
| --- | --- |
| Uma linha com os dados do lançamento...................................... | : Linha tipo "L" |
| Uma linha para cada rateio do lançamento por Departamento.......... | : Linhas tipo "D" |
| Uma linha para cada rateio do lançamento por Centro de Custos..... | : Linhas tipo "U" |
| Uma linha para cada conta contábil a débito ou a crédito................ | : Linhas tipo "C" |
| Uma linha para cada conta contábil que possui rateio gerencial...... | : Linhas tipo "R" |
| Uma linha com os dados dos campos complementares.................. | : Linhas tipo "M" |
| Uma linha para cada Tributo................................................... | : Linhas tipo "B" |

**Observações:**

As linhas tipo D e U podem ser informadas antes das linhas tipo C, ou após as linhas tipo R, ou seja, antes ou após as linhas referentes à contabilização do lançamento.

**Formato de campos:**  
N = Campo numérico, alinhado à direita com zeros à esquerda.  
A = Campo alfanumérico, alinhado à esquerda com espaços à direita.  
D = Campo data, no formato DDMMAA  
Tam. = Tamanho  
Form. = Formato  
Nº Dec. = Número de decimais  
Obs. = Observação

**Importante:**

1- para as posições com dados do tipo "Não utilizado" no formato alfanumérico (A) use espaços em branco.

2- O arquivo deve conter somente caracteres no formato ANSI caso use UTF-8 dará erro em texto com caracteres 'ç', 'ã' e 'õ'.

Linha de dados do Lançamento:

**Posição**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |  |  |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra L |  |  |
| 002 | 004 | 003 | A |  | Código do Banco CNAB |  |  |  |  |
| 005 | 008 | 004 | N |  | Código da Filial | X |  |  |  |
| 009 | 033 | 025 | A |  | Código do Cli/For ou CNPJ/CEI/CPF | X | Nota 16 |  |  |
| 034 | 043 | 010 | A |  | Código do Tipo de Documento | X |  |  |  |
| 044 | 083 | 040 | A |  | Número do Documento | X |  |  |  |
| 084 | 086 | 003 | A |  | Não utilizado |  |  |  |  |
| 087 | 087 | 001 | N |  | Não utilizado |  |  |  |  |
| 088 | 097 | 010 | A |  | Não utilizado |  |  |  |  |
| 098 | 107 | 010 | A |  | Não utilizado |  |  |  |  |
| 108 | 108 | 001 | N |  | A Pagar ou A Receber | X | Nota 2 |  |  |
| 109 | 133 | 025 | A |  | Código da Tabela Opcional 1 | Param. |  |  |  |
| 134 | 158 | 025 | A |  | Código da Tabela Opcional 2 | Param. |  |  |  |
| 159 | 183 | 025 | A |  | Código da Tabela Opcional 3 | Param. |  |  |  |
| 184 | 208 | 025 | A |  | Código da Tabela Opcional 4 | Param. |  |  |  |
| 209 | 233 | 025 | A |  | Código da Tabela Opcional 5 | Param. |  |  |  |
| 234 | 258 | 025 | A |  | Código do Departamento | Param. |  |  |  |
| 259 | 283 | 025 | A |  | Código do Centro de Custo | Param. |  |  |  |
| 284 | 289 | 006 | D |  | Data de Vencimento | X |  |  |  |
| 290 | 295 | 006 | D |  | Data de Emissão | X |  |  |  |
| 296 | 301 | 006 | N |  | Não utilizado |  |  |  |  |
| 302 | 307 | 006 | D |  | Data de Previsão de Baixa |  |  |  |  |
| 308 | 313 | 006 | D |  | Data de Contabilização |  |  |  |  |
| 314 | 319 | 006 | D |  | Data de Cancelamento |  |  |  |  |
| 320 | 325 | 006 | N |  | Não utilizado |  |  |  |  |
| 326 | 331 | 006 | N |  | Não utilizado |  |  |  |  |
| 332 | 337 | 006 | N |  | Não utilizado |  |  |  |  |
| 338 | 437 | 100 | A |  | Não utilizado |  |  |  |  |
| 438 | 438 | 001 | N |  | Tipo Contábil |  | Nota 3 |  |  |
| 439 | 448 | 010 | A |  | Código da Moeda | X |  |  |  |
| 449 | 458 | 010 | A |  | Código do Indexador |  |  |  |  |
| 459 | 468 | 010 | A |  | Código da Conta/Caixa | Param. |  |  |  |
| 469 | 486 | 018 | N | 4 | Valor Original | X |  |  |  |
| 487 | 504 | 018 | N | 4 | Não utilizado |  |  |  |  |
| 505 | 522 | 018 | N | 4 | Valor da Capitalização |  |  |  |  |
| 523 | 540 | 018 | N | 4 | Valor dos Juros |  |  |  |  |
| 541 | 558 | 018 | N | 4 | Valor do Desconto |  |  |  |  |
| 559 | 576 | 018 | N | 4 | Valor Opcional 1 |  |  |  |  |
| 577 | 594 | 018 | N | 4 | Valor Opcional 2 |  |  |  |  |
| 595 | 612 | 018 | N | 4 | Valor Opcional 3 |  |  |  |  |
| 613 | 630 | 018 | N | 4 | Valor Opcional 4 |  |  |  |  |
| 631 | 648 | 018 | N | 4 | Valor Opcional 5 |  |  |  |  |
| 649 | 666 | 018 | N | 4 | Taxa de Juros ao Dia |  |  |  |  |
| 667 | 684 | 018 | N | 4 | Taxa Capitalização Mensal |  |  |  |  |
| 685 | 688 | 004 | A |  | Não utilizado |  |  |  |  |
| 689 | 708 | 020 | A |  | Número Contábil |  |  |  |  |
| 709 | 728 | 020 | A |  | Segundo Número |  |  |  |  |
| 729 | 729 | 001 | N |  | Status do Lançamento | X | Nota 4 |  |  |
| 730 | 730 | 001 | N |  | Não utilizado |  |  |  |  |
| 731 | 731 | 001 | N |  | Não utilizado |  |  |  |  |
| 732 | 737 | 006 | A |  | Não utilizado |  |  |  |  |
| 738 | 747 | 010 | A |  | Não utilizado |  |  |  |  |
| 748 | 767 | 020 | A |  | Não utilizado |  |  |  |  |
| 768 | 773 | 006 | N |  | Não utilizado |  |  |  |  |
| 774 | 791 | 018 | N |  | Não utilizado |  |  |  |  |
| 792 | 792 | 001 | A |  | Não utilizado |  |  |  |  |
| 793 | 798 | 006 | D |  | Data Opcional 1 |  |  |  |  |
| 799 | 804 | 006 | D |  | Data Opcional 2 |  |  |  |  |
| 805 | 810 | 006 | D |  | Data Opcional 3 |  |  |  |  |
| 811 | 820 | 010 | A |  | Não utilizado |  |  |  |  |
| 821 | 821 | 001 | N |  | Não utilizado |  |  |  |  |
| 822 | 822 | 001 | N |  | Não utilizado |  |  |  |  |
| 823 | 825 | 003 | N |  | Carteira CNAB |  |  |  |  |
| 826 | 827 | 002 | N |  | Comando CNAB |  |  |  |  |
| 828 | 828 | 001 | N |  | Aceite CNAB |  |  |  |  |
| 829 | 830 | 002 | N |  | Instrução Codif. 1 |  |  |  |  |
| 831 | 832 | 002 | N |  | Instrução Codif. 2 |  |  |  |  |
| 833 | 852 | 020 | A |  | Nosso Número CNAB |  |  |  |  |
| 853 | 853 | 001 | N |  | Não utilizado |  |  |  |  |
| 854 | 863 | 010 | A |  | Não utilizado |  |  |  |  |
| 864 | 864 | 001 | N |  | Reembolsável |  | Nota 5 |  |  |
| 865 | 868 | 004 | N |  | Código Coligada Cli/For | X | Nota 18 |  |  |
| 869 | 884 | 016 | A |  | Código do Vendedor |  |  |  |  |
| 885 | 888 | 004 | N |  | Código Coligada da Conta/Caixa |  |  |  |  |
| 889 | 892 | 004 | N |  | Não utilizado |  |  |  |  |
| 893 | 893 | 001 | A |  | Tipo do Sacado |  | \*Nota 11 |  |  |
| 894 | 899 | 006 | A |  | Período Letivo |  | \* |  |  |
| 900 | 901 | 002 | N |  | Parcela |  | \* |  |  |
| 902 | 903 | 002 | N |  | Cota |  | \* |  |  |
| 904 | 905 | 002 | N |  | Não utilizado |  |  |  |  |
| 906 | 935 | 030 | A |  | Não utilizado |  |  |  |  |
| 936 | 936 | 001 | A |  | Local de Pagamento |  | \* |  |  |
| 937 | 941 | 005 | A |  | Não utilizado |  |  |  |  |
| 942 | 959 | 018 | N | 4 | Valor da Multa |  |  |  |  |
| 960 | 967 | 008 | N |  | Número do Recibo |  | \* |  |  |
| 968 | 985 | 018 | N | 4 | Valor Depositado |  | \* |  |  |
| 986 | 986 | 001 | A |  | Serviços Extras |  | \*Nota 12 |  |  |
| 987 | 992 | 006 | D |  | Data de pagamento |  | \* |  |  |
| 993 | 998 | 006 | N |  | Não utilizado |  |  |  |  |
| 999 | 1004 | 006 | N |  | Não utilizado |  |  |  |  |
| 1005 | 1019 | 015 | A |  | Não utilizado |  |  |  |  |
| 1020 | 1063 | 044 | A |  | Código de Barras |  |  |  |  |
| 1064 | 1111 | 047 | A |  | I.P.T.E. |  |  |  |  |
| 1112 | 1120 | 010 | A |  | Não utilizado |  |  |  |  |
| 1121 | 1138 | 018 | N | 4 | Não utilizado |  |  |  |  |
| 1139 | 1139 | 001 | N |  | Não utilizado |  |  |  |  |
| 1140 | 1140 | 001 | N |  | Não utilizado |  |  |  |  |
| 1141 | 1240 | 100 | A |  | Campo Alfa Op. 1 |  |  |  |  |
| 1241 | 1260 | 020 | A |  | Campo Alfa Op. 2 |  |  |  |  |
| 1261 | 1280 | 020 | A |  | Campo Alfa Op. 3 |  |  |  |  |
| 1281 | 1281 | 001 | A |  | Não utilizado |  |  |  |  |
| 1282 | 1299 | 018 | N | 4 | Não utilizado |  |  |  |  |
| 1300 | 1309 | 010 | A |  | Não utilizado |  |  |  |  |
| 1310 | 1327 | 018 | N | 4 | Não utilizado |  |  |  |  |
| 1328 | 1337 | 010 | A |  | Não utilizado |  |  |  |  |
| 1338 | 1355 | 018 | N | 4 | Valor Opcional 6 |  |  |  |  |
| 1356 | 1373 | 018 | N | 4 | Valor Opcional 7 |  |  |  |  |
| 1374 | 1391 | 018 | N | 4 | Valor Opcional 8 |  |  |  |  |
| 1392 | 1392 | 001 | N |  | Não utilizado |  |  |  |  |
| 1393 | 1407 | 015 | A |  | Não utilizado |  |  |  |  |
| 1408 | 1422 | 015 | A |  | Não utilizado |  |  |  |  |
| 1423 | 1428 | 006 | D |  | Data Opcional 4 |  |  |  |  |
| 1429 | 1434 | 006 | D |  | Data Opcional 5 |  |  |  |  |
| 1435 | 1449 | 015 | A |  | Código do Representante |  |  |  |  |
| 1450 | 1451 | 002 | A |  | Não utilizado |  |  |  |  |
| 1452 | 1471 | 020 | A |  | Não utilizado |  |  |  |  |
| 1472 | 1476 | 005 | A |  | Cód. Evento Contábil |  | Nota 13 |  |  |
| 1477 | 1481 | 005 | N |  | Não utilizado |  | Nota 13 |  |  |
| 1482 | 1483 | 002 | N |  | Não utilizado |  | Nota 7 |  |  |
| 1484 | 1497 | 014 | N |  | Não utilizado |  |  |  |  |
| 1498 | 1511 | 014 | N |  | Não utilizado |  |  |  |  |
| 1512 | 1512 | 001 | N |  | Tipo de Juros ao Dia |  | Nota 14 |  |  |
| 1513 | 1530 | 018 | N | 4 | Taxa de Juros do Vendor |  |  |  |  |
| 1531 | 1548 | 018 | N | 4 | Valor de Juros do Vendor |  |  |  |  |
| 1549 | 1566 | 018 | N | 4 | Não utilizado |  |  |  |  |
| 1567 | 1572 | 006 | D |  | Mês/Ano de Competência |  | Nota 15 |  |  |
| 1573 | 1577 | 005 | N |  | Pagamento Eletrônico |  |  |  |  |
| 1578 | 1581 | 004 | N |  | Reutilização |  |  |  |  |
| 1582 | 1589 | 008 | A |  | Série Documento |  |  |  |  |
| 1590 | 1844 | 255 | A |  | Histórico do Lançamento |  |  |  |  |
| 1845 | 1849 | 005 | N |  | Ocorrências do Autônomo |  | Nota 17 |  |  |
| 1850 | 1867 | 018 | N | 4 | INSS Outras Empresas |  | Nota 17 |  |  |
| 1868 | 1877 | 010 | A |  | Código da Receita |  |  |  |  |
| 1878 | 1895 | 018 | N | 4 | Base INSS Empregado |  |  |  |  |
| 1896 | 1913 | 018 | N | 4 | Base INSS Empregador |  |  |  |  |
| 1914 | 1914 | 001 | N | 4 | Indicador  da natureza da  receita |  | Nota 19 |  |  |
| 1915 | 1918 | 004 | N |  | Coligada dos Dados Bancários do CliFor |  |  |  |  |
| 1919 | 1919 | 001 | N |  | Classificação do Lançamento na LCDPR |  | Nota 20 |  |  |
| 1920 | 1920 | 001 | N |  | Tipo de Lançamento na LCDPR |  | Nota 21 |  |  |
| 1921 | 1940 | 020 | N |  | CPF/CNPJ do contribuinte sujeito passivo do tributo |  |  |  |  |
| 1941 | 1941 | 001 | N |  | Modalidade do Lançamento |  |  |  |  |
| 1942 | 1942 | 001 | N |  | Status da Aprovação Lançamento a Pagar |  | Nota 22 |  |  |
| 1943 | 1948 | 006 | D |  | Data da Aprovação Lançamento a Pagar |  | Nota 22 |  |  |
| 1949 | 1963 | 015 | A |  | Código Natureza Rendimento do IRRF |  |  |  |  |

**Observações:**Se o usuário tem permissão para incluir lançamentos para um Cli/For bloqueado, na inclusão, será perguntado se é para bloquear o lançamento e na importação será importado, mas sem perguntar.  
Se o usuário não tem permissão para incluir lançamentos para um Cli/For bloqueado, tanto a inclusão quanto a importação serão bloqueadas.

Linha de dados dos Rateios por Departamento:

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra D |
| 002 | 005 | 004 | N |  | Código da Coligada | X |  |
| 006 | 009 | 004 | N |  | Código da Filial | X |  |
| 010 | 034 | 025 | A |  | Código do Departamento | X |  |
| 035 | 052 | 018 | N | 2 | Valor | X |  |

Linha de dados dos Rateios por Centro de Custos:

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra U |
| 002 | 005 | 004 | N |  | Código da Coligada | X |  |
| 006 | 030 | 025 | A |  | Código do Centro de Custos | X |  |
| 031 | 048 | 018 | N | 2 | Valor | X |  |
| 049 | 303 | 255 | A |  | Histórico |  |  |
| 304 | 305 | 002 | N |  | Coligada Natureza Financeira |  | Nota 23 |
| 306 | 345 | 040 | A |  | Natureza Financeira |  |  |
| 346 | 349 | 004 | N |  | Coligada Natureza Financeira - 4 dígitos |  |  |

Linha de dados das Contabilizações:

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra C |
| 002 | 002 | 001 | N |  | Débito/Crédito | X | Nota 9 |
| 003 | 003 | 001 | N |  | Não utilizado |  |  |
| 004 | 007 | 004 | N |  | Cód. Coligada da Conta | X |  |
| 008 | 047 | 040 | A |  | Código da Conta | X |  |
| 048 | 065 | 018 | N | 2 | Valor | X |  |
| 066 | 069 | 004 | N |  | Código da Filial | X |  |
| 070 | 094 | 025 | A |  | Código do Departamento |  |  |
| 095 | 119 | 025 | A |  | Código Centro de Custos |  |  |
| 120 | 129 | 010 | A |  | Código Histórico Padrão |  |  |
| 130 | 379 | 250 | A |  | Complemento do Histórico |  |  |

Linha de dados dos Rateios Gerenciais:

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra R |
| 002 | 005 | 004 | N |  | Cód. Coligada da Conta Gerencial | X |  |
| 006 | 045 | 040 | A |  | Cód. da Conta Gerencial | X |  |
| 046 | 063 | 018 | N | 2 | Valor | X |  |

Linha de dados dos Campos Complementares:

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra M |

**Observações:**  
Informe os campos complementares em sequencia, a partir da posição "002".

Exemplo:  
Você possui os campos complementares:

* Data de Conferência – tamanho 6;
* Responsável – tamanho 10.

O preenchimento do layout deve ser:

Posição: 002 a 007  
Tamanho: 006  
Formato: N  
Nº Decimal:  
Descrição: Data de Conferencia  
   
Posição: 008 a 017  
Tamanho: 010  
Formato: A  
Nº Decimal:  
Descrição: Responsável

Para facilitar o TOTVS Gestão Financeira gera um layout dos registros de campos complementares cadastrados na base. Para gerar este layout você deve clicar sobre o botão "Gerar" localizado na tela do processo de "Importar Lançamentos".

Linha de dados dos tributos:

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra B |
| 002 | 011 | 010 | A |  | Código do Tributo | X |  |
| 012 | 029 | 018 | N | 2 | Base de Cálculos | X |  |
| 030 | 044 | 015 | A |  | Código Natureza Rendimento |  |  |

Notas explicativas

**Notas explicativas**

Nota 1: 0 = Não faturado 1 = Nota Fiscal 2 = Duplicata

Nota 2: 1 = A Receber 2 = A Pagar

Nota 3: 0 = Não contábil 1 = Contábil 2 = Baixa Contábil 3 = A Contabilizar

Nota 4: 0 = Em aberto 2 = Cancelado

Obs: Como o processo de cancelamento envolve a atualização de muitas informações no sistema, não importamos lançamentos já cancelados, sendo necessário realizar a importação (inclusão) e depois uma nova importação (cancelamento)

Nota 5: 0 = Não 1 = Sim

Nota 6: 0 = Não exportado 1 = Inclusão exportada 2 = Baixa exportada 3 = Estorno exportado 4 = Estorno da baixa exportado 5 = Cancelado

Nota 7: 00 = Sem Cheque 07 = Lançamento com Cheque Emitido 12 = Lançamento com Cheque a Receber

Nota 8: 0 = Não remetido 1 = Remetido 2 = Registrado 3 = Recusado 4 = Baixado

Nota 9**:** 1 = Débito 2 = Crédito

Nota 11: A = Aluno R = Responsável

Nota 12: S = Sim N= Não

Nota 13: Para visualizar o código do evento, acesse o Menu: Cadastro | Contabilidade | Eventos Contábeis, clique no ícone "configurar campos" e selecione o código.

Nota 14: 0 = Taxa (%) 1 = Valor

Nota 15: A data deverá ser sempre referente ao primeiro dia do Mês de Competência, por ex.: 01/05/01 para o mês de Maio/2001.

Nota 16: Caso seja escolhida a importação utilizando CNPJ/CEI/CPF, na posição onde deveria estar o Código do Cli/For, deve estar o CNPJ/CEI/CPF com a máscara.

Nota 17: O Número de Bloqueios só será importado se o parâmetro "Bloqueio de Lançamento para Baixa" (Menu Ambiente | Parâmetros | TOTVS Gestão Financeira | pasta Baixa), estiver habilitado para "Bloqueio Simples" ou para "Bloqueio Duplo", e os parâmetros "Incluir Lançamento A Pagar já Bloqueado" e "Incluir Lançamento A Receber já Bloqueado", estiverem Inativos.  
 O número de bloqueios do lançamento não pode ser maior que o número de bloqueios informado nos parâmetros. Se o parâmetro estiver "Sem Bloqueio", não é importado nenhum bloqueio, se o parâmetro estiver "Bloqueio Simples", só é importado 1 (um) bloqueio, se o parâmetro estiver "Bloqueio Duplo", é importado até 2 (dois) bloqueios.

Nota 18: O campo deve ser preenchido da seguinte maneira:

* Para Cliente/Fornecedor Global deve ser informado: 0000
* Para Cliente/Fornecedor Não Global deve ser informado 0 (zeros) a esquerda mais o Código da Coligada, respeitando o tamanho do campo que é de 4 (quatro) posições.

Nota 19: Descrição: Indicador da Natureza da Receita.

Obrigatório: Não Obrigatório.  
 Obs: Valores que podem ser preenchidos.  
 Nota XXX:  
 0 = Natureza Não Cumulativa  
 1 = Natureza Cumulativa

Nota 20: Classificação do Lançamento no Livro Caixa digital do Produtor Rural

1 - Nota Fiscal­  
2 - Fatura  
3 - Recibo  
4 - Contrato  
5 - Folha de Pagamentos  
6 - Outros

Nota 21: Tipo de Lançamento no Livro Caixa Digital do Produtor Rural

Obs: Valores que podem ser preenchidos.  
1 - Receita da atividade rural  
2 - Despesas de custeio e investimentos  
3 - Receita de produtos entregues no ano referente a adiantamento de recursos financeiros

Nota 22: Status da Aprovação

0- Não se aplica  
1- Pendente  
2- Aprovado  
3- Reprovado

Nota 23: Coligada Natureza Financeira  
Obs: caso o tamanho da coligada seja maior que 2, utilize as posições 346-349 e deixe as posições 304-305 em branco.

Exemplo de importação, arquivo.XML

<?xml version="1.0" standalone="yes"?>  
<FinLAN>  
  <FLAN>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <IDLAN>-1</IDLAN>  
    <NUMERODOCUMENTO>1234567890</NUMERODOCUMENTO>  
    <NFOUDUP>0</NFOUDUP>  
    <CLASSIFICACAO>5</CLASSIFICACAO>  
    <PAGREC>2</PAGREC>  
    <STATUSLAN>0</STATUSLAN>  
    <CODAPLICACAO>F</CODAPLICACAO>      
    <CODCCUSTO>01</CODCCUSTO>  
    <DATACRIACAO>2018-06-04T00:00:00-03:00</DATACRIACAO>  
    <DATAVENCIMENTO>2018-08-09T00:00:00-03:00</DATAVENCIMENTO>  
    <DATAEMISSAO>2018-06-04T00:00:00-03:00</DATAEMISSAO>  
    <DATAPREVBAIXA>2018-08-09T00:00:00-03:00</DATAPREVBAIXA>  
    <DATAOP1>2018-08-09T00:00:00-03:00</DATAOP1>  
    <DATAOP2>2018-06-04T00:00:00-03:00</DATAOP2>  
    <DATAOP3>2018-06-04T00:00:00-03:00</DATAOP3>  
    <DATAOP4>2018-06-04T00:00:00-03:00</DATAOP4>  
    <VALORORIGINAL>435.3100</VALORORIGINAL>  
    <VALORBAIXADO>0.0000</VALORBAIXADO>  
    <VALORCAP>0.0000</VALORCAP>  
    <VALORJUROS>0.0000</VALORJUROS>  
    <VALORDESCONTO>0.0000</VALORDESCONTO>  
    <VALORCHEQUE>0.0000</VALORCHEQUE>  
    <VALOROP1>0.0000</VALOROP1>  
    <VALOROP2>0.0000</VALOROP2>  
    <VALOROP3>0.0000</VALOROP3>  
    <VALOROP4>0.0000</VALOROP4>  
    <VALOROP5>0.0000</VALOROP5>  
    <VALOROP6>0.0000</VALOROP6>  
    <VALOROP7>0.0000</VALOROP7>  
    <VALOROP8>0.0000</VALOROP8>  
    <VALORMULTA>13.0600</VALORMULTA>  
    <VALORAUXILIAR>3.0000</VALORAUXILIAR>  
    <VALORBASEIRRF>100.0000</VALORBASEIRRF>  
    <VALORIRRF>0.0000</VALORIRRF>  
    <VALORREPASSE>0.0000</VALORREPASSE>  
    <VALORVENCIMENTOANTECIP>0.0000</VALORVENCIMENTOANTECIP>  
    <VALORNOTACREDITO>0.0000</VALORNOTACREDITO>  
    <VALORADIANTAMENTO>0.0000</VALORADIANTAMENTO>  
    <VALORDEVOLUCAO>0.0000</VALORDEVOLUCAO>  
    <JUROSDIA>0.0000</JUROSDIA>  
    <CAPMENSAL>0.0000</CAPMENSAL>  
    <TAXASVENDOR>0.0000</TAXASVENDOR>  
    <JUROSVENDOR>0.0000</JUROSVENDOR>  
    <CODCOLCFO>0</CODCOLCFO>  
    <CODCFO>C00013</CODCFO>  
    <CODCOLCXA>1</CODCOLCXA>  
    <CODCXA>0001</CODCXA>  
    <CODTDO>28</CODTDO>  
    <CODFILIAL>1</CODFILIAL>  
    <CODDEPARTAMENTO>02</CODDEPARTAMENTO>  
    <SERIEDOCUMENTO>U</SERIEDOCUMENTO>  
    <CODTB1FLX>0001</CODTB1FLX>  
    <CODTB2FLX>0004</CODTB2FLX>  
    <CODTB3FLX>0005</CODTB3FLX>  
    <CODTB5FLX>000000</CODTB5FLX>  
    <TIPOCONTABILLAN>0</TIPOCONTABILLAN>  
    <CODMOEVALORORIGINAL>R$</CODMOEVALORORIGINAL>  
    <LIBAUTORIZADA>0</LIBAUTORIZADA>  
    <STATUSEXPORTACAO>0</STATUSEXPORTACAO>  
    <NUMLOTECONTABIL>0</NUMLOTECONTABIL>  
    <STATUSEXTRATO>0</STATUSEXTRATO>  
    <CNABCARTEIRA>21</CNABCARTEIRA>  
    <CNABACEITE>0</CNABACEITE>  
    <CNABSTATUS>0</CNABSTATUS>  
    <CNABBANCO>275</CNABBANCO>  
    <REEMBOLSAVEL>0</REEMBOLSAVEL>  
    <USUARIO>mestre</USUARIO>  
    <BAIXAAUTORIZADA>1</BAIXAAUTORIZADA>  
    <TEMCHEQUEPARCIAL>0</TEMCHEQUEPARCIAL>  
    <JAIMPRIMIU>0</JAIMPRIMIU>  
    <NUMBLOQUEIOS>0</NUMBLOQUEIOS>  
    <COTACAOINCLUSAO>1.000000000</COTACAOINCLUSAO>  
    <COTACAOBAIXA>0.000000000</COTACAOBAIXA>  
    <CARENCIAJUROS>0</CARENCIAJUROS>  
    <TIPOJUROSDIA>0</TIPOJUROSDIA>  
    <USUARIOCRIACAO>mestre</USUARIOCRIACAO>  
    <DATAALTERACAO>2018-07-14T00:00:00-03:00</DATAALTERACAO>  
    <ALTERACAOBLOQUEADA>0</ALTERACAOBLOQUEADA>  
    <MULTADIA>0.0000</MULTADIA>  
    <IDFORMAPAGTO>1</IDFORMAPAGTO>  
    <DESCONTADO>0</DESCONTADO>  
    <VALORINSS>0.0000</VALORINSS>  
    <VALORDEDUCAO>0.0000</VALORDEDUCAO>  
    <APLICFORMULA>F</APLICFORMULA>  
    <FORMULAJUROS>JUROSDIA</FORMULAJUROS>  
    <INSSEMOUTRAEMPRESA>0.0000</INSSEMOUTRAEMPRESA>  
    <PERCENTBASEINSS>0.0000</PERCENTBASEINSS>  
    <CODRECEITA>0561</CODRECEITA>  
    <PERCBASEINSSEMPREGADO>0.0000</PERCBASEINSSEMPREGADO>  
    <INSSEDITADO>0</INSSEDITADO>  
    <IRRFEDITADO>0</IRRFEDITADO>  
    <REUTILIZACAO>0</REUTILIZACAO>  
    <CATEGORIAAUTONOMO>0</CATEGORIAAUTONOMO>  
    <VALORSESTSENAT>0.0000</VALORSESTSENAT>  
    <CONVENIO>2121</CONVENIO>  
    <DIGCONVENIO>23</DIGCONVENIO>  
    <PERCJUROS>0</PERCJUROS>  
    <PERCDESCONTO>0</PERCDESCONTO>  
    <PERCMULTA>3.00</PERCMULTA>  
    <PERCCAP>0</PERCCAP>  
    <PERCOP1>0</PERCOP1>  
    <PERCOP2>0</PERCOP2>  
    <PERCOP3>0</PERCOP3>  
    <PERCOP4>0</PERCOP4>  
    <PERCOP5>0</PERCOP5>  
    <PERCOP6>0</PERCOP6>  
    <PERCOP7>0</PERCOP7>  
    <PERCOP8>0</PERCOP8>  
    <VALORINSSEMPREGADOR>0</VALORINSSEMPREGADOR>  
    <VALORBASEINSSEMPREGADOR>0</VALORBASEINSSEMPREGADOR>  
    <VRBASEINSS>0</VRBASEINSS>  
    <VRBASEIRRF>0</VRBASEIRRF>  
    <VALORSERVICO>0.0000</VALORSERVICO>  
    <VRBASEINSSOUTRAEMPRESA>0.0000</VRBASEINSSOUTRAEMPRESA>  
    <IDHISTORICO>3720</IDHISTORICO>  
    <VALORDEDUCAODEPENDENTES>0.0000</VALORDEDUCAODEPENDENTES>  
    <VRPERDAFINANCEIRA>0.0000</VRPERDAFINANCEIRA>  
    <MODELOCONTABILIZACAO>0</MODELOCONTABILIZACAO>  
    <MODELOCONTABILIZACAOBAIXA>0</MODELOCONTABILIZACAOBAIXA>  
    <IDCONVENIO>17</IDCONVENIO>  
    <VALORORIGINALBX>0</VALORORIGINALBX>  
    <VALORDESCONTOBX>0</VALORDESCONTOBX>  
    <VALORJUROSBX>0</VALORJUROSBX>  
    <VALORMULTABX>0</VALORMULTABX>  
    <VALORCAPBX>0</VALORCAPBX>  
    <VALOROP1BX>0,0000</VALOROP1BX>  
    <VALOROP2BX>0,0000</VALOROP2BX>  
    <VALOROP3BX>0,0000</VALOROP3BX>  
    <VALOROP4BX>0,0000</VALOROP4BX>  
    <VALOROP5BX>0,0000</VALOROP5BX>  
    <VALOROP6BX>0,0000</VALOROP6BX>  
    <VALOROP7BX>0,0000</VALOROP7BX>  
    <VALOROP8BX>0,0000</VALOROP8BX>  
    <VALORINSSBX>0</VALORINSSBX>  
    <VALORIRRFBX>0</VALORIRRFBX>  
    <VALORSESTSENATBX>0</VALORSESTSENATBX>  
    <VALORDEVOLUCAOBX>0</VALORDEVOLUCAOBX>  
    <VALORNOTACREDITOBX>0</VALORNOTACREDITOBX>  
    <VALORADIANTAMENTOBX>0</VALORADIANTAMENTOBX>  
    <VALORJUROSVENDORBX>0</VALORJUROSVENDORBX>  
    <VALORRETENCOESBX>0</VALORRETENCOESBX>  
    <STATUSORCAMENTO>0</STATUSORCAMENTO>  
    <BAIXAPENDENTE>0</BAIXAPENDENTE>  
    <CODCOLTOMADOR>0</CODCOLTOMADOR>  
    <VALORDESCONTOACORDO>0.0000</VALORDESCONTOACORDO>  
    <VALORJUROSACORDO>0.0000</VALORJUROSACORDO>  
    <VALORACRESCIMOACORDO>0.0000</VALORACRESCIMOACORDO>  
    <VALORDEDUCAOVARIAVEL>0.0000</VALORDEDUCAOVARIAVEL>  
    <STATUSLIQDUVIDOSA>0</STATUSLIQDUVIDOSA>  
    <IDNATRENDIMENTOIRRF>1</IDNATRENDIMENTOIRRF>  
  </FLAN>  
  <FLANCOMPL>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <IDLAN>-1</IDLAN>  
    <GRPRECEITA>9999</GRPRECEITA>  
    <PERCENTUAL>100.0000</PERCENTUAL>  
    <TIPOREMESSA>01</TIPOREMESSA>  
  </FLANCOMPL>  
  <FLANRATCCU>  
    <IDRATCCU>-1</IDRATCCU>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <IDLAN>-1</IDLAN>  
    <CODCCUSTO>01.1</CODCCUSTO>  
    <NOME>Departamento Pessoal</NOME>  
    <VALOR>217.6600</VALOR>  
    <PERCENTUAL>50.0000</PERCENTUAL>  
    <CODCOLNATFINANCEIRA>1</CODCOLNATFINANCEIRA>  
    <CODNATFINANCEIRA>006</CODNATFINANCEIRA>  
    <DESCRICAO>Pagamento Diversos</DESCRICAO>  
    <RECCREATEDBY>mestre</RECCREATEDBY>  
    <RECCREATEDON>2018-07-14T12:25:15-03:00</RECCREATEDON>  
    <RECMODIFIEDBY>mestre</RECMODIFIEDBY>  
    <RECMODIFIEDON>2018-07-14T12:25:15-03:00</RECMODIFIEDON>  
  </FLANRATCCU>  
  <FLANRATCCU>  
    <IDRATCCU>-2</IDRATCCU>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <IDLAN>-1</IDLAN>  
    <CODCCUSTO>01.2</CODCCUSTO>  
    <NOME>Controladoria</NOME>  
    <VALOR>217.6500</VALOR>  
    <PERCENTUAL>50.0000</PERCENTUAL>  
    <CODCOLNATFINANCEIRA>1</CODCOLNATFINANCEIRA>  
    <CODNATFINANCEIRA>006</CODNATFINANCEIRA>  
    <DESCRICAO>Pagamento Diversos</DESCRICAO>  
    <RECCREATEDBY>mestre</RECCREATEDBY>  
    <RECCREATEDON>2018-07-14T12:25:15-03:00</RECCREATEDON>  
    <RECMODIFIEDBY>mestre</RECMODIFIEDBY>  
    <RECMODIFIEDON>2018-07-14T12:25:15-03:00</RECMODIFIEDON>  
  </FLANRATCCU>  
  <FLANRATDEP>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <IDLAN>-1</IDLAN>  
    <CODFILIAL>1</CODFILIAL>  
    <CODDEPARTAMENTO>03</CODDEPARTAMENTO>  
    <NOME>DAP - Depto Administrativo</NOME>  
    <VALOR>217.6550</VALOR>  
    <PERCENTUAL>50.00</PERCENTUAL>  
    <IDRATDEP>-1</IDRATDEP>  
  </FLANRATDEP>  
  <FLANRATDEP>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <IDLAN>-1</IDLAN>  
    <CODFILIAL>1</CODFILIAL>  
    <CODDEPARTAMENTO>04</CODDEPARTAMENTO>  
    <NOME>PDE - Depto Pesquisa e Desenvolvimento</NOME>  
    <VALOR>217.6550</VALOR>  
    <PERCENTUAL>50.00</PERCENTUAL>  
    <IDRATDEP>-2</IDRATDEP>  
  </FLANRATDEP>  
  <FTRBLAN>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <IDTRBLAN>-1</IDTRBLAN>  
    <IDLAN>-1</IDLAN>  
    <CODTRB>CSRF</CODTRB>  
    <CODRETENCAO>5952</CODRETENCAO>  
    <BASEDECALCULO>435.3100</BASEDECALCULO>  
    <ALIQUOTA>4.6500</ALIQUOTA>  
    <VALOR>20.2400</VALOR>  
    <EDITADO>0</EDITADO>  
    <IDNATRENDIMENTO>1</IDNATRENDIMENTO>  
  </FTRBLAN>   
</FinLAN>

Observações:

* Caso o campo não tenha valor não gerar a tag (não usar NULL).
* Para arquivo XML contendo mais de um registro de lançamento de mesma coligada, deve seguir as regras de banco no que diz respeito a chaves primárias, chaves estrangeiras e índices. Assim, o segundo registro, de uma mesma coligada, deve ter <IDLAN>-2</IDLAN>, o  terceiro <IDLAN>-3</IDLAN>, e assim por diante. Esse valor do campo IDLAN deve ser levado para os registros filhos (rateio, campo complementar, tributos). A mesma regra vale para os campos que são únicos por coligada (IDRATCCU, IDRATDEP e IDTRBLAN), devem ter valor diferente para uma mesma coligada.
