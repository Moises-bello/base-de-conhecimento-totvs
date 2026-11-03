---
article_id: 360004729532
category: esocial - Periódicos
content_hash: b8026b177475b41a01aca7c815072a850f512dce5f7696663b91552d05634953
fetched_at: '2026-06-28T22:47:09.465778+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Regra dos eventos periódicos para múltiplos vínculos
type: support-article
updated_at: '2026-04-17T19:30:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004729532-RH-RM-FOP-eSocial-Regra-dos-eventos-peri%C3%B3dicos-para-m%C3%BAltiplos-v%C3%ADnculos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24126712692503) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como são gerados os XMLs de eventos periódicos para funcionários que possuem múltiplos vínculos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH - (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Os XMLs de eventos periódicos são gerados por pessoa (CPF) e não por chapa, ou seja, em caso de funcionários que possuem mais de uma chapa, na mesma coligada, será considerado que esse funcionário possui múltiplos vínculos e, será gerado apenas um XML referente ao evento S-1200 e um XML referente ao evento S-1210. A mecânica de geração segue as instruções contidas no manual do eSocial.

• Evento S-1200

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24126691834775)

• Evento S-1210

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24126691846551)

**Importante**

Para funcionários que sejam cadastrados no TOTVS Folha de Pagamento (RM Labore) e também sejam autônomos cadastrados no TOTVS Gestão Financeira (RM Fluxus):

* Usuário TAF: Serão gerados dois XMLs sendo um do Labore e um do Fluxus. Deverá ser integrados os dois XML com o TAF antes de transmiti-los para o governo;
* Usuário Middleware: Será gerado um único XML com os dois vínculos.

**Saiba Mais**  
Para mais informações acesse:

* [S-1200 e S-1210 - Múltiplos Vínculos - Separação de demonstrativos por lançamento para autônomos do TOTVS Gestão Financeira (Middleware)](https://tdn.totvs.com/pages/releaseview.action?pageId=818466561);
* [Cálculo de INSS múltiplos vínculos conforme o eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=440829559)
