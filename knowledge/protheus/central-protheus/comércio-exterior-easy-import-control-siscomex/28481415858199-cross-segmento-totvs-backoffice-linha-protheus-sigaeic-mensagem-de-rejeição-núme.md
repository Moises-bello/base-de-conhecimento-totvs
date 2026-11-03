---
article_id: 28481415858199
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: 741b6fb1c1088d575e82b7d54c834c4edc21b27de7227b0de678c17220dae608
fetched_at: '2026-06-28T22:39:45.359428+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem de rejeição,
  "Número da Duimp inválido: você está informando o tamanho 5 quando o esperado é
  15"'
type: support-article
updated_at: '2025-04-22T14:44:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28481415858199-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-de-rejei%C3%A7%C3%A3o-N%C3%BAmero-da-Duimp-inv%C3%A1lido-voc%C3%AA-est%C3%A1-informando-o-tamanho-5-quando-o-esperado-%C3%A9-15
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28481390463767) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como corrigir a  mensagem de rejeição: "Número da DUIMP inválido: você está informando o tamanho 5 quando o esperado é 15"?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – Easy Import Control- a partir da versão 12.1.2310.  
  
**Solução**

Para que não seja apresentada a rejeição o número CE Mercante no campo Presença de Carga (W6\_PRCARGA) deve ser preenchido com tamanho de 15 caracteres e terminando entre 01 e 11 no desembaraço de importação, na aba embarque, conforme o Help de campos, após isso faça a integração novamente.

**Exemplo Incorreto** "CE","identificacao":"016493295590852"  
**Exemplo correto para envio** "CE","identificacao":"016493295590801"

Para que não seja apresentada a rejeição o número CE Mercante no campo Presença de Carga (W6\_PRCARGA) deve ser preenchido com tamanho de 15 caracteres e terminando entre 01 e 11 no desembaraço de importação, na aba embarque, conforme o Help de campos, após isso faça a integração novamente.

**Exemplo do procedimento**

![5588b3d7-fddc-43fb-9370-a87d0fae9bc7.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28481415830935)

[**Saiba mais**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10929728507543-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Integra%C3%A7%C3%A3o-DUIMP-registro)

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Integração DUIMP registro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10929728507543-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Integra%C3%A7%C3%A3o-DUIMP-registro)
