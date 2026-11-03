---
content_hash: 9555b1685b069bd572668ff18c53a9b0ac657f130117df0e11af1d4e0e2321c5
fetched_at: '2026-06-29T00:10:58.078800+00:00'
page_id: '603106970'
product: rm
source: tdn-rm
title: Geração QRCode PIX
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=603106970
version: 20
---

## **01. VISÃO GERAL**

Esta funcionalidade disponibiliza uma maneira de gerar o QRCode Pix através do TOTVS Pagamento Instantâneo.

## **02. EXEMPLO DE UTILIZAÇÃO**

1. Através do menu**Contas A Pagar / Receber**, no agrupamento **Totvs Pagamento Instantâneo** selecionando o botão **Mais**e a opção **Gerar QRCode** **Pix**.
2. Faça um filtro ou escolha um já existente para exibir os boletos. Selecione os boletos para que deseja gerar o QRCode Pix.
3. Escolha a data de cálculo e o tipo de agrupamento para geração do QRCode Pix.

## **03. TIPOS DE AGRUPAMENTO**

* **Um QRCode para cada Cliente/Fornecedor.** Os boletos serão agrupados por Cliente/Fornecedor e será gerado um QRCode para cada Cliente/Fornecedor.
* **Um QRCode para cada registro selecionado.** Para cada boleto selecionado, será gerado um QRCode. **Obs**: Caso seja selecionado algum boleto que já tenha um QRCode expirado junto com outro(s) que ainda não possui(em) o QRCode, o sistema irá gerar a transação com a data de expiração conforme a data do sistema e para os demais (que ainda não possuíam o QRCode), de acordo com a data de vencimento dos respectivos boletos.

## **04. TELA GERAÇÃO QRCODE PIX**

## **05. PROCESSO CONCLUÍDO**

* Após a conclusão do processo, o **QRCode gerado** é associado a uma **transação** referente ao PIX, que pode ser consultada através do menu 'Contas a Pagar / Receber - Transações', localizada no agrupamento "TOTVS Pagamento Instantâneo".
* Por padrão, a **Data/hora de expiração do QRCode Pix** será de uma hora a partir da data/hora da geração. Caso a hora da geração do QrCode seja após às 23:00, a expiração será às 23:59:59.
* A data de expiração é gerada no fuso horário zero (UTC 0) e convertida para a data/hora de acordo com o fuso horário do servidor de aplicação.
