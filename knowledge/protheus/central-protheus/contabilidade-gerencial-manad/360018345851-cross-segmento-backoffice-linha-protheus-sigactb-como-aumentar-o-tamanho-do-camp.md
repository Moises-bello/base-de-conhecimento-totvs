---
article_id: 360018345851
category: Contabilidade Gerencial - Manad
content_hash: 7cfe2bf6648269f448fb94dfb301b7c9fb2c56474a5a6dc87f96df841a25a269
fetched_at: '2026-06-28T22:40:58.441813+00:00'
product: protheus
section_id: 1500001548542
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como aumentar o tamanho
  do campo conta contábil na wizard do manad?
type: support-article
updated_at: '2023-12-01T15:10:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018345851-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-aumentar-o-tamanho-do-campo-conta-cont%C3%A1bil-na-wizard-do-manad
---

**Dúvida**Como aumentar o tamanho do campo conta contábil na wizard do manad?

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
   
**Solução**

Para aumentar o tamanho do campo deve-se alterar o limite dentro do arquivo MANAD.INI, disponível na pasta system do servidor protheus.

Na linha 184 altere para a instrução abaixo, eu como teste aumentei de 150 para 200 posições.

(PRE) aAdd (\_aTotal[007][4][3], {2,,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",1,,,,200})
