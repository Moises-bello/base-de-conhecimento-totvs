---
content_hash: 5636856abc59a8efffe78a9b906163c320e2c50f7f2c8755a38a610739e61d66
fetched_at: '2026-06-29T00:09:54.351498+00:00'
page_id: '444610216'
product: rm
source: tdn-rm
title: FISCAL01-7426 DT Lançamento Fiscal - Queda de conexão no Oracle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444610216
version: 1
---

# Cadastro de Lançamentos Fiscais

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Lançamentos Fiscais |
| **Situação/Requisito:** | A cliente informa que ao editar o lançamento fiscal é apresentado a  seguinte mensagem: "Erro de Conexão com ORACLE". |
| **Solução/Implementação:** | Foi removido o serviço estático de validação de documentos "Verifica se o Documento Utiliza Cupom Fiscal"  para que o lançamento fiscal ao consumir o serviço faça a busca no servidor sem cache. |
| **Requisito:** | FIS000062 |
