---
article_id: 360018751751
category: RH - Rescisão
content_hash: 258cb79e6e766f0b7e3e5fd13ba67a31e9b8f8cf0a538a1d8088936796b76938
fetched_at: '2026-06-28T22:43:50.809543+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que seguro Desemprego WEB não é gerado para
  alguns funcionários
type: support-article
updated_at: '2025-09-08T18:45:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018751751-RH-Linha-Protheus-GPE-Por-que-seguro-Desemprego-WEB-n%C3%A3o-%C3%A9-gerado-para-alguns-funcion%C3%A1rios
---

**Dúvida**Por que seguro desemprego não é gerado para alguns funcionários?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O Seguro Desemprego é gerado somente para funcionários demitidos sem justa causa. Para que o arquivo seja gerado corretamente, verifique as informações abaixo:

1 - **Datas Geração**, **Demissão** e **Homologação** da Rescisão devem estar dentro do range das datas informadas nos parâmetros da rotina **GPEM090** conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014212331)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014212351)

2 - Em **Manutenção Tabelas** (GPEA320) > Tabela S043 (Tipos de Rescisão) > Cod Resc. Rais deverá conter os códigos **11 (Rescisão de contrato de trabalho sem justa causa por iniciativa do empregador)** ou **12 (Término do contrato de trabalho)** para que o sistema gere o Seguro Desemprego.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14441020739223)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014211792)

**Saiba mais:**Para adquirir mais conhecimento acesse o(s) link(s) abaixo:

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Como fazer a geração do arquivo de seguro desemprego](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010783602-RH-Linha-Protheus-GPE-Como-fazer-a-gera%C3%A7%C3%A3o-do-arquivo-de-seguro-desemprego?source=search)

[MP - GPE - No Seguro Desemprego WEB os campos 'Soma dos três Últimos Salários' e 'Últimos Meses trabalhados' ficam em branco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018281132)  
[MP - GPE - Como identificar em qual campo está com erro no arquivo do Seguro Desemprego WEB?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022335751)  
[MP - GPE - Três últimos salários errados no Seguro Desemprego WEB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017471812)

#
