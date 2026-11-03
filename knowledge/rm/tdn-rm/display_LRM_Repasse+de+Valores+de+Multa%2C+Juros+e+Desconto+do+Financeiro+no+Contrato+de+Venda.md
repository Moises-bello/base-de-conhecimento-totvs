---
content_hash: 06696375e265bc75d0d8dd85c4b5edbe3e97b1654a0ad94bbffbb4c48a1c5b2e
fetched_at: '2026-06-29T00:11:22.383366+00:00'
page_id: '702365309'
product: rm
source: tdn-rm
title: Repasse de Valores de Multa, Juros e Desconto do Financeiro no Contrato de
  Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Repasse+de+Valores+de+Multa%2C+Juros+e+Desconto+do+Financeiro+no+Contrato+de+Venda
version: 3
---

**Fórmulas de Repasses**

---

**Incluindo as Fórmulas para Cálculo de Juros, Multa e Desconto**  
**Passo 1** - Acesse: TOTVS Serviços Globais/ Administração/ Fórmulas  
**Passo 2** - Selecione o Contexto do sistema de Gestão Financeira e clique em Incluir Fórmula.  
**Passo 3** - Informe o Código e Título para cada tipo abaixo

* **Juros:** VALORCAMPOLANCAMENTOGERADOR('VALORJUROSBX') \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTUAL')/100)
* **Multa:** VALORCAMPOLANCAMENTOGERADOR('VALORMULTABX') \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTUAL')/100)
* **Desconto:** VALORCAMPOLANCAMENTOGERADOR('VALORDESCONTOBX') \* (VALORCAMPOLANCAMENTOREPASSE('PERCENTUAL')/100)

**Parâmetros Financeiro**

---

**Acesse o Gestão Financeira,  Ambiente - Parâmetros - Totvs Gestão Financeira - Contas a Pagar - Manutenção de Lançamentos - Lançamento - Etapa 10 - Valores Opcionais do Lançamento Financeiro**.

Configure Conforme a imagem abaixo, incluindo os três tipos de fórmulas acima.  
 

**Associar o Tipo de Documento a Pagar**

---

**Selecione o Tipo de Documento a Pagar na Condição de Financiamento da Venda ou associe no Empreendimento**

**Tipo de Documento com as fórmulas de repasses de multa, juros e desconto**

**Plano de Financiamento e Baixa**

---

Gere o Plano de Financiamento. realize a baixa do título em atraso e depois realize a baixa do lançamento de repasse que serão inclusos esse valores

Baixa do lançamento original com multa,  juros e desconto

Baixa do lançamento de repasse e com os valores proporcionais de multa, juros e desconto
