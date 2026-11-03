---
content_hash: 40c427e7bec67f8a808f9d5d65583c0fcfac2432e3396c4c20a5c12303d9944c
fetched_at: '2026-06-29T00:09:12.223938+00:00'
page_id: '416842534'
product: rm
source: tdn-rm
title: 3831282 FISCAL01-6532 DT Escrituração - Código do Motivo da Referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416842534
version: 2
---

# Escrituração de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Escrituração de Lançamentos |
| **Situação/Requisito:** | Ao realizar a escrituração de um movimento de NF-e (modelo 55), criado a partir de cópia por referência de um movimento  de cupom fiscal (motivo de referência 3 - NF Acompanhamento de Cupom Fiscal), é apresentado o seguinte erro:  Erros no Serviço de Inclusão de Lançamentos --------------------------------------------------------------------------------- Erro na Inclusão do Registro: Documento 000012330 - Série 005 - Data 29/08/2018 - Parcela 1: Para Documento Fiscal que acoberta Cupom Fiscal, o Motivo de referência deve ser "04". --------------------------------------------------------------------------------- |
| **Solução/Implementação:** | Ajustado o serviço de inclusão de Lançamentos Fiscais para que a referência parametrizada no Tipo de Movimento não seja consistida. A referência que o usuário informar será escriturada quando for nota que acoberta Cupom Fiscal. |
| **Requisito:** | FIS000236 |
