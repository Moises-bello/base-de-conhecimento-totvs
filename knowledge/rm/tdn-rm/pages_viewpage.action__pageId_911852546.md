---
content_hash: 7003c473252e1ae6ef79eacd00e400d968f55cf559ca57e09cfca7e19a8c3228
fetched_at: '2026-06-29T00:12:03.561320+00:00'
page_id: '911852546'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Processo - Excluir Cálculos do Fechamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911852546
version: 7
---

---

# Excluir Cálculos do Fechamento

## 📌 Visão Geral

A funcionalidade **Excluir Cálculos do Fechamento** é utilizada quando o **fechamento de condomínio foi gerado de forma individualizada**, ou seja, quando **nem todas as apurações** foram realizadas para um determinado processo ou cálculo.

Nesses casos, a exclusão **não segue exatamente o mesmo comportamento da exclusão integral**, exigindo regras e validações específicas.

---

## 🎯 Quando utilizar

Utilize esta funcionalidade quando for necessário:

* Reverter **cálculos específicos** de um fechamento individualizado
* Ajustar apurações antes de uma nova geração
* Corrigir cálculos de **vacância** ou **taxas** já apurados

---

## ▶️ Como executar a exclusão

1. Acesse o **cadastro de Fechamento Individualizado**
2. Selecione **um ou mais registros de fechamento**
3. Execute o processo **“Excluir Cálculos do Fechamento”**
4. Selecione **quais cálculos deseja excluir**
5. Clique em **Avançar** para concluir o processo

📌 *Disponível a partir da versão **12.1.2602***

---

## ⚙️ Regras da Exclusão em Lote

* É permitida a seleção de **vários condomínios**, desde que todos sejam da **mesma competência**
* Caso sejam selecionados condomínios de **competências diferentes**, o sistema:

  + Exibirá uma **mensagem de alerta**
  + **Bloqueará a execução** do processo
* Antes da exclusão, será exibida uma **tela de confirmação**, contendo:

  + Lista de todos os condomínios selecionados
  + Dados para conferência e validação pelo usuário

---

## 🔄 Processamento da Exclusão

* A exclusão é realizada **em lote**, processando cada condomínio de forma **sequencial**
* Durante a execução, o sistema exibirá o **status por condomínio**:

  + Em processamento
  + Concluído com sucesso
  + Concluído com erro
* Ao final, será apresentado um **resumo do processamento**, com o resultado da exclusão por condomínio

📌 Os cálculos excluídos seguem as **mesmas regras aplicadas na exclusão individual**.

---

## 📊 Registros Apresentados para Exclusão

Ao iniciar o processo:

* Serão exibidos **todos os registros com Status = “Calculado”**, independentemente do processo que os originou
* O sistema indicará se o cálculo selecionado refere-se a:

  + **Vacância**
  + **Taxa**

O usuário pode selecionar **um ou mais cálculos** para exclusão em um único processamento.

---

## 🔁 Resultado da Exclusão

Após a conclusão:

* Todos os registros selecionados retornam para o status **“Em Preparação”**
* Os cálculos poderão ser **reprocessados em uma nova apuração individual**

---

## ⚠️ Atenção — Apurações Subsidiadas

Se uma apuração estiver **subsidiada**, isso significa que ela já está **integrada a lançamentos financeiros**.

Nessa situação, ao tentar excluir o cálculo, o sistema exibirá a seguinte mensagem:

> *Não é possível excluir o cálculo de fechamento, pois as apurações listadas estão integradas ao módulo financeiro e foram subsidiadas. Para prosseguir com a exclusão, será necessário cancelar a geração do processo financeiro.  
> Tipo de Imóvel: [xxxx]  
> Unidade: [xxxx]  
> Processo: [xxxxx].*

### ✔️ Como proceder

1. Cancelar os **Lançamentos Financeiros**
2. Retornar ao fechamento
3. Executar novamente o processo **Excluir Cálculos do Fechamento**

---

## 🔎 Veja também

---

* Calcular Fechamento
* Fechamento do Condomínio
* Histórico de Cálculo
