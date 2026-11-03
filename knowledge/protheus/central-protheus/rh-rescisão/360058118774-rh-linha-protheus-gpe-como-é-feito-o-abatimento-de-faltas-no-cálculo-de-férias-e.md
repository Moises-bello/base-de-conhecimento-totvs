---
article_id: 360058118774
category: RH - Rescisão
content_hash: 398ef2e33f83ad98f74688932815fc6ef04b09be5fd54044acc8aa95752c20c9
fetched_at: '2026-06-28T22:43:48.653687+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como é feito o abatimento de faltas no cálculo
  de férias em rescisão para funcionários com escala 12x36
type: support-article
updated_at: '2025-05-07T21:01:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058118774-RH-Linha-Protheus-GPE-Como-%C3%A9-feito-o-abatimento-de-faltas-no-c%C3%A1lculo-de-f%C3%A9rias-em-rescis%C3%A3o-para-funcion%C3%A1rios-com-escala-12x36
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25990807936023) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como é feito o abatimento de faltas no cálculo de férias em rescisão para funcionários com escala 12x36?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**O sistema realiza a apuração para abatimento das faltas em férias no cálculo de rescisão através do lançamento da verba de falta Id 0054 e/ou 0242 e o cadastro do funcionário onde consta o total de horas dias (cadastro funcionário aba funcionais campo Horas Dias RA\_HRSDIA).  
  
Exemplo: funcionário possui carga horária mês 180 horas, sendo 6 horas por dias. Neste contexto caso seja lançada falta Id 0054 com total de 12 horas, o sistema irá dividir o total das horas pela quantidade de horas dia (12\6 = 2), desta maneira será abatido de saldo de férias 02 dias de faltas.

Para este tipo de jornada, o Id 0054 ou 0242 devem ser lançado com referência Dia, assim o sistema realiza o abatimento por dias e não por horas.

**Saiba mais:**

[RH - Linha Protheus - PON - Como utilizar a funcionalidade de Contador de Faltas no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015852071-RH-Linha-Protheus-PON-Como-utilizar-a-funcionalidade-de-Contador-de-Faltas-no-Ponto-Eletr%C3%B4nico?source=search)  
[RH - Linha Protheus - GPE - Como não abater as faltas justificadas das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016444831-RH-Linha-Protheus-GPE-Como-n%C3%A3o-abater-as-faltas-justificadas-das-f%C3%A9rias?source=search)  
[RH - Linha Protheus - GPE - Quais são as verbas de Faltas que podem influenciar nos cálculos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412351039767-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-verbas-de-Faltas-que-podem-influenciar-nos-c%C3%A1lculos?source=search)  
[RH - Linha Protheus - GPE - Como conferir Faltas do Funcionário apresentadas no cálculo de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053018573-RH-Linha-Protheus-GPE-Como-conferir-Faltas-do-Funcion%C3%A1rio-apresentadas-no-c%C3%A1lculo-de-F%C3%A9rias?source=search)  
[RH - Linha Protheus - GPE - Dias de Faltas injustificadas não estão abatendo nas Férias da Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016647531-RH-Linha-Protheus-GPE-Dias-de-Faltas-injustificadas-n%C3%A3o-est%C3%A3o-abatendo-nas-F%C3%A9rias-da-Rescis%C3%A3o?source=search)
