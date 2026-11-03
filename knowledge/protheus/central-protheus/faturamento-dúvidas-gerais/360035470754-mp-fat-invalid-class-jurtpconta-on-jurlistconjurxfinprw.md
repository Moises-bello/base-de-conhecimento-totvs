---
article_id: 360035470754
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: ce854b740952896cdfa047160860efb38acef7978e11bd241623e9990a7185df
fetched_at: '2026-06-28T22:38:33.157116+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-invalid class JURTPCONTA on JURLISTCON(JURXFIN.PRW) '
type: support-article
updated_at: '2021-04-28T15:54:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035470754-MP-FAT-invalid-class-JURTPCONTA-on-JURLISTCON-JURXFIN-PRW
---

**Ocorrência**

Ao pesquisar a natureza financeira no cadastro do cliente (**MATA030**), ocorre o erro:

**invalid class JURTPCONTA on JURLISTCON(JURXFIN.PRW) 13/05/2019 14:42:43 line : 15**

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O erro ocorre por que o sistema não consegue identificar a classe **JURTPCONTA** no RPO.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Aplique o pacote da classe **JURTPCONTA**: <https://suporte.totvs.com/portal/p/10098/download?e=678493>

2. Via TDS ou IDE, aplique o pacote no RPO;

3. Reinicie o smartclient e refaça o processo.

**Obs:** Para aplicação de pacotes é necessário o conhecimento em estrutura Protheus.

Em caso de dúvidas para a aplicação, consulte a equipe de Framework para auxiliar.

Sempre aplique pacotes ao RPO em ambiente de homologação para validar, efetuando os devidos backups, para posteriormente aplicar em ambiente de produção.
