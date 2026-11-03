---
article_id: 360006908012
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 8a37973430b531830ad87dd4dcf0eccc5d87d5b81493195239f3d6a832a26707
fetched_at: '2026-06-28T22:40:50.543394+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: Cross Segmento - Backoffice  Linha Protheus - SIGACTB - CTBA161 /CTBA130 -
  Amarração Visão Gerencial ao Livro
type: support-article
updated_at: '2024-12-02T18:41:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro
---

**Dúvida**

Procedimento para amarrar a visão gerencial ao Livro

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Contabilidade Gerencial – Todas as versões

**Solução**

Obs: Código do livro pode ser utilizada na emissão de relatório e geração de obrigações como ECD, ECF, FCONT

[MP - SIGACTB - CTBA161 - Arquivos modelos Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006687252-MP-SIGACTB-CTBA161-Arquivos-modelos-Vis%C3%A3o-Gerencial)  
  
**Passo 1** - Através da rotina CTBA161 -Visão gerencial

* [Importar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-MP-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial-?source=search) ou cadastre a visão gerencial

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007508651)

**Passo 2 - Através da rotina**CTBA130 Configurações Contábeis

* Selecione opção Configuração de Livros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007508851)

* Inclua um novo código de Livro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007509731)

* Informe :
* O código a visão gerencial que será amarrada ao Livro
* Cod Conf.Liv que será utilizado
* Descrição do livro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007510991)

Veja  se as tabelas :

* Estão com o [compartilhamento da Tabela está](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search) correto
* se são populadas corretamente ao importar uma nova visão gerencial

 Tabelas

|  |  |
| --- | --- |
| • | CTS - Entidade Gerencial |

|  |  |
| --- | --- |
| • | CVE - Visão gerencial |

|  |  |
| --- | --- |
| • | CVF - Itens da Visão Gerencial |

|  |  |
| --- | --- |
| •  • | CT1 - Cadastro Plano de Contas.  CTN - Codigo livro |

|  |  |
| --- | --- |
| • | CTD - Cadastro Itens Contábeis. |

|  |  |
| --- | --- |
| • | CTH - Cadastro Classe de Valor. |

|  |  |
| --- | --- |
| • | CTS - Planos Gerenciais. |

|  |  |
| --- | --- |
| • | CTT- Cadastro Centros de Custo. |

|  |  |
| --- | --- |
| • | SL - Tabela de Tipos de Saldos. |

 

|  |  |
| --- | --- |
| • | CTG - Calendários Contábeis |

|  |  |
| --- | --- |
| • | CTN - Configuração de Livros Contábeis |

|  |  |
| --- | --- |
| • | CTO - Moedas |
