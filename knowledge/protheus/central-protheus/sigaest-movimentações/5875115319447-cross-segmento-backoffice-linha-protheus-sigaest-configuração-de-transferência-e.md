---
article_id: 5875115319447
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 7131aff21b332e86df742d766c637acdb0355c55c066fa73a037413e36fbb73c
fetched_at: '2026-06-28T22:38:55.427444+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de transferência
  entre filiais (MATA310) via Controle de Qualidade (CQ)
type: support-article
updated_at: '2023-01-13T19:01:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5875115319447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-transfer%C3%AAncia-entre-filiais-MATA310-via-Controle-de-Qualidade-CQ
---

**Dúvida**  
Como configurar transferência entre filiais via armazém de CQ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para realizar transferências entre filiais via CQ é necessário verificar as seguintes configurações:

1.1 Parâmetro ***MV\_M310TRV = .T.***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5874020420759/mceclip0.png)

1.2 Configure o TES (Tipo de Entrada e Saída) com os campos  
***Trans.Filial (F4\_TRANFIL) = Sim e Trans.Fil CQ (F4\_TRANCQ) = Sim***, na filial de saída e filial destino:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5874061361687/mceclip1.png)

1.3 Ter saldo no armazém CQ na filial de saída:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5874174992407/mceclip2.png)

2.1 Ao acessar a rotina de Transferência entre filiais(MATA310), selecione o armazém 98 da filial origem e destino. Após isso ir em:  Outras Ações > Relações >  Outras Ações > Consulta Saldo CQ > Ok.

Escolha a quantidade que irá ser transferida e confirme, segundo processo abaixo:

![20220504_161116.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5874760089495/20220504_161116.gif)

**Observações:**

* A transferência é permitida apenas quando o armazém origem e destino forem de Controle de  
  Qualidade.
* Gera-se no armazém destino um novo processo de Controle de Qualidade.
* Se no processo de transferência entre filiais a geração do documento de entrada a classificar não  
  se permite alteração no campo Armazém.
* Esse processo é exclusivo para a rotina MATA310, não tem essa funcionalidade disponível na rotina MATA311

**Saiba mais:**

*[SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-)*

[*MP - SIGAEST - MATA310/MATA311 - Transferência entre Filiais utilizando o parâmetro MV\_FILTRF*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-MP-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF)

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
