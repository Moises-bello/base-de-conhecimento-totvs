---
content_hash: ed1446db5c12f51deaf43553099841fb88176d9fe22e260f72d66460384b8c11
fetched_at: '2026-06-29T00:11:05.442593+00:00'
page_id: '631316664'
product: rm
source: tdn-rm
title: Documentos do Fiador
type: documentation
url: https://tdn.totvs.com/display/LRM/Documentos+do+Fiador
version: 6
---

**Acesse:** Financeiro / Contábil | Contratos | Fiadores | Anexo - Documentos ou Currículo e Oferta | Aluno e Professor | Alunos | Anexo - Fiadores | Anexo - Documentos

Este anexo do , exibe todos os documentos que foram exigidos do fiador. Os  são cadastrados no anexo da . Neste anexo é possível incluir, alterar e visualizar um arquivo digital.

Para cada documento é informado a **situação**do mesmo e caso seja rejeitado um deverá ser informado.

* **Situação do documento:** fornece 4 status para seleção, sendo que estes status irão indicar a entrega efetiva ou não do documento.
  + **Não entregue**: indica que o aluno **não**entregou o documento.
  + **Entregue em validação**: indica que o aluno entregou o documento, mas está em validação pela instituição.
  + **Recusado**: indica que o aluno até entregou o documento, mas foi recusado pela instituição, este status **necessita** informa um **motivo de rejeição**.
  + **Validado**: indica que de fato o aluno entregou o documento.
* **Motivo da rejeição do documento:** obrigatório informar caso o status for **recusado**, para os demais status este campo deverá ser vazio.

Para os status **não entregue**, **entregue em validação** e **recusado** o sistema entenderá que o documento não está válido, portanto não é considerado como entregue, com isso, será cobrado o mesmo. Apenas o status **validado**, que o sistema considera como entrega do documento.

A partir do patch **12.1.29.295** os documentos não poderão ser editados ou excluídos caso estejam com o **status validado** e o fiador esteja **aprovado**.

Não é possível incluir dois documentos iguais para um mesmo fiador.
