---
content_hash: a547147bbdc306ce8d3a2d7bf0994d2f75b308ec087bf0d66e310c690f21f907
fetched_at: '2026-07-02T19:24:23.989387+00:00'
page_id: '454832997'
product: protheus
source: tdn-tec
title: Correção - Componente TOleContainer não carrega conteúdo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454832997
version: 1
---

Correção - Componente TOleContainer não carrega conteúdo

|  |  |
| --- | --- |
| Situação | O componente TOleContainer não está carregando seu conteúdo. |
| Ocorrência | Ausência da biblioteca de dependência mswin32ext.dll (ou mswin32ext64.dll para build 64-bit) no pacote de distribuição do SmartClient. |
| Correção | Disponibilização da biblioteca mswin32ext.dll (para build 32-bit) ou mswin32ext64.dll (build 64-bit) no pacote de distribuição do SmartClient. Além das bibliotecas, foram incluídos também seus respectivos instaladores TOleContainerInstaller.msi ou TOleContainer64Installer.msi. |
| Informações adicionais | * Referente ao chamado: PP-645 * Referente à ocorrência: ITEC-403 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.5\_RC7 |
