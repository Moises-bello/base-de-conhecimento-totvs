---
article_id: 360017783691
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d894c390ff1a5d96e97146a892039d795224e333b5cff36a86a914e7be9371b0
fetched_at: '2026-06-28T22:38:29.853885+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Notas sobre o uso da consulta
  ao SERASA no Microsiga Protheus
type: support-article
updated_at: '2026-04-07T18:27:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017783691-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Notas-sobre-o-uso-da-consulta-ao-SERASA-no-Microsiga-Protheus
---

**Dúvida**

Há alguma documentação para integrar o Protheus com a interface **SERASA**?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - desde a release 11.80.  
  
**Solução**

A integração com a SERASA (rotina **SERASA RELATO**) está descontinuada em todas as releases do Protheus e, **a****partir da versão 12.1.2510, seu acesso tornou-se indisponível**. Nas versões anteriores, a rotina ainda pode ser utilizada, porém, por estar descontinuada, não conta mais com suporte, evolução ou manutenção.

Essa descontinuidade ocorreu em função do encerramento da parceria entre a TOTVS e a Serasa, razão pela qual não há documentação atualizada para essa integração.

Dessa forma, não são realizadas alterações, melhorias ou manutenções na rotina SERASA RELATO, nem mesmo por meio de integrações via WebServices (IP-23). Da mesma forma, não haverá inclusão de novas funcionalidades da SERASA, como consultas de crédito ou conciliação, uma vez que a TOTVS não possui mais acesso às tecnologias (libs, funções e documentações) anteriormente disponibilizadas.

Como alternativa, atualmente existe um processo no módulo financeiro que permite a exportação da base de títulos do Protheus para posterior importação no serviço **PEFIN** d**a Serasa Experian**, por meio da rotina [**FINA770**](https://tdn.totvs.com/x/_aGcHQ).
