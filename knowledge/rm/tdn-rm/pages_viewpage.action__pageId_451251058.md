---
content_hash: 8f9ca71b7c433f0507c173be586344cb3382114c2460469796fd5943cac238b2
fetched_at: '2026-06-29T00:09:58.084972+00:00'
page_id: '451251058'
product: rm
source: tdn-rm
title: FISCAL01-6296 DT NF-e - Nota Técnica 2018/001 - Inutilização de numeração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451251058
version: 3
---

# Inutilização de Numeração da NF-e

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Inutilização de Numeração da NF-e |
| Situação/Requisito: | O controle de Inutilização de Numeração não será aplicado para o emitente pessoa física. |
| Solução/Implementação: | Cadastro de Filial   * Ajuste ao salvar os dados Fiscais da filial quando ocorre verificação se a filial matriz é do Simples Nacional. A inconformidade ocorria quando é informado CPF na Filial em vez do CNPJ.   Cadastro\Processo de Inutilização   * Não Permitir Inutilizar numeração de NF-e quando o emitente é pessoa física. |
