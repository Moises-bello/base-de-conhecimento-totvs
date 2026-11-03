---
article_id: 360026098892
category: Inspeção de Processos (SIGAQIP)
content_hash: b8aad1d5a67b1223bae1eb0a14a3d0e7f63b1122ddacd431bda52d0b63196212
fetched_at: '2026-06-28T22:42:25.863626+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Não existem ensaios definidos para
  esta especificação
type: support-article
updated_at: '2024-04-17T18:01:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026098892-Manufatura-Linha-Protheus-SIGAQIP-N%C3%A3o-existem-ensaios-definidos-para-esta-especifica%C3%A7%C3%A3o
---

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Na rotina **QIPA215**, ao clicar no botão **Resultados** é apresentado o aviso: **Não existem ensaios definidos para esta especificação**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**Esta mensagem é apresentada quando o **Protheus** não encontra ensaios cadastrados para todas as operações da **Especificação do Produto - QIPA010**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se a **Ordem de Produção** vinculada a este resultado está com o campo **Roteiro - C2\_ROTEIRO** preenchido na rotina de **Ordens de Produção - MATA650**. Caso o mesmo estiver em branco, o **Protheus** não consegue validar os respectivos ensaios que deveriam estar vinculados ao roteiro de produção. Neste caso, é necessário preencher o campo **Roteiro** na abertura da **Ordem de Produção**.  
  
2. Caso o roteiro já estiver preenchido na **Ordem de Produção** e ainda assim a mensagem persistir, acesse a rotina **QIPA010** e confirme se existem ensaios definidos para **todas as operações** do roteiro de produção que foi informado na **Ordem de Produção**.
