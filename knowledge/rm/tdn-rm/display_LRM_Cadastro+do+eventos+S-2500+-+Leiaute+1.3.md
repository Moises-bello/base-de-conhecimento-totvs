---
content_hash: a384694d289cefde0710c13dfaa0094b89df0dd839e9a16b6bdae5557f76df3d
fetched_at: '2026-06-29T00:12:00.721423+00:00'
page_id: '887737071'
product: rm
source: tdn-rm
title: Cadastro do eventos S-2500 - Leiaute 1.3
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+do+eventos+S-2500+-+Leiaute+1.3
version: 1
---

Evento S-2500 - Leiaute 1.2NovidadesO que está diferente?

* **Criação dos campos {dtAdmRespDir} e {matRespDir} no grupo {ideResp}**

 

Importante

* + A validação “igual ou anterior ao ano do óbito, se existente” será realizada pelo Governo, a tela realiza a validação somente entre os campos exibidos.
  + A validação “Se informado, deve corresponder a uma matrícula informada pelo empregador de origem (responsável direto) no evento S-2190, S-2200 ou S-2300, pertencente ao trabalhador preenchido em cpfTrab, no empregador informado em ideResp/nrInsc”  será realizada pelo Governo, a tela realiza a validação somente entre os campos exibidos.

* **Alteração da validação do campo {codCateg} do grupo {mudCategAtiv}**

Importante

* + A validação “indContr = S” será realizada pelo Governo, a tela realiza a validação somente entre os campos exibidos.

* **Alteração na lista de opções do campo {indReperc} do grupo {infoVlr}**

* **Criação do grupo {infoInterm} que pertence ao grupo {idePeriodo}**

* + **Descrição do grupo {infoInterm}:** Informações relativas ao trabalho intermitente.
  + **Ocorrência do grupo {infoInterm}:** 0-31.
  + **Chave do grupo {infoInterm}:** dia
  + **Condição do grupo {infoInterm}:** O ((se infoContr/indContr = [N] e infoContr/codCateg = [111]) ou (se infoContr/indContr = [S] e o código de categoria no RET for igual a [111])); N (nos demais casos).

Importante

* + A condição “código de categoria no RET for igual a [111]” será realizada pelo Governo, a tela realiza a validação somente entre os campos exibidos.

A validação “Preenchimento obrigatório e exclusivo se classTrib em S-1000 = [22]” será realizada pelo Governo, a tela realiza a validação somente entre os campos exibidos.

* **Alteração na validação do grupo {infoDeslig}**
