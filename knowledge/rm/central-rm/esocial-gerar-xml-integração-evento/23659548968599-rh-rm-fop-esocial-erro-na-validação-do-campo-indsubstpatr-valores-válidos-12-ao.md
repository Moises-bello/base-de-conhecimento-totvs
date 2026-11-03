---
article_id: 23659548968599
category: eSocial - Gerar XML/ Integração Evento
content_hash: 946fa35e97c7d23cbac85821cfdddee235f7418b91ad94763d9fb495533f5ae9
fetched_at: '2026-06-28T22:47:12.948251+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na "validação do campo ''indSubstPatr'' Valores
  válidos: 1,2" ao transmitir XML S-1280 para o governo'
type: support-article
updated_at: '2026-06-05T17:16:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23659548968599-RH-RM-FOP-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-indSubstPatr-Valores-v%C3%A1lidos-1-2-ao-transmitir-XML-S-1280-para-o-governo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23659548959383)** Tempo aproximado para leitura: **00:03:00** **min.**

**Ocorrência**  
Ao transmitir o evento S-1280, ocorre o erro de Schema. **Erro de schema: Element '{http://www.esocial.gov.br/schema/evt/evtInfoComplPer/v\_S\_01\_02\_00}indSubstPatr': [facet 'enumeration'] The value '0' is not an element of the set {'1', '2'}.**

**Element '{http://www.esocial.gov.br/schema/evt/evtInfoComplPer/v\_S\_01\_02\_00}indSubstPatr':**  
**'0' is not a valid value of the atomic type '{http://www.esocial.gov.br/schema/evt/evtInfoComplPer/v\_S\_01\_02\_00}TS\_indSubstPatr'.**

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões.

**Causa**  
O erro ocorre quando o indicativo de substituição no cadastro de período de apuração está sem preenchimento, com isso a informação no xml é retornado como 0. De acordo com o Leiaute S -1.2 o mesmo deve ser retornado como 1 ou 2

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23659575071383)

**Solução**  
Acesse: **Módulo RH | Folha de Pagamento | eSocial | Período de apuração |** Acesse o período de apuração desejado e ajuste o campo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23659548960407)

Após regere o XML S-1280 e integre o mesmo. 

**Saiba mais**  
[RH - RM - FOP - eSocial - Mapeamento dos eventos eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679-RH-RM-FOP-eSocial-Mapeamento-dos-eventos-eSocial)  
[RH - RM - FOP - eSocial - Como desonerar uma empresa no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028307112-RH-RM-FOP-eSocial-Como-desonerar-uma-empresa-no-eSocial)
