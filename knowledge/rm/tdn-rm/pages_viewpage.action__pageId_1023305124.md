---
content_hash: 2824e3f4d27d7577087e77b0bbf90f83bf99a7d0d010a0d9044a330e690ffff0
fetched_at: '2026-06-29T00:05:48.130314+00:00'
page_id: '1023305124'
product: rm
source: tdn-rm
title: Reforma Tributária - Empreendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023305124
version: 5
---

## **Cadastro de Empreendimento**

## HELP – Cadastro de Empreendimentos, Subunidades e Banco de Terrenos

Com o objetivo de atender à **legislação vigente** e à **evolução do produto** voltada para a **reforma tributária**, foram incluídos novos campos nos cadastros de **Empreendimentos**, **Subunidades** e **Banco de Terrenos**.  
Esses campos são fundamentais para garantir a **padronização nacional de registros imobiliários** e o **atendimento às exigências legais**.

---

## 🏗️ Novos Campos – Cadastro de Empreendimentos

### **1. Cadastro Imobiliário Brasileiro (CIB)**

Código nacional de identificação do imóvel.  
**Estrutura:** `AAAAAAA-D`

* **A:** caracteres alfanuméricos (7 posições)
* **D:** dígito verificador (1 posição)  
  **Exemplo:** `12AB34C-8`

---

### **2. Código Nacional de Matrícula (CNM)**

Padroniza o número da matrícula do imóvel em formato nacional.  
**Estrutura:** `CCCCCC.L.NNNNNNN-DD`

* **C:** código do cartório (**alfanumérico**, 6 posições)
* **L:** código do livro (**alfanumérico**, 1 posição)
* **N:** número da matrícula (**numérico**, 7 posições)
* **D:** dígitos verificadores (**numéricos**, 2 posições)  
  **Exemplo:** `AB1234.A.0001234-09`

**Importante:**

* O campo deve ser do tipo **string (texto)**, permitindo o uso de letras, números e separadores (`.` e `-`).
* Mesmo que parte da estrutura seja numérica, o armazenamento como texto é necessário para preservar zeros à esquerda e o formato completo.

---

### **3. Cadastro Imobiliário Fiscal (CIF)**

Corresponde à **inscrição municipal do imóvel**, podendo variar conforme o município.  
**Sugestão:** campo texto de até **30 caracteres** para garantir flexibilidade.  
**Exemplo:** `012345678900123456789`

---

### **4. Valor de Referência**

Valor oficial atribuído ao imóvel, **atualizado anualmente** pelo órgão responsável.

---

### **5. Ano do Valor de Referência**

Indica o **ano-base** utilizado para o valor de referência informado.

---

### **6. Localização Georreferenciada**

Campo destinado a armazenar as **coordenadas geográficas** (latitude e longitude) do empreendimento.  
Facilita integrações com mapas e sistemas de geolocalização.

---

## 🗂️ Sugestão de Organização na Tela – Empreendimentos

* Os cinco primeiros campos devem ser incluídos na aba **“Informações”** do cadastro de Empreendimentos.
* O campo **“Localização Georreferenciada”** deve ser posicionado **logo após o endereço**.

### Regra Tributária do Empreendimento

Campo destinado ao armazenamento dos **Parâmetros do Movimento**  relacionados ao empreendimento.

Todas as alterações realizadas neste campo são registradas em **log de auditoria** e o seu conteúdo é considerado nos processos de **atualização em lote também.**

Funcionalidade disponível a partir da versão **12.1.2502** do TOTVS Construção Gestão de Imóveis.

Tipo de Finalidade :

* Comercial
* Residencial
* Misto
