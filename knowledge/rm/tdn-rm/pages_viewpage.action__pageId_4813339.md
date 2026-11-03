---
content_hash: 33d665dc08bd5f922fe722495bf2f74476ed909b55a47a5c511f0dc72ba9da4c
fetched_at: '2026-06-29T00:10:19.325629+00:00'
page_id: '4813339'
product: rm
source: tdn-rm
title: Data do movimento está fora do exercício fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813339
version: 4
---

BLOCK

Data do movimento está fora do exercício fiscal

FAQ: **Data do movimento está fora do exercício fiscal**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

**Sintoma**Ao tentar incluir/alterar um movimento é apresentada a seguinte mensagem: *“Data do movimento está fora do exercício fiscal”.*

**Causas**A data do movimento não esta compatível com o Exercício Fiscal parametrizado para movimentação.

Solução

1. Acessar o Menu Utilitários / Selecionar Exercício Fiscal / e verificar qual é o exercício fiscal corrente.
2. Acessar o Menu Cadastros / Tabelas de Tributação / Exercício Fiscal / escolher o exercício fiscal corrente e verificar qual o período do exercício definido nos campos “Data Inicial” e “Data Final”.
3. Nos parâmetros do tipo de movimento e na etapa **Movimento – Datas** e verificar a data default do campo **“Data do Movimento Default”,** caso não esteja informada, defina uma data para ser considerada no período de movimentação. Lembrando que a data escolhida também deverá estar habilitada para ser utilizada no tipo de movimento, onde sua edição deverá ser diferente de “Não Edita”. Exemplo: A data default do movimento é a Data Extra1. No qual a Data Extra1 também deverá ser habilitada e sua edição deverá ser “Edita”, Edita Obrigatoriamente“ ou Mostra”, conforme conveniência do cliente.
4. Após verificado as parametrizações confirmar se durante a inclusão/alteração do movimento a data definida como default do movimento esta dentro do período de movimentação definido. No caso do exemplo acima a data extra1.
