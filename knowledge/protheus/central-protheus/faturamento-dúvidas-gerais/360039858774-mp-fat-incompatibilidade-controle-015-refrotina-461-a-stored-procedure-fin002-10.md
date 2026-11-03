---
article_id: 360039858774
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 2b01a4a9846271f90ad89b2a0c0a0ecd07f4a51646e72b31afd2d6f2bc9be963
fetched_at: '2026-06-28T22:38:31.230147+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Incompatibilidade - Controle 015 ref.rotina 461 -  a stored procedure
  fin002_10_01 está desatualizada.
type: support-article
updated_at: '2021-04-28T15:53:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039858774-MP-FAT-Incompatibilidade-Controle-015-ref-rotina-461-a-stored-procedure-fin002-10-01-est%C3%A1-desatualizada
---

**Dúvida**

Ao faturar uma nota no pedido de venda (**MATA410**) do faturamento, aparece a mensagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052907414/mceclip0.png)  
  
**Ambiente**

Microsiga Protheus -  a partir da release 12.1.17.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Aplique o pacote da rotina **Finxfin**para a versão do ambiente utilizado:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=859194> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=859193> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=859192> ;

2. Via TDS ou IDE, aplique o pacote no RPO;

3. Reinicie o smartclient e refaça o processo.

**Obs:** Para aplicação de pacotes é necessário o conhecimento em estrutura Protheus.

Em caso de dúvidas para a aplicação, consulte a equipe de Framework para auxiliar.

Sempre aplique pacotes ao RPO em ambiente de homologação para validar, efetuando os devidos backups, para posteriormente aplicar em ambiente de produção.

Procure atualizar o ambiente  com o uso dos pacotes de expedição continua de sua release ao invés de utilizarem apenas pacotes pontuais, eles garantem que o ambiente esteja com a ultimas correções até a data de expedição do pacote, evitando erros e problemas de performance, para download, acesse o endereço:

12.1.17: <https://suporte.totvs.com/portal/p/10098/download#000006/P12117/P12117AP/>

12.1.23: <https://suporte.totvs.com/portal/p/10098/download#000006/P12123/P12123AP/>

12.1.25: <https://suporte.totvs.com/portal/p/10098/download#000006/P12125/P12125AP/>
