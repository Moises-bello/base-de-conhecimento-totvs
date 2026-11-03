---
content_hash: 83dd5b85a4f538ac623ec6e2605a5701984536bb29478b892944d73a090913f3
fetched_at: '2026-06-29T00:05:52.389137+00:00'
page_id: '1058445119'
product: rm
source: tdn-rm
title: Configurações Obrigatórias para Geração do Valor Tributário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058445119
version: 2
---

# 📘 **Geração do Valor Tributário – Configurações Obrigatórias**

Para que o sistema calcule corretamente os valores tributários no módulo de Incorporação do **TOTVS Construção e Gestão de Imóveis**, é indispensável que algumas parametrizações estejam corretamente configuradas.

⚠️ **Importante:**  
A ausência ou configuração incorreta de qualquer um dos itens abaixo impedirá a geração dos valores tributários.

---

## ✅ **1. Cadastro do Componente**

📍 *Caminho: Contratos > Plano > Componentes*

O componente utilizado no contrato **NÃO pode estar com a opção marcada:**

❌ **Desconsiderar Valor Base IVA**

✔️ Caso essa opção esteja marcada, o sistema **ignora a base de cálculo tributária**, impossibilitando a geração do valor.

---

## ✅ **2. Regra Tributária**

📍 *Caminho: Contratos > Regras Tributárias*

* Deve existir uma **Regra Tributária cadastrada**
* Dentro dessa regra, é obrigatório possuir:

✔️ **Parâmetros Tributários configurados**

✔️ Sem esses parâmetros, o sistema não terá base para aplicar os cálculos fiscais.

---

## ✅ **3. Cadastro do Empreendimento**

O empreendimento precisa estar devidamente parametrizado:

### **3.1 Identificação**

* Informar a **URL Geográfica**

---

### **3.2 Aba EFD-PIS/COFINS**

* ❌ **NÃO marcar** a opção:

**Usar RET (Regime Especial de Tributação)**

✔️ O empreendimento **não pode estar enquadrado no RET** para este cenário de cálculo.

---

### **3.3 Aba Reforma Tributária**

Deve estar:

✔️ Parametrizada  
✔️ Com **Regra Tributária vinculada**

---

### **3.4 Finalidade do Empreendimento**

📍 *Identificação*

O empreendimento e suas subunidades devem estar com:

✔️ **Tipo de Finalidade = Residencial**

---

## ✅ **4. Cadastro da Subunidade**

📍 *Cadastro da Subunidade*

Deve estar configurado:

✔️ **Fração Ideal preenchida**  
✔️ **Valor Fracionado habilitado**

---

## 📊 **Exemplo Prático – Fração Ideal**

Considere o seguinte cenário:

* Empreendimento com:
  + 1 bloco
  + 10 unidades
  + Valor total: **R$ 1.000.000,00**

### 📌 **Fração ideal por unidade**

Cada unidade representa:

* **1 ÷ 10 = 0,10 (10%)**

---

## 🧮 **Cálculo do Valor por Fração**

**Fórmula:**

Valor da Unidade = Valor Total × Fração Ideal

**Aplicando no exemplo:**

* Valor total: R$ 1.000.000,00
* Fração ideal: 0,10

**Cálculo:**

Valor da unidade = 1.000.000 × 0,10  
✔️ **Valor da unidade = R$ 100.000,00**

---

## 💰 **Reflexo no Cálculo Tributário**

O sistema utilizará esse valor proporcional como base para cálculo dos tributos.

✔️ Ou seja:  
Cada unidade terá seu imposto calculado **com base na sua fração ideal dentro do empreendimento**

---

## 🚨 **Principais Problemas (Erros Comuns)**

Se o valor tributário não for gerado, verifique:

* ❌ Componente com *Desconsiderar Valor Base IVA* marcado
* ❌ Falta de Regra Tributária
* ❌ Empreendimento com RET ativo
* ❌ Fração ideal não preenchida
* ❌ Regra não vinculada na aba de Reforma Tributária

---

## 🎯 **Resumo Final**

Para que o cálculo tributário funcione corretamente:

✔️ Componentes válidos  
✔️ Regra tributária completa  
✔️ Empreendimento parametrizado corretamente  
✔️ Subunidades com fração ideal definida
