---
article_id: 360028992272
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fb47c7450c9ecc23f5f723628489032393feb1be27bd5be6db404dce0963a24b
fetched_at: '2026-06-28T22:42:43.610531+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Mensagem A680MODSB1 '
type: support-article
updated_at: '2024-02-08T13:24:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028992272-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A680MODSB1
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:17 min****Ocorrência**Ao tentar realizar um apontamento via **MATA681 - PCP Produção Mod2** ou **MATA680 - PCP Produção Mod1** é apresentada a mensagem **A680MODSB1**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**O Sistema apresenta essa mensagem quando o **centro de custo** vinculado ao **recurso** apontado não possui produto **MOD - Mão de Obra** correspondente.  
  
**Solução**  
O Sistema sempre requisita o produto **MOD** do **recurso**, quando o apontamento for realizado através do **MATA681** ou **MATA680** e informado tempo. Esse produto **MOD** deve ser cadastrado no **MATA010 - Produtos**, com o código **MOD + Centro de Custo do recurso**.  
  
**Exemplo**  
Se o código do centro de custo for **CC140**, será necessário cadastrar um produto do tipo **MOD** com o código **MODCC140**.  
  
E se o produto **MOD** estiver cadastrado corretamente do **MATA010 - Cadastrado de Produto**, verifique se o campo **B1\_MSBLQL - Blq de Tela** está igual a **1 - Sim**, ou seja, o produto está bloqueado.  
Neste caso é necessário alterar para **2 - Não**.
