---
content_hash: bbcc983ea681878e921e925d0874e3b85be7e3b943af80bb008534a8950eb0ad
fetched_at: '2026-06-29T00:09:58.279981+00:00'
page_id: '452403252'
product: rm
source: tdn-rm
title: 4887016 - DEDUINTEGRACOES-4254 DT Simulação de valores de contratos com bolsa
  com código alfanumérico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452403252
version: 1
---

# SIMULAÇÃO DE VALORES DE PARCELAS DE CONTRATOS (WEBSERVER)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Simulação de valores de parcelas de contratos via WebServer |
| **Situação/Requisito:** | Erro de conversão de tipos na simulação de valores de parcelas de contratos |
| **Solução/Implementação:** | Ajuste no TBC tratando o campo CODBOLSA como alfanumérico. Ajuste na validação feita pela edição de uma bolsa quando alteramos o tipo do sacado. Ao alterar o tipo do sacado de uma bolsa com código alfanumérico, o sistema tentava converter o código da bolsa para inteiro dando um erro de conversão. Ajuste na geração / regeração de lançamentos financeiros ao incluir uma bolsa no contrato do aluno. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
