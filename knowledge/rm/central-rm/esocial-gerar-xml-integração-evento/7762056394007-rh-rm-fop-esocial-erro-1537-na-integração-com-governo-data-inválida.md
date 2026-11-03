---
article_id: 7762056394007
category: eSocial - Gerar XML/ Integração Evento
content_hash: 80a7a79acc92705028e353e25e5fd4a93ca4406746cba3f671f4f95582ec1478
fetched_at: '2026-06-28T22:47:12.096127+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 1537 na integração com governo:  Data inválida'
type: support-article
updated_at: '2025-12-29T14:40:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7762056394007-RH-RM-FOP-eSocial-Erro-1537-na-integra%C3%A7%C3%A3o-com-governo-Data-inv%C3%A1lida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24166767605271) Tempo aproximado para leitura: **00:02:30 min**  
  
**Ocorrência**  
Ao transmitir o evento S-2299, o governo retorna o erro: **O evento ID 'IDXXXXXXXXXX' foi rejeitado pelo RET. Erro código 1537: Data invalida.Acao Sugerida: Deve ser uma data maior ou igual a data de admissao e nao superior a data de desligamento. Localização: /eSocial/evtDeslig/infoDeslig/dtAvPrv.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
O erro ocorre quando a data de concessão do aviso prévio está em branco, ou com data inválida. De acordo com o leiaute 1.0 a *tag* **dtAvPrv** deverá ser preenchida com data maior que a admissão, e menor ou igual à data da demissão do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28621493529111)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Identifique no XML a data da demissão e a data do aviso prévio

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7761689717783)

2. Verifique se a data da demissão está de acordo com a regra do eSocial;  
3. Após altere a data do aviso prévio para a mesma data do desligamento, ou data menor. Deverá ser uma data maior que a data de início do funcionário.

**Saiba mais**  
Para mais informações sobre a regra eSocial acesse:  
     • [MOS esocial (Manual orientação esocial)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-06-2025.pdf)  
     • [Regra de Leiaute eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s-1-3-cons-nt-05-2025/regras.html)
