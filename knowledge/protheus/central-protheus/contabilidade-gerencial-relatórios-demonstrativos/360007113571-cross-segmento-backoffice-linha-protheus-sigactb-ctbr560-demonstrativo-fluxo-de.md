---
article_id: 360007113571
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: 0084e9459c3ab200c4cb3ac1652930bf018f4505a3c7393d7cb35d8c348a4b91
fetched_at: '2026-06-28T22:40:38.829891+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR560 - Demonstrativo
  Fluxo de Caixa, DFC
type: support-article
updated_at: '2026-04-28T17:15:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007113571-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR560-Demonstrativo-Fluxo-de-Caixa-DFC
---

**Duvida**  
Como configurar visão gerencial DFC -Demonstrativo Fluxo de Caixa  (CTBR560)?

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80

**Solução**

A extração das informações Demonstrativo Fluxo de Caixa deve ser gerado pelo relatório CTBR560 A qual pede a existência de  visão gerencial, para sua impressão, que devera ser configurada, para a extração das informações necessárias.

Esta configuração sera montada conforme a movimentação em contas que trata os saldos que movimenta os dados que deseja

Modelos

Para configuração, temos modelos, podendo ser configurados e amarrados com plano de contas da empresa, disponíveis no portal do cliente.

<https://suporte.totvs.com/portal/p/10098/download#company/>

acesso ao cliente > suporte/portal cliente>Download

Linha de produto > Protheus

Software > Todos

Categoria > arquivo modelo

localize o arquivo  **CTB - Modelos de Visão Gerencial**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27160342529815)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27160329706903)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27160342533527)

Para que o relatório traga a variação entre os períodos (sem uso do parâmetro "Variação?", é necessário configuração uma expressão no campo "Fórmula", na estrutura da Visão Gerencial.  
  
Nesta configuração, poderá aplicar uma função de usuário, conforme sua necessidade.

**Saiba mais:**  
- Expressões Especiais:  
[**http://tdn.totvs.com.br/pages/releaseview.action?pageId=234455566**](http://tdn.totvs.com.br/pages/releaseview.action?pageId=234455566)

[**https://tdn.totvs.com/pages/releaseview.action?pageId=6068417**](https://tdn.totvs.com/pages/releaseview.action?pageId=6068417)

- Campo Fórmula:  
[**http://tdn.totvs.com.br/pages/releaseview.action?pageId=233766503**](http://tdn.totvs.com.br/pages/releaseview.action?pageId=233766503)

**\***O suporte help desk não auxilia na montagem da visão gerencial e nem desenvolve fórmulas. Caso sinta dificuldades, sugerimos analista  de sua confiança in loco para criar a visão de acordo com a necessidade da empresa.  
  
[Campos e exemplos para criação de estrutura](https://tdn.totvs.com/pages/releaseview.action?pageId=235569753)

[Remoção da Exibição dos Campos CVF\_SLDENT e CTS\_SLDENT da Visão Gerencial (CTBA161)](https://tdn.totvs.com/pages/viewpage.action?pageId=337349007)

**Saiba mais**  
[MP - SIGACTB - CTBA161 - Arquivos modelos Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006687252-MP-SIGACTB-CTBA161-Arquivos-modelos-Vis%C3%A3o-Gerencial)

[Visão Gerencial - Modos de exibição da Visão Gerencial](https://tdn.totvs.com/pages/viewpage.action?pageId=6068447)

[Visão Gerencial - Uso de fórmulas](https://tdn.totvs.com/pages/releaseview.action?pageId=6068421)

[\_\_Acervo - CPC 03: Demonstração dos Fluxos de Caixa (IAS 7](https://tdn.totvs.com/pages/releaseview.action?pageId=62390997))

[Modo de exibição da Visão Gerencial](https://tdn.totvs.com/pages/releaseview.action?pageId=6068447)

[MP - SIGACTB CTBA161 - Detalhamento da funcionalidade dos campos CTS\_FATSLD, CTS\_SLDENT, CTS\_VISENT, CTS\_TOTVIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016012672-MP-SIGACTB-CTBA161-Detalhamento-da-funcionalidade-dos-campos-CTS-FATSLD-CTS-SLDENT-CTS-VISENT-CTS-TOTVIS)

[DSERCTR1-28389 Função FTENTIDADE não compõe saldo anterior no DFC](https://tdn.totvs.com/pages/releaseview.action?pageId=234455566)
