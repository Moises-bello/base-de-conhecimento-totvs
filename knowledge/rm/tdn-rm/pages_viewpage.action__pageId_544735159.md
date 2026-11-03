---
content_hash: bf950ce83d7b3c191c8bec42bb24db6aa63d81cdb816147b476b2a0f7df66a21
fetched_at: '2026-06-29T00:10:38.792533+00:00'
page_id: '544735159'
product: rm
source: tdn-rm
title: Contrato de Locação - Processo - Lançamentos de previsão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544735159
version: 12
---

### **Introdução**

---

Os lançamentos financeiros de previsão permitem o usuário simular as parcelas de aluguel previstas para aquele período.   
Para que o usuário possa acessar a funcionalidade *(para Geração e cancelamento dos lançamentos de Previsão),* devemos inicialmente habilitá-la no perfil de usuário ***Aluguel / Contrato de Locação / Contrato de Locação / Contrato de Locação: Gerar Lançamento Previsão.***

### **Processos**

---

**Processo de Geração Lançamento de Previsão**

* O Lançamento poderá ser gerado para contratos efetivados ou em elaboração;
* As parcelas criadas pelo contrato serão apenas parcelas simuladas, ou seja, não poderão ser baixadas ou alteradas;
* O Lançamento financeiro de previsão será substituído quando o usuário gerar lançamentos financeiros oficiais no mesmo período (diferente de previsão)
* Para que os lançamentos sejam gerados corretamente, o parâmetro de integração Financeira do contrato deverá ter o campo marcado "Utiliza lançamentos futuros como provisão" e associado neste campo um tipo de documento a receber, classificado como "Previsão".
* O documento a pagar cadastrado no parâmetro de lançamentos futuros não é obrigatório, visto que nem sempre o contrato de aluguel possuirá lançamentos de repasse.
* Não serão gerados lançamentos de previsão para uma data a qual já existe lançamentos oficiais já gerados.

**Processo de Cancelar Parcela de Previsão**

* O processo de cancelamento de lançamento de previsão possibilitará cancelar as parcelas de previsão geradas;
