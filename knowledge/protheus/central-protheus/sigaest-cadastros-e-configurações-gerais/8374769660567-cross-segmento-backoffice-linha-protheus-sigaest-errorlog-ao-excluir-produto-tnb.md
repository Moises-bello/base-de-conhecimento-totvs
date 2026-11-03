---
article_id: 8374769660567
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 695d1072cd859bc8f193b40b76ca479c5c2a0183ac84275cdff7ded2b5a34c35
fetched_at: '2026-06-28T22:39:08.231404+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Error.log ao excluir
  produto - TNB010: SetOrder - Index not found. on MDTVALESB1(MDTUTIL.PRX)'
type: support-article
updated_at: '2022-08-23T19:38:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8374769660567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Error-log-ao-excluir-produto-TNB010-SetOrder-Index-not-found-on-MDTVALESB1-MDTUTIL-PRX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:10 min**

**Ocorrência**Ao tentar excluir produtos na rotina MATA010 apresenta o error.log abaixo.

***TNB010: SetOrder - Index not found. on MDTVALESB1(MDTUTIL.PRX)*** 08/04/2022 14:23:02 line : 1721

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões

**Causa**Esse incidente ocorre, ***ausência do índice da tabela TNB*,** as vezes também ocorre para o ***índice da tabela TNX*.**

**Solução:**

Seguem abaixo prints para criação dos índices pelo módulo Configurador nas tabelas citadas.

Após esses passos não ocorrerá mais o erro.

***PARA A TABELA TNB:*  
  
![](https://totvssuporte.zendesk.com/attachments/token/dCT2elwCoSRAySvkbgVkJafjC/?name=inline1501337338.png)  
![](https://totvssuporte.zendesk.com/attachments/token/o0PfzS33Mj8uPqWQzkIEFDXQW/?name=inline-2121611426.png)  
![](https://totvssuporte.zendesk.com/attachments/token/hAui3Idu0jVmNSwHsNEoWi3F5/?name=inline-1593048649.png)  
  
  
*PARA A TABELA TNX:*  
  
![](https://totvssuporte.zendesk.com/attachments/token/E40GZRaPwCgrB4V0BCLigBd6p/?name=inline-1578435610.png)**

**Saiba Mais:**[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
