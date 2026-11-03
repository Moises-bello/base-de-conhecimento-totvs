---
article_id: 30995444598807
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: b5b551a7f53a722bd178c501eb1421c279851b0dcaa3795e2f9ab7ff0aa389f6
fetched_at: '2026-06-28T22:37:49.272156+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA713 - Monitor
  de Pendências - Erro 400 - Não foi possível Excluir
type: support-article
updated_at: '2025-06-12T12:40:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30995444598807-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Monitor-de-Pend%C3%AAncias-Erro-400-N%C3%A3o-foi-poss%C3%ADvel-Excluir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30995444580247) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a exclusão de uma ocorrência de erro, apresenta a mensagem 400 - Não foi possível Excluir

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30995465575703)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a Receber - a partir do release 12.1.2310  
  
**Causa**Esse incidente ocorre, pois está tentando excluir um registro de "INCLUSÃO - SEA" devido a isso, o sistema não permite realizar a exclusão da ocorrência no Monitor de pendências.  
  
**Solução**O Monitor de pendências permitirá somente deletar os registros que estão na tabela **FI2** para instruções de cobranças **ALTERAÇÃO/CANCELAMENTO.**  
  
**Permite a exclusão de um registro de Ocorrência "Tabela FI2", desde que:**

* Usuário tenha privilégio para excluir na rotina "Instrução de Cobrança - (FINA151)"
* Título que corresponde ao registro não esteja em borderô  
    
  **Saiba mais**  
  [Monitor de Boletos com Pendências - FINA710](https://tdn.totvs.com/pages/viewpage.action?pageId=619123545)
