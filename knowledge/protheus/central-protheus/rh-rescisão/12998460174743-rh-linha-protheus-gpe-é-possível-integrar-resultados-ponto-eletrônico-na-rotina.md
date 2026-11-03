---
article_id: 12998460174743
category: RH - Rescisão
content_hash: 3120cf40d7fa008313cce48eef48a4605f64d1f670dab1806a36d886a00b2711
fetched_at: '2026-06-28T22:43:49.704370+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - É possível integrar resultados ponto eletrônico
  na rotina Múltiplas Rescisões
type: support-article
updated_at: '2025-09-09T21:37:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12998460174743-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-integrar-resultados-ponto-eletr%C3%B4nico-na-rotina-M%C3%BAltiplas-Rescis%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34822485056535) Tempo aproximado para leitura: **00:01:30: min** **Dúvida**É possível integrar resultados ponto eletrônico na rotina Múltiplas Rescisões ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**Sim é possível integrar resultados ponto eletrônico na rotina Múltiplas Rescisões para mais de um funcionário ou em lote.

Inclusão de opção, nos parâmetros da rescisão coletiva, para indicar se deve ou não ser feita a integração automática dos resultados do ponto eletrônico dos funcionários processados.

Caso a opção seja ativada, o sistema irá buscar o período atual do ponto eletrônico (MV\_PAPONTA), e integrará os resultados referentes a este período.

Caso o período de ponto não seja preenchido de forma completa (MV\_PAPONTA = "10/09" por exemplo), será buscado o período que contemple a data de demissão informada.

**Exemplo:**

MV\_PAPONTA = 10/09 e data de demissão igual a 20/03/2023

Período de busca nos resultados = 10/03/2023 - 09/04/2023

MV\_PAPONTA = 10/09 e data de demissão igual a 08/03/2023

Período de busca nos resultados = 10/02/2023 - 09/03/2023

**Saiba mais**

<https://tdn.totvs.com/x/Uc5pL>
