---
content_hash: 4e19cc513275ce5d8ba4b986557bcb75f03c978eb9cffc33be482274aec38311
fetched_at: '2026-06-29T00:10:15.048835+00:00'
page_id: '463800253'
product: rm
source: tdn-rm
title: '5081987 FISCAL01-8058 DT Erro ao escriturar movimento: String or binary data
  would be truncated'
type: documentation
url: https://tdn.totvs.com/display/LRM/5081987+FISCAL01-8058+DT+Erro+ao+escriturar+movimento%3A+String+or+binary+data+would+be+truncated
version: 2
---

# String or binary data would be truncated

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Escrituração |
| **Situação/Requisito:** | Ao escriturar um movimento que esteja utilizando uma natureza que possui a flag "Possui Documentos Relacionados" marcada na aba "Outros Dados" e o movimento esteja parametrizado na etapa Fis-Escrituração 1/2 com o "Código Motivo"= "99" e "Desc Para Outros Motivos" = "Histórico" o sistema retorna a mensagem abaixo:  \*"String or binary data would be truncated." |
| **Solução/Implementação:** | Ajuste na escrituração para truncar o campo observação da referência, caso exceda 150 caracteres. |
