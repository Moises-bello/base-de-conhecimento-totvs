---
article_id: 28113459370903
category: Financeiro - Conciliador Backoffice
content_hash: 121dc9f1fef29af40629d18a0f8a1b59b99aab7799ea7f99eb93083872209892
fetched_at: '2026-06-28T22:37:47.093933+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Conciliação Manual
  no novo Conciliador Backoffice
type: support-article
updated_at: '2026-02-18T16:17:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28113459370903-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Concilia%C3%A7%C3%A3o-Manual-no-novo-Conciliador-Backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28113459339799) Tempo aproximado para leitura: **00****:10:00 min**

**Dúvida:**  
Como realizar a conciliação Manual no novo Conciliador Backoffice?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução:**

As configurações disponíveis para seleção neste campo são importadas por meio do WIZARD de Configuração Inicial.

Para efetuar a conciliação manual dos movimentos bancários no sistema, o usuário deve selecionar o menu de configuração **0024 - Conciliação Manual** no Conciliador Backoffice:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35043185690903)

Em seguida, clique em "Ver Filtros", o que abrirá os campos para preenchimento do filtro.

⚠️ **Atenção:**  
A conciliação manual **(setup 0024) apresenta somente os filtros a partir da FK5,** não exibindo mais o filtro SIG desde a atualização contínua de fevereiro de 2025.

O campo **Exibir** pode ser preenchido com as seguintes opções: **Ambos**, **Conciliados** ou **Não conciliados**. Nessa tela, é **obrigatório** preencher os campos **"Data Mov. Ex** de" e **"Data Dispon. de" e informações bancárias**. Após o preenchimento, clique em **Aplicar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35043155101975)

A rotina será aberta em **Dados da Conciliação**, porém, clique em **Dados Não Encontrados**. Nessa tela, será possível validar os movimentos bancários, selecione os registros, clique em Ações, depois em conciliar.

![gif 1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/35043185693719)

Esta ação mantém os dados em **tabelas temporárias**, até que o registro seja efetivado por meio do botão **"Aplicar Conciliação"** na aba *Dados Conciliados*.  
Somente após a efetivação um registro será gerado na tabela **Movimentos Extrato (SIG)**, alimentando as tabelas de origem (**E5\_RECONC** e **FK5\_DTCONC**). Nesse momento, os movimentos passam a ficar disponíveis de forma definitiva na aba *Dados da Conciliação*.

⚠️ **Importante:** enquanto a efetivação não for concluída, caso o sistema seja encerrado ou os filtros sejam atualizados, os registros armazenados nas tabelas temporárias serão descartados e voltarão a ser exibidos na aba *Dados Não Encontrados*.

![gif 2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/35043185694615)

Para cancelar a conciliação, basta clicar nos três pontos e selecionar a opção **Cancelar Match**.

![gif 3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/35043155107607)

Para visualização de saldos há possibilidade de visualização do extrato clicando no botão "**Saldos Bancários**", onde é possível visualizar o **saldo anterior (bancário e conciliado)**, as **entradas e saídas**, além do **saldo atual (bancário e conciliado)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35043185696919)

**Saiba mais**

[Conciliador BackOffice - Conciliação Bancária Manual](https://tdn.totvs.com.br/pages/releaseview.action?pageId=754621064)
