---
article_id: 360019767011
category: NFe - Nota Fiscal Eletrônica
content_hash: 0fa763d22ce80f9864999e8943b1b3e82c2aab9cf6f38aacef2b411be3a85b36
fetched_at: '2026-06-28T22:40:01.978155+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Wizard Config
  em branco após preencher os parâmetros'
type: support-article
updated_at: '2021-10-11T14:51:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019767011--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Wizard-Config-em-branco-ap%C3%B3s-preencher-os-par%C3%A2metros
---

**Dúvida**Após fazer o Wizard Config na rotina de transmissão e acessar novamente os campos estão em branco.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Os parâmetros preenchidos no Wizard Config ficam gravados na tabela SPED000. Ao acessar a rotina fica em branco mesmo, porém com as informações salvas na tabela.

Os dados só aparecem no Wizard Config quando estão preenchidos no configurador, em Ambiente >. Email/proxy >> Configurar.

Porém se a configuração de email informada no configurador para relatórios for diferente da configuração do TSS aparecerá também no Wizard Config.

Se forem configurações diferentes, auxiliamos não preencher no configurador para que não ocorram erros no Wizard Config do TSS
