---
content_hash: 72e96869f699e31563d2537f791dd05d646329584a2ad38bec6cc8c511a65436
fetched_at: '2026-06-29T00:05:48.752363+00:00'
page_id: '1028941827'
product: rm
source: tdn-rm
title: Grupos totalizadores dos tributos IBS e CBS
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupos+totalizadores+dos+tributos+IBS+e+CBS
version: 7
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Obrigatório | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- |
| **IBSCBSTot** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **Não** | **Totais da NF-e com IBS e CBS** |  | **Grupo gerado apenas quando há IBS/CBS no item do movimento, cujas bases de cálculo sejam maiores que zero.** |
| vBCIBSCBS | IBSCBSTot | Não | Valor total da BC do IBS e da CBS |  |  |
| gIBS | vBCIBSCBS | Não | Grupo total do IBS |  |  |
| gIBSUF | gIBS | Não | Grupo total do IBS da UF |  |  |
| vDif | gIBSUF | Não | Valor total do diferimento |  |  |
| vDevTrib | gIBSUF | Não | Valor total de devolução de tributos | **Não será gerado no momento** |  |
| vIBSUF | gIBSUF | Não | Valor total do IBS da UF |  |  |
| gIBSMun | gIBS | Não | Grupo total do IBS do Município |  |  |
| vDif | gIBSMun | Não | Valor total do diferimento |  |  |
| vDevTrib | gIBSMun | Não | Valor total de devolução de tributos | **Não será gerado no momento** |  |
| vIBSMun | gIBSMun | Não | Valor total do IBS do Município |  |  |
| vIBS | gIBS | Não | Valor total do IBS |  |  |
| vCredPres | gIBS | Não | Valor total do crédito presumido |  |  |
| vCredPresCondSus | gIBS | Não | Valor do Crédito Presumido em condição suspensiva. | **Não será gerado no momento** |  |
| gCBS | IBSCBSTot | Não | Grupo total da CBS |  |  |
| vDif | gCBS | Não | Valor total do diferimento |  |  |
| vDevTrib | gCBS | Não | Valor total de devolução de tributos | **Não será gerado no momento** |  |
| vCBS | gCBS | Não | Valor total da CBS |  |  |
| vCredPres | gCBS | Não | Valor total do crédito presumido |  |  |
| vCredPresCondSus | gCBS | Não | Valor do Crédito Presumido em condição suspensiva. | **Não será gerado no momento** |  |
| gMono | IBSCBSTot | Não | Grupo total da Tributação Monofásica. Não será gerado no momento | Não será gerado no momento |  |
| vIBSMono | gMono | Não | Total do IBS monofásico | **Não será gerado no momento** |  |
| vCBSMono | gMono | Não | Total da CBS monofásica | **Não será gerado no momento** |  |
| vIBSMonoReten | gMono | Não | Total do IBS monofásico sujeito a retenção | **Não será gerado no momento** |  |
| vCBSMonoReten | gMono | Não | Total da CBS monofásica sujeita a retenção | **Não será gerado no momento** |  |
| vIBSMonoRet | gMono | Não | Total do IBS monofásico retido anteriormente | **Não será gerado no momento** |  |
| vCBSMonoRet | gMono | Não | Total da CBS monofásica retida anteriormente | **Não será gerado no momento** |  |
