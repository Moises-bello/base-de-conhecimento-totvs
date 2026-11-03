---
article_id: 4416165307927
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 26152460c7d3e34374ab5c5f64fc4a5b934fd08a61e0d557c8d225efd246d45b
fetched_at: '2026-06-28T22:38:43.922356+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Tentativa de
  reservar registro no alias SD0 em EOF Stack chamadas em msrlock.eof controle de
  transações habilitado.
type: support-article
updated_at: '2021-12-17T14:59:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416165307927-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tentativa-de-reservar-registro-no-alias-SD0-em-EOF-Stack-chamadas-em-msrlock-eof-controle-de-transa%C3%A7%C3%B5es-habilitado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao excluir a nota de saída, seja deixando o pedido apto a faturar ou em carteira, gera a mensagem: Tentativa de reservar registro no alias SD0 em EOF Stack chamadas em msrlock.eof controle de transações habilitado. Tenta novamente? Essa mensagem será fechada em 5 segundos.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Causa**Uma validação da programação de entrega, **mata412**, que estava efetuando um busca indevida na tabela **SD0**, desta forma, foi efetuada a alteração no fonte **Fatxfun** para que apenas altere a variavel **lProgEnt,** caso confirme a existência do registro na tabela **SD0**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote de correção correspondente ao release utilizado:

12.1.17:<https://r.totvs.io/p/1054924> ;

12.1.25:<https://r.totvs.io/p/1054925> ;

12.1.27:<https://r.totvs.io/p/1054926> ;

12.1.33:<https://r.totvs.io/p/1054927> ;

2. Via Vs-Code, aplique o pacote no seu ambiente para atualização.  
3. Posteriormente, reinicie o smartclient e efetue novamente o processo.

Obs. Para efetuar a correção é necessário ter conhecimento na ferramenta Vs-code, na dúvida para aplicação do pacote contate nossa equipe de ADVPL.
