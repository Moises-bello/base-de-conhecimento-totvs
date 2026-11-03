---
article_id: 10167789118487
category: RH - Soluções para error.log
content_hash: bbd837dc462c8877d2d4a968963be48d3531573d71589a6d06add5ad97476ceb
fetched_at: '2026-06-28T22:44:08.924164+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error log ao tentar incluir e/ou alterar afastamento
  de funcionário: invalid field name in Alias SRA->RA_CODRPAT on {|a,b,c| FWInitCpo(a,b,c),xRet:=(SRA->RA_CODRPAT)...'
type: support-article
updated_at: '2024-10-10T11:10:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10167789118487-RH-Linha-Protheus-GPE-Error-log-ao-tentar-incluir-e-ou-alterar-afastamento-de-funcion%C3%A1rio-invalid-field-name-in-Alias-SRA-RA-CODRPAT-on-a-b-c-FWInitCpo-a-b-c-xRet-SRA-RA-CODRPAT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26970621730583) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar incluir e/ou alterar **afastamento de funcionário**, através da rotina **GPEA240** : ***invalid field name in* Alias SRA->RA\_CODRPAT on {|a,b,c| FWInitCpo(a,b,c),xRet:=(SRA->RA\_CODRPAT)...**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre em ambientes com o inicializador do campo: **R8\_CODRPAT** incorreto  
  
**Solução**Para correção do error log, será necessário efetuar a manutenção do inicializador padrão do campo **R8\_CODRPAT,** conforme o padrão abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26970621732887)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10167773913623)

**Informações complementares**Pacote de Expedição Contínua do RH:[https://centraldeatendimento.totvs.com/hc/pt-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)[br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)Pacote de Expedição Contínua do eSocial:[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
