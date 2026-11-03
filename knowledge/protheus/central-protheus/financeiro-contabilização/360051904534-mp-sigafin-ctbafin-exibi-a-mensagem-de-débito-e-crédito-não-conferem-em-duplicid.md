---
article_id: 360051904534
category: Financeiro - Contabilização
content_hash: 6829975dfa157b63b31e597e771cb665ae7265a99df04a775e6a779105bc3610
fetched_at: '2026-06-28T22:38:05.563342+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: MP- SIGAFIN - CTBAFIN - Exibi a mensagem de débito e crédito não conferem em
  duplicidade
type: support-article
updated_at: '2021-08-31T16:44:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051904534-MP-SIGAFIN-CTBAFIN-Exibi-a-mensagem-de-d%C3%A9bito-e-cr%C3%A9dito-n%C3%A3o-conferem-em-duplicidade
---

**Ocorrência**No dia 29/07 foi feita a contabilização de uma transferência bancária referente ao dia 01/07 conforme imagem abaixo exibiu a mensagem de "Atenção" duas vezes, uma para débito e outra para crédito, após confirmar está mensagem o lançamento foi salvo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084064353/mceclip0.png)  
   
 **Ambiente**Microsiga Protheus – Financeiro – CTBAFIN– A partir da versão 11.0  
   
 **Causa**Esse incidente ocorre, pois a parametrização das perguntas dos parâmetros "**Separa por**" da rotina que está incorreta e dependendo da parametrização o parâmetro  interfereMV\_GPDOCTB = .F.

**Solução**Verificar os links abaixo, pois o problema está nas perguntas dos parâmetros da rotina "**Separa por"**  e configuração do parâmetro dependo do conteúdo da parametrização da pergunta.  
  
<http://tdn.totvs.com/display/public/PROT/FIN0023_LPAD_contabilizacao_off_line_LP_560_561>  
<http://tdn.totvs.com/pages/releaseview.action?pageId=272696341>
