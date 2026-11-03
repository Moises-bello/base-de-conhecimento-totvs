---
article_id: 360034293713
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d7adc5ca9119c7cebe240ccc516a2e098f02acaaded1d4f80449050c2c110475
fetched_at: '2026-06-28T22:38:31.280819+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function TK510TAXEN in AppMap'
type: support-article
updated_at: '2021-04-28T15:54:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034293713-MP-FAT-InterFunctionCall-cannot-find-function-TK510TAXEN-in-AppMap
---

**Ocorrência**

Ao excluir um registro do cadastro do cliente (**MATA030**), ocorre o erro: **InterFunctionCall: cannot find function TK510TAXEN in AppMap on A30DELETA(MATN030.PRX) 27/06/2019 18:25:31 line : 1856**  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O erro ocorre por que a função **TK510TAXEN**não se encontra no RPO ou a rotina pai encontra-se desatualizada.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1.Efetue o download do do fonte **tmka510 .prw,** conforme versão do ambiente:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=777123> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=777122> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=777121> ;

2. Via TDS ou IDE, aplique o pacote no RPO;

3. Reinicie o smartclient e refaça o processo.

**Obs:** Para aplicação de pacotes é necessário o conhecimento em estrutura Protheus.

Em caso de dúvidas para a aplicação, consulte a equipe de Framework para auxiliar.

Sempre aplique pacotes ao RPO em ambiente de homologação para validar, efetuando os devidos backups, para posteriormente aplicar em ambiente de produção.
