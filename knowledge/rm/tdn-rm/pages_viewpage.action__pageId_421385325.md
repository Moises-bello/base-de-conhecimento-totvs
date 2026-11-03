---
content_hash: 3070fd51d43041a1656d477682821b7a1674f402db93155854f15b2bb77144f2
fetched_at: '2026-06-29T00:09:14.981748+00:00'
page_id: '421385325'
product: rm
source: tdn-rm
title: Desfazer Conciliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385325
version: 4
---

---

O processo Desfazer Conciliação deve ser utilizado se uma conciliação for efetuada considerando dois apontamentos (dos coletores) errados. Ele desfaz a conciliação, altera o status dos apontamentos originais para "Pendente" e exclui os registros de apontamentos conciliados.

**Observação:**

Esta opção somente poderá ser realizada caso o apontamento conciliado ainda não tenha sido apropriado.

Este processo é disparado sem a necessidade de uma interface específica em que o usuário precise informar algum dado em particular.

O usuário acessa o menu Cadastros | Mobilidade | Ciclos de transporte | Anexos | Apontamentos Conciliados, seleciona o conjunto de registros que deseja efetuar o cancelamento da conciliação e executa o processo Desfazer Conciliação.

O sistema valida se algum dos registros está com o status diferente de "Pendente" ou "Validado" e, em caso afirmativo, o processo executará normalmente e será incluída mensagem no final do processo informando que a conciliação não foi realizada para tais registros.

Caso negativo, o sistema realiza o processo, altera o status dos registros originais (em Apontamentos dos Coletores) para "Pendente" e exclui o registro de Apontamentos Conciliados.

O processo poderá ser executado para vários registros simultaneamente.
