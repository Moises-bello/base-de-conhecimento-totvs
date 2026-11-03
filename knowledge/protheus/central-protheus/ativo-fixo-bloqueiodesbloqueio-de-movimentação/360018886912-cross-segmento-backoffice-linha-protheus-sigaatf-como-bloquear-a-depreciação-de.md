---
article_id: 360018886912
category: Ativo Fixo - Bloqueio/Desbloqueio de Movimentação
content_hash: 89ca6a13a28e4c78e8bdafa94dc1893560eb1bb808dae1f354fb4a0d9133e16d
fetched_at: '2026-06-28T22:41:49.681554+00:00'
product: protheus
section_id: 1500001547562
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Como bloquear a depreciação
  de alguns Bens?
type: support-article
updated_at: '2024-04-15T13:53:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018886912-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Como-bloquear-a-deprecia%C3%A7%C3%A3o-de-alguns-Bens
---

**Dúvida**Como bloquear a depreciação de alguns Bens?  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**Para bloquear a depreciação de alguns bens é possível através da  rotina Bloqueio e desbloqueio de Bens  ATFA200,  ou através do cadastro do ativo ATFA012 em outras ações , Bloquear/Desbloquear.

A diferença entre os dois procedimentos é que uma permite indicar até quando o bem ficará bloqueado e a outra apenas bloqueia.

ATFA200

O objetivo desta rotina é efetuar o bloqueio ou desbloqueio do cálculo de depreciação de alguns bens. É possível que haja a necessidade de interromper temporariamente a depreciação de um bem. Um exemplo disso é quando máquinas que são depreciadas pelo uso, por algum motivo não estão sendo usadas e portanto não estão depreciando. As operações de bloqueio e desbloqueio devem ser efetuadas separadamente.

Para efetuar o bloqueio/desbloqueio de depreciação

- Acessar a rotina   
- Definir os parâmetros  
- Preencha os dados conforme orientação do help e necessidade  
- Confirme a operação

![Help_button](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif)Dica:

**Para efetuar o bloqueio e desbloqueio de bens por filiais, informe "Sim" no campo "Seleciona Filais" e determine o intervalo de filiais desejado**
