---
content_hash: a13562b4e2f2f526def1849880ff81cf20b18427c4fefeea62b512d9a625b766
fetched_at: '2026-06-29T00:09:17.671473+00:00'
page_id: '421388613'
product: rm
source: tdn-rm
title: Importação de Layout de Extratos de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388613
version: 8
---

Para a importação de arquivo texto contendo dados para a inclusão de Extratos de Caixa no aplicativo TOTVS Gestão Financeira, é necessário seguir algumas normas de preenchimento para que todos os dados sejam incluídos corretamente.  
O arquivo deve ser dividido em linhas e cada linha possuir um conjunto de informações. Os conjuntos de informações serão divididos em:

* A primeira linha deve possuir informações sobre a Identificação, Tabelas Opcionais e Dados Adicionais;
* A segunda linha deve possuir informações sobre os Campos Complementares do Extrato de Caixa;
* A partir da terceira linha devem ser informados os Dados da Contabilização, da seguinte forma:

Uma linha contendo informações sobre a Conta Contábil seguida por uma linha contendo informações sobre o seu Rateio Gerencial.  
Estas linhas deverão ser identificadas com os prefixos apropriados, conforme explicado abaixo:

|  |  |
| --- | --- |
| Linha com os Dados do Extrato de Caixa.................................. | : Linha tipo "E" |
| Linha com os Campos Complementares do Extrato de Caixa........ | : Linha tipo "M" |
| Linha com as Contas Contábeis................................................. | : Linha tipo "C" |
| Linha com os Rateios Gerenciais............................................... | : Linha tipo "R" |

**Observações**

Quando o arquivo possuir mais de um Extrato de Caixa, esse conjunto de linhas deverá ser individualmente para cada um, ou seja, devem constar todas as linhas para um extrato de caixa e logo após a última linha começam as linhas para o próximo extrato de caixa.

**Formato dos campos no layout:**

F = Fixo, identificador da linha.  
N = Campo numérico, alinhado à direita com zeros à esquerda.  
A = Campo alfanumérico, alinhado à esquerda com espaços à direita.  
D = Campo data, no formato DDMMAA

**Descrição de títulos do layout**

Tam. = Tamanho do Campo  
Form. = Formato do Campo  
Nº Dec. = Número de decimais  
Obs. = Observação  
Linha de Dados dos Extratos de Caixa

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| De | Até | Tam. | Form. | Nº Dec. | Descrição | Obrigatório | Obs. |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra E |
| 002 | 011 | 010 | A |  | Código da Conta/Caixa | X |  |
| 012 | 017 | 006 | D |  | Data de Emissão | X |  |
| 018 | 035 | 018 | N | 04 | Valor | X |  |
| 036 | 135 | 100 | A |  | Histórico |  |  |
| 136 | 137 | 002 | N |  | Tipo de Extrato | X | Nota 1 |
| 138 | 157 | 020 | A |  | Número do Documento | X |  |
| 158 | 158 | 001 | N |  | Compensado ou Não | X | Nota 8 |
| 159 | 164 | 006 | D |  | Data de Compensação | X | Nota 2 |
| 165 | 165 | 001 | N |  | Contábil ou Não | X | Nota 3 |
| 166 | 166 | 001 | N |  | Status Exportação para o RM Saldus | X | Nota 11 |
| 167 | 191 | 025 | A |  | Código do Departamento |  |  |
| 192 | 216 | 025 | A |  | Código do Centro de Custos |  |  |
| 217 | 220 | 004 | N |  | Código da Filial | X |  |
| 221 | 230 | 010 | A |  | Código da Conta/Caixa Transferência | X | Nota 5 |
| 231 | 290 | 060 | A |  | Nominal a |  |  |
| 291 | 294 | 004 | N |  | Código da Coligada da Conta/Caixa | X |  |
| 295 | 298 | 004 | N |  | Cód. da Coligada da Conta/Caixa Transferência | X | Nota 5 |
| 299 | 299 | 001 | N |  | Cheque já Impresso | X | Nota 11 |
| 300 | 324 | 025 | A |  | Código da Tabela Opcional 1 |  |  |
| 325 | 349 | 025 | A |  | Código da Tabela Opcional 2 |  |  |
| 350 | 374 | 025 | A |  | Código da Tabela Opcional 3 |  |  |
| 375 | 399 | 025 | A |  | Código da Tabela Opcional 4 |  |  |
| 400 | 424 | 025 | A |  | Código da Tabela Opcional 5 |  |  |
| 425 | 427 | 003 | A |  | Código do Banco |  |  |
| 428 | 433 | 006 | A |  | Código da Agência |  |  |
| 434 | 448 | 015 | A |  | Código da Conta Corrente |  |  |
| 449 | 454 | 006 | D |  | Data de Vencimento | X | Nota 9 |
| 455 | 494 | 040 | A |  | Nome do Emitente |  |  |
| 495 | 509 | 015 | A |  | Telefone do Emitente |  |  |
| 510 | 541 | 032 | A |  | Praça do Cheque |  |  |
| 542 | 542 | 001 | N |  | Tipo de Custódia | X | Nota 6 |
| 543 | 548 | 006 | D |  | Data de Custódia Filial | X | Nota 7 |
| 549 | 554 | 006 | D |  | Data de Custódia Banco | X | Nota 7 |
| 555 | 557 | 003 | A |  | Código do Banco Custódia | X | Nota 7 |
| 558 | 563 | 006 | A |  | Código da Agência Custódia | X | Nota 7 |
| 564 | 564 | 001 | N |  | Pré-Datado | X | Nota 8 |
| 565 | 568 | 004 | A |  | Código da Filial Custódia | X | Nota 7 |
| 569 | 569 | 001 | N |  | Reconciliado |  | Nota 11 |
| 570 | 575 | 006 | D |  | Data da Prorrogação |  | Nota 9 |
| 576 | 595 | 020 | A |  | Número Contábil | X | Nota 10 |
| 596 | 600 | 005 | A |  | Código do Evento Contábil |  | Nota 10 |
| 601 | 601 | 001 | N |  | Extrato tem Cheque ou Não | X | Nota 8 |
| 602 | 619 | 018 | N | 4 | Valor Contábil |  | Nota 11 |
| 620 | 637 | 018 | N | 4 | Valor em Reais |  | Nota 11 |
| 638 | 651 | 014 | N |  | Cotação na Data de Inclusão |  |  |
| 652 | 657 | 006 | D |  | Data da Contabilização |  | Nota 10 |
| 658 | 661 | 004 | N |  | Coligada da Natureza Orçamentária |  |  |
| 662 | 701 | 040 | A |  | Natureza Orçamentária |  |  |
| 702 | 705 | 004 | E |  | Filial de Transferência |  |  |
| 706 | 706 | 001 |  |  | Classificação do lançamento no LCDPR |  | Nota 12 |
| 707 | 707 | 001 |  |  | Tipo de lançamento no LCDPR |  | Nota 13 |
| 708 | 727 | 020 | A |  | CPF/CNPJ do Participante |  |  |
| 728 | 731 | 004 | N |  | Coligada do Extrato |  | Nota 14 |

NOTAS EXPLICATIVAS  
Nota 1:

|  |  |
| --- | --- |
| 1 | = Saque Manual |
| 2 | = Depósito Manual |
| 3 | = Saque de Transferência |
| 4 | = Depósito de Transferência |
| 11 | = Saque de CPMF |

Atenção:

Válido somente para registros manuais.

Nota 2: Obrigatório, se Compensado.

Nota 3:

|  |  |
| --- | --- |
| 0 | = Não Contábil |
| 1 | = Contábil |

Nota 5: Obrigatório, se Transferência.

Nota 6:

|  |  |
| --- | --- |
| 0 | = Não Custodiado |
| 1 | = Custódia Banco |
| 2 | = Custódia Filial |

Nota 7: Obrigatório, se Custodiado.

Nota 8:

|  |  |
| --- | --- |
| 0 | = Não |
| 1 | = Sim |

Nota 9: Se cheque pré-datado.

Nota 10: Se Contábil.

Nota 11: Campo não utilizado, preencher com espaços.

Nota 12:

Classificação do lançamento no LCDPR:

* 1 - Nota Fiscal
* 2 – Fatura
* 3 – Recibo
* 4 – Contrato
* 5 - Folha de Pagamento
* 6 - Outros

Nota 13:

Tipo de Lançamento no LCDPR

* 1 - Receita da Atividade Rural
* 2 - Despesas de custeio e investimentos
* 3 – Receita de produtos entregues no ano referente a adiantamento de recursos financeiros

Nota 14:

Se não informado, será considerado a coligada corrente. Disponível a partir do patch 12.1.31.131.

Linha de Campos Complementares dos Extratos de Caixa

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| De | Até | Tam. | Form. | Nº Dec. | Descrição | Obrigatório | Obs. |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra M |

Observação:

Informe os campos complementares em sequência, a partir da posição "002".

Exemplo:

Você possui os campos complementares:

* Contabilizado por – tamanho 25;
* Responsável – tamanho 20;
* Valor de Desconto – tamanho 18.

O preenchimento do layout deve ser:

Posição: 002 a 026  
Tamanho: 025  
Formato: A  
Nº Decimal:  
Descrição: Contabilizado por  
Posição: 027 a 046  
Tamanho: 020  
Formato: A  
Nº Decimal:  
Descrição: Responsável  
Posição: 047 a 064  
Tamanho: 018  
Formato: N  
Nº Decimal: 4  
Descrição: Valor de Desconto

Para facilitar o TOTVS Gestão Financeira gera um layout dos registros de campos complementares cadastrados na base. Para visualizar este layout você deve clicar sobre o botão "Gerar" localizado na tela do processo "Importar Extrato de Caixa".

Linha de Dados da Contabilização dos Extratos de Caixa

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| De | Até | Tam. | Form. | Nº Dec. | Descrição | Obrigatório | Obs. |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra C |
| 002 | 002 | 001 | N |  | Débito ou Crédito | X | Nota 9 |
| 003 | 006 | 004 | N |  | Código da Coligada da Conta Contábil | X |  |
| 007 | 046 | 040 | A |  | Código da Conta Contábil | X |  |
| 047 | 064 | 018 | N | 2 | Valor | X |  |
| 065 | 068 | 004 | N |  | Código da Filial | X |  |
| 069 | 093 | 025 | A |  | Código do Departamento |  |  |
| 094 | 118 | 025 | A |  | Código do Centro de Custo |  |  |
| 119 | 128 | 010 | A |  | Código do Histórico Padrão |  |  |
| 129 | 378 | 250 | A |  | Complemento do Histórico |  |  |

**Notas explicativas**

Nota 9:

|  |  |
| --- | --- |
| 1 | = Débito |
| 2 | = Crédito |

Linha de Dados dos Rateios Gerenciais dos Extratos de Caixa

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| De | Até | Tam. | Form. | Nº Dec. | Descrição | Obrigatório | Obs. |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra R |
| 002 | 005 | 004 | N |  | Código da Coligada da Conta Gerencial | X |  |
| 006 | 045 | 040 | A |  | Código da Conta Gerencial | X |  |
| 046 | 063 | 018 | N | 2 | Valor | X |  |
