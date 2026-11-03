---
content_hash: 4c51965210b2ff143b6fd375f2b6415a7a68194609ee0dbc49c19ca1d77de414
fetched_at: '2026-06-29T00:08:49.554573+00:00'
page_id: '331842429'
product: rm
source: tdn-rm
title: 1891343 RMSAU-2060 DT Mensagem em branco ao validar AIH
type: documentation
url: https://tdn.totvs.com/display/LRM/1891343+RMSAU-2060+DT+Mensagem+em+branco+ao+validar+AIH
version: 1
---

# Mensagem em branco ao validar AIH

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Elaboração de AIH |
| **Situação/Requisito:** | Ao efetuar a validação da uma aih com um paciente onde não tem data de nascimento no cadastro desse, o sistema informa uma linha em branco nas mensagens de validação. |
| **Solução/Implementação:** | Alterado o sistema e adicionado a mensagem "Data de nascimento não informado(a)" quando o campo não for informado no cadastro do paciente. |
