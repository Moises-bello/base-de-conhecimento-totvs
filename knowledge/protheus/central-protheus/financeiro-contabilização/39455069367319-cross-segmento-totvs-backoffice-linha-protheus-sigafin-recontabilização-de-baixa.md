---
article_id: 39455069367319
category: Financeiro - Contabilização
content_hash: 171720041af598d040076e1972094d6d093269280b3770ceb197d4feb1fec5f0
fetched_at: '2026-06-28T22:38:05.302253+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Recontabilização
  de baixa excluída ou cancelada
type: support-article
updated_at: '2026-04-07T14:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39455069367319-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Recontabiliza%C3%A7%C3%A3o-de-baixa-exclu%C3%ADda-ou-cancelada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39455069348631) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como realizar a recontabilização de uma baixa que foi excluída ou cancelada no módulo Financeiro?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução:**

O processo de contabilização relacionado ao cancelamento/exclusão da baixa está vinculado ao **LP 527**.  
Nesse contexto, a chamada do LP pode ocorrer tanto no **cancelamento da baixa** quanto na **exclusão**; porém, para a recontabilização, é importante destacar que o sistema trata cada situação de forma distinta.

**Passos**

1. **Cenário de Cancelamento da Baixa:**

* Ao utilizar a rotina de cancelamento, o Protheus gera um lançamento de estorno (via LP 527) e cria registros nas tabelas de movimentação (**SE5/FK1/FK5**).
* Este processo limpa o flag de contabilização, permitindo que o usuário utilize a rotina **CTBAFIN** para refazer a contabilização com base no cenário atual, caso necessário.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39455069349655)

2. **Cenário de Exclusão (Deleção) da Baixa:**

* Na exclusão, o sistema apenas marca o registro como deletado (logicamente).
* o registro original fica indisponível para uso.
* Nesta situação, a rotina **CTBAFIN** não localizará o registro para recontabilização.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39455096727319)

3. **Ajuste Manual (Exclusão):**

* Caso a baixa tenha sido excluída e o lançamento contábil original precise de ajuste ou estorno, o procedimento pode ser realizado manualmente por meio da rotina **Lançamentos Contábeis (CTBA102)** no módulo de Contabilidade Gerencial (SIGACTB).

Saiba mais

[A contabilização do LP 527 gera o valor do lançamento contábil incorreto](https://tdn.totvs.com/display/public/PROT/TVSCJ5_DT_contabil_cancel_bx_LP_527)
