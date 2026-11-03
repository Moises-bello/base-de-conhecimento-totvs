---
content_hash: 919fbae0123e8068fe62673058eb29253dbffb5b785e9eda6a4038d1e44f967c
fetched_at: '2026-06-29T00:09:25.249270+00:00'
page_id: '423938077'
product: rm
source: tdn-rm
title: Manutenção (Parâmetros de Integrações)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938077
version: 11
---

**Integrar objeto de oficina ao item de movimento:**  Habilitando esta opção será disponibilizado na pasta Integração do Item do Movimento/"TOTVS Manutenção/Objeto" o campo onde o usuário poderá associar um objeto do Officina ao item. Ao indicar o objeto de manutenção será habilitado o botão que informa o valor de indicador de uso do objeto de manutenção selecionado.

**Integração por API de Reporte:** Habilitando esta opção será marcado o tipo de movimento que reportará os dados para API: **Reporte de Itens Atendidos.**

Na tela de parâmetros -> Manutenção é possível escolher se o tipo de movimento selecionado terá integração com a API de Reporte, e qual fórmula poderá ser utilizado no valor reportado.

Para selecionar a integração basta marcar o Checkbox referente a ela.

Ao marcar o Checkbox a opção para selecionar uma fórmula será habilitada, esta poderá  ser utilizada nas situações onde se deseja retornar um valor do item calculado por uma fórmula, conforme a necessidade da empresa, valor ressaltar que a fórmula criada deverá ter campos do item.

Nas situações onde não for selecionada uma fórmula a API retornará o valor unitário do item do movimento.

**Ponto de Atenção:**

O Identificador do Movimento e o Número Seq. interno do Item do Movimento que originou a movimentação a ser reportada que deverá ser informando nos campos da API, conforme abaixo:

Para mais detalhes da API Reporte de Itens Atendidos acesso o Link  <https://api.totvs.com.br/apidetails/ReportInputs_v1_000.json>.

Atenção

A API esta disponível na release 12.1.2205 ou superior.
