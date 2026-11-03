---
article_id: 360026182131
category: Integrações Nativas
content_hash: ab3d56ebb89f3d434dafdba295e813cb07e9d038b0c7edcd3588a5a47200572d
fetched_at: '2026-06-28T22:42:35.507972+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Procedimento para gerar a Solicitação de
  Armazém
type: support-article
updated_at: '2025-02-05T13:22:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026182131-Manufatura-Linha-Protheus-MNT-Procedimento-para-gerar-a-Solicita%C3%A7%C3%A3o-de-Armaz%C3%A9m
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27719638039063)*Tempo aproximado para leitura: **00:02:15 min****Dúvida**  
Como funciona a geração **SA - Solicitação de Armazém**no **Manutenção de Ativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**Para gerar a **SA**, será necessário seguir os seguintes passos:

1. Acessar o **Configurador - SIGACFG**;
2. Ir em **Ambiente/Cadastros/Parâmetros** - **CFGX017**;
3. Configurar o parâmetro **MV\_NGMNTAS** **- Define se aglutina as Solicitações de Armazém para a mesma Ordem de Serviço,** **MV\_NGGERSA - Indica se deve gerar Solicitação ao Armazém em vez de gerar Solicitação de Compra** e **MV\_NGCORPR - Permite gerar Empenho e SCs para OS. Corretivas**
4. Acessar o **Manutenção de Ativos** e **Gestão de Frotas** - **SIGAMNT**;
5. Ir em **Atualizações/Controle de Oficina/Cadastros Básicos/Produtos** - **MATA010**;
6. Cadastrar um produto que será utilizado como insumo previsto.
7. Ir em **Atualizações/Controle de Oficina/Manutenção/Serviços** - **MNTA040**;
8. Cadastrar um serviço do tipo Corretivo;
9. Ir em **Atualizações/Controle de Oficina/Bens/Bens** - **MNTA080**;
10. Cadastrar um bem;
11. Ir em **Atualizações/Controle de Oficina/Ordem de Serviço/Corretiva** - **MNTA420**;
12. Incluir uma **Ordem de Serviço**, informando o produto como insumo previsto, o serviço e o bem cadastrados anteriormente.
13. Acessar o **Estoque/Custos - SIGAEST**;
14. Ir em **Atualizações/Movimentações/Internas/Armazém/Gerar Pré-requis. - MATA106**;
15. Selecionar a **SA** gerada pela **Ordem de Serviço** no passo 12 e selecionar a opção **Gera**.

As informações serão detalhadas conforme o passo a passo, incluindo a **Ordem de Serviço**, e em seguida alterando para informar novos insumos.

|  |  |
| --- | --- |
| **Parâmetro** | **Conteúdo** |
| **MV\_NGMNTAS** | **1** |
| **MV\_NGGERSA** | **S ou P** |

Sem Pré-requisição  
OS 000001

|  |  |
| --- | --- |
| **Produto** | **Número da SA** |
| P1 | 000001 |
| P2 | 000001 |

Adicionar um novo produto  
OS 000001

|  |  |
| --- | --- |
| **Produto** | **Número da SA** |
| P1 | 000002 |
| P2 | 000002 |
| P3 | 000002 |

Quando não há pré-requisição é gerado um novo número para **SA**, conforme sequência disponível para a mesma.  
  
Gera pré-requisição  
OS 000002

|  |  |
| --- | --- |
| **Produto** | **Número da SA** |
| P1 | 000003 |
| P2 | 000003 |

Adicionar novo produto  
OS 000002

|  |  |
| --- | --- |
| **Produto** | **Número da SA** |
| P1 | 000003 |
| P2 | 000003 |
| P3 | 000003 |

Mantém o código da **SA** quando for gerada pré-requisição para pelo menos um dos produtos.

|  |  |
| --- | --- |
| **Parâmetro** | **Conteúdo** |
| **MV\_NGMNTAS** | **2** |
| **MV\_NGGERSA** | **S ou P** |

Sem pré-requisição  
OS 000003

|  |  |
| --- | --- |
| **Produto** | **Número da SA** |
| P1 | 000004 |
| P2 | 000005 |

Adicionar novo produto  
OS 00003

|  |  |
| --- | --- |
| **Produto** | **Número da SA** |
| P1 | 000006 |
| P2 | 000007 |
| P3 | 000008 |

Cria nova **SA** para todos os produtos e gerando o próximo número disponível.  
Gera pré-requisição  
OS 000004

|  |  |
| --- | --- |
| **Produto** | **Número da SA** |
| P1 | 000009 |
| P2 | 000010 |
| P3 | 000011 |

Mantém o código da **SA** pelo qual foi gerada pré-requisição.

**Saiba Mais**Para saber mais consulte o *link* abaixo: [Inclusão ou alteração de insumos previstos associados a uma solicitação de armazém](https://tdn.totvs.com/pages/releaseview.action?pageId=560635996)
