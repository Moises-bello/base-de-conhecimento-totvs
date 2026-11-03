---
article_id: 4402252317335
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 88fe08bbcdb342c2dfdf32a60ffed9d8b42b95f85a8f34e490c6929e85ceb5a0
fetched_at: '2026-06-28T22:42:44.478519+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem FWFORMBEFORE ao excluir uma
  operação
type: support-article
updated_at: '2021-06-07T11:53:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402252317335-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-FWFORMBEFORE-ao-excluir-uma-opera%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:05 min**  
**Ocorrência**Ao tentar excluir uma operação no **MATA632 - Roteiro de Operações**  ou no **PCPA124 - Processo Produtivo** o usuário recebe a mensagem **FWFORMBEFORE - Violação de Integridade. Foi encontrada referência do produto (G2\_PRODUTO) \_ Código (G2\_CODIGO) + Operação (G2\_OPERAC) na tabela SGF - Amarr Operação x Componente. Formulário MATA632\_SG2**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem surge quando existe um relacionamento entre os componentes da estrutura e a operação que se deseja excluir.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **MATA637 - Operação x Componente**;  
2. Pesquise pelo produto do qual deseja remover a operação;  
3. Clique em **editar**;  
4. Veja quais são os componentes que estão vinculados com a operação em questão e exclua esse relacionamento;  
5. Relacione os componentes com outra operação ou não faça o relacionamento, de modo que os componentes serão requisitados ao apontar a última operação.
