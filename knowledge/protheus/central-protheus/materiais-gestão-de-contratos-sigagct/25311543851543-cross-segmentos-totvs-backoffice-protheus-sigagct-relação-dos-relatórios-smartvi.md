---
article_id: 25311543851543
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 27b16ab243cfffcc04c4a0fe653ac0824ab1acfa2c9bc801ce2707cce14c7fa3
fetched_at: '2026-06-28T22:37:24.110076+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Relação dos relatórios
  SmartView do módulo Gestão de Contratos
type: support-article
updated_at: '2026-05-29T13:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25311543851543-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Rela%C3%A7%C3%A3o-dos-relat%C3%B3rios-SmartView-do-m%C3%B3dulo-Gest%C3%A3o-de-Contratos
---

O artigo apresenta uma lista de relatórios SmartView para o módulo Gestão de Contratos do TOTVS Protheus, destacando que não substituem exatamente os relatórios descontinuados, mas oferecem uma solução inovadora com novos conceitos e informações. Explica funcionalidades, filtros disponíveis, opções de personalização. Links para documentação e quais relatórios estão disponíveis para consulta.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25311543838743) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
  
Relação dos relatórios SmartView do módulo Gestão de Contratos  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de Contratos - Todas as versões   
  
**Solução**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25457597619479)**

Abaixo disponibilizamos uma lista de relatorios do smartview que pode conter informações semelhantes aos relatorios descontinuados!

**Importante:** Os relatorios Smartview possuem novos conceitos sobre a visão dos dados, ou seja, ele NÃO é um substituo exato dos relatorios descontinuados, e sim solução inovadora. Dessa forma, existem informações dos antigos relatorios que não serão apresentados no Smartview, assim como poderá ter novas informações que não existiam nos antigos relatorios.

* [Smart View - Contratos](https://tdn.totvs.com/display/PROT/Smart+View+-+Contratos)
* [Smart View - Medições de Contratos](https://tdn.totvs.com/pages/viewpage.action?pageId=818472008)
* [Smart View - Medições não Efetuadas](https://tdn.totvs.com/pages/viewpage.action?pageId=818470364)
* [Smart View - Medições por Fatura](https://tdn.totvs.com/pages/viewpage.action?pageId=819064441)
* [Smart View - Recebíveis por Medição](https://tdn.totvs.com/pages/viewpage.action?pageId=874608250)

Segue lista do TDN abaixo com todos os novos relatórios do SmartView

[Smart View - Gestão de Contratos](https://tdn.totvs.com/pages/releaseview.action?pageId=840391656)

***Obs1:***

Por padrão, o Relatório "[Smart View - Medições não Efetuadas](https://tdn.totvs.com/pages/viewpage.action?pageId=818470364)" possui funcionalidade de trazer informações de medições apenas de Contratos com Cronograma Financeirio (Medição Eventual=Não), não possuindo característica de trazer informações de medições de Contratos sem Cronograma Financeiro (Medição Eventual=Sim).

***Obs2:***

Caso se deseje realizar algum tipo de personalização/customização em relatórios Smartview, para o apoio e como realizar, orientamos o contato junto a suporte ao Framework para este apoio e orientação.

***Obs3:***

Existe um relatório que demonstre o valor do contrato líquido em uma determinada data específica?

R:O relatório que possui de  contratos é [Smart View - Contratos](https://tdn.totvs.com/display/PROT/Smart+View+-+Contratos) Relatório CNTSV010, nesse relatório o filtro por Data é da Data é apenas pela data de vigência do contrato. Não é apresentado os valores de saldo por datas específicas é demonstrado os saldos atuais do contrato, assim como é demonstrado na visualização do contrato.

***Obs4:***

No configurador do sistema em **Ambientes >Smartview> Integração Smartview** tem a opção de menu "Personalização de Campos", que permite adicionar novos campos em um objeto de negócio.

Atenção

* Não é possível adicionar campos MEMO ou virtual.
* Para que o campo apareça na listagem o mesmo precisa estar configurado como "Usado" no SX3

Veja mais detalhes na documentação: [Amarração Protheus x Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=708098869)

Em caso de dúvidas na customização de relatórios Smartview, orientamos o contato junto ao suporte ao Framework do Protheus.

***Obs5:***

Qual relatório é possível filtrar todos os contratos em abertos e parcialmente recebidos?

**R:**É possível utilizar o relatório de contratos [Smart View - Contratos](https://tdn.totvs.com/display/PROT/Smart+View+-+Contratos) Relatório CNTSV010 nele é possível utilizar os os filtros abaixo para visualização dos contratos.

No relatório estão disponíveis filtros:

* **Número do contrato**
* **Revisão**
* **Período da Vigência**
* **Situação do contrato:**

  Podendo ser preenchido com:  
  01  -  Cancelado  
  02  -  Em Elaboração  
  03  - Emitido  
  04  - Em Aprovação  
  05  - Vigente  
  06  - Paralisado  
  07  - Solicitação de Finalização  
  08  - Finalizado  
  09  - Em Revisão  
  10  - Revisado  
  11  -  Rejeitado
* **Fornecedor**
* **Cliente**

Dessa forma, basta selecionar os filtros desejados para visualizar para visualizar os contratos conforme os filtros de busca.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40819104288023)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40819104288151)

***Saiba Mais:***

[Relatórios - Descontinuados a partir de 31/10/2024](https://tdn.totvs.com/pages/releaseview.action?pageId=860251495)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o SmartView ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21746957789463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-SmartView)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
