---
content_hash: 827b9f372811214085caf344a6ea34a4528932f1e803fffcdf3f98e6eab62942
fetched_at: '2026-06-29T00:08:59.482024+00:00'
page_id: '362458493'
product: rm
source: tdn-rm
title: 2843418 FISCAL01-4648 DT Geração TAF/REINF - Registro T015 campo Cst
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362458493
version: 3
---

# Geração TAF/REINF - Registro T015 campo Cst

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Registro TAF |
| **Situação/Requisito:** | Ao processar a integração do RM com o TAF ocorre a mensagem abaixo:  Motivo: Código do Erro Descrição: [000009][Registro Inconsistente.] Detalhamento: Registro não integrado. Duplo clique para mais informações!  Erro 1 - Linha: 3 O valor '16' informado na coluna 39 para o campo  CST NF Complementar ( C30\_CSTCOM ) não existe na base de dados. |
| **Solução/Implementação:** | Foi identificado que o erro ocorre no preenchimento do campo 39 do Registro T015 na Geração dos Registros TAF  Foi realizado um ajuste no campo 39 do registro T015 do Layout TAF para quando o campo CST do Item  do Lançamento Fiscal estiver com mais de 2 caracteres, este seja truncado em 2 posições da esquerda para a direita, gerando assim o registro corretamente. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Documento de Referência:** | Não se Aplica |
