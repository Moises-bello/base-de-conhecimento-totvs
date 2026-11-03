---
content_hash: c0c3b193106f9b177e80804988ae53972fc2c1224923fda1154349e7916e565d
fetched_at: '2026-06-29T00:05:49.909965+00:00'
page_id: '1042921692'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Anexo - Despesa Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1042921692
version: 6
---

# 🔷 Cadastro de Despesa Financeira

O cadastro de Despesa Financeira permite o usuário definir quais os lançamentos financeiros irão incidir na apuração dos valores do condomínio durante o fechamento.

false

# 🗂️ Aba Identificação

---

**🆔 Cód. Despesa Financeira**

código identificador do cadastro da despesa financeira;

---

**🔒 Fechamento do Condomínio**

campo somente leitura que indica qual é o fechamento;

---

📝 **Descrição**

campo livre onde o usuário poderá descrever a despesa financeira;

---

**🧾 Item de cobrança**

indica qual o item de cobrança será associado a despesa financeira;

---

🏢 **Empreendimento**

campo somente leitura que indica qual é o empreendimento associado ao fechamento;

false

## 🔗 Associar Por

Indica o tipo de associação de subunidades que será feita com a despesa financeira para geração da despesa financeira no fechamento.

🏢 **Empreendimento**

Todas as subunidades do empreendimento ligado ao fechamento serão consideradas

🏬 **Unidade**

Todas as subunidades das unidades incluídas serão consideradas. Só é possível incluir unidades do empreendimento do fechamento

🏠 **Subunidade**

Todas as subunidades incluídas serão consideradas. Só é possível incluir subunidades do empreendimento do fechamento

false

## 🔗 Tipo de Valor

Permite ao usuário escolher qual valor será considerado no cálculo:

🏢 **Valor Liquido:** O sistema irá utilizar o valor líquido do lançamento.

🏬 **Valor Original:** Quando selecionado, o cálculo da despesa financeira irá utilizar o valor original do lançamento financeiro, desconsiderando descontos ou abatimentos, juros e multas ou outros valores de acréscimo.

false

## 📊 Modelo de Cálculo de Rateio

permite indicar o modelo de cálculo que será utilizado no rateio.

### Os tipos de Rateio são:

* [Valor Fixo](https://tdn.totvs.com/pages/viewpage.action?pageId=435105104)
* [Rateio por CRD](https://tdn.totvs.com/pages/viewpage.action?pageId=435105196)
* [Rateio por Fração Ideal](https://tdn.totvs.com/pages/viewpage.action?pageId=435105183)
* [Rateio por M² Construído](https://tdn.totvs.com/pages/viewpage.action?pageId=435105299)
* [Rateio por M² Locado](https://tdn.totvs.com/pages/viewpage.action?pageId=435105202)
* [Rateio Linear por Total de Subunidade do Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105092)
* [Rateio Linear por Total de Subunidade da Unidade](https://tdn.totvs.com/pages/viewpage.action?pageId=435105215)
* [Rateio Linear por Total de Subunidades](https://tdn.totvs.com/pages/viewpage.action?pageId=435105093)
* [Rateio por M² Ocupado](https://tdn.totvs.com/pages/viewpage.action?pageId=435105252)
false

💰 **Lançamentos**

permite o usuário selecionar um ou vários lançamentos do tipo a pagar.

**📋 Tabela de Associação**

Só é exibida quando o campo Associar Por tem selecionado Unidade ou Subunidade. Nesta tabela deve-se incluir as associações desejadas para a geração da despesa.

Quando o campo Associar Por tem selecionado Empreendimento, todas as subunidades do Empreendimento do fechamento serão consideradas, não sendo necessário fazer nenhuma associação explícita.

# ⚙️ Regras

Os lançamentos financeiros associados a uma despesa não poderão ser associados a outras despesas financeiras.

Poderão ser incluídas quantas despesas financeiras quanto forem necessárias, contudo o sistema não permite incluir, alterar ou remover uma despesa quando o seu Fechamento estiver com a situação diferente de "Em preparação".
