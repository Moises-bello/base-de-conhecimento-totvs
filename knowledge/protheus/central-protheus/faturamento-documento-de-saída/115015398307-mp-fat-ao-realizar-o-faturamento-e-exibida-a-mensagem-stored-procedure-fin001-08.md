---
article_id: 115015398307
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 6577cb9d153dee89ac2fa94226366ccc0fa6b4770ffc85133d665e98ee8596ec
fetched_at: '2026-06-28T22:38:45.198234+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT -  Ao realizar o faturamento e exibida a mensagem 'Stored Procedure
  FIN001_08 está desatualizada
type: support-article
updated_at: '2021-04-28T15:14:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015398307-MP-FAT-Ao-realizar-o-faturamento-e-exibida-a-mensagem-Stored-Procedure-FIN001-08-est%C3%A1-desatualizada
---

**Ocorrência**

Ao realizar o faturamento e exibida a mensagem 'Stored Procedure FIN001\_08 está desatualizada'

**Causa**

A procedure estava sendo chamada no momento que há um processo que envolva a compensação automática, onde os parâmetros MV\_CMPDEVV  e MV\_CMPDEVC estão habilitados.

O problema também pode ocorrer no momento da inclusão/ alteração do pedido ou mesmo na liberação do pedido de vendas.  
  
  
**Ambiente**

Microsiga Protheus - versão 12.  
  
**Solução**  

Para solucionar essa ocorrência, realize os seguintes passos:

1. Aplique o pacote da rotina **Finxapi**para a versão do ambiente utilizado:

**12.1.27:<https://r.totvs.io/p/999114> ;**

**12.1.25:<https://r.totvs.io/p/999113> ;**

**12.1.23:<https://r.totvs.io/p/999112> ;**

**12.1.17:<https://r.totvs.io/p/999111> ;( com garantia estendida);**

12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=889847> (30.12.2019)

2. Via TDS ou Vs-code, aplique o pacote no RPO;

3. Reinicie o smartclient e refaça o processo.

**Lembrando que a versão 12.1.17 foi descontinuada em 31.12.2019.**

**Obs:** Para aplicação de pacotes é necessário o conhecimento em estrutura Protheus.

Em caso de dúvidas para a aplicação, consulte a equipe de Framework para auxiliar.

Sempre aplique pacotes ao RPO em ambiente de homologação para validar, efetuando os devidos backups, para posteriormente aplicar em ambiente de produção.

Procure atualizar o ambiente  com o uso dos pacotes de expedição continua de sua release ao invés de utilizarem apenas pacotes pontuais, eles garantem que o ambiente esteja com a ultimas correções até a data de expedição do pacote, evitando erros e problemas de performance, para download, acesse o endereço:

12.1.17: <https://suporte.totvs.com/portal/p/10098/download#000006/P12117/P12117AP/>

12.1.23: <https://suporte.totvs.com/portal/p/10098/download#000006/P12123/P12123AP/>

12.1.25: <https://suporte.totvs.com/portal/p/10098/download#000006/P12125/P12125AP/>

12.1.27: <https://suporte.totvs.com/portal/p/10098/download#000006/P12127/P12127AP/>
