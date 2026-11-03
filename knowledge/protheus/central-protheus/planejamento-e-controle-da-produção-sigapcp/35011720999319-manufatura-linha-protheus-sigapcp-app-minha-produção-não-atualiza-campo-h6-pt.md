---
article_id: 35011720999319
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4e3c1a9274bbb15f256cce37d5ba2bef05177c196c484d6f9a5f9fea5ad057f9
fetched_at: '2026-06-28T22:42:40.833543+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - APP Minha Produção - Não atualiza campo
  H6_PT
type: support-article
updated_at: '2025-09-22T12:02:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35011720999319-Manufatura-Linha-Protheus-SIGAPCP-APP-Minha-Produ%C3%A7%C3%A3o-N%C3%A3o-atualiza-campo-H6-PT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35011762145559) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao realizar o apontamento de produção via **APP Minha Produção - Aplicativo Minha Produção** utilizando o formulário de apontamento do **MATA681 - Apontamento MOD2**, o campo **H6\_PT - Parcial/Total** não é atualizado.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
No **APP Minha Produção** não ocorre a atualização do campo **H6\_PT** com base na quantidade informada,   
Isto porque no apontamento via **APP** ao preencher a quantidade não é feita a validação se essa quantidade somada aos apontamentos anteriores dessa operação corresponde a quantidade maior ou igual ao previsto pela **OP - Ordem de produção.**

**Saiba Mais**   
No entanto, é possível utilizar o ponto de entrada [PApPosAp](https://tdn.totvs.com/pages/releaseview.action?pageId=639176401) para ajustar o conteúdo do campo **H6\_PT** conforme a necessidade.
