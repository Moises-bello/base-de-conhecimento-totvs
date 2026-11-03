---
content_hash: 70f4b27d9e005748e03cc74cfb879dcfe5ac147abb45dce092f2af7bd20d99b1
fetched_at: '2026-06-29T00:11:17.237462+00:00'
page_id: '678562720'
product: rm
source: tdn-rm
title: Layout de Importação de Saldo Anterior com Rateio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=678562720
version: 4
---

Esse layout tem como objetivo permitir que seja inserido o saldo inicial com rateios. Desta forma o sistema permite a inserção de saldo anterior com a repetição da mesma conta, desde que sejam distintos Centros de Custo, Departamentos ou Contas Gerenciais.

**Importante:** Se deseja trabalhar com [implantação de saldo anterior de Eliminação](https://tdn.totvs.com/x/N0_gJg), faça primeiro a implantação das eliminações.

Saldo Anterior:

| # | Descrição | Tipo | Tamanho | Obrigatório | Observação |
| --- | --- | --- | --- | --- | --- |
| **1** | Código da Conta | Alfanumérico | 40 | X |  |
| **2** | Código Gerencial | Alfanumérico | 40 |  |  |
| **3** | Código da Filial | Numérico | 3 | X |  |
| **4** | Código do Centro de Custo | Alfanumérico | 40 |  |  |
| **5** | Código do Departamento | Alfanumérico | 40 |  |  |
| **6** | Valor | Numérico com 2 decimais | 15 |  | Separado por Virgula. Ex: 1500,55 |
| **7** | Valor2 | Numérico com 2 decimais | 15 |  | Separado por Virgula. Ex: 700,32 |
| **8** | Coligada da Eliminação | Alfanumérico | 40 |  |  |
| **9** | Código da Conta Eliminação | Alfanumérico | 40 |  |  |

Exemplo de Arquivo Modelo:

(trocar os textos dos campos pelos valores correspondentes).

**Observação**

* Todos os campos devem ser inseridos no arquivo da esquerda para a direita, separados por **Ponto e Virgula ";**".
* Os preenchimentos dos campos devem ser idênticos aos valores do banco. Exemplo: **Código Departamento “01”** é diferente de **Código Departamento “1”**.
* O processo sempre utilizará o último **Exercício Fechado** "não liberado".
* O processo de importação de Saldo Anterior só executa uma única vez para o exercício fechado.
* Caso alguma informação tenha sido importada incorretamente o **Exercício Fechado** precisará ser Reaberto e Fechado novamente, assim será possível importar o arquivo novamente.
* Quebra de linha apenas com a tecla **"ENTER"**.
* Esta funcionalidade está disponível a partir da Release 12.1.32.
