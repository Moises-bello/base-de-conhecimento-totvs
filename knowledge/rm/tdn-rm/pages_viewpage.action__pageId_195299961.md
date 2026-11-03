---
content_hash: c8e13be71d2a792e318db30aa61edffe0f76868a9def0a09503f7de11019640c
fetched_at: '2026-06-29T00:06:00.194211+00:00'
page_id: '195299961'
product: rm
source: tdn-rm
title: RMFIS00011_03 - Plano de Contas, Referenciamento e Saldos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=195299961
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: todas** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 27/07/2015 |

**Bloco J: Plano de Contas e Mapeamento**

**Bloco K: Saldos das Contas Contábeis e Referenciais**

Para geração desses dois blocos, a rotina da ECF verifica se a integração "RM Liber x RM Saldus" está habilitada. Para conferir sua integração acesse: Nova MDI | Ambiente | Parâmetros | Integrações de Sistemas.

No Bloco K, não geramos os seguintes registros:

* Registro K156: Mapeamento Referencial do Saldo Final
* Registro K356: Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento

O próprio PVA monta esses registros na importação do arquivo de acordo com as contas contábeis e o mapeamento informado no Bloco J.
