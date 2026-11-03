---
content_hash: 28a0d22b6a9ef8b144645035e017f54947807b367618359b139c972a0cf36f9d
fetched_at: '2026-06-29T00:09:24.785372+00:00'
page_id: '423938015'
product: rm
source: tdn-rm
title: Importação de Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938015
version: 6
---

Para que seja possível realizar a importação do orçamento via arquivo texto (. txt) e/ou planilhas (.xls), deve-se, seguir as configurações conforme especificação abaixo:

**Importação via arquivo TXT**

* A data deverá seguir o formato DD/MM/AAAA;
* A importação sempre afetará o valor orçado. Caso este seja zero e tente importar um valor negativo, deverá ser gerada uma exceção e a importação não poderá ser concluída;
* A importação pode ser feita inclusive para orçamentos que estejam bloqueados;
* A coluna Tipo deve ser preenchida com '**R**' para **Receita** e '**D**' para **Despesa**. Caso o arquivo txt não tenha a informação de **Tipo** o orçamento será incluído como **Despesa**;

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **CAMPO** | **TIPO** | **TAMANHO** | **DEC** | **POSIÇÃO** |
| Código do Centro de Custo | A | 25 |  | 001 - 025 |
| Código Natureza | A | 40 |  | 026 - 065 |
| Data | Data | 10 |  | 066 - 075 |
| Valor Orçado | N | 20 | 4 | 076 - 095 |
| Grupo Orçamentário | A | 40 |  | 096 - 135 |
| Tipo | A | 1 |  | 136 |

***Observação*:** Caso não esteja parametrizada a edição do Grupo Orçamentário, a posição do mesmo deve ser desconsiderada e o campo **Tipo** deverá ser informado a partir da **posição 96**.

**Importação via Planilha Excel**

* Deverá ser informado o nome da planilha que se deseja importar (quando gera um arquivo novo do Excel, geralmente criam-se 3 planilhas automaticamente, a Plan1, Plan2 e a Plan3);
* A primeira linha do arquivo deve conter o nome das colunas de acordo com a parametrização referente ao grupo orçamentário na seguinte ordem:
* **Usa grupo orçamentário:** CODCCUSTO, CODTBORCAMENTO, DATAORCAMENTO, VALOREFEITOORCAMENTO, CODTBGRUPOORC e TIPO;
* **Não usa grupo orçamentário:** CODCCUSTO, CODTBORCAMENTO, DATAORCAMENTO, VALOREFEITOORCAMENTO e TIPO;
* O Nome das colunas podem ser alterados, ex: Centro de Custo, Data do Orçamento, etc..., mas a ordem deve ser mantida;
* A data deve estar no formato dd/MM/yyyy, ex: 06/09/2018;
* A coluna **Tipo** deve ser preenchida com '**R**' para **Receita** e '**D**' para **Despesa;** Importação da planilha sem a informação na coluna **Tipo**,neste caso o orçamento será incluído como **Despesa**;
* Caso não esteja parametrizada a edição do grupo orçamentário, a coluna do mesmo deve ser desconsiderada e o campo **Tipo** deverá ser a próxima coluna.

***Importante!***É recomendado que todos os valores estejam como texto, para que não hajam problemas na importação.
