---
content_hash: 548242de60c5a17dd8c490f2612e03d9baa1f82b846c20d187a2e98b805f9bd2
fetched_at: '2026-06-29T00:09:49.733007+00:00'
page_id: '435105353'
product: rm
source: tdn-rm
title: Contrato de Administração - Processo - Gerar Movimento Administração de Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105353
version: 27
---

## 🔵 Introdução

📘 A geração de movimentos para os contratos de administração é utilizada quando a administradora do imóvel deseja gerar notas fiscais para os valores negociados nos contratos de locação dos imóveis associados.  
O movimento será gerado no módulo TOTVS Gestão de Estoque, Compras e Faturamento, possibilitando o cálculo dos impostos devidos.

📌 Para calcular o valor do movimento, o sistema exige que o lançamento financeiro já tenha sido gerado e que suas datas de vencimento estejam dentro do período informado pelo usuário no momento da execução do processo.  
A forma de cálculo do valor está vinculada ao parâmetro **“Cobrança de imposto sobre o repasse do contrato de administração”**, definido no contrato de administração.

---

## 🟣 Variações de cálculo

### 🔹 Quando o parâmetro estiver definido como Administradora

📊 O sistema irá buscar os **lançamentos em aberto** e do tipo **“a pagar”**.  
Será geradoapenas um movimento, agrupando os valores das parcelas dos respectivos contratos de locação.

false

🔎 **Exemplo**

* Contrato de Locação: Aluguel de R$ 1.000,00
* Contrato de Administração:

  + Taxa de Administração (5%)
  + Taxa de Intermediação (10%)

🧮 **Cálculo**  
Repasse = R$ 1.000,00 − R$ 50,00 (Admin.) − R$ 100,00 (Interm.) = **R$ 850,00**

📄 **Movimento Gerado**  
O movimento de repasse terá o valor de **R$ 850,00**.

---

### 🔹 Quando o parâmetro estiver definido como Proprietário

📂 Os movimentos serão desagrupados, e o cálculo seguirá o modelo de repasse definido no contrato:

* **Condicional**  
  O sistema buscará os lançamentos baixados e do tipo “a receber” dentro do período informado.  
  O valor do item do movimento será a soma dos valores originais baixados das parcelas, considerando descontos, juros e multas, calculados conforme a taxa de repasse cadastrada no contrato de administração.
* **Garantido**  
  O sistema buscará os lançamentos em aberto e do tipo “a receber” dentro do período informado.  
  O valor do item do movimento será a soma dos valores das parcelas.

---

## 🟠 Geração de movimento de taxas

⚙️ Existe a opção de gerar o movimento das taxas do contrato de administração.  
Nessa opção, será gerado um movimento cujo valor corresponde à soma das taxas de Administração e Intermediação cobradas no período selecionado.

false

🔎 **Exemplo (mesmo cenário anterior)**

* Aluguel a Receber: **R$ 1.000,00**
* Taxa de Administração (5%): **R$ 50,00**
* Taxa de Intermediação (10%): **R$ 100,00**

📄 **Movimento de Taxas Gerado**  
Valor total do movimento: **R$ 150,00 (R$ 50,00 + R$ 100,00)**

## 🔴 Pré-condições

✅ O módulo TOTVS Gestão de Estoque, Compras e Faturamento deve estar devidamente parametrizado para geração de movimento;  
✅ Devem estar cadastrados os parâmetros para geração de movimento no menu:  
**TOTVS Incorporação > Aluguel > Cadastros > Cadastros Aluguel > Parâmetro de Movimento Aluguel**

## 🟢 Campos do cadastro de parâmetros de geração do movimento

🆔 **Código**: campo identificador gerado automaticamente pelo cadastro;  
🏷️ **Tipo de geração**: valor padrão **“Administração de Aluguel”**;  
✏️ **Descrição**: campo de livre digitação;  
🔄 **Tipo de movimento**: o sistema filtra apenas **pedidos de venda**, pois a administradora está prestando um serviço ao locador;  
🏢 **Buscar filial**: valor padrão **“Parâmetro”**, não editável, indicando que o campo seguinte deve ser informado;  
💰 **Buscar natureza**: define de onde será buscada a natureza financeira do movimento, com valor padrão **“Parâmetro”**, não editável;  
📊 **Buscar centro de custo**: define de onde será obtido o centro de custo do movimento, com as opções:

* + **Não se aplica**: movimento sem centro de custo;
  + **Imóvel**: centro de custo será o mesmo do imóvel;
  + **Parâmetro**: centro de custo informado manualmente no campo seguinte;

📍 **Centro de custo**: deve ser informado apenas quando o campo anterior estiver com valor **“Parâmetro”**;  
🔀 **Busca rateio centro de custo**: define como será feito o rateio:

* + **Não se aplica**: não realiza rateio;
  + **Imóvel**: rateio entre os imóveis do contrato de administração.

false

## 🔵 Cálculo de rateio do Centro de Custo quando houver mais de um imóvel

Quando um contrato de administração possui mais de um imóvel, o sistema trata o cálculo da seguinte forma:

Se todos os imóveis tiverem o valor original informado:  
O sistema calcula o percentual de rateio com base nesses valores.

### 📌 Exemplo prático:

Contrato de administração com **2 imóveis**:

* *Imóvel A: Centro de Custos 01.01* = **R$ 100.000**
* *Imóvel B: Centro de Custos 02.02* = **R$ 200.000**

**Total dos valores**: R$ 300.000

Cálculo do percentual:

* *Imóvel A - Centro de Custos 01.01:* 100.000 / 300.000 = **33,33%**
* *Imóvel B - Centro de Custos 02.02:* 200.000 / 300.000 = **66,67%**

➡️ O rateio será proporcional ao valor de cada imóvel.

false

## **🔵** Quando algum imóvel não possui valor original informado

Se algum imóvel não tiver o valor original informado:  
O sistema faz o rateio igualitário, dividindo o valor de forma igual entre os imóveis, considerando apenas a quantidade de imóveis.

### 📌 Exemplo prático:

Contrato de administração com **3 imóveis**:

* Imóvel A: valor original = **R$ 100.000**
* Imóvel B: valor original = **não informado**
* Imóvel C: valor original = **R$ 200.000**

Como nem todos os imóveis possuem valor original, o sistema ignora os valores e faz o rateio igualitário.

Cálculo do rateio:

* Quantidade de imóveis: 3
* Percentual para cada imóvel: **33,33%**

➡️ O valor é dividido igualmente entre todos os imóveis.

🏢 **Coligada do movimento**: define em qual coligada o movimento será gerado;  
📦 **Produto**: produto do movimento, que deve estar marcado como **“Serviço”**, permitindo a tributação correta;  
🏬 **Filial**: filial onde o movimento será gerado;  
💼 **Natureza financeira**: natureza financeira do movimento;  
🔒 **Não permitir alterações dos parâmetros default no processo**: quando marcado, impede alterações dos dados durante a geração.

false

## 🧮 Cálculo do Rateio quando possui Beneficiários

Quando existem beneficiários vinculados a um locador em um Contrato de Administração, o cálculo é realizado de forma hierárquica.  
Primeiro é considerado o percentual do locador e, em seguida, os percentuais dos beneficiários são aplicados sobre a parte do locador, e não diretamente sobre o valor total da taxa.

---

### **👥**Exemplo prático:

#### 📄 Participantes do Contrato de Administração

👤 **Locador**  
• Carlos – **100% da Taxa de Administração**

👥 **Beneficiários vinculados ao locador**  
• Maria – **10% sobre o percentual do locador**  
• Pedro – **30% sobre o percentual do locador**

---

### 📐 Regra de Cálculo

📌 O locador Carlos possui 100% da Taxa de Administração.

📌 Os percentuais dos beneficiários são calculados sobre esse valor total do locador, e não diretamente sobre o valor global da taxa.

---

### 💰 Cálculo do Rateio

Supondo que, ao executar a rotina de **geração de movimentos do Contrato de Administração**, o valor total da **Taxa de Administração** (100% do Carlos) seja **R$ 1.500,00**, o sistema realizará os cálculos da seguinte forma:

👩 **Maria** possui **10% sobre os 100% do Carlos**  
➡️ 10% de R$ 1.500,00 = **R$ 150,00**

👨 **Pedro** possui **30% sobre os 100% do Carlos**  
➡️ 30% de R$ 1.500,00 = **R$ 450,00**

👤 **Carlos** permanece com o valor restante após o rateio dos beneficiários:  
➡️ R$ 1.500,00 − (R$ 150,00 + R$ 450,00) = **R$ 900,00**

---

### 📊 Resultado da Geração dos Movimentos

#### 🧾 Movimento para Carlos (Locador)

• Percentual: **100%**  
• Valor líquido após rateio dos beneficiários: **R$ 900,00**

#### 🧾 Movimento para Maria (Beneficiária)

• Percentual: **10% sobre o locador**  
• Valor: **R$ 150,00**

#### 🧾 Movimento para Pedro (Beneficiário)

• Percentual: **30% sobre o locador**  
• Valor: **R$ 450,00**

### 🧩 Comportamento do Sistema

📌 O sistema gerará os movimentos **individualmente** para cada participante do **Contrato de Administração**, permitindo que cada um possua seu **lançamento financeiro** e a respectiva **emissão de nota fiscal**, conforme o rateio definido.

---

## 🔵Execução do processo

📍 O processo está disponível em:  **TOTVS Incorporação > Aluguel > Contrato de Administração > Processos > Gerar Movimento Administração de Aluguel**

🟢 **Campos do processo de geração do movimento**

⚙️ **Parâmetros default do Movimento**: parâmetro previamente cadastrado. Ao selecioná-lo, os campos **Código do movimento, Filial e Centro de custo** são preenchidos automaticamente;  
📅 **Data de emissão**: data de emissão do movimento;  
🚚 **Data de entrega**: data de entrega do movimento;  
📝 **Histórico do movimento**: campo de livre digitação;  
🧾 **Produto/Serviço**: podem ser informados um ou vários produtos, sendo sugerido o produto do parâmetro;  
⏳ **Período de geração**: data inicial e final, considerando os aluguéis com vencimento dentro do período informado.

Após clicar em **Avançar**, será possível selecionar o tipo de movimento:

🏠 **Taxa de administração do imóvel**: gera apenas o movimento das taxas de administração incidentes nos lançamentos de repasse ao locador;

🤝 **Taxa de intermediação do imóvel**: gera apenas o movimento das taxas de intermediação incidentes nos lançamentos de repasse ao locador.

📎 Após a conclusão do processo, o movimento poderá ser visualizado em:  
**TOTVS Incorporação > Aluguel > Contrato de Administração > Anexos > Movimento(s) Gerado(s)**
