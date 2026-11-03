---
content_hash: 6f2aa34030980b4276f99fb34ff89735a4a4f5b31c41d351538c4856ad542534
fetched_at: '2026-06-29T00:09:52.362607+00:00'
page_id: '439356998'
product: rm
source: tdn-rm
title: FINANCEIRO01-9795 DT Geração de Extratos da Conciliação com
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439356998
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Conciliação de Cartão Cielo |
| **Situação/Requisito:** | Em determinadas situações, o arquivo de retorno retorna vazio para o campo NSU (Linha CV, posição 93~98). Em função disto o extrato apresenta um erro caso o parâmetro "Copiar ref. para o número do documento" estiver desabilitado. |
| **Solução/Implementação:** | O extrato gerado pela conciliação de cartão sempre irá gerar extratos com o número do documento gerado a partir da referência do extrato, desobrigando a habilitação do parâmetro supracitado. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | Não se aplica |
| **Requisito:** | FIN000228 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | 12.1.21, 12.1.22, 12.1.13 |
