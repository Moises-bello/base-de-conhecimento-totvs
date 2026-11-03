---
article_id: 360017523572
category: Ativo Fixo - Moedas
content_hash: 258d357acc489df3279752a9d811621a1bae0715ca88415bec304c6464680130
fetched_at: '2026-06-28T22:41:37.783642+00:00'
product: protheus
section_id: 1500001536641
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - INCONSISTÊNCIA REFERENTE
  A MOEDA  NA VERIFICAÇÃO DE INTEGRIDADE '
type: support-article
updated_at: '2023-02-09T14:12:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017523572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-INCONSIST%C3%8ANCIA-REFERENTE-A-MOEDA-NA-VERIFICA%C3%87%C3%83O-DE-INTEGRIDADE
---

**Ocorrência**Na execução da rotina de integridade (ATFA100) retorna inconsistência referente a moeda

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - SIGAATF  – A partir da versão 11.80

**Causa**A mensagem de inconsistência se deve em função da moeda cadastrada no parametro mv\_atfmoed

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

Se o parametro estiver configurado com a moeda 1 esta inconsistência não será exibida.

MV\_ATFMOED - (Moeda a ser considerada para cálculo do Ativo Fixo Utilizar uma das moedas do Sistema (2,3,4,5)

<http://tdn.totvs.com/pages/viewpage.action?pageId=105316418>
