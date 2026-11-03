---
article_id: 1500011068541
category: Contabilidade Gerencial - Plano de Contas
content_hash: 68cb181e0cd23f0aef324ecae7d7917226fdf7a975b9917ba861db0919f5bd9b
fetched_at: '2026-06-28T22:40:33.393359+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA020 - Como cadastrar
  um plano de contas
type: support-article
updated_at: '2024-04-17T18:27:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068541-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Como-cadastrar-um-plano-de-contas
---

**Dúvida**Como cadastrar um plano de contas (CTBA020)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial  - Todas as versões  
  
**Solução**

Menu padrão: Atualizações + Entidades + Plano de contas (Rotina CTBA020)

No teclado + F12

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017813182)

Opção + Cadastro em árvore:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018115261)

A apresentação do Plano de Contas em estrutura de árvore é utilizada para facilitar a pesquisa e organização de dados.

Cadastro em Árvore?

* Não - Utiliza o formato de manutenção padrão, não estruturado em árvore.
* Sim - torna padrão a estrutura em árvore para manutenção dos dados, a partir do próximo acesso ao cadastro.
* Perguntar - a cada acesso ao cadastro, será exibida uma pergunta sobre o uso da estrutura em árvore para manutenção dos dados.

Sobre a conta contábil, o número de contas disposto num plano de contas depende do volume e da natureza dos negócios de uma empresa. Todavia, na estruturação do plano de contas (chamada de Planificação Contábil), deverão ser considerados os interesses dos usuários (gerentes, investidores, Fisco, etc). 

Vale lembrar que um estudo detalhado deverá ser feito antes da implantação do Plano de Contas, pois após estar em uso será praticamente inviável reestruturá-lo.

|  |
| --- |
| ***Dica:***  O campo CT\*\_DTEXIS é utilizado para determinar a data de criação das [Entidades Contábeis](https://tdn.totvs.com/x/VTKbEg).  É possível realizar o controle dos lançamentos contabéis por meio da opção [Controles Contábeis](https://tdn.totvs.com/x/Ko1WF). |

Outras informações sobre a lei 11.638/07 e Instrução Normativa CVN 469-08 consulte [http://www.presidencia.gov.br](http://www.presidencia.gov.br/).

No browse do Plano de Contras estão disponíveis as opções [Importar](https://tdn.totvs.com/x/HjCbEg) e [Exportar](https://tdn.totvs.com/x/cDGbEg), que permite a importação e exportação de dados, em arquivos no formato **.CSV**.

Se configurada a rotina Schedule e o Adapter EAI, é possível a integração do TIN (TOTVS Incorporações) e Protheus para o envio e o recebimento de arquivos XML, de acordo com o XSD homologado pela Totvs®. 

Parâmetros da rotina:

* [MV\_REDUZID](https://tdn.totvs.com/pages/viewpage.action?pageId=312160919)
* [MV\_CTBLGET](https://tdn.totvs.com/pages/viewpage.action?pageId=312160877)

[MV\_CTRCTB](https://tdn.totvs.com/pages/viewpage.action?pageId=312160877)

<https://tdn.totvs.com/pages/viewpage.action?pageId=341216554>

Tabelas utilizadas

* CT1 - Plano de Contas.
* CT2 - Lançamentos Contábeis
* CT8 - Histórico Padrão.
* CTA - Amarração Entidades.
* CVD - Plano de Contas Referencial.
* CTS - Visões Gerenciais.
* CVE - Visão Gerencial.
* CVF - Estrutura da Visão Gerencial.

CTBA020 inclusão via EXCAUTO

<https://tdn.totvs.com/pages/viewpage.action?pageId=286011081>
