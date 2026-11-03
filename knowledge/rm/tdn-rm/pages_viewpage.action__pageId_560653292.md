---
content_hash: fdd4c6f6583e5b174a97c34202acad238d04159ebdd280ac0bcd098e9ad42c85
fetched_at: '2026-06-29T00:10:47.671445+00:00'
page_id: '560653292'
product: rm
source: tdn-rm
title: Dados da atividade econômica relacionada ao serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653292
version: 6
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **atividade** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **0-1** | **Tag raíz para as informações sobre a atividade do documento.** |  |  |
| codigo | atividade | E | 1-1 | Código da atividade do RPS. |  | Se algum dos serviços possuir o campo código CNAE preenchido no anexo: tributos do produto por município preenchido para o município da filial.  Então: primeiro código encontrado: DTRBMUNICIPIOPRD.CNAE  Senão Se campo Código de Serviço preenchido no movimento (Integrações | Fiscal)  Então: TMOV.CODIGOSERVICO  Senão Se Filial é SCP (sócio ostensiva) e  código atividade federal socio ostensivo preenchido  Então: FILIALSOCIOOSTENSIVO.CODATIVFED  Senão Se o CNAE da filial estiver preenchido  Então: GFILIAL.CODATIVFED |
| aliquota | atividade | E | 1-1 | Alíquota de ISS da atividade do RPS. |  |  |
