---
article_id: 1500010462862
category: TAF - REINF
content_hash: 277629429b237230a84f77b5df8c84b3d2f56f563f0cad357d1d601ded42e3d2
fetched_at: '2026-06-28T22:41:34.719345+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - MS0092
type: support-article
updated_at: '2023-07-12T20:05:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010462862-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-MS0092
---

**Dúvida**Como corrigir o erro de transmissão MS0092  
  
**Ambiente**A partir de 12.1.33  
  
**Solução**

1) O parâmetro **MV\_TAFVLRE**precisa estar com o conteúdo**1\_05\_01** 

* [TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-TAF-CONFIGURADOR-Como-acessar-os-par%C3%A2metros-do-sistema-?source=search)

  

2) Atualização no TSS:

É **obrigatório** a atualização do TSS, caso contrário ocorrerá erro de Schema nos eventos. Os schemas do layout 1.5 possuem o nome do **evento + nome do schema,** não devem ser renomeados. É um novo padrão da Receita Federal, exemplo:

**evtprestadorservicos-v1\_05\_01.xsd. = XML montado incorreto (fonte TSSREINF do TSS desatualizado)**

**evt2020prestadorservicos-v1\_05\_01.xsd = XML montado correto (fonte TSSREINF atualizado)**

* Substituir o RPO do TSS: [MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)
* Schemas: [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS?source=search)

Informações adicionais

Parâmetro **MV\_TAFAMBR** se o ambiente está em **produção** ou **homologação.**

* 1 = Produção
* 2 = Homologação

Para excluir um evento gerado incorretamente, segue passo a passo:

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente-?source=search)

Após realizada a exclusão do evento inconsistente, apure e transmita novamente o seu evento.
