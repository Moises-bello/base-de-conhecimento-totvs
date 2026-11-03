---
article_id: 8610495169815
category: RH - CNAB
content_hash: e1b783b259f850f9a812ae24813e17e86405eb28078c7b2d219495953ab1dfcf
fetched_at: '2026-06-28T22:43:39.249935+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do ponto de entrada GP080US1
type: support-article
updated_at: '2025-06-16T18:36:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8610495169815-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-entrada-GP080US1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17434283637783) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Funcionalidade do Ponto de entrada GP080US1.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.

**Solução**

Este ponto de entrada permite que a gravação do arquivo seja realizada ou não.

**Exemplos de uso:**

#Include '[Protheus.ch](http://protheus.ch/)'  
  
User Function GP080US1()

Local nValorTotal := PARAMIXB[1]

Local lRet := .T.

/\*

Validação do usuário

\*/

Return lRet

**Variáveis de retorno:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8611166294807)

Ponto de entrada sendo executado no processamento da rotina GPEM080:

![GP080US1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17438847064471)

**Saiba Mais:**

[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM080](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045165513-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM080)

[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
