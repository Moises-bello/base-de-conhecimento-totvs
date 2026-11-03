---
article_id: 4408161095575
category: Inspeção de Entradas (SIGAQIE)
content_hash: 941c23ba829990160622ce2690fec863cd7537b901d90d1e8a982860a0292b6a
fetched_at: '2026-06-28T22:42:27.064364+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Legenda não aparece no plano de amostragem
type: support-article
updated_at: '2021-09-10T12:21:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408161095575-Manufatura-Linha-Protheus-SIGAQIE-Legenda-n%C3%A3o-aparece-no-plano-de-amostragem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:20 min** **Dúvida**Por quê na rotina **QIEA215 - Resultados**, quando é utilizado **Plano de Amostragem - QIPA160**, ao realizar o registro de uma **medição** como **rejeitado** não ocorre a atualização da **legenda**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**

Na rotina **QIEA215 - Resultado** ao digitar uma medição como rejeitada, isto não indica que o ensaio em questão foi rejeitado, pois de acordo com o configurado no **Plano de Amostragem - QIPA160**, existe um número de rejeites tolerados. Além disto, a legenda dos ensaios é atualizada de acordo com a quantidade de **NCs - Não Conformidades** digitadas na aba **Não Conformidades**, desconsiderando o número de medições rejeitadas.  
O correto é que o usuário associe uma ou mais **NCs** para cada medição rejeitada. No entanto, atualmente o **SIGAQIE - Inspeção de Entradas** não obriga este preenchimento da **NC - Não Conformidade**.  
  
Para realizar validações adicionais poderão ser utilizados os pontos de entrada à seguir:

* [Q215PINT - Contagem do Plano Interno](https://tdn.totvs.com/display/public/PROT/Q215PINT+-+Contagem+do+Plano+Interno)
* [QE215LE - Criação de Regra](https://tdn.totvs.com/pages/releaseview.action?pageId=6802966)
* [Q215PL1 - Não Conformidade Plano de Amostragem](https://tdn.totvs.com/pages/releaseview.action?pageId=6802950)
* [Q215QNCI - Gravação de Medições](https://tdn.totvs.com/pages/releaseview.action?pageId=6802954)

**Saiba mais**  
A documentação disponível no *link* à seguir detalhada como é realizada a validação : [Planos de Amostragem (QIPA160)](https://tdn.totvs.com/pages/releaseview.action?pageId=306860217)
