---
article_id: 37559494551319
category: Financeiro - Recalculo
content_hash: 44a0900ff8f84a81f5ededfabbc7ee619c05da7b2027b7e56be6e4609b22587a
fetched_at: '2026-06-28T22:37:27.635645+00:00'
product: protheus
section_id: 35058632967831
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA410 - Como recalcular saldo
  cliente e fornecedor?
type: support-article
updated_at: '2026-02-04T14:29:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37559494551319-Cross-Segmento-Backoffice-Linha-Protheus-FINA410-Como-recalcular-saldo-cliente-e-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37559469551511) Tempo aproximado para leitura: **00:15 min**  
  
**Dúvida**  
Como recalcular saldo cliente e fornecedor e quais campos são atualizados?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA410 - Todas as versões  
  
**Solução**  
Antes de realizar a instalação do pacote de **Stored Procedures**, é imprescindível verificar se o **ambiente encontra-se devidamente atualizado**, bem como assegurar que as **procedures também estejam na versão mais recente**, efetuando sua atualização quando necessário.

Processo para atualizar as procedores no link a seguir:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como atualizar as procedures](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018325612-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-atualizar-as-procedures)

---

### Descrição da Rotina FINA410

A rotina **FINA410** é responsável por **atualizar os arquivos de Clientes e Fornecedores**, recalculando, quando necessário, seus **acumulados financeiros**. Essa rotina deve ser utilizada para **verificação e correção de inconsistências nos dados financeiros**, com base nas movimentações dos módulos de **Faturamento, Compras e Financeiro**.

---

### Dados Avaliados e Recalculados

A rotina avalia, recalcula e ajusta os seguintes dados:

* Saldo financeiro e saldo de duplicatas de **Clientes e Fornecedores em moeda corrente**.
* Saldo financeiro e saldo de duplicatas de **Clientes e Fornecedores em moeda forte**.
* Informações relacionadas a **pagamentos realizados** e **eventuais atrasos de clientes**.

---

### **Campos Atualizados - Cadastro Cliente - SA1**

* **A1\_SALDUP** – Saldo de duplicatas do cliente
* **A1\_SALDUPM** – Saldo de duplicatas do cliente em moeda forte
* **A1\_SALFIN** – Saldo de duplicatas no limite de crédito secundário
* **A1\_SALFINM** – Saldo de duplicatas no limite de crédito secundário em moeda forte
* **A1\_VACUM** – Valor acumulado de vendas no ano

**Quando habilitado o recálculo de dados históricos (mv\_par02 == 1), também serão atualizados:**

* **A1\_METR** – Média de atrasos do cliente
* **A1\_MAIDUPL** – Valor da maior duplicata
* **A1\_ATR** – Valor total dos atrasos
* **A1\_MATR** – Maior atraso do cliente
* **A1\_PAGATR** – Pagamentos realizados com atraso  
  *(Valor controlado historicamente na moeda corrente da localização. Na localização BRA, os valores são expressos em Reais.)*
* **A1\_NROPAG** – Número de pagamentos do cliente
* **A1\_ULTCOM** – Data da última compra
* **A1\_MCOMPRA** – Maior compra do cliente
* **A1\_MSALDO** – Maior saldo devedor do cliente
* **A1\_NROCOM** – Número de compras do cliente

**Observação**  
O campo **A1\_MSALDO** armazena o **maior saldo devedor histórico** do cliente. Dessa forma, o valor somente será sobrescrito caso a rotina apure um saldo superior ao já registrado.

---

#### **Campos Atualizados - Cadastro Fornecedor - SA2**

* **A2\_SALDUP** – Saldo de duplicatas
* **A2\_SALDUPM** – Saldo em moeda forte
* **A2\_MCOMPRA** – Maior compra em valor
* **A2\_MNOTA** – Maior nota do fornecedor *(quando o campo existir na base)*

**Quando habilitado o recálculo de dados históricos (mv\_par02 == 1), também serão atualizados:**

* **A2\_NROCOM** – Número total de compras
* **A2\_MSALDO** – Maior saldo credor

---

### Procedimento para Atualização de Dados

Para realizar a atualização dos dados de **Clientes e/ou Fornecedores**, siga os passos abaixo:

1. Acesse a janela de manutenção **Refaz Dados Clientes/Fornecedores**.  
   Clique em Perguntas

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37560026925719)
2. Preencher as informações dos parâmetros conforme necessário.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37560026928663)
3. Depois selecione **informações** e clique em **Executar**

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37560026930455)
4. Ao confirmar a execução, o sistema processará as informações com base nas movimentações dos módulos de **Faturamento, Compras e Financeiro**, realizando os ajustes necessários.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37560001509143)

**Saiba mais**

[Cross Segmento - Backoffice Linha Protheus - FINA410 - Recalculo e preenchimento dos campos A1\_MSALDO, A1\_MCOMPRA e A1\_MAIDUPL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062989353-Cross-Segmento-Backoffice-Linha-Protheus-FINA410-Recalculo-e-preenchimento-dos-campos-A1-MSALDO-A1-MCOMPRA-e-A1-MAIDUPL)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como atualizar as procedures](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018325612-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-atualizar-as-procedures)
