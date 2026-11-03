---
article_id: 360027941372
category: Inspeção de Processos (SIGAQIP)
content_hash: 5de4d0a1f4d23895ca0ce42cb75ea052d6274039a3a2606fb630348ef8e2a773
fetched_at: '2026-06-28T22:42:25.732673+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Exclusão de OP vinculada a um resultado
  no SIGAQIP
type: support-article
updated_at: '2021-10-01T13:14:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027941372-Manufatura-Linha-Protheus-SIGAQIP-Exclus%C3%A3o-de-OP-vinculada-a-um-resultado-no-SIGAQIP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:00 min****Ocorrência**  
No módulo **Planejamento e Controle da Produção - PCP**, ao tentar **excluir** uma **Ordem de Produção - OP** que está vinculada a um resultado no módulo **Inspeção de Processos - QIP**, é apresentada a mensagem:**Existe resultado já coletado para esta Ordem de Produção. Esta O.P. não poderá ser excluída.**   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**Esta mensagem ocorre porque a **OP** possui medições já coletadas no módulo de **QIP**.  
  
**Solução**Para excluir a **OP** é necessário excluir todas as medições vinculadas à mesma. Para isto, siga os passos a seguir:

1. Acesse a rotina **Resultados - QIPA215**, selecione o registro vinculado à **OP** que deseja excluir e clique em **Outras Ações** > **Excluir**. Isto faz com que qualquer registro da inspeção seja apagado;
2. Acesse a rotina **Ordem de Produção - MATA650** e tente excluir a **OP** novamente.
