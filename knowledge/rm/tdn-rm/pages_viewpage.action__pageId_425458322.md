---
content_hash: 5d47333e8fa1deee8e7c1def8f7b85fc714c69c1d5d7ce634407ddfdd933c44e
fetched_at: '2026-06-29T00:09:29.868136+00:00'
page_id: '425458322'
product: rm
source: tdn-rm
title: RM Portal - Parâmetros Gerais 10/18
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458322
version: 16
---

---

1
incomplete
**Permitir imprimir boletos não registrados (válido para convênios do tipo de cobrança registrada)**: quando marcado, a exibição dos boletos que ainda não foram registrados independente do tipo de serviço associado a parcela será permitida. Caso esteja desmarcado, a opção de impressão de boleto só aparecerá se o boleto estiver registrado ou se o serviço educacional, vinculado ao boleto, estiver marcado no parâmetro "**"**. Essa parametrização permitirá que o boleto seja registrado ao clicar na opção de impressão de boleto.

**Serviços que permitem registrar boleto online:** Os boletos, cujo o serviço vinculado esteja marcado, serão registrados na impressão do boleto, caso não tenham sido registrados anteriormente.

3
incomplete
**Permitir imprimir boletos vencidos não registrados com X dias para o próximo vencimento**: permite que boletos vencidos ainda não registrados possam ser impressos pelo portal do aluno.

Para isso:

* o parâmetro **,** deve ter serviço(s) selecionado(s)
* este parâmetro deverá estar marcado
* a quantidade de dias, que será utilizada para calcular a próxima data de vencimento do boleto, preenchida;
* no parâmetro **,** o(s) serviço(s) selecionado(s) devem ter associados a eles a conta caixa com o registro online de boleto configurado.

Importante

Este parâmetro só será aplicado se o convênio do boleto utilizar valor líquido ou parcial no código de barras.
