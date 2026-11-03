---
article_id: 29563709412247
category: eSocial - Gerar XML/ Integração Evento
content_hash: 9683113981baf73a0e033cf773c8cc326397fd851334c117c57973970f621f43
fetched_at: '2026-06-28T22:47:13.129711+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - S-1210 Erro Plano de saúde coletivo deve ser preenchido
  e Informações relacionadas a retenção na fonte, aos rendimentos tributáveis e não
  tributáveis, deduções e/ou isenções, etc., de acordo com a legislação aplicada ao
  imposto
type: support-article
updated_at: '2026-03-24T23:19:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29563709412247-RH-RM-FOP-eSocial-S-1210-Erro-Plano-de-sa%C3%BAde-coletivo-deve-ser-preenchido-e-Informa%C3%A7%C3%B5es-relacionadas-a-reten%C3%A7%C3%A3o-na-fonte-aos-rendimentos-tribut%C3%A1veis-e-n%C3%A3o-tribut%C3%A1veis-dedu%C3%A7%C3%B5es-e-ou-isen%C3%A7%C3%B5es-etc-de-acordo-com-a-legisla%C3%A7%C3%A3o-aplicada-ao-imposto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29563709379095) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**

Ao enviar o evento S-1210 para o Governo, ocorre o erro **Código 8: Grupo #39;Plano de saúde coletivo#39; deve ser preenchido. Verifique as condições de preenchimento no leiaute.**  
**Localização: /eSocial/evtPgtos/ideBenef/infoIRComplem**., seguida do erro **Código 8: Grupo #39;Informacoes relacionadas a retenção na fonte, aos rendimentos tributáveis e não tributáveis, deduções e/ou isenções, etc., de acordo com a legislação aplicada ao imposto de renda.#39; deve ser preenchido. Verifique as condições de preenchimento no leiaute.**  
**Localização: /eSocial/evtPgtos/ideBenef**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29629011313175)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2402.245; 12.1.2406.185; 12.1.2410.121 e Superiores.  
  
**Causa**

O erro ocorre pois, com a entrada do leiaute S-1.3, o governo passou a validar se foi encaminhado remuneração para o funcionário, onde há algum evento em que no governo consta com **Incidência de IRRF 67, 9067 ou Natureza de rubrica 9219**

**S-1.2**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29628981891863)

**S-1.3**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29629011323927)

**Solução**

Para solucionar a ocorrência referente ao plano de saúde de férias lançado no envelope, siga os passos descritos na documentação a seguir:

**1. Para casos de férias -** O evento de plano de saúde referente às férias, quando lançado no envelope, não pode possuir a natureza de rubrica 9219 nem a incidência CC014. Este código de cálculo e natureza de rubrica deverão constar somente no recibo de férias;  
[RH - RM - FOP - eSocial - Como cadastrar assistência de saúde nas férias do funcionário para correta geração da incidência no XML S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20039309735191-RH-RM-FOP-eSocial-Como-cadastrar-assist%C3%AAncia-de-sa%C3%BAde-nas-f%C3%A9rias-do-funcion%C3%A1rio-para-correta-gera%C3%A7%C3%A3o-da-incid%C3%AAncia-no-XML-S-1210)  
É necessário identificar que, se o governo está apontando o erro, é porquê em algum momento foi encaminho a informação no S-1200 incorretamente, ou seja, constando a natureza e as incidências informadas no erro. Com isto, após o ajuste é necessário:

1- Enviar o S-1010 da nova rubrica criada, com incidência igual ou anterior ao período referência indicado no S-1210. Exemplo: se as férias foram em dezembro/2024, será necessário enviar a rubrica com competência igual ou anterior a 12/2024;  
2- Retificar o S-1200 correspondente. Utilizando o exemplo do passo 1, seria necessário retificar o S-1200 12/2024.

**2. Para casos de folha mensal -** No caso de descontos relativos à assistência de saúde no envelope mensal, siga os passos de validação indicados na documentação abaixo:  
[RH - RM - FOP - eSocial - Assistência Saúde na geração do S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20025718353175-RH-RM-FOP-eSocial-Assist%C3%AAncia-Sa%C3%BAde-na-gera%C3%A7%C3%A3o-do-S-1210)

**3. Para casos de reembolso -** Onde o reembolso de assistência médica realizado pela empresa por meio do contra cheque, siga o procedimento abaixo:   
[Reembolso da Operadora de Assistência à Saúde](https://tdn.totvs.com/pages/releaseview.action?pageId=452718759)
