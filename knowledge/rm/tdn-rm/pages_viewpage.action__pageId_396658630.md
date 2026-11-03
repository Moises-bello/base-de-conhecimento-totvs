---
content_hash: c12eb541e97e47c9e2c1e0bc7ddd35959b51792e35c2576db9c2af8b74ea6ea9
fetched_at: '2026-06-29T00:09:10.048119+00:00'
page_id: '396658630'
product: rm
source: tdn-rm
title: 2789148 FISCAL01-4737 DT SPED Fiscal - Registros C195 , 0450 e 0460 - Tratativa
  de sequências de escape
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=396658630
version: 2
---

# SPED Fiscal - Registros C195 , 0450 e 460 - Tratativa de sequências de escape

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | SPED Fiscal - Registros C195 , 0450 e 460 |
| **Situação/Requisito:** | Na validação do SPED FISCAL nos registro 0460 e C195 campo TXT ocorre mensagem:  Conteúdo de campo inválido |
| **Solução/Implementação:** | Foi modificado a forma de geração dos campos de histórico do lançamento para que seja retirado as sequências de Escape como (tab, enter) para que não haja erro de validação no SPED.  Foram efetuados as tratativas:  \a Campainha (alerta) \b Backspace \f Avanço de página \t Tabulação horizontal \v Tabulação vertical |
