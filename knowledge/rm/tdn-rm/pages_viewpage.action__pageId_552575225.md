---
content_hash: 0c4e12d5b0c56ce429b54b0184d972746a3b64077d85637639b67a9aab931c87
fetched_at: '2026-06-29T00:10:44.383468+00:00'
page_id: '552575225'
product: rm
source: tdn-rm
title: 4.1 Parâmetros que interferem na contabilização dos Contratos Educacionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552575225
version: 5
---

Ao executar o processo de contabilização por competência dos contratos educacionais, o sistema verifica algumas parametrizações para realizar a contabilização.

* **Status do Contrato**: Os contratos com status do tipo “*Cancelado*” **NÃO** serão contabilizados.

* **Tipo de Contrato**: Os contratos do tipo “*Acordo*” NÃO serão contabilizados.

* **Parcelas**: Os contratos precisam ter parcelas para compor o seu valor e ser contabilizado. Contratos **SEM** parcelas **NÃO** serão contabilizados. **Observação**: As parcelas não precisam estar geradas para o financeiro.

* **Serviços**: Só serão contabilizados os serviços que tiverem marcados “Compõe contabilização por competência”.

* **Situação de Matrícula**: Serão contabilizados somente os contratos cuja situação de matrícula do aluno esteja marcada “Gera contabilização por competência”. Ir em *Situação de Matricula | Aba Status no período letivo.*
