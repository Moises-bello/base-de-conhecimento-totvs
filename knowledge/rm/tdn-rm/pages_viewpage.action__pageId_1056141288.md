---
content_hash: 85cd448d4c8a7eb36679c31165b39dff7b283fb77df55e563ab1b6d44d0f4ef2
fetched_at: '2026-06-29T00:05:51.881094+00:00'
page_id: '1056141288'
product: rm
source: tdn-rm
title: Geração de Movimento a partir de Baixas Financeiras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056141288
version: 1
---

# 🧾 **Geração de Movimentos a partir de Baixas Financeiras**

### **Reforma Tributária (IBS/CBS)**

---

## 📦 **Produto**

**TOTVS Incorporação**

---

## 🏷️ **Versão**

Funcionalidade disponibilizada a partir da versão **12.1.2502**.

---

## 🎯 **Objetivo**

Atender às exigências da Reforma Tributária, considerando que o **fato gerador da emissão do documento fiscal é o pagamento (baixa financeira)**.

---

⚙️ **Regras de Geração**

* Gerar movimentos apenas para lançamentos **baixados**
* Considerando apenas baixas **sem movimento vinculado**
* Utilizar:
  + Parâmetros do **empreendimento**
  + Dados do **lançamento financeiro**

---

## 📊 **Informações Obrigatórias no Movimento**

* CIB
* Inscrição Imobiliária (CIF)
* Regra Tributária
* Local (Município e Estado)

### 💰 Valores calculados:

* Valor da baixa (nota)
* Base de cálculo
* Alíquotas
* Tributos (IBS e CBS, quando aplicável)

---

## 🏗️ **Empreendimentos com RET**

* Caso o empreendimento esteja enquadrado no **RET (Regime Especial de Tributação)**, os tributos **IBS e CBS não serão destacados no movimento**, uma vez que não são evidenciados na nota fiscal.

  Ainda assim, a **geração do movimento permanece obrigatória**, pois a emissão do documento fiscal deve ocorrer normalmente.

---

## 🧾 **Tipo de Movimento**

➡️ **Pedido de Venda (2.1.x)**

---

# 🚨 **PONTO CRÍTICO – CONFIGURAÇÃO DO MOVIMENTO**

⚠️ ATENÇÃO  
Configuração incorreta do tipo de movimento pode causar:  
  
• Movimentos sem valor  
• Falha na geração dos itens  
• Problemas na emissão fiscal

---

## ⚙️ **Parâmetros obrigatórios**

### 🔹 Etapa 26 – Item | Identificação

* Tipo de Itens
* ❌ NÃO marcar: **Serviços**

👉 Impacto: Itens podem não ser gerados corretamente

---

### 🔹 Etapa 28 – Item | Preços

* Edição de Preço
* ❌ NÃO marcar: **Não Edita**

👉 Impacto: Movimento será gerado **sem valor**

---

### 🔹 Etapa 65 – Fiscal

* Utilizar Tributação dos Itens
* ✅ Deve estar marcado

👉 Impacto: Garante cálculo correto de IBS/CBS

---

## ✅ **Checklist de Validação (Recomendado)**

Antes de rodar o processo:

✔ Tipo de item não é Serviço  
✔ Edição de preço habilitada  
✔ Tributação por item ativa

---

## 🏢 **Observações – CIB**

* Antes da entrega: usar CIB do empreendimento
* Após individualização: usar CIB da subunidade
