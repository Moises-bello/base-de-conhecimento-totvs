---
article_id: 360027347792
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4947af0aee9d00b7546c6ffac9452b88f2200071145b6b00ea74e33aba95df48
fetched_at: '2026-06-28T22:42:45.794755+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Quando o Sistema avaliará o estoque
  dos componentes no apontamento '
type: support-article
updated_at: '2021-10-19T11:08:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027347792-Manufatura-Linha-Protheus-SIGAPCP-Quando-o-Sistema-avaliar%C3%A1-o-estoque-dos-componentes-no-apontamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:01:00 min****Dúvida**Em quais situações o Sistema irá avaliar o estoque dos componentes no apontamento realizado através do **MATA680 -****Produção** **PCP MOD 1/MATA681 - Produção PCP MOD 2**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O Sistema poderá verificar a disponibilidade de estoque em três situações:

* Quando o componente estiver vinculado com alguma operação, ao realizar o apontamento da operação o Sistema avaliará a disponibilidade de estoque e requisitará o material vinculado;
* Caso o componente não esteja vinculado a uma operação, ao apontar a última operação do roteiro será avaliada a disponibilidade;
* Caso o parâmetro **Ver Saldo Por Opera** do **F12** da rotina **MATA680/MATA681** estiver com o valor **Sim**, a cada apontamento o Sistema avaliará a disponibilidade de todos os materiais, mesmo daqueles não vinculados com a operação apontada.
