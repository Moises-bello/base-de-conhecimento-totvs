---
content_hash: ea24ea8b7651bb872cccb11b7b580fa9835521f364c9c5007a7abea5e97e88e2
fetched_at: '2026-06-29T00:09:26.697085+00:00'
page_id: '423938374'
product: rm
source: tdn-rm
title: Alteração na Contabilização de Movimento Associado a CTRC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938374
version: 3
---

Permitir que na alteração dos movimentos de recebimento onde são associados os Conhecimentos de Transporte da nota, seja possível refazer a contabilização do movimento de acordo com a necessidade.

**Parametrização**  
    
 **Integração Contábil:**Acessar os parâmetros do TOTVS Gestão de Estoques, Compras Faturamento na etapa **04.03.02 – Contábil | Definições Contábeis | Campos que Afetam o movimento – Lançamentos Contábeis** a opção **Conhecimentos de CTRC.**

**Transporte Associados** que indicará que quando estes dados forem alterados no movimento, implicará na regeração da Contabilidade pelo serviço de alteração do movimento.  
  O serviço de alteração do movimento, passa a considerar as alterações na tela de Conhecimentos de transporte associados como indicativa para regerar a contabilidade caso o parâmetro mencionado acima tenha sido marcado. Essa alteração será transparente para o usuário, mas implicará em mais performance na alteração dos movimentos.
