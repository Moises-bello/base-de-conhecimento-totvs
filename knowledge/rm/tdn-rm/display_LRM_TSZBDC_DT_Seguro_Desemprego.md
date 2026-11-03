---
content_hash: afcc031f832b28dcb77ffae2407b942493bfb163ed0835d5977c9899f154f76e
fetched_at: '2026-06-29T00:06:04.105923+00:00'
page_id: '200905664'
product: rm
source: tdn-rm
title: TSZBDC_DT_Seguro_Desemprego
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZBDC_DT_Seguro_Desemprego
version: 1
---

# SEGURO DESEMPREGO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Seguro Desemprego* |
| **Situação/Requisito:** | *Erro ao gerar arquivo de seguro desemprego.* |
| **Solução/Implementação:** | *Ao incluir um telefone no cadastro de funcionários contendo caracteres especiais quando não existe máscara cadastradas para o telefone no Parametrizador o sistema acusa erro de conversão de dados. Foi realizado ajuste em campos de telefone e DDD na rotina de seguro desemprego para retirar os caracteres especiais letras e espaços antes de realizar qualquer tipo de conversão.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSZBDC* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
