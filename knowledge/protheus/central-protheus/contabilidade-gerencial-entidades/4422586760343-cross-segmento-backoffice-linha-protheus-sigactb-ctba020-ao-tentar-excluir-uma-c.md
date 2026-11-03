---
article_id: 4422586760343
category: Contabilidade Gerencial - Entidades
content_hash: 00718798ec1b37b764ef5ec3234e8c66953f527212cd82c6fb72bbba82dabc15
fetched_at: '2026-06-28T22:40:49.753862+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA020 - Ao tentar
  excluir uma conta contábil sem movimento através da rotina de Plano de contas, sistema
  apresenta Help  “Violação de Integridade"
type: support-article
updated_at: '2026-03-25T18:56:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422586760343-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Ao-tentar-excluir-uma-conta-cont%C3%A1bil-sem-movimento-atrav%C3%A9s-da-rotina-de-Plano-de-contas-sistema-apresenta-Help-Viola%C3%A7%C3%A3o-de-Integridade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32092749051031) Tempo aproximado para leitura: **H0:05:00S min**  
  
**Ocorrência**  
No módulo Contabilidade Gerencial, ao tentar excluir uma conta contábil no Plano de Contas (CTBA020), sem movimento, sistema apresenta o help: FWFORMCANCEL Violação de integridade. Foi encontrada referência de Cod Visao (CTS\_CODPLA) na tabela CTN  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
  
**Solução**  
  
Para solucionar essa ocorrência, realize os seguintes passos:

**Importante**

Antes de qualquer procedimento sugerimos realizar o **BACKUP** do ambiente em sua totalidade e após realizar os testes em ambiente de **homologação/testes**, em caso de dúvidas entrar em contato com a equipe de suporte.

Os Relacionamentos que devem ser excluídos são as duas linhas abaixo na tabela de relacionamentos **(SX9)**.

Regra para exclusão: 

| X9\_DOM | X9\_IDENT | X9\_CDOM | X9\_EXPDOM | X9\_EXPCDOM |
| --- | --- | --- | --- | --- |
| CTS | 001 | CVF | CTS\_CONTAG | CVF\_CONTAG |
| CTS | 002 | CVF | CTS\_CTASUP | CVF\_CTASUP |
| CTS | 001 | CTN | CTS\_CODPLA | CTN\_PLAGER |

**Saiba Mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=570755500>
