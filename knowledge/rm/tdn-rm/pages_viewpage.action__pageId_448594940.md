---
content_hash: 21e9e04d090d84861c3ced71b312d3d6925a929428bf77d8320ed9c915cc0e32
fetched_at: '2026-06-29T00:09:55.586233+00:00'
page_id: '448594940'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-4104 Dt Importação SHORARIOTURMA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448594940
version: 4
---

# Importador - TOTVS Educacional SHORARIOTURMA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Importador - TOTVS Educacional |
| **Situação/Requisito:** | Após analise, foi verificado que não era possível realizar a importação de dois ou mais registros para SHORARIOTURMA em um mesmo arquivo. |
| **Solução/Implementação:** | A correção consiste em realizar o copia da referência do objeto(EduTableDef) utilizado durante a importação, visto que era alterado ao longo da execução e causando o erro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
