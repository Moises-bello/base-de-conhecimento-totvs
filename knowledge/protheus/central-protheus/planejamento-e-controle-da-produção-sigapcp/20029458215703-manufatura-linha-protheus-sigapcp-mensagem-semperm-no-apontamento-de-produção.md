---
article_id: 20029458215703
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9617e871683614272ec0a89c1fbf98925c3b3cbf6ce156e3a336d60659df085f
fetched_at: '2026-06-28T22:42:44.552726+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem SEMPERM no apontamento de
  produção
type: support-article
updated_at: '2024-02-06T14:23:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20029458215703-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-SEMPERM-no-apontamento-de-produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20029458200343) Tempo aproximado para leitura: **00:00:40 min  
  
Ocorrência**Ao tentar incluir um apontamento de produção é apresentada a mensagem **SEMPERM - Problema: Usuário sem permissão para utilizar esta rotina. Solução: Solicite permissão ao Administrador do Sistema.  
  
Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
O parâmetro **MV\_RESTTM - Restringe a utilização dos tipos de movimentação aos usuários relacionados no cadastro de de permissões?** está ativo e o usuário não tem permissão para usar essa **TM - Tipo de Movimentação.  
  
**Solução****Altere o parâmetro **MV\_RESTTM** para **.F.**, ou inclua o usuário nas permissões da **TM**, seguindo os passos:

1. Verifique a **TM** utilizada no apontamento;
2. Acesse a rotina **MATA230 - Tipos de Movimentação**, selecione essa **TM** no *browser* e vá em **Outras Ações/Permissões por TM;**
3. Adicione esse usuário ou o grupo do qual faz parte.
