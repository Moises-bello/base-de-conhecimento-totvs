---
article_id: 360021150472
category: ADVPL - Rotina Automática
content_hash: 97bc4bb883dc6cde6461e05bf7c748430a52a34559d75a385d8ae8733db6139d
fetched_at: '2026-06-28T22:40:24.117793+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Help TMKPROMDI na execauto
  TMKA271
type: support-article
updated_at: '2021-12-29T15:12:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021150472-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Help-TMKPROMDI-na-execauto-TMKA271
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Conseguimos parametrizar para não ocorrer esta mensagem no execauto da rotina TMKA271  
  
**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**A mensagem **TMKPROMDI** é apresentada quando o usuário, utilizando a agenda do operador, tenta abrir outra rotina do Telecobrança, o Help informa quais rotinas não podem ser abertas ao mesmo tempo.  
O sistema executa uma validação e verifica o ID e usuário que está acessando o sistema, quando dois usuários estivessem logados com o mesmo contato ou ID é apresentado o Help.  
Esta validação tem relação direta também com o modo em que o sistema foi aberto, **SIGAMDI**/**SIGAADV**, segue a regra;  
1. SIGAMDI   
1.1 Mesma máquina   
1.1.1 Mesmo usuário no mesmo processo: SIM   
1.1.2 Mesmo usuário em processos diferente: SIM   
1.2 Máquinas diferentes   
1.2.1 Mesmo usuário em processos diferentes: SIM   
  
2. SIGAADV   
2.1 Mesma máquina   
2.1.1 Mesmo usuário no mesmo processo: SIM   
2.1.2 Mesmo usuário em processos diferentes: SIM   
2.2 Máquinas diferentes   
2.2.1 Mesmo usuário em processos diferentes: NÃO
