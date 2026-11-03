---
content_hash: 054cbc0ea3382cfca8e8d6279be4060f473d30d475c3027a159dcafa8b2984cb
fetched_at: '2026-06-29T00:09:58.455339+00:00'
page_id: '452699647'
product: rm
source: tdn-rm
title: 4809885 FISCAL01-7703 DT Envio da NF-e - Tag CRT
type: documentation
url: https://tdn.totvs.com/display/LRM/4809885+FISCAL01-7703+DT+Envio+da+NF-e+-+Tag+CRT
version: 2
---

# Envio da NF-e

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Envio da NF-e |
| **Situação/Requisito:** | O cliente solicita a geração da tag CRT = “2” - O código 2 será preenchido pelo contribuinte optante pelo Simples Nacional que tiver ultrapassado o sublimite de receita bruta fixado pelo Estado ou DF e estiver impedido de recolher o ICMS/ISS por esse regime, conforme arts. 19 e 20 da LC 123/06. |
| **Solução/Implementação:** | Implementação do campo Sublimite Excedido em Filial\Dados Fiscais:  [Documentação da Implementação do Campo SubLimite](http://tdn.totvs.com/x/yp37Gg)  No envio da NF-e a tag CRT (Código de Regime Tributário) será preenchida conforme regra abaixo:  **Se** Filial Optante Simples (DFILIAL.OPTANTESIMPLES) **E** Sublimite excedido (DFILIAL.SUBLIMITEEXCEDIDO) Marcados  **Então** CRT **igual a** 2:Simples Nacional, excesso sublimite de receita bruta  **Senão** **Se** Filial Optante Simples (DFILIAL.OPTANTESIMPLES)  **Então** CRT **igual a** 1:Simples Nacional  **Senão** CRT **igual a** 3:Regime Normal |
