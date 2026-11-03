---
content_hash: c5c807a5b666b91fcecf3659b3d8d02f12c707de27fbc3871f657f817354fcc4
fetched_at: '2026-06-29T00:09:48.420174+00:00'
page_id: '435105148'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Integral - Anexo - Despesa Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105148
version: 7
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

**🧾 Item de cobrança**

indica qual o item de cobrança será associado a despesa financeira;

---

📝 **Descrição**

campo livre onde o usuário poderá descrever a despesa financeira;

---

🏢 **Empreendimento**

campo somente leitura que indica qual é o empreendimento associado ao fechamento;

---

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

## 🔗 Associar Por

Indica o tipo de associação de subunidades que será feita com a despesa financeira para geração da despesa financeira no fechamento.

🏢 **Empreendimento**

Todas as subunidades do empreendimento ligado ao fechamento serão consideradas

🏬 **Unidade**

Todas as subunidades das unidades incluídas serão consideradas. Só é possível incluir unidades do empreendimento do fechamento

🏠 **Subunidade**

Todas as subunidades incluídas serão consideradas. Só é possível incluir subunidades do empreendimento do fechamento

false

💰 **Lançamentos**

permite o usuário selecionar um ou vários lançamentos do tipo a pagar.

**📋 Tabela de Associação**

Só é exibida quando o campo Associar Por tem selecionado Unidade ou Subunidade. Nesta tabela deve-se incluir as associações desejadas para a geração da despesa.

Quando o campo Associar Por tem selecionado Empreendimento, todas as subunidades do Empreendimento do fechamento serão consideradas, não sendo necessário fazer nenhuma associação explícita.

# ⚙️ Regras

Os lançamentos financeiros associados a uma despesa não poderão ser associados a outras despesas financeiras.

Poderão ser incluídas quantas despesas financeiras quanto forem necessárias, contudo o sistema não permite incluir, alterar ou remover uma despesa quando o seu Fechamento estiver com a situação diferente de "Em preparação".
