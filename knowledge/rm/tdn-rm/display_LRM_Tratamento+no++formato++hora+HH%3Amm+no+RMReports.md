---
content_hash: 7a55b1cded6fe5b36b8429d3163814436483b850c8c929c08b79b0b0b3ddd36b
fetched_at: '2026-06-29T00:05:57.153864+00:00'
page_id: '165282429'
product: rm
source: tdn-rm
title: Tratamento no  formato  hora HH:mm no RMReports
type: documentation
url: https://tdn.totvs.com/display/LRM/Tratamento+no++formato++hora+HH%3Amm+no+RMReports
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.xx |
| **Processo** | **:** | Report |
| **Subprocesso** | **:** | Tratamento no  formato  hora HH:mm no RMReports |
| **Data da publicação** | **:** | 01/10/2014 |

* No exemplo a ser demonstrado, existem alguns campos na base de dados que trazem a hora em minutos, um exemplo, e o campo HORA da tabela PFFINANC. Com isso surge a dúvida:

**Como efetuar a tratativa para que o relatório retorne este campo no formato HH: mm?**

* Conforme select abaixo veja que o resultado da coluna HORA vem em Minutos e fica fora do padrão este formato em uma estrutura de relatório Reports:

* Criaremos um relatório teste para fazermos a configuração deste dado no relatório.
* Dados utilizados, com base na tabela **PFFINANC**:

**Chapa, Mês Competência e HORA**

* Edite o campo HORA, vá nas propriedades deste, selecione o campo hora (aperte F4)
* Na opção Converter Para Horas alterar o valor para **VERDADEIRO**

Gere o relatório e verá que o campo será retornado para o padrão **HH.mm**

\_GoBack
