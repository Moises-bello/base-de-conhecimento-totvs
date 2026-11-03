---
article_id: 7605879985815
category: RH - Rescisão
content_hash: a217e0b972d16297339ee6f1c9ea8551431b4b7b00e44014e9ffee5e3135bc8f
fetched_at: '2026-06-28T22:43:53.752095+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Qual a finalidade da tabela S149
type: support-article
updated_at: '2025-06-16T18:20:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7605879985815-RH-Linha-Protheus-GPE-Qual-a-finalidade-da-tabela-S149
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Qual a finalidade da tabela S149?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.27.  
  
**Solução**Implementada a possibilidade de definir o acréscimo aos dias de aviso prévio indenizado, definida por faixas, de acordo com o tempo de casa do funcionário (anos contados a partir da data de admissão até a data de demissão). Foi efetuado a criação da tabela auxiliar S149 - Acréscimo Aviso Tempo de Casa, cuja estrutura segue abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7605719614231/mceclip0.png)

**Importante:**No campo "Dias de Acréscimo" somente dever ser preenchido quantidade de dias entre 3 e 60, ou seja, não será permitido informar valor menor que 3 dias nem maior do que 60 dias.

**Exemplos do cálculo dos dias de aviso prévio indenizado:**Considerando o exemplo de preenchimento da tabela S149 citada no início da documentação, sem filial e mês/ano preenchido, para os sindicato 01 e 11, considerando mnemônico P\_ANOAVPRO configurado com 1, segue exemplos de cálculos:  
  
**Exemplo 1:**Sindicato **11**.  
Admissão em **02/01/2017**.  
Demissão em **07/01/2022**.  
Tempo de casa: **5 anos**.

Acréscimo do aviso prévio indenizado: **12 dias**.  
Total do aviso prévio indenizado: **42 dias**.  
  
**Exemplo 2:**Sindicato **11**.  
Admissão em **02/01/2002**.  
Demissão em **07/01/2022**.  
Tempo de casa: **20 anos**.

Acréscimo do aviso prévio indenizado: **30 dias**.  
Total do aviso prévio indenizado: **60 dias**.  
  
**Exemplo 3:**Sindicato **01**.  
Admissão em **02/01/2003.**Demissão em **07/01/2022**.  
Tempo de casa: **19 anos**.

Acréscimo do aviso prévio indenizado: **30 dias**.  
Total do aviso prévio indenizado: **60 dias**.  
  
**Exemplo 4:**Sindicato **11**.  
Admissão em **02/01/1997.**Demissão em **07/01/2022**.  
Tempo de casa: **25 anos**.

Acréscimo do aviso prévio indenizado: **60 dias**.  
Total do aviso prévio indenizado: **90 dias**.

**Observação:**Como na tabela S149 não há faixa cadastrada para o tempo de casa de 25 anos, será utilizado o cálculo padrão dos aviso prévio, de acréscimo de 3 dias a cada ano trabalhado, limitado a 60 dias.

**Saiba mais**Para adquirir maior conhecimento acesse os *links* abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=659590175#exemplos-Exemplo3>
