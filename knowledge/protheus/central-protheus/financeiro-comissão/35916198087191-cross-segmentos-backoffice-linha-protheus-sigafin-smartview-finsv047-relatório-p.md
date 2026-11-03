---
article_id: 35916198087191
category: Financeiro - Comissão
content_hash: 66e348564c166ec3c9f6226b72698edbdb586706f6893f6b7c30a4f52530dc04
fetched_at: '2026-06-28T22:37:50.852855+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - SmartView - FINSV047
  Relatório Previsão de Comissões, como os registros são ou não demostrados.
type: support-article
updated_at: '2025-10-30T17:16:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35916198087191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-SmartView-FINSV047-Relat%C3%B3rio-Previs%C3%A3o-de-Comiss%C3%B5es-como-os-registros-s%C3%A3o-ou-n%C3%A3o-demostrados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35916160460951) Tempo aproximado para leitura: **00:08:00 min**  
  
**Dúvida**  
Como é demostrado a previsão da comissão no relatório, e quando essa comissão deixa de ser apresentada?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2410

**Solução**  
Conforme documentação oficial da rotina, a comissão **apenas deixará de ser exibida no relatório após o efetivo pagamento**, ou seja, **após a execução da rotina MATA530 (Atualização de Pagamento de Comissão)**.

> “Após efetivação do pagamento da comissão, ou seja, execução da rotina MATA530 - Atualização de Pagamento de Comissão, os registros deixarão de ser exibidos no relatório apenas neste cenário.”

#### **1. Quando o título será apresentado no relatório FINSV047 - Previsão de Comissões?**

Para que o título a receber seja exibido no relatório **FINSV047**, é necessário que:

* O título tenha sido gerado na rotina **FINA040 - Títulos Contas a Receber**;
* O título possua **vendedor com comissão** associada.

  **Observação:**  
  Não é obrigatório que o título gere registros na rotina **MATA490 - Manutenção de Comissão (SE3 -Comissões de Vendas)**. Mesmo sem a geração da comissão, o título será exibido no relatório **FINSV047 - Previsão de Comissões**.

---

#### **2. Quando o título não será mais apresentado no relatório FINSV047?**

O título deixará de ser exibido no relatório **FINSV047** apenas após a efetivação do **pagamento da comissão** ao vendedor, ou seja, após a execução da rotina **MATA530 - Atualização de Pagamento de Comissão**.  
A seguir, os dois cenários possíveis:

##### **A) Comissão 100% na emissão**

1. O título “A” é criado na rotina **FINA040 - Títulos a Receber**, vinculado a um vendedor com comissão 100% na emissão;
2. O título é exibido no relatório **FINSV047 - Previsão de Comissões**;
3. A comissão é gerada automaticamente (conforme **MV\_TPCOMIS = O**) na rotina **MATA490 - Manutenção de Comissão (SE3)**;
4. O título “A” permanece no relatório até que o pagamento da comissão seja processado;
5. Ao executar a rotina **MATA530 - Atualização de Pagamento de Comissão**, é gerado um novo título “B” na rotina **FINA050 - Contas a Pagar**, correspondente ao pagamento da comissão;
6. Após essa execução, o título “A” deixa de ser exibido no **FINSV047 - Previsão de Comissões**.

---

##### **B) Comissão 100% na baixa**

1. O título “A” é criado na rotina **FINA040 - Títulos a Receber**, vinculado a um vendedor com comissão 100% na baixa;
2. O título é exibido no relatório **FINSV047 - Previsão de Comissões**;
3. Ao realizar a baixa do título na rotina **FINA070 - Baixa de Títulos a Receber**, é gerada a comissão (conforme **MV\_TPCOMIS = O**) na rotina **MATA490 - Manutenção de Comissão (SE3)**;
4. O título “A” continua sendo exibido no relatório até o pagamento da comissão;
5. A execução da rotina **MATA530 - Atualização de Pagamento de Comissão** gera um novo título “B” na rotina **FINA050 - Contas a Pagar**;
6. Após essa etapa, o título “A” deixa de ser exibido no **FINSV047 - Previsão de Comissões**.

**Saiba mais:**

[Smart View - Previsão de comissões](https://tdn.totvs.com/pages/releaseview.action?pageId=815586043)
