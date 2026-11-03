---
content_hash: ec24ee62c5bfc1094a23e9b317af1f0ff3c8018c36115e5d82ebe295895dca5e
fetched_at: '2026-06-29T00:09:29.722833+00:00'
page_id: '425451724'
product: rm
source: tdn-rm
title: 3529555 FINANCEIRO01-8826 DT Tratamento de IOF Virtual no Resgate após Come-Cotas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425451724
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Gestão Financeira |
| **Módulo:** | Aplicação Financeira |
| **Função:** | Resgate |
| **Situação/Requisito:** | Em determinadas situações, o valor calculado para IOF/IR em resgate após o come-cotas, gera divergências com o extrato bancário |
| **Solução/Implementação:** | Constatamos que determinados bancos vem adotando um tratamento diferenciado ao considerar o IOF Virtual, incidente no primeiro resgate após a execução do come-cotas. Foi implementado um checkbox que pode ser demarcado no diálogo de resgate, permitindo habilitar o novo comportamento, caso a caso. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 3529555 |
| **Requisito:** | FIN000214 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | 12.1.19, 12.1.23 |
