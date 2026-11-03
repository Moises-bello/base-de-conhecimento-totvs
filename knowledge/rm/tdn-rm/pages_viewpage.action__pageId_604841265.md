---
content_hash: c8f532aa44fff3e15b4a0d1040e119ba45cb2c86e336840fba4b19bc7deae72e
fetched_at: '2026-06-29T00:10:58.265891+00:00'
page_id: '604841265'
product: rm
source: tdn-rm
title: DT- Parametrizador – Paga férias em dobro quando segundo período aquisitivo
  vence durante projeção do aviso prévio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604841265
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Parametrizador |
| **Situação/Requisito:** | O sistema não está pagando férias em dobro na rescisão quando as mesmas vencem durante o aviso prévio.  Funcionário tinha férias vencidas com relação ao ano de 2018/2019, mas as férias de 2019/2020 não tinham vencido ainda, porém, como a mesma tem 90 dias de aviso prévio, com a projeção do aviso acabou vencendo a segundas férias. E sobrando um avo de férias proporcionais. |
| **Solução/Implementação:** | Criado parâmetro “Paga férias em dobro quando segundo período aquisitivo vence durante projeção do aviso prévio” para o caso de demissões com projeção do aviso prévio indenizado em que houver o vencimento de segundo período de férias durante essa projeção, será pago as Férias em Dobro com o código de cálculo 365 - FÉRIAS EM DOBRO RESCISÃO verificando até o final da projeção do aviso prévio indenizado.  Se o parâmetro estiver desmarcado, será pago as Férias em Dobro com o código de cálculo 365 - FÉRIAS EM DOBRO RESCISÃO verificando até a data da demissão. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-12431](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-12431) |
| **Documento de Referência:** | [Parametrizador - Rescisão / Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719504) |
| **Pacote:** | N/A |
