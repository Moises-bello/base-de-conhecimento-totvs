---
article_id: 360044412433
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 28e3c2d37bbfe3c24d46f34e26835ae16d8cd2662a137ad719d7dda4dbebda99
fetched_at: '2026-06-28T22:42:44.549582+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem SEMPERM
type: support-article
updated_at: '2021-11-30T18:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044412433-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-SEMPERM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:05 min**  
  
**Ocorrência**Ao tentar alterar o cadastro de uma **OP - Ordem de Produção** no **MATA650 - Ordens de Produção** é apresentada a mensagem **SEMPERM - Problema: Usuário sem permissão para utilizar esta rotina. Solução: Solicite permissão ao Administrador do Sistema**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**O parâmetro **MV\_RESTARM - Indica se utiliza o controle de permissão de uso de armazéns e em qual nível. (0=Não utiliza;1=Por usuário;2=Por produto;3=Por usuário e produto)** está diferente de **0** e o usuário que está tentando realizar a alteração não tem permissão no armazém.  
  
**Solução**Alterar o parâmetro **MV\_RESTARM** para **0** ou incluir o usuário no **AGRA045 - Locais de Estoque** no armazém que ele não tem permissão.
