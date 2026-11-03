---
article_id: 36180292086679
category: eSocial - Tabelas/Não Periódicos
content_hash: bf4ba07092b96fed07dffa230d63d5286cf4e5d3517bfeb62583cf73b6813dcc
fetched_at: '2026-06-28T22:47:10.417320+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro de schema: Element ''{http://www.esocial.gov.br/schema/evt/evtAfastTemp/v_S_01_03_00}observacao'''
type: support-article
updated_at: '2026-05-26T19:28:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36180292086679-RH-RM-FOP-eSocial-Erro-de-schema-Element-http-www-esocial-gov-br-schema-evt-evtAfastTemp-v-S-01-03-00-observacao
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36180308780823) Tempo aproximado para leitura: 00**:05:00 min**  
  
**Ocorrência**  
Ao gerar o arquivo **XML S-2230 (Afastamento Temporário)**, é apresentado o seguinte erro: **Erro de schema: Element '{http://www.esocial.gov.br/schema/evt/evtAfastTemp/v\_S\_01\_03\_00}observacao': [facet 'minLength'] The value has a length of '0'; this underruns the allowed minimum length of '1'.**  
**Element '{http://www.esocial.gov.br/schema/evt/evtAfastTemp/v\_S\_01\_03\_00}observacao': [facet 'pattern'] The value '' is not accepted by the pattern '[\s\S]{1,255}'.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O incidente ocorre quando o campo **Observação** no **Histórico de Afastamento** do colaborador está preenchido com espaço em branco.  
O leiaute do evento **S-2230** exige que este campo contenha ao menos um caractere, caso seja preenchido.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o RM Folha de pagamento, administração de pessoal selecione o funcionário que será enviado o S2230, Administração de Pessoal → Anexos → Histórico → Histórico de Afastamento

2. No registro de afastamento, **limpe o espaço em branco do campo,** ou preencha com qualquer informação relevante (mínimo de 1 caractere).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36180292072599)

3.  Salve as alterações, gere novamente o arquivo **XML S-2230**.

**Saiba mais:**

Para mais informações sobre a geração de gatilhos do S-2230, acesse:  
     - [S-2230 Afastamento Temporário](http://tdn.totvs.com/pages/releaseview.action?pageId=364908488)
