---
article_id: 360035192133
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 840488f642ed7d67b7205bc3da3ae57bb29ed1efeca63a0f5508ca2239090dbf
fetched_at: '2026-06-28T22:37:21.626015+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a Revisão
  de Índices de um Contrato ?
type: support-article
updated_at: '2023-07-03T15:51:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035192133-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-Revis%C3%A3o-de-%C3%8Dndices-de-um-Contrato
---

**Dúvida**Como realizar a Revisão de Índices de um Contrato ?  
  
**Ambiente**Microsiga Protheus – Gestão de contratos – A partir da versão 12   
  
**Solução**Permite a troca do índice econômico, sua periodicidade e habilitar ou desabilitar o pro rata associado a um contrato.  
A escolha desta opção não habilita o preenchimento dos campos **Modo** e **Espécie**.

**Obs:** Só será permitido efetuar a revisão de índices se, no cabeçalho do contrato, o campo Reajuste S/N **(CN9\_FLGREAJ) =**Sim e o campo Indice **(CN9\_INDICE)** estiverpreenchido com o Índice.

Para solucionar essa dúvida, realize os seguintes passos:

1. Realize o cadastro do tipo da revisão de índice acesse >Cadastros>Tipos >Revisões rotina**(CNTA010)>**Incluir.

No campo tipo selecione a opção 9 = Índices

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045901453)

2. Acesse a rotina Manutenção de Contratos**(CNTA300)**e clique em Outras Ações>Revisões>Índices.

- Selecione o tipo de revisão de índice no campo Tipo de Revisão**(CN9\_TIPREV)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045041374)

- Serão habilitados os campos: Indice (**CN9\_INDICE**) do cabeçalho do contrato, Un.Per.Reaj(**CNA\_UNIPERI),**Ìndice **(CNA\_INDICE),**Períod.Reaju **(CNA\_PERI),** Modo **(CNA\_MODORJ)** e Pró-Rata **(CNA\_PRORAT)** da planilha para que possam ser ajustados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15747957698839)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045037594)

**Exemplo:**

*Dados do Contrato Antes do Reajuste de Índices*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Índice** | **Un.Per.Reaj** | **Períd.Reaju** | **Modo** | **Pro Rata** |
| IGP-DI | Meses | 3 | Por Data | Não |

*Contrato Reajustado*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Índice** | **Un.Per.Reaj** | **Períd.Reaju** | **Modo** | **Pro Rata** |
| IGP-M | Anos | 1 | Por Competência | Sim |

**Obervação 2**:Os campos de Reajuste tanto do Cabeçalho do Contrato **(CN9\_FLGREAJ).**,Reajuste da Planilha **(CNA\_FLGREAJ)** e Reajuste do Item **(CNB\_FLGREAJ)**são bloqueados para alteração nessa revisão , os mesmos poderão ser preenchidos somente na inclusão do Contrato ou os campos ,Reajuste da Planilha **(CNA\_FLGREAJ)** e Reajuste do Item **(CNB\_FLGREAJ)** podem ser editados na inclusão de uma Nova Planilha do Contrato caso o campo Reajuste S/N **(CN9\_FLGREAJ)** esteja preenchido = **Sim** através da Revisão de Aditivo ou de Renovação

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a Configuração e Revisão de Reajuste em Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059174393-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-Configura%C3%A7%C3%A3o-e-Revis%C3%A3o-de-Reajuste-em-Contratos-?source=search)

[MP - SIGAGCT - Como aumentar ou reduzir os meses e redistribuição das parcelas de um contrato na Revisão de Aditivo ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028039532-MP-SIGAGCT-Como-aumentar-ou-reduzir-os-meses-e-redistribui%C3%A7%C3%A3o-das-parcelas-de-um-contrato-na-Revis%C3%A3o-de-Aditivo-?source=search)

[MP - SIGAGCT - Revisão de Renovação para adição de novos itens, planilhas, preço unitário, prazo e condição de pagamento no contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659713-MP-SIGAGCT-Revis%C3%A3o-de-Renova%C3%A7%C3%A3o-para-adi%C3%A7%C3%A3o-de-novos-itens-planilhas-pre%C3%A7o-unit%C3%A1rio-prazo-e-condi%C3%A7%C3%A3o-de-pagamento-no-contrato?source=search)
