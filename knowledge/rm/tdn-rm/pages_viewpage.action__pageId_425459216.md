---
content_hash: c1e5b520636299b5e883d2642b51de92459f610be8d1ebf8382c8f27d375b2d1
fetched_at: '2026-06-29T00:09:34.663477+00:00'
page_id: '425459216'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Condição de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459216
version: 5
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Condição de Pagamento**

---

As inclusões, alterações e exclusões de Condições de Pagamento são feitas através do Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT. Através da sincronia de dados o Protheus pode utlizar as condições de pagamento enviadas em seus processos de Manutenção de Ativos.  
   
O sistema protheus interpreta a mensagem de acordo com os  dados enviados, classificando a condição de pagamento como tipo 1, 5 ou 6.

Os dados sincronizados pela mensagem única são:

**Aba Identificação :**

* Codigo
* Descrição
* Carencia por Dias da Semana

**Aba Composição de Parcelas :**

* % do Valor Total
* Número de Vezes
* Prazo
* intervalo
* Tipo

**Anexos / Dias de Carência :**

* Dia de Carência

**Observações:**

1. Alguns  Campos da condição de pagamento  possuem as regras abaixo :

* % do valor total: Se for informado o % de Valor Total de mais de uma linha simultaneamente , o sistema efetua a soma do % de todas as linhas. O valor  de uma das linhas   ou  a soma de  diversas linhas,  deve ser  igual a 100
* Tipo: Campo enviado somente quando houver mais de uma linha de composição de parcelas informado.A quantidade de dias para vencimento da parcela será calculado para cada composição de parcela, considerando os campos "Prazo" e "Intervalo".
* Intervalo: Enviado somente para Composição de parcelas que tenha apenas uma linha preenchida .
* Prazo: O campo Prazo  aceita somente os valores  quando a integração  está ativada: 0,1 , 7 , 10 , 15 , 30.
* O campo Prazo é enviado ao sistema Protheus somente quando mais de uma composição de parcelas for preenchido. A quantidade de dias para vencimento da parcela será calculado para cada composição de parcela, considerando os campos "Prazo" e "Intervalo".

2. Devido a algumas restrições do sitema Protheus, os tipos de condição de pagamento aceitos  por ele devem ser preenchido conforme  abaixo especificado:

* **Condição t1 - O sistema Protheus considera como tipo 1 quando:**  
  + Preencher **mais de uma** linha da composição de parcelas.
  + O dia fixo da semana, na aba Identificação, não estiver selecionado.
* **Condição  t5 -O sistema Protheus considera como tipo 1 quando:**  
  + Preencher **apenas uma** linha da composição de parcelas.
  + O dia fixo da semana, na aba Identificação, não estiver selecionado.
* **Condição t6 - O sistema Protheus considera como tipo 1 quando:**  
  + Preencher **apenas uma** linha da composição de parcelas.
  + Selecionar um dia da semana na aba identificação.

 3. Caso o "Código da Condição de Pagamento" no RM seja maior que 3 caracteres, o código da condição de pagamento no Protheus deve ser configurado como autoincremento.

---

Para mais detalhes sobre  o cadastro , acese o Boletim Técnico.

**Recursos Adicionais**

TDN - Boletim Técnico : [Condição de Pagamento](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+CONDI%c3%87%c3%83O+DE+PAGAMENTO_BR_CON000158.pdf?version=1&modificationDate=1380044682000)
