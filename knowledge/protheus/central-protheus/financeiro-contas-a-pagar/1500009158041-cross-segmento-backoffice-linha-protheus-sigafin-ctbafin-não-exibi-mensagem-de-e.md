---
article_id: 1500009158041
category: Financeiro - Contas a Pagar
content_hash: d8b361cc42de2d1dd2cd2d29cdfeb00f109782d54acae064604c7916737369fb
fetched_at: '2026-06-28T22:38:07.263523+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Não exibi
  mensagem de erro na Integração Contabil '
type: support-article
updated_at: '2021-05-05T20:28:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009158041-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-N%C3%A3o-exibi-mensagem-de-erro-na-Integra%C3%A7%C3%A3o-Contabil
---

**Ocorrência**No módulo Financeiro, ao tentar realizar a contabilização do lançamento não é apresentado mensagem de erro.  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois o parâmetro **MV\_CT105MS** está em branco ou como **"N"**, onde não irá apresentar a mensagem.

Este parâmetro é utilizado para indicar se serão exibidas mensagens de alerta ao encontrar inconsistências em lançamentos de integração, neste caso o parâmetro **MV\_ALTLCTO**com conteúdo **N**  o sistema estará configurado para não permitir a alteração destes lançamentos no momento da contabilização.  
  
**Solução**Alterar o conteúdo do parâmetro **MV\_CT105MS** para **"S"**

**1** - **S** - Mostra mensagem.  
**2** - **N** - Não mostra mensagem.

Saiba mais:   
**<https://tdn.totvs.com/pages/releaseview.action?pageId=6068560>**
