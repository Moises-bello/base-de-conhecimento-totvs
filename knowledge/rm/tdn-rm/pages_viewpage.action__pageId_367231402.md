---
content_hash: bc22c361a268737231f62710c5f564b36fafac263d1dd4395141aef3373c32d2
fetched_at: '2026-06-29T00:09:00.300337+00:00'
page_id: '367231402'
product: rm
source: tdn-rm
title: 2798896 FOPCALCULO01-3792 - Cadastro de Perfil - Campos Histórico Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=367231402
version: 3
---

# Histórico de Função

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Funcionários | Histórico de Função |
| **Situação/Requisito:** | Ao criar um perfil e retirar a permissão da tabela PFHSTFCO nos campos 'CODFAIXA' e 'CODNIVEL' tanto no Gestão de Pessoas quanto no Folha de Pagamento, ao acessar o histórico de Função, na visão, o sistema apresenta os dois campos, porém ao editar o cadastro, os campos não aparecem. |
| **Solução/Implementação:** | Ajustado as permissões do campos CODFAIXA e CODNIVEL da tabela PFHSTFCO para que os mesmos não sejam exibidos na visão do cadastro de histórico de função quando o mesmo não tem permissão no Totvs Gestão de Pessoas ou Totvs Folha de Pagamento. |
| **Tickets relacionados:** | 2798896 |
