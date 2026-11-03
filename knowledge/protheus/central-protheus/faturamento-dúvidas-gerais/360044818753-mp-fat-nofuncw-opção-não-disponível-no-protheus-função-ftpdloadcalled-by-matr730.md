---
article_id: 360044818753
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3f2e65456b2b7bd35698a8eabcc81d4f8af2c0042ba0b6783ae8a94ca9328fdb
fetched_at: '2026-06-28T22:38:31.305308+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-NOFUNCW: opção não disponível no Protheus. Função: FTPDLOADCalled by
  MATR730'
type: support-article
updated_at: '2021-04-28T15:53:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044818753-MP-FAT-NOFUNCW-op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-FTPDLOADCalled-by-MATR730
---

**Ocorrência**

Ao acessar o relatório MATR730, ocorre o Help:

NOFUNCW: opção não disponível no Protheus. Função: FTPDLOADCalled by MATR730

E na sequência o erro:

InterFunctionCall: cannot find function FTPDLOAD in AppMap on MATR730(MATR730.PRX) 08/01/2020 15:25:15 line : 20

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17 (com garantia extendida)  
   
 **Causa**

O erro ocorre devido a falta de proteção a rotina com relação aos componente que tratam a **LGPD** no módulo.  
   
 **Solução**  
1. Para solucionar essa ocorrência, efetue o donwload do pacote mais atual do **matr730**, conforme o ambiente :  
**12.1.27:<https://r.totvs.io/p/951371> ;**

**12.1.25:<https://r.totvs.io/p/951370> ;**

**12.1.23:[https://r.totvs.io/p/951369](https://r.totvs.io/p/951369%20) ;**

**12.1.17:<https://r.totvs.io/p/951368> (Garantia Extendida);**

2. Vai TDS ou VS-CODE, aplique o pacote de atualização ao RPO .

3. Reinicie o Smartclient e refaça o processo.

Obs: O tratamento indicado na FAQ, requer conhecimento técnico de estrutura Protheus, caso necessite de apoio mais técnico, contate a equipe de framework.

Caso o ambiente esteja em Cloud Totvs, solicite a equipe a aplicação do pacote no RPO do ambiente de uso.

Em caso de balance, aplique em todos os RPOS para garantir a atualização.
