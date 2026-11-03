---
article_id: 8432953581975
category: RH - CNAB
content_hash: 5056b6f6576ec91be09754c95fafb569c9a760b25e3df2a6178f2e93a7a0c57f
fetched_at: '2026-06-28T22:43:39.239260+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na geração rotina GPEM080: Variable does
  not exist NSOMAVALOR: STRZERO(SOMAVALOR().'
type: support-article
updated_at: '2025-06-17T12:29:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8432953581975-RH-Linha-Protheus-GPE-Erro-na-gera%C3%A7%C3%A3o-rotina-GPEM080-Variable-does-not-exist-NSOMAVALOR-STRZERO-SOMAVALOR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32866947814551) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Erro na geração rotina GPEM080: Variable does not exist NSOMAVALOR: STRZERO(SOMAVALOR().  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -Gestão de Pessoal - Todas as Versões.

**Solução:**1) Ao processar a rotina GPEM080 para geração de CNAB folha de pagamento, é apresentada a mensagem :

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8432914672919)**

2) No fonte GPEM080 não tem a variável, NSOMAVALOR, sendo tratado apenas nos fontes do módulo Financeiro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8432887595927)

3) Desta forma existem as seguintes opções para geração do arquivo CNAB:

-> Verificar se o arquivo utilizado é o arquivo CNAB folha de pagamento e não algum arquivo CNAB do módulo Financeiro

-> Realizar a alteração no arquivo de configuração, podendo usar como exemplo o arquivo CNAB modelo padrão anexo.   
[RH - Linha Protheus - GPE - Editar Layout CNAB Pré definido através do Wizard CNAB (CFGX049a - SIGACFG)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5719944484759-RH-Linha-Protheus-GPE-Editar-Layout-CNAB-Pr%C3%A9-definido-atrav%C3%A9s-do-Wizard-CNAB-CFGX049a-SIGACFG-)

-> Em caso de necessidade de apoio, solicitar a abertura de um chamado para nosso time HUB para que seja realizado a análise e orçamento para sua demanda.

**Saiba Mais:**[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
