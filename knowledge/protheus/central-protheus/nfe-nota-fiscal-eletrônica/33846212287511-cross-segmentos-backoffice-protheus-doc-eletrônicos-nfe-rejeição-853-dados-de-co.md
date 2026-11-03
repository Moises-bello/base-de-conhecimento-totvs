---
article_id: 33846212287511
category: NFe - Nota Fiscal Eletrônica
content_hash: 342925c9cbadfe2635850026fd92816e4ee4411a823d0ee7afe225a7e8b29480
fetched_at: '2026-06-28T22:40:06.913215+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Rejeição
  853: Dados de cobrança não devem ser informados para pagamento a vista'
type: support-article
updated_at: '2025-10-08T14:15:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33846212287511-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Rejei%C3%A7%C3%A3o-853-Dados-de-cobran%C3%A7a-n%C3%A3o-devem-ser-informados-para-pagamento-a-vista
---

**Ocorrência**  
Ao realizar a transmissão de uma NF-e em ambiente de homologação ocorre a rejeição 853, como proceder?  
  
**Ambiente**  
Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
A rejeição é causada quando o grupo de cobrança (<cobr>) é informado em uma nota cuja forma de pagamento está marcada como à vista (<indPag> = 0), isso significa que, para operações à vista, não deverá informar duplicatas, faturas ou outros dados do grupo de cobrança no xml.  
  
**Solução**  
Para contemplar essa nova exigência da Sefaz, se faz necessário a aplicação do patch do link abaixo e compilação do fonte NFESEFAZ que esta dentro do pacote no RPO do Protheus:

**12.1.2310**: [https://](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[supo](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[r](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[te](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[.totvs.](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[c](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[o](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[m](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[/p](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[ortal](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[/](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[p/](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[1](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[0098/download#detail/11](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[2](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[49](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)[63](https://suporte.totvs.com/portal/p/10098/download#detail/1124963) **(Somente garantia estendida)**  
**12.1.2410**: <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>

**Necessário atualizar o NFESEFAZ no qual possui a correção :** <https://suporte.totvs.com/portal/p/10098/download#detail/1152113>   
  
Observação: Importante realizar um backup do RPO antes da atualização.  
  
**Documentação:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=969576447>
