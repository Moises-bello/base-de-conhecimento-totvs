---
content_hash: 26934459c8533927001298c127b356b4ce8442d540c5e57a7a0446936649a50b
fetched_at: '2026-06-29T00:10:19.297959+00:00'
page_id: '4813220'
product: rm
source: tdn-rm
title: O Valor do Bem não é preenchido após salvar a movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813220
version: 4
---

BLOCK

O Valor do Bem não é preenchido após salvar a movimentação

FAQ: **O Valor do Bem não é preenchido após salvar a movimentação**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Sintoma

* **Sintoma**

O Valor do Bem não é preenchido após salvar a movimentação

Causa

* **Causas**

1- A fórmula do valor do bem, não esta preenchida no tipo de movimento utilizado.

2- O resultado da fórmula do valor do bem retorna um valor zerado ou nenhum valor.

3- O Grupo de Contas do Produto utilizado na movimentação não esta preenchido.

Solução

* **Solução**

1- Informe a fórmula do valor do bem na etapa “Patrimônio” do tipo de movimento utilizado.

2- Analise a fórmula do valor do bem informada nos parâmetros do tipo de movimento e certifique que o resultado apresentado retorna um valor maior que zero.

3- Dentro do cadastro do produto utilizado na movimentação, informe o “Grupo de Contas” na pasta de Integração.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/dica-o-valor-do-bem-nao-e-preenchido.html>
