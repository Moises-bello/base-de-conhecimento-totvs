---
content_hash: 87f4575d5bfbfd63c4ebc6d425d67c6b4bf784bc586c6174c12fc9073a5ddc74
fetched_at: '2026-06-29T00:09:50.812926+00:00'
page_id: '436274973'
product: rm
source: tdn-rm
title: CONTROLADORIA01-2022 DT Registro K300
type: documentation
url: https://tdn.totvs.com/display/LRM/CONTROLADORIA01-2022+DT+Registro+K300
version: 3
---

# SPED Contábil - Registro K300

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Contábil |
| **Função:** | SPED Contábil |
| **Situação/Requisito:** | Está sendo gerado o registro K300 para uma conta que não foi gerada no K200 (pois não tem saldo e respeita parâmetro de sistema dentro de rotinas legais). Com este funcionamento atual o PVA acaba gerando uma mensagem que invalida o arquivo, impactando em alteração manual do arquivo por parte do cliente. |
| **Solução/Implementação:** | O registro K300 deixou de adicionar contas que não foram geradas no registro K200 por não ter saldo e respeitar o parâmetro de sistema "Enviar para o SPED Contábil / ECF Contas Contábeis que não tenham saldo ou movimentação no período da geração", existente em rotinas legais. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
