---
content_hash: 4622966ee798e9a201c31027a4d13c8666e7634eab936c73c50bd160ba92d47b
fetched_at: '2026-06-29T00:06:01.483079+00:00'
page_id: '198938825'
product: rm
source: tdn-rm
title: TSVUZP_DT_INSS_BASEIRRF_Pensao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVUZP_DT_INSS_BASEIRRF_Pensao
version: 3
---

# Estorno de INSS na Base IRRF da Pensão

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *No cálculo da Pensão Alimentícia está fixado para sempre deduzir o valor do INSS na Base do IRRF. Cliente questiona que tem que acatar o parâmetro no cadastro do evento de CC 3, para estornar IRRF.* |
| **Solução/Implementação:** | *Alterar o comportamento do cálculo do CC 13 - Pensão Alimentícia, para acatar a parametrização do cadastro do evento de CC 3, para que o desconto do INSS seja estornado na Base de IRRF.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSVUZP* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.39, 11.82.40* |
