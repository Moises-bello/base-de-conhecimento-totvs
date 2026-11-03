---
content_hash: c929db0a9f3e5fccfd88de124ce5b86dddb314ba649c25ec7f43ee4faedb9ee9
fetched_at: '2026-06-29T00:08:53.474520+00:00'
page_id: '345541443'
product: rm
source: tdn-rm
title: GetReportInfo
type: documentation
url: https://tdn.totvs.com/display/LRM/GetReportInfo
version: 2
---

Para utilizar o método GetReportInfo deve ser passado como parâmetro o código da coligada do relatório e não o código da coligada do contexto.

RptExecutorClient report = new RptExecutorClient();

RptReportInfo repInfo = report.GetReportInfo(this.CodColigadaRel, this.IdRelatorio, Context.CodUsuario);
