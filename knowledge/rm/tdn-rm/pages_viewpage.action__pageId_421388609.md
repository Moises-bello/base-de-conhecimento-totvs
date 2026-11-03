---
content_hash: 2431ce59bbe2902c8c097322fbae4ec0e6c2d43fedab5b6d264ba0bdfbcf42ac
fetched_at: '2026-06-29T00:09:17.501720+00:00'
page_id: '421388609'
product: rm
source: tdn-rm
title: Importação de Baixa do Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388609
version: 5
---

**Layout de importação de Baixa**

Para a importação de arquivo texto contendo dados para a baixa de Lançamentos no TOTVS Gestão Financeira, é necessário seguir o seguinte layout:  
 No arquivo texto deverá existir uma linha contendo os dados da baixa do lançamento, linhas contendo dados da contabilização da baixa caso ele seja contábil e linhas contendo dados do rateio contábil, caso exista.  
 Estas linhas deverão ser identificadas com os prefixos apropriados, conforme explicado abaixo:

|  |  |
| --- | --- |
| Uma linha com os dados da baixa do lançamento................ | Linha tipo "L" |
| Uma linha para cada conta contábil a débito ou a crédito..... | Linhas tipo "C" |
| Uma linha para cada conta contábil que possui rateio gerencial | Linhas tipo "R" |

O separador dos campos que possuem casas decimais deve ser o ponto.  
 Alinhamento de campos:  
 N = Campo numérico, alinhado à direita com zeros à esquerda.

A = Campo alfanumérico, alinhado à esquerda com espaços à direita.

Tam. = Tamanho

Form. = Formato

Nº Dec. = Número de decimais

Obs. = Observação

**Linha de dados da baixa do Lançamento:**

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra L |
| 002 | 005 | 004 | N |  | Código da Filial | X |  |
| 006 | 030 | 025 | A |  | Código do Cli/For | X | Nota 1 |
| 031 | 040 | 010 | A |  | Código do Tipo de Documento | X |  |
| 041 | 080 | 040 | A |  | Número do Documento | X |  |
| 081 | 086 | 006 | N |  | Data da Baixa |  |  |
| 087 | 104 | 018 | N | 4 | Valor Baixado |  |  |
| 105 | 122 | 018 | N | 4 | Valor dos Juros |  |  |
| 123 | 140 | 018 | N | 4 | Valor do Desconto |  |  |
| 141 | 144 | 004 | N |  | Cód. Coligada da Conta/Caixa |  |  |
| 145 | 154 | 010 | A |  | Código da Conta/Caixa |  |  |
| 155 | 174 | 020 | A |  | Número Contábil da Baixa |  |  |
| 175 | 179 | 005 | N |  | Cód. Evento Contábil da Baixa |  |  |
| 180 | 183 | 004 | N |  | Cód. Coligada do Cli/For |  |  |
| 184 | 186 | 003 | A |  | Série do Documento |  |  |
| 187 | 204 | 018 | N | 4 | Valor Opcional 1 |  |  |
| 205 | 222 | 018 | N | 4 | Valor Opcional 2 |  |  |
| 223 | 240 | 018 | N | 4 | Valor Opcional 3 |  |  |
| 241 | 258 | 018 | N | 4 | Valor Opcional 4 |  |  |
| 259 | 276 | 018 | N | 4 | Valor Opcional 5 |  |  |
| 277 | 294 | 018 | N | 4 | Valor Opcional 6 |  |  |
| 295 | 312 | 018 | N | 4 | Valor Opcional 7 |  |  |
| 313 | 330 | 018 | N | 4 | Valor Opcional 8 |  |  |
| 331 | 348 | 018 | N | 4 | Valor Multa |  |  |
| 349 | 352 | 004 | N | 4 | Reutilização |  |  |
| 353 | 372 | 020 | A |  | Número do Cheque |  |  |
| 373 | 627 | 255 | A |  | Histórico |  |  |
| 628 | 652 | 025 | A |  | Código da Tabela Opcional 1 |  |  |
| 653 | 677 | 025 | A |  | Código da Tabela Opcional 2 |  |  |
| 678 | 702 | 025 | A |  | Código da Tabela Opcional 3 |  |  |
| 703 | 727 | 025 | A |  | Código da Tabela Opcional 4 |  |  |
| 728 | 752 | 025 | A |  | Código da Tabela Opcional 5 |  |  |
| 753 | 852 | 100 | A |  | Alfa 1 |  |  |
| 853 | 872 | 020 | A |  | Alfa 2 |  |  |
| 873 | 892 | 020 | A |  | Alfa 3 |  |  |
| 893 | 898 | 006 | N |  | Data Opcional 1 |  |  |
| 899 | 904 | 006 | N |  | Data Opcional 2 |  |  |
| 905 | 910 | 006 | N |  | Data Opcional 3 |  |  |
| 911 | 916 | 006 | N |  | Data Opcional 4 |  |  |
| 917 | 922 | 006 | N |  | Data Opcional 5 |  |  |
| 923 | 930 | 008 | A |  | Série Documento (8 posições) |  | Nota 2 |
| 931 | 936 | 006 | N |  | IDFORMAPAGTO | X |  |

****NOTAS EXPLICATIVAS:****

**Nota 1** Caso seja escolhida a importação utilizando CNPJ/CEI/CPF, na posição onde deveria estar o Código do Cli/For, deve estar o CNPJ/CEI/CPF.

Isso foi feito para permitir que se importe Séries de Documento maiores que três posições, sem, no entanto, exigir a alteração dos layouts já utilizados pelos clientes.

**Nota 2** Se o campo Série Documento(8 posições) (posições 923 a 930) estiver preenchido, os dados preenchidos nas posições 184 a 186 serão desprezados. Caso contrário, permanecerão sendo considerados para a série do documento.

**Observação:**  
 A baixa via arquivo de importação, utilizando a flag "Considerar valores zerados de Multa/ Juros/ Desconto/ Valores Opcionais do arquivo" na visão de importação de baixa é utilizado para que todos os dados do arquivo referente a juros, multa, desconto e valores opcionais sejam considerados independente dos dados informados no lançamento financeiro.

**Linha de dados das Contabilizações de Baixa:**

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra C |
| 002 | 002 | 001 | N |  | Débito/Crédito | X | Nota 1 |
| 003 | 003 | 001 | N |  | Inclusão/Baixa | X | Nota 2 |
| 004 | 007 | 004 | N |  | Cód. Coligada da Conta | X |  |
| 008 | 047 | 040 | A |  | Código da Conta | X |  |
| 048 | 065 | 018 | N | 2 | Valor | X |  |
| 066 | 069 | 004 | N |  | Código da Filial | X |  |
| 070 | 094 | 025 | A |  | Código do Departamento |  |  |
| 095 | 119 | 025 | A |  | Cód do Centro de Custos |  |  |
| 120 | 129 | 010 | A |  | Cód do Histórico Padrão |  |  |
| 130 | 379 | 250 | A |  | Complemento do Histórico |  |  |

****NOTAS EXPLICATIVAS:****  
 **Nota 1:** 1 = Débito 2 = Crédito  
 **Nota 2:** 3 = Baixa  
    
 **Linha de dados dos Rateios Gerenciais:**

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra R |
| 002 | 005 | 004 | N |  | Cód. Coligada da Conta Gerencial | X |  |
| 006 | 045 | 040 | A |  | Cód. da Conta Gerencial | X |  |
| 046 | 063 | 018 | N | 2 | Valor | X |  |

**Linha de dados dos Campos Complementares:**

**Posição**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| 001 | 001 | 001 | A |  | Tipo da linha | X | Letra M |

**Observação:**  
 Informe os campos complementares em seqüência, a partir da posição "002".  
    
 **Exemplo:**  
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
