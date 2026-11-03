---
article_id: 360052535713
category: Integrações Nativas
content_hash: 8cc0eb0785b08df6250cd38ad2f9161c450aba50c2fa0566826952e088daf2a9
fetched_at: '2026-06-28T22:42:35.406189+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Finalização ou Cancelamento da O.S com
  S.A ou S.C
type: support-article
updated_at: '2021-06-02T14:44:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052535713-Manufatura-Linha-Protheus-MNT-Finaliza%C3%A7%C3%A3o-ou-Cancelamento-da-O-S-com-S-A-ou-S-C
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:45 min**  
**Dúvida**Qual é o comportamento da **S.A. -****Solicitação de Armazém** ou **S.C. - Solicitação de Compra** ao **Finalizar** ou **Cancelar** uma **O.S. - Ordem de Serviço** no **Manutenção de Ativos** ou **Gestão de Frotas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**As informações, referentes ao **Cancelamento** e **Finalização** de uma **O.S.** com **S.A.** ou com **S.C.** serão detalhadas conforme passo a passo abaixo:  
  
Define se aglutina as **S.As** para a mesma**O.S.,** sendo **1 - Sim**, **2 - Não**.

| Parâmetro | Conteúdo |
| --- | --- |
| **MV\_NGMNTAS - Define se aglutina as Solicitações de Armazém para a mesma Ordem de Serviço** | **1** |
| **MV\_NGGERSA - Indica se deve gerar Solicitação ao Armazém em vez de gerar Solicitação de Compra.** | **S** ou **P** |

**Cancelamento  
Sem Pré-requisição**  
**OS 000001**

| Produto | Número da S.A. |
| --- | --- |
| P1 | 000001 |
| P2 | 000001 |

Quando não há**Pré-Requisição** a **S.A.** é **deletada** assim que a **O.S.** é **Cancelada**.  
  
**Cancelamento**  
**Gera Pré-requisição  
O.S. 000001**

| Produto | Número da S.A | Número da S.C. |
| --- | --- | --- |
| P1 | 000002 | 000003 |
| P2 | 000002 | 000003 |

Quando há **Pré-requisição** é gerada uma **S.C.** e não é permitido **Cancelar** a **O.S.** pelo **Manutenção de Ativos - SIGAMNT,** por haver relacionamento com uma **S.A**.  
  
**Finalizar O.S.**  
**Sem Pré-requisição  
O.S. 000002**

| Produto | Número da S.A. |
| --- | --- |
| P3 | 000003 |
| P4 | 000003 |
| P5 | 000003 |

Quando não há **Pré-requisição** somente é permitido **finalizar** a**O.S**. se forem realizados insumos diferentes dos relacionados à **S.A.  
  
Finaliza O.S.****Gera Pré-requisição****O.S. 000002**

| Produto | Número da S.A. | Número da S.C. |
| --- | --- | --- |
| P3 | 000004 | 000005 |
| P4 | 000004 | 000005 |
| P5 | 000004 | 000005 |

Quando há **Pré-requisição** é gerada uma **S.C.,** e ao executar a **Baixa da Pré-requisição,**para que os insumos sejam realizados, a **S.C.**é **deletada**. Ao finalizar-se a **O.S.,** a **S.A.** é mantida para que se mantenha o registro da **S.C.** gerada através da **Pré-requisição**.  
Define se aglutina as **S.As** para a mesma **O.S.,** sendo**1 - Sim, 2 - Não**.

| Parâmetro | Conteúdo |
| --- | --- |
| **MV\_NGMNTAS** | **2** |
| **MV\_NGGERSA** | **S** ou **P** |

**Cancelamento  
Sem Pré-requisição  
O.S. 000003**

| Produto | Número da S.A. |
| --- | --- |
| P1 | 000006 |
| P2 | 000007 |
| P3 | 000008 |

Quando não há **Pré-requisição** a **S.A.** é **deletada** assim que a**O.S**. é **Cancelada**.  
  
**Cancelamento  
Gera** **Pré-requisição****O.S. 000003**

| Produto | Número da S.A. | Número da S.C. |
| --- | --- | --- |
| P1 | 000009 | 000012 |
| P2 | 000010 | 000013 |
| P3 | 000011 | 000014 |

Quando há **Pré-requisição**é **gerada uma S.C.,** e não é permitido cancelar a **O.S.** pelo **SIGAMNT** por haver relacionamento com uma **S.A**.  
  
**Finalizar O.S.  
Sem Pré-requisição  
O.S. 000004**

| Produto | Número da S.A. |
| --- | --- |
| P4 | 000009 |
| P5 | 000010 |
| P6 | 000011 |

Quandonão há **Pré-requisição** somente é permitido **finalizar** a **O.S**. se forem realizados insumos diferentes dos relacionados à **S.A.****Finalizar O.S.  
Gera** **Pré-requisição****OS 000004**

| Produto | Número da S.A. | Número da S.C. |
| --- | --- | --- |
| P4 | 000009 | 000012 |
| P5 | 000010 | 000013 |
| P6 | 000011 | 000014 |

Quando há **Pré-requisição**é gerada uma **S.C.** e ao executar a baixa da **Pré-requisição,** para que os insumos sejam realizados. a **S.C.** é deletada**.** Ao **finalizar** a **O.S.** a **S.A.** é mantida para que se mantenha o registro da **S.C.** gerada através da **Pré-requisição**.  
  
**Saiba mais**As informações referentes à inclusão de **S.A.**, podem ser verificadas através do artigo [MP - MNT - Procedimento para gerar a Solicitação de Armazém](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026182131)
