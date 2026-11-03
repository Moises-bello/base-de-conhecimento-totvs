---
content_hash: b5f52c4dd3cebb8211f11d6804714cfda09699fdab59f0da1e66d80d363aa29a
fetched_at: '2026-07-02T19:24:27.860163+00:00'
page_id: '685002679'
product: protheus
source: tdn-tec
title: Correção - AutoUpdate em Linux não repassa permissões de execução - v20.3.1.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=685002679
version: 2
---

Correção: AutoUpdate em Linux não repassa permissões de execução

| Situação | Ao atualizar o SmartClient em Linux pelo AutoUpdate, os arquivos recebidos ficam sem permissão de execução |
| --- | --- |
| Ocorrência | Situação foi identificada e reportada por usuário. Após atualizar o SmartClient com o AutoUpdate em Linux, o usuário é obrigado a definir as permissões de execução manualmente. |
| Melhoria | Adicionado permissões de execução aos arquivos recebidos pelo AutoUpdate em Linux. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-3353 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.0.4 e 7.00.210324P - 20.3.1.0 |
