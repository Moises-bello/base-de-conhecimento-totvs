---
article_id: 4403484247703
category: TAF - REINF
content_hash: 70b8e48d729befa82c36e532399076b2e89a27d413356c1ff271bf1e21ff76ec
fetched_at: '2026-06-28T22:41:34.825698+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1009 - Não
  existem Informações do Contribuinte vigentes na data do evento
type: support-article
updated_at: '2023-10-16T23:34:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403484247703-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1009-N%C3%A3o-existem-Informa%C3%A7%C3%B5es-do-Contribuinte-vigentes-na-data-do-evento
---

**Dúvida**

EFD REINF - Rejeição MS1009 - Não existem Informações do Contribuinte vigentes na data do evento  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF -  a partir da versão 12.1.17  
  
**Solução**

Passo 1.

1° Verificar se no e-cac consta um R-1000 ativo na receita, caso tenha, somente atualize o seu ambiente do TSS.

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)

Exclua a apuração inconsistente apure e transmita novamente.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente-?source=search)

Apure e transmita o evento periódico novamente.

Caso não tenha R-1000 ativo verificar o Passo 2.

2° Erro ocorre por não ter o registro R-1000 válido no E-cac, sendo necessário que apure e envie o evento R-1000 antes de transmitir os eventos periódicos.

**Assuntos relacionados:**

TAF - REINF - R-1000 - Cadastro do Complemento de Cadastral

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022208052-TAF-REINF-R-1000-Cadastro-do-Complemento-de-Cadastral-?source=search>
