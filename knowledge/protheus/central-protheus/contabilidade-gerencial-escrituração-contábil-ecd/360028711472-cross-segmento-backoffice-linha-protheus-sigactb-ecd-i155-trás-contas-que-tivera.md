---
article_id: 360028711472
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 5accb048be7d801512cf2d6992d574d193e581daf8544ab825d20dce7a86bf15
fetched_at: '2026-06-28T22:40:44.671156+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD - I155 trás contas
  que tiveram movimentações em anos anteriores porém estão com saldos zerados
type: support-article
updated_at: '2022-05-12T11:08:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028711472-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-I155-tr%C3%A1s-contas-que-tiveram-movimenta%C3%A7%C3%B5es-em-anos-anteriores-por%C3%A9m-est%C3%A3o-com-saldos-zerados
---

**Ocorrência** I155 trás contas que tiveram movimentações em anos anteriores porém estão com saldos zerados  
   
 **Ambiente**Microsiga Protheus – Contabilidade gerencial– A partir da versão 11.80  
   
 **Causa**Problema com arrendondamentos devido a uma condição interna do servidor de aplicação do **Protheus** **32 bits** para valores numéricos com muitas casas decimais.

**Solução**

Para trabalhar com uma precisão mais acurada de tais valores numéricos é imprescindível habilitar o parâmetro "*FloatingPointPrecise"*(deixando com o valor igual a 1). Este parâmetro deverá ser informado no arquivo de configurações do sistema (**appserver.ini**) dentro do seção**[General]**.

**Saiba Mais**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=494991436>
