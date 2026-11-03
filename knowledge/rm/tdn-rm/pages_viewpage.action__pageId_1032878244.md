---
content_hash: a2b5808a33d60b6ab6151bd36019470d4f8354fac65f481552c7fba0afafd60f
fetched_at: '2026-06-29T00:05:48.888591+00:00'
page_id: '1032878244'
product: rm
source: tdn-rm
title: Contrato de Locação - Anexos - Saldos Retidos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1032878244
version: 5
---

---

## 📘 Introdução

O **Anexo de Saldos Retidos** funciona como um **repositório de pendências financeiras**.  
Ele concentra valores de **taxas e encargos** que já foram identificados pelo sistema como devidos, mas que **ainda não foram totalmente descontados do beneficiário**.

🎯 **Objetivo da funcionalidade**  
Oferecer uma **visão clara, centralizada e confiável** dos valores pendentes, garantindo que nenhuma taxa seja esquecida, independentemente da data em que os lançamentos foram gerados.

---

## 🔐 Procedimentos para Utilização

Para acessar o **Anexo de Saldos Retidos**, é necessário:

1. Conceder permissão ao usuário em:  
   **Serviços Globais → Segurança → Perfis**
2. Acessar o **perfil de usuário** do módulo Gestão de Imóveis
3. Navegar até:  
   **Aluguel → Contrato de Locação → Saldos Retidos**

📌 *Sem a permissão adequada, a funcionalidade não ficará disponível para o usuário.*

---

## 🔄 Taxa de Intermediação em Contratos de Administração

Esta funcionalidade controla o **saldo da Taxa de Intermediação** quando um **Contrato de Locação** está vinculado a um **Contrato de Administração**.

✅ Esse controle é essencial principalmente em contratos **pró-rata**, nos quais o desconto automático da taxa **não ocorreria corretamente** sem a gestão de saldo.

---

## 1️⃣ Como funciona o Saldo de Intermediação?

O sistema cria uma espécie de **“conta corrente” da taxa de intermediação**.

🔁 Funcionamento:

* O valor total da taxa é registrado como **saldo devedor**
* A cada **repasse ou lançamento financeiro**, o sistema:

  + Verifica se há saldo disponível
  + Realiza o desconto automaticamente
* O processo continua até que o saldo seja **totalmente quitado**

---

### 📌 Exemplo Prático

**Configuração do contrato:**

* Valor do Contrato de Locação: **R$ 10.000,00**
* Taxa de Intermediação: **80% do aluguel**
* Recorrência: **2 parcelas**

**Resultado no sistema:**

* 80% de R$ 10.000,00 = **R$ 8.000,00**
* R$ 8.000,00 × 2 ocorrências = **R$ 16.000,00**

💡 Este será o **Saldo Total de Intermediação**, que será abatido gradualmente nos repasses.

---

## 2️⃣ Fluxo de Abatimento (Descontos)

O abatimento ocorre de forma **automática, progressiva e controlada**:

1. **Geração do Lançamento**  
   Sempre que um lançamento financeiro é gerado para o proprietário, o sistema verifica o saldo.
2. **Aplicação do Desconto**  
   O valor da taxa configurada é descontado do repasse.
3. **Atualização do Saldo**  
   O valor descontado é abatido do saldo total.
4. **Conclusão**  
   O processo se repete até que o saldo chegue a **zero**.

---

## 3️⃣ Visualização do Histórico de Descontos

Para garantir **transparência e rastreabilidade**, é possível consultar o histórico detalhado:

🔎 **Como acessar:**

1. Localize o registro do **Saldo de Intermediação** no contrato
2. Dê **duplo clique** sobre o registro

📊 A tela de histórico exibirá:

* Data de cada desconto
* Valor descontado
* Lançamento financeiro de origem

---

## 4️⃣ Taxa de Intermediação com Escalonamento

O sistema passa a considerar **Escalonamentos cadastrados** para o período inicial do contrato.

✔️ Se houver escalonamento ativo:

* A taxa de intermediação será calculada com base no **valor escalonado vigente**
* Garante uma cobrança **mais justa e precisa**, conforme o valor realmente pago pelo locatário

📌 **Importante:**  
Agora é possível cadastrar escalonamentos **antes da efetivação do contrato**, garantindo que o cálculo já seja gerado corretamente desde o início.

---

### 🔄 Fluxo com Escalonamento

1. **Cadastro do Contrato de Locação**  
   O imóvel deve estar vinculado a um Contrato de Administração.
2. **Cadastro do Escalonamento**  
   Utilize quando houver:

   * Carência
   * Desconto nos primeiros meses
3. **Efetivação do Contrato**  
   O sistema:

   * Verifica a data de início da vigência
   * Identifica se existe escalonamento ativo

📌 Resultado:

* **Com escalonamento:** saldo gerado sobre o **valor escalonado**
* **Sem escalonamento:** saldo gerado sobre o **valor integral do aluguel**

---

### 📌 Exemplo Prático

**Cenário com Escalonamento**

* Aluguel integral: **R$ 2.000,00**
* Aluguel escalonado (3 primeiros meses): **R$ 1.500,00**
* Taxa de Intermediação: **100% do primeiro aluguel**

➡️ **Saldo Gerado:** R$ 1.500,00

**Cenário sem Escalonamento**  
➡️ **Saldo Gerado:** R$ 2.000,00

---

## 5️⃣ Estornos, Cancelamentos e Reutilização de Saldo

O sistema possui uma **gestão dinâmica**, garantindo consistência mesmo em cenários de cancelamento.

### 🅰️ Cancelamento de um Lançamento

Se um lançamento que já teve desconto for cancelado:

* O sistema realiza o **estorno automático**
* O valor retorna para o **Saldo de Intermediação**

---

### 🅱️ Geração de Nova Parcela

Ao gerar uma nova parcela após o cancelamento:

* O sistema identifica saldo disponível
* O desconto da taxa é **aplicado novamente**

---

### 🅲 Regra de Precedência (Saldo Exaurido)

Se o saldo já tiver sido totalmente consumido:

* Novos lançamentos **não sofrerão desconto**
* O sistema **nunca cobrará valores excedentes**

---

## 🧾 Resumo Técnico

* 🎯 **Objetivo:** Garantir o recebimento integral da taxa contratada
* 🔁 **Comportamento:**

  + Lançamento ativo → desconto aplicado
  + Lançamento cancelado → desconto retorna ao saldo
* 🚫 **Limite:**

  + O sistema nunca desconta além do saldo total configurado

---

## ❓ Dúvidas Frequentes

Em caso de divergências no saldo:  
👉 Consulte sempre o **Histórico de Movimentação (duplo clique)** para identificar quais parcelas consumiram o saldo da intermediação.

---
