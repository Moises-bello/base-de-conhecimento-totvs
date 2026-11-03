---
content_hash: 7016fff0df6e6c5298cbdd142417c20ff95fe885e7e0033e0b12421c5fa71581
fetched_at: '2026-06-29T00:11:04.097314+00:00'
page_id: '625159638'
product: rm
source: tdn-rm
title: Campo Ativo (Filiais)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625159638
version: 1
---

A partir da biblioteca **12.1.29** no formulário de Cadastro de Filiais foi incluído um campo de checagem para validação do status da Filial. Por default ao atualizar o script da base o mesmo será setado como ativo.

**O campo não tem efeitos de desativar a Filial, trata-se de um campo auxiliar meramente informativo.**

Imagem

Para utilizar a implementação basta atualizar a base com o seguinte script:

Código: **LI.2021.06\_06**;

Tipo do campo na base: SMALLINT, sendo 1 para *true* e 0 *false.*
