---
content_hash: f11a6203405bf3cc63d5a62656de2616875009c955a4c741355a53c1ed20a2f3
fetched_at: '2026-06-29T00:10:50.727835+00:00'
page_id: '562960347'
product: rm
source: tdn-rm
title: Layout para Importação de Tabelas de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562960347
version: 1
---

**Importante:**

Caso, não haja valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:

- 0 (zero), no caso de serem dos tipos inteiro ou real ou;

- ' ' (branco), no caso de serem dos tipos string, caractere ou data.

Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

 Atenção:

PARÂMETROS a serem observados:

Campos do tipo MEMO começam com /@ e terminam com @/

DELIMITADOR DE CAMPOS : ";"

FORMATO DE DATA   : ddmmyyyy

SEPARADOR DECIMAL  : ","

FORMATO DE DECIMAL : 999999999999,99

 **Atenção!**

Campos em vermelho foram inseridos nos arquivos de uma versão para outra.

F - campos cuja alteração ligam os flags de FGTS

H - campos cuja alteração geram histórico

Q - campos que podem ser alterados via RM Portal

|  |  |  |  |
| --- | --- | --- | --- |
| DESCRIÇÃO | TIPO | TAMANHO | CAMPO |
| 1 | Inteiro | 1 | 1 |
| Código da Cálculo | String | 6 | 2 |
| Inicio de Vigência | Data | 8 | 3 |
| Nome do Cálculo | String | 30 | 4 |
| Fim de Vigência | Data | 8 | 5 |
| Indicativo de Arredondamento de Valor | Inteiro | 2 | 6 |
| Truncamento de centavos | Inteiro | 2 | 7 |
| Finalidade | Inteiro | 2 | 8 |
| Atualiza Vigência | Inteiro | 2 | 9 |
| 2 | Inteiro | 1 | 10 |
| Código de Cálculo | String | 6 | 11 |
| Início da Vigência da Tabela | Data | 8 | 12 |
| Número da Faixa | Inteiro | 2 | 13 |
| Valor de Limite Superior | Real | 9 | 14 |
| Primeiro Percentual Aplicável | Real | 9 | 15 |
| Valor a Deduzir | Real | 9 | 16 |
| Valor a Acrescentar | Real | 9 | 17 |
| Segundo Percentual Aplicável | Real | 9 | 18 |

 **Observação:**

Os itens do layout que iniciam com 2 devem vir logo abaixo dos itens que iniciam com 1 por se tratarem de dependência, ou seja, os itens 2 dependem do item 1 anterior a eles.

**Exemplo:**

1;0001;01/01/1997;CALCULO DA COMISSAO;31/01/2004;1;0;0;1

2;0001;01/01/1997;1;16000;50;0;0;0

2;0001;01/01/1997;2;40000;65;0;100;0

2;0001;01/01/1997;3;99999999;70;0;200;0
