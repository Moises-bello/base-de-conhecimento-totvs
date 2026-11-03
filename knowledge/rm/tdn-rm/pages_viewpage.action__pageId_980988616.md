---
content_hash: 43958e00a6bc2d95fe76936e5a11c29d1ebda531a4418f97aa7ff058a3ef78e9
fetched_at: '2026-06-29T00:12:15.531712+00:00'
page_id: '980988616'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Processo - Calcular Rateio de Vacância
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=980988616
version: 5
---

## **Introdução**

O processo de **calcular o rateio de vacância** deve ser utilizado para consolidar os valores de rateio quando o condomínio adota uma das seguintes opções de vacância:

* **Rateio entre lojistas**
* **Rateio por percentual de ocupação**

Para entender como realizar previamente estes cadastros, [consulte a documentação (clique aqui)](https://tdn.totvs.com/pages/viewpage.action?pageId=680244548)

Este processo **não deve ser confundido com a geração de lançamentos para sócios**. Ele é exclusivo para os dois cenários acima.

---

## **Quando Utilizar**

O cálculo de rateio de vacância deve ser realizado preferencialmente, **após a existência de operações calculadas** e somente quando configurada uma das opções no menu Vacância do Empreendimento:

* Rateio entre Lojistas
* Rateio por Percentual de Ocupação

Se o cálculo de vacância for feito **antes da completa apuração de todas as cobranças das subunidades, posso ter valores ainda em processamento que não serão rateados.**  
Isso pode gerar distorções no resultado final da competência.

É de fundamental importância que o cálculo de rateio de vacância seja executado por último em determinado fechamento. Isto é, após as cobranças das subunidades forem apuradas.

#### **Exemplo Prático**

* Cobrança calculada até o momento na competência: **R$ 1.000,00 (Cobrança Direta)**
* Vacância calculada até o momento na competência: **R$ 200,00 (Pro-Rata Cobrança Direta)**
* Cobrança ainda não apurada: **??? (Consumos)**
* Vacância ainda não apurada**: ??? (Consumos)**

**No exemplo acima, se calculo o meu rateio de vacância, sem concluir o processamento dos meus consumos, posso ter valores divergentes que serão distribuídos entre os lojistas, visto que o sistema ainda não possui o cálculo processado.**

---

## **Funcionalidades do Processo**

O cálculo de rateio de vacância possui três opções principais.

Lembrando que para acessar o menu Processos / Calcular Rateio de Vacância, deve ser dada permissão no perfil do usuário. (*Condomínio / Fechamento do Condomínio / Fechamento Individualizado / Calcular Rateio de Vacância*)

Ao acessar o processo,

### **Gerar cálculo**

* Realiza o cálculo da vacância na data de referência.
* Gera **uma nova linha de “Cálculo de Rateio de Vacância”** para todas as subunidades incluídas.
* Um **log do processo** indica quando e por quem o cálculo foi executado

### **Remover cálculos**

* Exclui os cálculos de vacância de todas as subunidades envolvidas.
* Utilizado quando o cálculo precisa ser completamente removido.

### **Reprocessar cálculos (sobrescreve o atual)**

* Permite recalcular a vacância caso existam **novos processamentos** que tenham gerado valores adicionais, ou existam parametrizações diferentes.
* Atualiza os valores de vacãncia de acordo com as novas informações apuradas.

---

## **Boas Práticas**

* Sempre **executar o cálculo no fim do fechamento** para garantir consistência nos valores.
* Verificar os logs do processo para assegurar rastreabilidade.
* Reprocessar sempre quando houver novas apurações que impactem os valores de vacância.

---
