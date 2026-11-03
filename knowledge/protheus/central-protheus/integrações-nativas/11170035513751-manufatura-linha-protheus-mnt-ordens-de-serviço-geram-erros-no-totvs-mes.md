---
article_id: 11170035513751
category: Integrações Nativas
content_hash: be32b5967209dcfed9581b10047a0b3301c469aaa5b9131e3585d9482cfd17d8
fetched_at: '2026-06-28T22:42:35.480530+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Ordens de serviço geram erros no Totvs
  MES
type: support-article
updated_at: '2024-12-19T12:20:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11170035513751-Manufatura-Linha-Protheus-MNT-Ordens-de-servi%C3%A7o-geram-erros-no-Totvs-MES
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28646202870551)* Tempo aproximado para leitura: **00:01:06 min  
  
Ocorrência**Quando o módulo está integrado com o **Planejamento e Controle da Produção (SIGAPCP)** ao realizar processos nas ordens de serviço retorna mensagem **Atenção! Ocorreram erros na integração com o TOTVS MES. Erro: ..."**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11169527656727)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Causa**A situação acontece porque as ordens de serviço geradas pelo módulo **não podem passar pelo processo de integração** com o **TOTVS MES**. É necessário incluir uma condição nos parâmetros do **TOTVS MES** para a situação.  
  
**Solução**  
Acesse a rotina **SIGAPCP > Atualização > Integração M. E. .S > Parâmetros - PCPA109** e inclua filtros para a ordem de produção pelo **Item - C2\_ITEM** diferente de **OS** e pelo **Produto - C2\_PRODUTO** diferente do conteúdo do parâmetro **MV\_PRODMNT** **- Item de estoque para ordem de produção do SIGAMNT**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11465607105687)
