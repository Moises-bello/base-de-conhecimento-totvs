---
article_id: 4409007471127
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: cc15ac411927f6120397c675df524b16ab51c68987ceb0eab556e3e1987d4d20
fetched_at: '2026-06-28T22:39:50.199122+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Rejeição 441:
  Descrição do pagamento obrigatória para meio de pagamento 99-outros'
type: support-article
updated_at: '2021-09-20T12:42:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409007471127-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Rejei%C3%A7%C3%A3o-441-Descri%C3%A7%C3%A3o-do-pagamento-obrigat%C3%B3ria-para-meio-de-pagamento-99-outros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:08:00 min** **Dúvida**Ao transmitir a nota para um processo de importação apresenta a rejeição 441, como podemos resolver?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* - Todas as versões.  
  
**Solução**Para que a Nota Fiscal Eletrônica não seja rejeitada com motivo **441-Rejeição: Descrição do pagamento obrigatória para meio de pagamento 99-outros**, será necessário a criação dos parâmetros listados no boletim técnico: <https://tdn.totvs.com.br/pages/releaseview.action?pageId=626650334>

Estes parâmetros tem como objetivo informar  a descrição da forma de pagamento utilizada na operação (TAG **xPag**). Esta descrição se faz necessário apenas quando não é informada uma forma de pagamento da condição de pagamento nas operações de entrada e saída (NF-e), que neste caso são transmitidas como pagamento: **99-outros** (TAG **tPag**).  
  
Necessário aplicar o pacote de correção:  
A Release Oficial foi expedida e publicada na Central de Downloads.  
O pacote pode ser acessado no endereço: 12.1.17:<https://r.totvs.io/p/1029718> ; 12.1.23:<https://r.totvs.io/p/1029719> ; 12.1.25:<https://r.totvs.io/p/1029720> ; 12.1.27:<https://r.totvs.io/p/1029721> ;  
  
**Saiba mais**  
[DSERTSS1-16630 DT Adequação a Nota Técnica 2020.006 - v.1.20](https://tdn.totvs.com.br/pages/releaseview.action?pageId=626650334)
