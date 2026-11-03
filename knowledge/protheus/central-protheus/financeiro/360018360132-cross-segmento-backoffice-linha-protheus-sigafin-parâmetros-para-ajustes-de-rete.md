---
article_id: 360018360132
category: Financeiro
content_hash: a082bd35af0ab4a02ec92ae6dd74eea2aa1992f5082cb2979c16c470e958b23b
fetched_at: '2026-06-28T22:38:00.854931+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Parâmetros para ajustes
  de Retenção de IRRF Pessoa Física no Módulo (06) FINANCEIRO
type: support-article
updated_at: '2026-02-27T13:25:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018360132-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Par%C3%A2metros-para-ajustes-de-Reten%C3%A7%C3%A3o-de-IRRF-Pessoa-F%C3%ADsica-no-M%C3%B3dulo-06-FINANCEIRO
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21674216918679)***Tempo aproximado para leitura: **00:08 min**

**Dúvida**  
Quais parâmetros é preciso configurar para o imposto **IRRF** Pessoa Físi**ca?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro -  A partir da versão 11.80  
  
**Solução**  
**Configuração do Imposto IRRF:**

### 

### **1. Natureza**

* **Campos principais:**

  + **Calcula IRRF?** → ED\_CALCIRF
  + **Percentual de cálculo de IRRF** → ED\_PERCIRF
* **Vinculação:** Associar a **Natureza** ao **cadastro de Cliente/Fornecedor**.

**Campo Cod.Dd.At. (ED\_RECIRRF):**  
Define quem será responsável pelo recolhimento do IRRF:

1. **Cliente (SIM)**
2. **Emitente do Documento (NÃO)**
3. **Conforme Cadastro do Cliente (Cad.Cliente)**

---

### 

### **2. Cliente**

* **Vincular natureza:** Campo A1\_NATUREZ
* **Informar alíquota:** Campo A1\_ALIQIRF
* **Recolhe IRRF (A1\_RECIRRF):** *Sim*
* **Modo de abatimento do imposto (A1\_ABATIMP):** calculado pelo sistema.
* **IRPJ Baixa (A1\_IRBAX):**  
  Define se a retenção do IRPJ para clientes pessoas jurídicas (empresas públicas ou mistas) ocorrerá na baixa:

  + **Sim:** retenção na baixa.
  + **Não:** retenção na emissão.

---

### 

### **3. Fornecedor**

* **Vincular natureza:** Campo *A2\_NATUREZ*
* **Cálc. IRRF:** Neste caso deverá selecionar a opção desejada:

**1 - Normal** (geração na emissão do título)

**2 - Baixa** (geração na baixa do título)

---

### 

### **4. Produtos**

* **Calcula IRRF (B1\_IRRF):** *Sim*
* **Redução de IRRF (B1\_REDIRRF):** Preencher caso haja redução aplicável.

---

### 

### **5. Parâmetros**

| **Parâmetro** | **Descrição** |
| --- | --- |
| **MV\_ALIQIRF** | Define a alíquota de IRRF para títulos com retenção na fonte (percentuais conforme tabela legal). |
| **MV\_VLRETIR** | Valor mínimo para dispensa de retenção de IRRF. |
| **MV\_IMPADT** | Define se haverá geração de IRRF em adiantamentos a pagar. |
| **MV\_NATNDF** | Natureza do título NDF gerado via apuração de IRRF (*“NDF”*). |
| **MV\_PRZIRRF** | Número de dias para pagamento do IRRF após a emissão do título. |
| **MV\_VENCIRF** | Define se o título de IRRF será gerado com base na data de **(E)** Emissão, **(V)** Vencimento ou **(C)** Contabilização. |
| **MV\_IRF** | Natureza utilizada para o Imposto de Renda. |
| **MV\_RATIRRF** | Indica se o valor do IRRF será rateado entre os títulos a pagar de uma nota fiscal (**T** = Rateia / **F** = Não rateia). |
| **MV\_RNDIRF** | Critério de arredondamento do IRRF (**.T.** arredonda / **.F.** trunca). |
| **MV\_AGLIMPJ** | Define a forma de verificação da base de IRRF: 1 = Apenas Filial Corrente (default); 2 = Todas as Filiais por CNPJ; 3 = Todas as Filiais por raiz do CNPJ (8 dígitos). |
| **MV\_IRMP232** | Define se a empresa terá IRRF retido conforme MP 232 (1 = Sim / 2 = Não). |
| **MV\_VCTIRPF** | Define a data de geração do título de IRRF (Pessoa Física): **E** = Emissão, **V** = Vencimento, **C** = Contabilização. |
| **MV\_ACMIRPF** | Define se a cumulatividade dos valores de IR-PF considerará a data de **Emissão (1)** ou **Vencimento Real (2)**. |
| **MV\_ACMIRPJ** | Define se a cumulatividade dos valores de IR-PJ considerará a data de **Emissão (1)**, **Vencimento Real (2)** ou **Contabilização (3)**. |

> **Observação:**  
>   
> Para fornecedores **pessoa física**, o sistema utiliza os dados da tabela **IRRF (CFX011)** do **Configurador**. Não há relação direta com o **TES**.

---

### 

### **6. Cumulatividade**

| **Parâmetro** | **Descrição** | **Valores possíveis** |
| --- | --- | --- |
| **MV\_ACMIRCR** | Define se acumula o valor mínimo do IRRF – **Contas a Receber** | 1 = Acumula (Default); 2 = Não acumula |
| **MV\_ACMIRRF** | Define se acumula o valor mínimo do IRRF – **Contas a Pagar** | 1 = Acumula (Default); 2 = Não acumula |

> **Importante:**  
> O acúmulo é diário — se o valor mínimo não for atingido no mesmo dia, não será transferido para o dia seguinte.
>
> **Saiba mais:**
>
> [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - IR Simplificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17448867907351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-IR-Simplificado#:~:text=Trata%2Dse%20da%20Dedu%C3%A7%C3%A3o%20Simplificada,baseado%20na%20tabela%20de%202024)
