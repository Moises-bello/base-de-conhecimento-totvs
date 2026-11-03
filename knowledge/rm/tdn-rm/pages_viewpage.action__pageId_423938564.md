---
content_hash: f5ca37389770790c827e3653124df59054374bf3068a514b4d999dffcd4b9e0f
fetched_at: '2026-06-29T00:09:27.897908+00:00'
page_id: '423938564'
product: rm
source: tdn-rm
title: Layout de Importação de Saldo Anterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938564
version: 5
---

Esse *layout* permite a importação do saldo inicial contábil sem ou com rateios por Centros de Custo, Departamentos ou Contas Gerenciais.

**Importante:** Se deseja trabalhar com multimoedas, após a importação do saldo anterior, faça a importação do .

Saldo Anterior:

| # | Descrição | Tipo | Tamanho | Obrigatório | Observação |
| --- | --- | --- | --- | --- | --- |
| **1** | Código da Conta | Alfanumérico | 40 | X |  |
| **2** | Código Gerencial | Alfanumérico | 40 |  |  |
| **3** | Código da Filial | Numérico | 2 | X |  |
| **4** | Código do Centro de Custo | Alfanumérico | 25 |  |  |
| **5** | Código do Departamento | Alfanumérico | 25 |  |  |
| **6** | Valor | Numérico com 2 decimais | 15 | X | Separado por Virgula. Ex: 1500,55 |
| **7** | 2º Valor | Numérico com 2 decimais | 15 |  | Separado por Virgula. Ex: 700,32 |
| **8** | Coligada de Eliminação | Alfanumérico | 2 | - | Esse campo passa a ser de preenchimento obrigatório caso seja informado o Código da Conta de Eliminação. |
| **9** | Código da Conta Eliminação | Alfanumérico | 40 | - | Esse campo passa a ser de preenchimento obrigatório caso seja informado a Coligada de Eliminação |

Exemplo de Arquivo Modelo:  (trocar os textos dos campos pelos valores correspondentes).

**Observação**

* Todos os campos devem ser inseridos no arquivo da esquerda para a direita, separados por **Ponto e Virgula ";**".
* Os preenchimentos dos campos devem ser idênticos aos valores do banco. Exemplo: **Código Departamento “01”** é diferente de **Código Departamento “1”**.
* O processo sempre utilizará o último **Exercício Fechado** "não liberado".
* O processo de importação de Saldo Anterior só executa uma única vez para o exercício fechado.
* Caso alguma informação tenha sido importada incorretamente o **Exercício Fechado** precisará ser Reaberto e Fechado novamente, assim será possível importar o arquivo novamente.
* Quebra de linha apenas com a tecla **"ENTER"**.
* Esta funcionalidade está disponível a partir da Release 12.1.32.
