---
article_id: 38044195483287
category: Financeiro - Serasa
content_hash: a9389b2192cac90d7dd4ea4a138c4cd53564da4ac9bae096a3e9acacddb55c29
fetched_at: '2026-06-28T22:37:28.263233+00:00'
product: protheus
section_id: 35058289522071
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA770 - Integração Serasa
type: support-article
updated_at: '2026-04-29T17:30:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38044195483287-Cross-Segmentos-Backoffice-Linha-Protheus-FINA770-Integra%C3%A7%C3%A3o-Serasa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38044195464471) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
O protheus possui integração com o Serasa?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA770 - Todas as versões.  
  
**Solução**  
A integração com a SERASA (rotina **SERASA RELATO**) está descontinuada em todas as releases do Protheus e, **a****partir da versão 12.1.2510, seu acesso tornou-se indisponível**. Nas versões anteriores, a rotina ainda pode ser utilizada, porém, por estar descontinuada, não conta mais com suporte, evolução ou manutenção.

Essa descontinuidade ocorreu em função do encerramento da parceria entre a TOTVS e a Serasa, razão pela qual não há documentação atualizada para essa integração.

Dessa forma, não são realizadas alterações, melhorias ou manutenções na rotina SERASA RELATO, nem mesmo por meio de integrações via WebServices (IP-23). Da mesma forma, não haverá inclusão de novas funcionalidades da SERASA, como consultas de crédito ou conciliação, uma vez que a TOTVS não possui mais acesso às tecnologias (libs, funções e documentações) anteriormente disponibilizadas.

Como alternativa, atualmente existe um processo no módulo financeiro que permite a exportação da base de títulos do Protheus para posterior importação no serviço **PEFIN**d**a Serasa Experian**, por meio da rotina [**FINA770**](https://tdn.totvs.com/x/_aGcHQ).

**Saiba mais**

[Serasa - FINA770](https://centraldeatendimento.totvs.com/hc/pt-br/sections/35058289522071-Financeiro-Serasa)
