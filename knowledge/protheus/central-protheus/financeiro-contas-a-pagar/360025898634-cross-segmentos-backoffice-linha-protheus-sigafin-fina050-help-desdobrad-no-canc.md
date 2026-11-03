---
article_id: 360025898634
category: Financeiro - Contas a Pagar
content_hash: afb404c65290b713923fc3afa8404ec13b604b23b5738fea61034e27e62f23af
fetched_at: '2026-06-28T22:38:08.559227+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - HELP DESDOBRAD
  no cancelamento de desdobramento
type: support-article
updated_at: '2022-08-05T16:58:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025898634-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-HELP-DESDOBRAD-no-cancelamento-de-desdobramento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:02:00 min**

**Ocorrência**No módulo Financeiro, ao acessar a rotina de Contas a Pagar  apresenta a mensagem  
Help: DESDOBRAD  Não é possível a exclusão de títulos geradores ou gerados por desdobramento, Favor utilizar a rotina de cancelamento de Desdobramento   
![fina050.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360040460894/fina050.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA050 - Todas as versões  
  
**Causa**Compartilhamento diferentes das tabelas **SE2 e FI8**

**Solução**Para correção se faz necessário adequar a verificação do compartilhamento dos campos **Ac.Filial Ac.Unidade e Ac.Empresa** das tabelas **SE2** e **FI8** estão com mesmo nível de compartilhamento, forma, essa mensagem de help é apresentada somente quando estiverem diferentes os níveis.  
Acesse o **Configurador** (**SIGACFG**) > **Base de Dados** > **Dicionário** > **Base de Dados**, selecione a tabela e verifique o compartilhamento.
