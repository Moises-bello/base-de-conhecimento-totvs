---
article_id: 26488868050071
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1238b8c1c6fbfb58afbaf947ed5aa214a1addb48fa3490bff7d49b48ff53d0cd
fetched_at: '2026-06-28T22:38:58.512619+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - MATA311 - Rotina
  de Transferência entre Filiais causando lentidão em outras rotinas
type: support-article
updated_at: '2024-09-19T17:15:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26488868050071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-MATA311-Rotina-de-Transfer%C3%AAncia-entre-Filiais-causando-lentid%C3%A3o-em-outras-rotinas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26488868029463) Tempo aproximado para leitura: **00:02:13 min** **Dúvida**Ao incluir ou efetivar uma Solicitação de Transferência entre Filiais (MATA311), outros usuários que acessam rotinas como Documento de Entrada, Pedido de Venda ou Preparação de Documento de Saída ficam travados sem mensagem na tela e só destrava ao concluir a Transferência entre Filiais. Como corrigir este problema?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Este tipo de problema normalmente está relacionado à trava (*lock*) do registro (normalmente SB2, SD1 ou SD2). Isso ocorre quando mais de um usuário prepara documentos de saída simultaneamente, dessa forma, ocorre trava do registro das tabelas envolvidas. Como a rotina MATA311, acaba por sua vez chamando o Pedido de Venda e Documento de Saída na filial origem e Documento de Entrada na filial de destino, pode-se haver essa concorrência caso outro usuário, no mesmo momento esteja utilizando estas outras rotinas, até mesmo rotinas do Contábil (caso empresa trabalhe com contabilização on-line de Doc de Entrada ou Doc de Saída).

**Como resolver?**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se possui em seu ambiente a configuração do parâmetro **MV\_FATTRAV;**  
2. Configure o parâmetro mencionado acima com o conteúdo 3 ou 4.

**Obs**: a partir do AppServer versão 13.9.1.4, liberado em 14.12.2020 houve uma melhoria no contador de *locks* para não impedir a execução das rotinas caso a conexão esteja transacionada, mitigando o travamento de registros, desta forma, além de configurar o parâmetro é interessante avaliar a atualização do binário.

**Saiba mais:**

*[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Trava registro SB2 na preparação do Documento de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036134513-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Trava-registro-SB2-na-prepara%C3%A7%C3%A3o-do-Documento-de-Sa%C3%ADda)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
