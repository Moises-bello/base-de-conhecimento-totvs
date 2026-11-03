---
content_hash: 916c7fdaafaad806babc458b9a965111188563cc84ef8f04b5e185be90c097b6
fetched_at: '2026-06-29T00:10:13.338362+00:00'
page_id: '455807230'
product: rm
source: tdn-rm
title: 5019047 FISCAL01-7948 DT Ajuste na Integração RM X TAF Registro T007
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=455807230
version: 2
---

# Integração RM X TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Integração RM X TAF |
| **Situação/Requisito:** | Ao realizar o processo de Integração TAF - WebService - Consulta foi apresentado a seguinte mensagem: Inconsistência na Integração\Consulta do registro. Identificador: [18] Tipo : [T007]. Motivo: Código do Erro Descrição: [000001][Registro Inconsistente.] Detalhamento: Erro de estrutura, favor verificar o Layout TAF. |
| **Solução/Implementação:** | No Registro T007 (Registro de item) foi incluído o campo  29 - TIP\_SERV - "Informar o tipo de serviço da fatura/recibo" Origem - Classificação do Serviço - Dados Fiscais do Produto |
