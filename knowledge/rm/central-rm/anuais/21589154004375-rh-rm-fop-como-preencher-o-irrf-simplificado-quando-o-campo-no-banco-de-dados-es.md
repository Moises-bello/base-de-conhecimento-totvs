---
article_id: 21589154004375
category: Anuais
content_hash: 972605dbf4c9c3ec0f43caa43bb3930099cbd1fb1456eb0c8e69c082d4badd5c
fetched_at: '2026-06-28T22:46:51.022185+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Como preencher o IRRF simplificado quando o campo no banco
  de dados estiver como NULL
type: support-article
updated_at: '2024-09-16T18:47:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21589154004375-RH-RM-FOP-Como-preencher-o-IRRF-simplificado-quando-o-campo-no-banco-de-dados-estiver-como-NULL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21589157670679) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como levar a marcação do IRRF simplificado para campo IRRFSIMPLIFICADO, IRRF13SIMPLIFICADO, IRRFFERSIMPLIFICADO .

**Ambiente**

O campo está disponível a partir dos patchs/releases abaixo:

* 12.1.2302.265
* 12.1.2306.228
* 12.1.2310.167
* 12.1.2402.107
* 12.1.2406

**Solução**

Atualmente existe os campos IRRFSIMPLIFICADO, IRRF13SIMPLIFICADO, IRRFFERSIMPLIFICADO na Tabela PFPERFF. Porém os mesmos não são visualizados e consequentemente não permitem edição por parte do usuário através da interface do período da ficha financeira. Quando os campos foram criados, foi disponibilizado nos patchs de mercado através do recurso de defensivo para que permitisse que o usuário executasse o cálculo da Folha sem a necessidade de executar o atualizador para que os campos fossem criados e assim não impedisse o lançamento do movimento para a Ficha Financeira do Colaborador.

Após o usuário executar o atualizador, estes campos são criados e preenchidos como NULL para toda a ficha financeira existente do Colaborador e para que os mesmos fosse preenchido com**0 - Não** ou **1 - Sim**, indicando se usou o valor simplificado para deduzir da base de IRRF de acordo com as regras do Cálculo de IRRF, era necessário executar o recalculo.

Porém em muitos casos a Folha já havia fechado ou até mesmo alterada de competência, não sendo possível que o usuário executasse o recalculo. 

Criar os campos no período da ficha financeira e Ficha financeira complementar, com as opções Sim ou Não, permitindo que o usuário marque a opção de acordo com o cálculo que foi executado nos casos em que o campo esteja como NULL.

Para os casos onde os campos já estavam preenchidos ou após o usuário informar, estes campos ficarão desabilitados para Edição permitindo somente a Visualização.

* [Campo como NULL no banco](https://tdn.totvs.com.br/pages/releaseview.action?pageId=827305670#tabs-passo1)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21589157672983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21589157673623)

Atenção: O campo só ficará habilitado para marcar quando o campo no banco estiver como NULL

Saiba mais: [DT - IRRF Simplificado - Indicativo de Cálculo no Período da Ficha Financeira](https://tdn.totvs.com.br/pages/releaseview.action?pageId=827305670)
