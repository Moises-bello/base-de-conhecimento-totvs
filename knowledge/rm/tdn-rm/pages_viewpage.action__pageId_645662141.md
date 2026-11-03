---
content_hash: f32d0f7c8ceff8318bd78c8abe41b87d5a7007c99e76229c3be3e534e2d447a1
fetched_at: '2026-06-29T00:11:11.111725+00:00'
page_id: '645662141'
product: rm
source: tdn-rm
title: Layout de Importação de Saldo Anterior MultiMoeda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=645662141
version: 14
---

O layout em questão tem como objetivo permitr que seja inserido o saldo inicial das MultiMoedas que foram configuradas no sistema. Desta forma o sistema terá saldo anterior para multimoedas sem a necessidade que se faça a manutenção dessa informação em cada lançamento em exercícios já fechados.

**Importante:** Se deseja trabalhar com [implantação de saldo anterior de Eliminação](https://tdn.totvs.com/x/N0_gJg) e MultiMoeda, faça primeiro a implantação das eliminações.

Saldo Anterior MultiMoeda

| # | Descrição | Tipo | Tamanho | Obrigatório | Observação |
| --- | --- | --- | --- | --- | --- |
| **1** | Código da Coligada | Numérico | 2 | X |  |
| **2** | Código da Conta | Alfanumérico | 40 | X |  |
| **3** | Código Gerencial | Alfanumérico | 40 |  |  |
| **4** | Código da Filial | Numérico | 3 | X |  |
| **5** | Código do Centro de Custo | Alfanumérico | 40 |  |  |
| **6** | Código do Departamento | Alfanumérico | 40 |  |  |
| **7** | Coligada da Eliminação | Alfanumérico | 40 |  |  |
| **8** | Código da Conta Eliminação | Alfanumérico | 40 |  |  |
| **9** | Símbolo da Moeda | Alfanumérico | 10 | X |  |
| **10** | Valor | Numérico com 2 decimais | 15 |  | Separado por Virgula. Ex: 1500,55 |

Exemplo de Arquivo Modelo: 

(trocar os textos dos campos pelos valores correspondentes).

**Observação**

* Todos os campos devem ser inseridos no arquivo da esquerda para a direita, separados por **Ponto e Virgula ";**".
* Os preenchimentos dos campos devem ser idênticos aos valores do banco. Exemplo: **Código Departamento “01”** é diferente de **Código Departamento “1”**.
* O processo sempre utilizará o último **Exercício Fechado** "não liberado".
* O processo de importação de Saldo Anterior de MultiMoedas só executa uma única vez.
* Caso alguma informação tenha sido importada incorretamente o **Exercício Fechado** precisará ser Reaberto e Fechado novamente, assim será possível importar o arquivo novamente.
* Quebra de linha apenas com a tecla **"ENTER"**.
* Esta funcionalidade está disponível a partir da Release 12.1.33.
