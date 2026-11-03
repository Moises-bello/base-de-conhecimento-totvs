---
article_id: 24300803419543
category: Financeiro - Configurador de Tributos
content_hash: be2263dc8245abf69677713dc83fc965bec4816b6792c1a562a5294ef75720f5
fetched_at: '2026-06-28T22:37:45.841533+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como deduzir
  o valor do imposto no tipo NF que gerou no contas a receber, onde o seu imposto
  gerou um tipo ISS no contas a pagar pelo configurador de tributos?
type: support-article
updated_at: '2025-09-15T19:26:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24300803419543-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-deduzir-o-valor-do-imposto-no-tipo-NF-que-gerou-no-contas-a-receber-onde-o-seu-imposto-gerou-um-tipo-ISS-no-contas-a-pagar-pelo-configurador-de-tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24300803397911) Tempo aproximado para leitura: **15:00:00 min****Dúvida**Como deduzir o valor do imposto no tipo NF que gerou no contas a receber, em que o seu imposto gerou um tipo ISS no contas a pagar pelo configurador de tributos vindo do faturamento.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

A primeira etapa é criar as Regras Fiscais e Financeiras disponíveis no configurador de tributos **FISA170,** atentando-se às Regras de Escrituração.

Os cadastros básicos não devem conter parametrizações de impostos porque serão tratados pelo configurador de tributos.

**Configurador de tributos:**

Para o tratamento específico de abatimento de ISS no contas a receber, acesse:

**Regras Fiscais / Regras de Escrituração / Guia Incidência**

**1.** Cálculo do ISS com abatimento na Nota Fiscal no Contas a Receber.

No campo Total da Nota, selecione a opção:

"4 - Subtrair somente do total da duplicata" e, no campo "Percentual de Diferimento", deixe zerado.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24309945843607)](https://centraldeatendimento.totvs.com/hc/article_attachments/24309945843607)

Exemplo do cálculo - Nota com abatimento do ISS:

Nota de R$ 10.000.

Vlr. Imposto (5%): R$ 500.

Nota deduzindo o valor do abatimento: R$ 9.500.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24300803401111)](https://centraldeatendimento.totvs.com/hc/article_attachments/24300803401111)

**Segue exemplo de cadastros:**

**1)** FISA710 - **Regras Fiscais** > Perfis > **Perfil do Produto**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321540381079)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321540381079)

Segue exemplo de cadastro

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321518369687)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321518369687)

**2)** FISA710 - **Regras Fiscais** > Perfis > **Perfil de Participante**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321540428951)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321540428951)

Segue exemplo de cadastro:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321518396183)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321518396183)

**3)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Base de Cálculo**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321518407447)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321518407447)

Segue exemplo de cadastro:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321540465943)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321540465943)

**4)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Alíquota**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534360727)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534360727)

Segue exemplo de cadastro

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534365079)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534365079)

**5)** FISA710 - **Regras Fiscais** > Regras de Cálculo Documento Fiscal > **Regra de Escrituração**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553810327)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553810327)

Segue exemplo de cadastro:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553820951)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553820951)

**6)** FISA710 - **Regras Financeiras** > Regra do Título

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553832983)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553832983)

Segue exemplo de cadastro:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553840407)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553840407)

**7)** FISA710 - **Regras Financeiras** > Regra de Cálculo - Títulos Financeiros

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553846295)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553846295)

Segue exemplo:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553852439)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553852439)

**8)** FISA710 - **Regras Financeiras** > Regra de Vencimento

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553855767)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553855767)

Segue exemplo:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553859607)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553859607)

**9)** FISA710 - **Regras Financeiras** > Regra de Retenção

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534423063)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534423063)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553864727)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553864727)

**10)** FISA710 - **Regras Financeiras** > Regras Financeiras

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553874839)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553874839)

Segue exemplo de cadastro:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534460183)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534460183)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534484887)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534484887)

**11)** FISA710 - **Regras Fiscais** > Regras de Cálculo - Documentos Fiscais> **Regra de Cálculo - Documentos Fiscais**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534495127)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534495127)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553931799)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553931799)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553962391)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553962391)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553966999)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553966999)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534546967)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534546967)

**12)** Inclusão da nota pelo módulo Faturamento no valor de R$ 10.000 com imposto de ISS no valor de R$ 500.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534550423)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534550423)

**13)** **FINA040** - Geração da NF no contas a receber com o número 000005 no valor de **R$ 9.500.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534555159)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321534555159)

**14)** **FINA050** - Geração do imposto ISS no contas a pagar com o número 000005 no valor de **R$ 500.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553994775)](https://centraldeatendimento.totvs.com/hc/article_attachments/24321553994775)

**Saiba mais**

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10)

[Regras de Escrituração](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10#CFGTRIBConfiguradordeTributos12.1.22.10-CadastrodeRegradeEscritura%C3%A7%C3%A3o)
