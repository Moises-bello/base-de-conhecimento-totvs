---
article_id: 360048634493
category: RH - Contrato Intermitente
content_hash: 61af734a371b2da4555e77b3b1df78ec57cce39b7a559073daa6712e51e08a25
fetched_at: '2026-06-28T22:43:40.092351+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema trata o cálculo do afastamento de
  funcionário em contrato intermitente?
type: support-article
updated_at: '2026-02-11T14:14:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048634493-RH-Linha-Protheus-GPE-Como-o-sistema-trata-o-c%C3%A1lculo-do-afastamento-de-funcion%C3%A1rio-em-contrato-intermitente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25967509820183)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como o sistema trata o cálculo do afastamento de funcionário em contrato intermitente?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus)  GPE - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**  
A legislação não trata de forma clara como deve ser realizado o cálculo de um funcionário em contrato intermitente afastado, porém o Protheus realiza o cálculo normalmente, onde os primeiros 15 dias é calculado na verba de correspondente ao afastamento e de acordo com o Tipo de Ausência que o funcionário estiver relacionado, mas fica a cargo do RH verificar como essas informações serão tratadas pelo INSS, uma vez que na legislação não fala sobre o assunto.  
  
**Observação:**

Para que o cálculo do afastamento seja realizado da forma correta, é necessário que o funcionário possua convocação cadastrada nos dias de afastamento e que o parâmetro MV\_TPCALEN esteja igual a 1 - analítico.

Se estiver com o conteúdo 2 - sintético, o sistema perde a referência para buscar os dias trabalhados e DSR's do mês para montagem dos cálculos.

**Saiba mais:**

[Orientação Consultoria de Segmentos - 5786265 - Contrato Intermitente](https://tdn.totvs.com/pages/releaseview.action?pageId=490973583)

[Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010081347-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-TPCALEN>
