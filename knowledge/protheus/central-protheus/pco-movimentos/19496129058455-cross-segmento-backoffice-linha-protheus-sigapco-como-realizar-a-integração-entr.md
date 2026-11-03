---
article_id: 19496129058455
category: PCO - Movimentos
content_hash: 9e113ed857c008be3d0ec9778ffd8c05ee94f0b1b312e636dca4626f02d2a276
fetched_at: '2026-06-28T22:37:09.496257+00:00'
product: protheus
section_id: 1500001550962
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Como realizar a integração
  entre os módulos do Protheus com o PCO.
type: support-article
updated_at: '2023-12-04T15:09:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19496129058455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Como-realizar-a-integra%C3%A7%C3%A3o-entre-os-m%C3%B3dulos-do-Protheus-com-o-PCO
---

**Dúvida**Como Realizar a integração dos módulo com o PCO.  
  
**Ambiente**

Cross Segmento - BackOffice Linha Protheus - Planejamento e Controle orçamentário  - Todas as versões  
  
**Solução**

Para realizar a integração dos módulo com com o PCO é necessário que siga os passos abaixo:

**1°** Habilitar o parametro MV\_PCOINTE = 1

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Conceito - Principais parâmetros e Principais tabela do módulo PCO - Planejamento e Controle Orçamentário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017496452-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Conceito-Principais-par%C3%A2metros-e-Principais-tabela-do-m%C3%B3dulo-PCO-Planejamento-e-Controle-Or%C3%A7ament%C3%A1rio)

**2°** Incluir Orçamento para o processo e para entidades que iram integrar com o PCO:

- Elaborar**Planilha Orçamentária (Rotina PCOA100)**

Após o preenchimento dos cadastros a planilha orçamentária pode ser criada definindo suas contas orçamentárias, informando a periodicidade e seus valores, além da classe/operação e entidades contábeis.

**Saiba mais**

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO- PCOA100 - Cadastro de conta orçamentária na planilha.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403022922391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA100-Cadastro-de-conta-or%C3%A7ament%C3%A1ria-na-planilha-?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA100 Importação de Dados na Planilha Orçamentaria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001416102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA100-Importa%C3%A7%C3%A3o-de-Dados-na-Planilha-Or%C3%A7amentaria?source=search)

**3 °** Cadastrar um Processo para integração envolvendo as entidades que utilizara para integração, através da rotina PCOA030:

- Configurar o processo na rotina PCOA030:

#### [Configuração de Lançamentos por Processo (PCOA030)](https://tdn.totvs.com/pages/viewpage.action?pageId=691437643)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA030 Quais são as Rotinas que possuem integração com o Módulo PCO ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018809411-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA030-Quais-s%C3%A3o-as-Rotinas-que-possuem-integra%C3%A7%C3%A3o-com-o-M%C3%B3dulo-PCO-?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA030 - Configuração on-line dos lançamentos por processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567972-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA030-Configura%C3%A7%C3%A3o-on-line-dos-lan%C3%A7amentos-por-processo?source=search)

**4 °** Após configurado o processo na rotina PCOA030 e habilitado o parametro basta realizar o processo na rotina de origem do lançamento configurado, que as informações serão levadas para o PCO, alimentando a tabela AKD e AKT.

**Os vídeos abaixo demonstram com mais detalhes as informações sobre o processo de integração mencionado:**

#### **How To | MP - SIGAPCO - Integrações Parte 01**

#### **How To | MP - SIGAPCO - Integrações Parte 02**

#### **How To | MP - SIGAPCO - Integrações Parte 03**

***Saiba Mais :***

#### [Controladoria - PCO - Protheus 12](https://tdn.totvs.com/display/PROT/Controladoria+-+PCO+-+Protheus+12)

#### [Planejamento e Controle Orçamentário (SIGAPCO)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545582-Planejamento-e-Controle-Or%C3%A7ament%C3%A1rio-SIGAPCO-)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - CheckList para utilização do modulo Planejamento de Custos Orçamentários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017496452-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Conceito-Principais-par%C3%A2metros-e-Principais-tabela-do-m%C3%B3dulo-PCO-Planejamento-e-Controle-Or%C3%A7ament%C3%A1rio?source=search#title-text)

#### [How To PCO - Planejamento e Controle Orçamentário - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=763235880)
