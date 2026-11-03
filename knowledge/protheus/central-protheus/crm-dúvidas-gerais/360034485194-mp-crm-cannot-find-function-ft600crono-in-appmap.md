---
article_id: 360034485194
category: CRM - Dúvidas Gerais
content_hash: 4c2893753990fdc2713078c7649161efcdb0fa29e06fe22c0c6e197205427e83
fetched_at: '2026-06-28T22:40:27.551681+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'MP-CRM-Cannot find function FT600CRONO in AppMap '
type: support-article
updated_at: '2021-04-28T14:49:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034485194-MP-CRM-Cannot-find-function-FT600CRONO-in-AppMap
---

**Ocorrência**Ao  incluir uma proposta da Oportunidade do CRM, e esta dando a mensagem de erro:

**InterFunctionCall: cannot find function FT600CRONO in AppMap on FT600MDLACT(FATN600.PRW) 20/03/2017 15:24:18**  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

**Causa**

A função **ft600crono** foi encapsulada para a **ft600getcron**, por isso a mesma não é encontrada no RPO.  
   
 **Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download dos pacotes do fontes abaixo:

**fata600: <https://suporte.totvs.com/portal/p/10098/download?e=753735>  
fatn600: <https://suporte.totvs.com/portal/p/10098/download?e=734217>**

2. Via TDS ou IDE, aplique o pacote para atualização do RPO;

3. Reinicie o smartclient e refaça o processo.

**OBS**: É recomendado que toda aplicação de pacote seja efetuada primeiro em ambiente de homologação, para validar o processo e posteriormente, aplicado no ambiente de produção.

Para aplicação de pacote requer que o analista detenha conhecimentos de estrutura de de ambiente Protheus.

Caso necessite de apoio para aplicação, acione a equipe de Frame Work.
