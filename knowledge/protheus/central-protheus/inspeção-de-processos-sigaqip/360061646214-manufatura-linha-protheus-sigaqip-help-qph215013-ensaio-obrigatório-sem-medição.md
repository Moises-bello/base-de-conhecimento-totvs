---
article_id: 360061646214
category: Inspeção de Processos (SIGAQIP)
content_hash: fa46827907848d2e511d76ca10636daf266d6191d9da718b08bbc510bd834260
fetched_at: '2026-06-28T22:42:25.775794+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help QPH215013 - Ensaio obrigatório
  sem medição
type: support-article
updated_at: '2024-10-29T19:30:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061646214-Manufatura-Linha-Protheus-SIGAQIP-Help-QPH215013-Ensaio-obrigat%C3%B3rio-sem-medi%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22672102644375)**Tempo aproximado para leitura: **00:00:55 min****Ocorrência**Na rotina QIPA215 - Resultados, ao selecionar a aba **Laudo de Laboratório** é retornada o *help* QPH215013 - Existe ensaio obrigatório cuja medição não foi apontada, para que seja possível informar o laudo do Laboratório, favor apontar medições para o ensaio: xxx.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O *help* **QPH215013** ocorre quando o ensaio está definido como obrigatório na rotina **QIPA010 - Especificação de Produtos**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Na rotina **QIPA215 - Resultados**, realizar o apontamento de medição no ensaio obrigatório;
2. Ou validar o parâmetro MV\_QPIESMD - Define se ignora ensaios sem medições no laudo do laboratório mesmo que estes sejam definidos como obrigatórios. 1=Sim; 2=Não.
