---
content_hash: 4f1f5ddd39760eea60ed5f5db455c67e86ebeaa669072a89be5f40b6e5e8e1dd
fetched_at: '2026-06-29T00:09:00.304762+00:00'
page_id: '367231539'
product: rm
source: tdn-rm
title: 2783563 FISCAL01-4717 DT Geração de Registros TAF - REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=367231539
version: 3
---

# Geração de Registros TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Registros TAF |
| **Situação/Requisito:** | Cliente está solicitando melhoria na geração de registros TAF, onde o mesmo passe a gerar somente  registros pertinentes a rotina federal REINF. |
| **Solução/Implementação:** | * Inclusão do Parâmetro "Gerar somente registros pertinentes a rotina REINF" no Layout TAF este parâmetro será visível na pasta Demais Parâmetros 3.  * No contexto do gerador de saídas os métodos utilizados pelo layout TAF será verificado o parâmetro "Gerar somente registros pertinentes a rotina REINF"  habilitado, gerando apenas registros pertinentes a rotina federal REINF. Observação: Para os registros do Bloco K o Parâmetro "Gerar Bloco K - T045 e Filhos" será verificado no contexto para evitar execução do serviço desnecessariamente. * Serão gerados apenas registros T013 e filhos referente a Lançamento Fiscal com a presença dos tributos INSS, FUNRURAL ou Contribuição Previdenciária em algum dos itens dos Lançamentos. Observação: Os registros filhos do lançamento e outros como por exemplo participante T003 também serão gerados. |
| **Requisito:** | FIS000408 |
| **Documento de Referência:** |  |
