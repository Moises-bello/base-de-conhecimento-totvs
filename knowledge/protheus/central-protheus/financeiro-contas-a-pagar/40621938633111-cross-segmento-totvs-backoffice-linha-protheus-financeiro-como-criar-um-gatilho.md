---
article_id: 40621938633111
category: Financeiro - Contas a Pagar
content_hash: 983052bfa4f136e8fe37a2238c65e68fe318d450c4e9a7a50619d84d797eb404
fetched_at: '2026-06-28T22:38:08.379881+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Como criar
  um gatilho para o campo natureza na inclusão do título
type: support-article
updated_at: '2026-05-21T11:03:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40621938633111-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-Como-criar-um-gatilho-para-o-campo-natureza-na-inclus%C3%A3o-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40621908523287) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como criar um gatilho para o campo natureza na inclusão do título?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Acesse **Configurador (SIGACFG) > Base de Dados > Dicionário > Gatilhos** e clique em **Incluir**. Preencha os dados exatamente desta forma:

* **Campo (**`X7_CAMPO`**):** `E2_FORNECEDOR` *(Este será o campo que vai disparar a ação após você digitar a loja)*
* **Sequência (**`X7_SEQUENC`**):** `001` *(ou a próxima disponível para o campo)*
* **Cnt. Dominio (**`X7_CDOMIN`**):** `E2_NATUREZ` *(Campo que receberá a informação)*
* **Tipo (**`X7_TIPO`**):** `Primário`
* **Regra (**`X7_REGRA`**):** `SA2->A2_NATUREZ`
* **Posiciona (**`X7_SEEK`**):** `Sim`
* **Alias (**`X7_ALIAS`**):** `SA2`
* **Ordem (**`X7_ORDEM`**):** `1` *(A1\_FILIAL + A2\_COD + A2\_LOJA)*
* **Chave (**`X7_CHAVE`**):** `xFilial("SA2")+M->E2_FORNECE+M->E2_LOJA`
* **Condição (**`X7_CONDIC`**):** *(Pode deixar em branco, ou colocar algo como* `!Empty(M->E2_FORNECE)` *se quiser evitar disparos vazios)*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40621908524183)
