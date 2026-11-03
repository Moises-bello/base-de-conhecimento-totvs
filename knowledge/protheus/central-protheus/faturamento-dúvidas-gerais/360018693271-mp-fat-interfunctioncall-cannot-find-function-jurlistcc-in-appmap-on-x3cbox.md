---
article_id: 360018693271
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b15b5c0de023c8971fe2dcada851a3713c34406305d1774b9c47c5528885cba8
fetched_at: '2026-06-28T22:38:31.265063+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function JURLISTCC in AppMap on X3CBOX'
type: support-article
updated_at: '2021-04-28T15:55:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018693271-MP-FAT-InterFunctionCall-cannot-find-function-JURLISTCC-in-AppMap-on-X3CBOX
---

**Ocorrência**

Ao clicar na natureza do pedido está gerando o erro: **InterFunctionCall: cannot find function JURLISTCC in AppMap on X3CBOX(AP5TRANSLATE.PRW)**  
  
   
 **Ambiente**

Microsiga Protheus -  a partir da versão 12.  
   
 **Causa**

O erro ocorre por que a função **JURLISTCC** não se encontra no RPO;

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1.Efetue o download do do fonte jurxfin.prw, de acordo com a sua **12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=752881> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=752880> ;**  
 2. Via TDS ou IDE, aplique o pacote no RPO;  
 3. Reinicie o smartclient e refaça o processo.

**Obs:** Para aplicação de pacotes é necessário o conhecimento em estrutura Protheus.

Em caso de dúvidas para a aplicação, consulte a equipe de Framework para auxiliar.

Sempre aplique pacotes ao RPO em ambiente de homologação para validar, efetuando os devidos backups, para posteriormente aplicar em ambiente de produção.

**Obs 2 :** O fonte jurxfin também trata as ocorrências:

**Nofuncw - JURLISTCON CALLED BY X3CBOX**
