---
content_hash: c903e7b2141b5d2438b23eed3abb313e7d2ab8a459921afac0a4b2f0316fda8c
fetched_at: '2026-06-29T00:05:52.157743+00:00'
page_id: '1056937472'
product: rm
source: tdn-rm
title: API para Gerar QRCode TOTVS Pagamento Instantâneo (PIX)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056937472
version: 6
---

# Sumário

---

Sumário

# Objetivo

---

      Esse documento tem o objetivo de exemplificar o uso da API para Gerar QRCode TOTVS Pagamento Instantâneo (PIX) utilizando o método implementado.

Importante

Recurso disponível a partir dos patches 12.1.2506.287, 12.1.2510.208 e 12.1.2602.129.

# 1 - Métodos

---

      Será apresentado 1 método, o qual foi implementado na API para Geração de QRCode TOTVS Pagamento Instantâneo (PIX):

* POST

# 1.1 - POST

---

## 1.1.1 - Post (Inserir QRCode PIX)

---

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/financial/v1/paymenthub/qrcodepix

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada: <http://localhost:8051/api/financial/v1/paymenthub/qrcodepix>**

falseExemplo de Entrada

O campo data de cálculo ("CalculationDate") não é obrigatório, caso não informado será utilizada a data atual.

Ver resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true
