---
article_id: 115012824687
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 947e818dab3502490b71b66f71554bfd26eefa4eadee7a3ac7bac019935aa787
fetched_at: '2026-06-28T22:37:20.044089+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Erro de " Variable
  is not an object on FWFLDGET(PROTHEUSFUNCTIONMVC.PRX) " ao acessar rotina de Contratos
type: support-article
updated_at: '2022-05-19T20:49:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115012824687-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-de-Variable-is-not-an-object-on-FWFLDGET-PROTHEUSFUNCTIONMVC-PRX-ao-acessar-rotina-de-Contratos
---

**Ocorrência**

Erro de " Variable is not an object on FWFLDGET(PROTHEUSFUNCTIONMVC.PRX) " ao acessar rotina de Contratos

**Causa**

Incidente apresentado na atualização da versão 11 para versão 12, onde não há atualização do menu correspondente a versão.  
  
**Am****biente**

Microsiga Protheus - a partir da versão 12  
  
**Solução**  
A partir da versão 12 do sistema, foi desenvolvida a rotina CNTA300 para o cadastro do contrato como um todo: Planilha, Cronograma Financeiro/físico e contábil.

Além de usar para cadastros, a rotina CNTA300 foi desenvolvida também para realizar as revisões nos contratos, não utilizando mais a rotina CNTA140 - revisões.

Para que o erro mencionado não ocorra:

1-Baixe do portal do cliente o menu da versão 12.

2-Descompacte-o dentro da pasta systemload do Protheus, atualizando o menu existente, assim o problema deixará de ser apresentado.

Para maiores informações da atualização menu, consulte a FAQ no TDN: **<http://tdn.totvs.com/pages/viewpage.action?pageId=286745774>**

Por se tratar de um procedimento extremamente técnico, é recomendado que seja um analista especialista para efetuar a atualização do ambiente, em caso de dúvida para efetuar o processo, contate a equipe de Framework.  
  

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
