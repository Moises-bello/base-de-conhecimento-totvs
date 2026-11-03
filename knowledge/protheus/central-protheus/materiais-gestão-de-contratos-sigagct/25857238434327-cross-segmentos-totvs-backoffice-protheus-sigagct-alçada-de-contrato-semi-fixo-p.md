---
article_id: 25857238434327
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 39aa9d4854053322ae7ec54eeaa688120a4bad7d35ca05a13658ed5eb61375c5
fetched_at: '2026-06-28T22:37:20.331673+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alçada de Contrato
  Semi-fixo pelo Total da Planilha do Contrato (CT) e por Entidades Contabeis (IC)
type: support-article
updated_at: '2025-11-13T11:13:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25857238434327-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Al%C3%A7ada-de-Contrato-Semi-fixo-pelo-Total-da-Planilha-do-Contrato-CT-e-por-Entidades-Contabeis-IC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25857238408343) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

É possível gerar a alçada de Contrato Semi-fixo pelo Total da Planilha do Contrato (Docto alçada tipo "CT") e por Entidades Contábeis (Docto alçada tipo "IC") ?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

**Alçada Sem Entidades Contabeis (Docto alçada tipo "CT"):**

Sim, é possível realizar essa configuração por meio da Alçada de Contrato por Tipo Documento (Tipo de docto da alçada "CT"). Dessa forma, o campo CR\_TOTAL será preenchido com o valor total da planilha.

Segue o link da documentação:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como habilitar controle de alçada na mudança de situação / revisão do contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000766347-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-habilitar-controle-de-al%C3%A7ada-na-mudan%C3%A7a-de-situa%C3%A7%C3%A3o-revis%C3%A3o-do-contrato)

**Obs:**

Nesse Tipo de Alçada (sem Entidades Contabeis, Docto da alçada Tipo "**CT**") é permitido utilizar a Configuração de Semi-fixo por Produto e Semi-fixo por Agrupador.

**Alçada por Entidades Contabeis (Docto alçada tipo "IC"):**

Para o processo de Alçada Por Entidade Contábil (Tipo de docto da alçada "IC") é possível alçada para planlha Semi-Fixa desde que se configure o **Valor mínimo do cadastro do Perfil de Aprovação atrelado ao aprovador no grupo de aprovação com "0,00"**, pois, o tipo de contrato Semi-fixo, valida o bloqueio/alçada por item do Contrato/Planilha e o campo CR\_TOTAL será sempre preenchido com "0", pois, a quantidade para contratos semi-fixo será informada apenas na Inclusão da Medição.

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alçada Por Entidade Contábil na Mudança de Situação do Contrato e / ou Revisão do Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404552326039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Al%C3%A7ada-Por-Entidade-Cont%C3%A1bil-na-Mudan%C3%A7a-de-Situa%C3%A7%C3%A3o-do-Contrato-e-ou-Revis%C3%A3o-do-Contrato?source=search)

**Obs:**

No processo de alçada por Entidade contábil **só é permitido configurar alçada em Contratos/planilha Semi-Fixo "Por Produto"**, já para **Contrato Semi-Fixo "Por Agrupador"** não é possível realizar a configuração visto que este não possui item na planilha configurado com seu respectivo centro de custo/entidade contábil vinculado no item da planilha do contrato, e como a particularidade da alçada por Entidade Contabil ser por item e por valor, com o não há item, nõa há como possuir este tipo de alçada (por Entidade Contabil, no Semi-Fixo "Por Agrupador").

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como habilitar controle de alçada na mudança de situação / revisão do contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000766347-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-habilitar-controle-de-al%C3%A7ada-na-mudan%C3%A7a-de-situa%C3%A7%C3%A3o-revis%C3%A3o-do-contrato)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
