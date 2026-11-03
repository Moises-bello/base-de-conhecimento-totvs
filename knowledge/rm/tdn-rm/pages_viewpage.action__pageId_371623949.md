---
content_hash: 63bb800685726c679e72791f82ec35e68590081fce3485a2ad8723134d96185d
fetched_at: '2026-06-29T00:09:01.040307+00:00'
page_id: '371623949'
product: rm
source: tdn-rm
title: 3096590 FINANCEIRO01-7526 DT Registro online itaú
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=371623949
version: 1
---

# REGISTRO ONLINE DE BOLETO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Registro Online de Boleto |
| **Situação/Requisito:** | Ao informar no cadastro de convênio (aba de Cobrança Bancária ) ou no boleto(aba de Dados Cnab) o código de instrução 03 o sistema não está salvando o dígito 0 a esquerda, mantendo apenas o numeral.  Com isso, o banco Itaú não aceita o código de instrução enviado, pois de acordo com a página 11 do manual bancário os códigos de instrução devem ser precedidos do numeral 0. |
| **Solução/Implementação:** | Ajuste no processo de registro online de boleto do banco Itaú para formatar corretamente os campos de instrução de cobrança (1,2 e 3). |
| **Tickets relacionados:** | N/A |
