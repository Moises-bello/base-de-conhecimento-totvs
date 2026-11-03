---
article_id: 24427886507031
category: eSocial - Gerar XML/ Integração Evento
content_hash: 81e23ccaba3632aa2768f0a89eef049fccf5e10d59a6ba54fd4fd51e5838ef99
fetched_at: '2026-06-28T22:47:12.288807+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro de Schema nmSoc na transmissão do evento S-2200
  /S-2300 para o Governo (S-1.2)
type: support-article
updated_at: '2024-12-26T15:57:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24427886507031-RH-RM-FOP-eSocial-Erro-de-Schema-nmSoc-na-transmiss%C3%A3o-do-evento-S-2200-S-2300-para-o-Governo-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24427916169751) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao integrar o evento S-2200 / S-2300 com o governo retorna o **Erro de schema: Element '{ http://www.esocial.gov.br/schema/evt/evtTSVInicio/v\_S\_01\_02\_00}nmSoc': [facet 'minLength'] The value has a length of '1'; this underruns the allowed minimum length of '2'. Element '{ http://www.esocial.gov.br/schema/evt/evtTSVInicio/v\_S\_01\_02\_00}nmSoc'**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24427886488343)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e Superiores.  
  
**Causa**O erro ocorre quando existe alguma informação incorreta no campo Nome Social no cadastro do funcionário. O preenchimento é validado conforme consta no leiaute do eSocial. **Validação**: Informação validada na base de dados do CPF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24427886489623)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
Acesse: **Módulo Folha de Pagamento | Administração de Pessoal | Funcionário | Identificação** e verifique se o campo Nome Social possui informação, se a mesma for indevida, deverá apagar a informação. Se a mesma for devida, verifique se a informação consta na base de dados do CPF do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24427916173079)

Após regere o XML S-2200 e o erro será sanado. 

**Saiba mais**- [Mapeamento dos eventos eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679-RH-RM-FOP-eSocial-Mapeamento-dos-eventos-eSocial?source=search)
