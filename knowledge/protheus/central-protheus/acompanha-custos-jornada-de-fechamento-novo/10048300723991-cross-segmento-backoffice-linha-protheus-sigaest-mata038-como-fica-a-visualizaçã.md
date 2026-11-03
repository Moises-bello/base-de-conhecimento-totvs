---
article_id: 10048300723991
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 1168290a3cdcfcc8b9c5f5dd974f44fc9dc001119148c47baf20ab8b90432319
fetched_at: '2026-06-28T22:38:48.195059+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Como fica
  a visualização dos lançamentos contábeis na Nova Jornada de Fechamento?
type: support-article
updated_at: '2025-03-12T12:27:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10048300723991-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Como-fica-a-visualiza%C3%A7%C3%A3o-dos-lan%C3%A7amentos-cont%C3%A1beis-na-Nova-Jornada-de-Fechamento
---

**Dúvida**Agora é possível realizar o ajuste de lançamentos contábeis com algum tipo de inconsistência dentro da própria Jornada de Fechamento não sendo mais necessário acessar outra rotina para realizar este procedimento.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Nas versões dos fontes anteriores da jornada de fechamento não era mais possível interagir com a tela de lançamentos contábeis durante a execução do recalculo do custo médio. Sendo necessário o tratamento com o parâmetro **[MV\_PRELAN](https://tdn.totvs.com/pages/viewpage.action?pageId=284348618)** como **D**, os lançamentos inconsistentes serão gerados como Pré-Lançamentos a serem ajustados posteriormente no **módulo de contabilidade gerencial Efetivação de Pré-Lançamentos (CTBA350).**

A visualização dos lançamentos sera apresentada, apenas se durante a contabilização for identificado **INCONSISTENCIAS**, caso não seja, a tela não sera apresentada.

**Com os fontes atuais será possível as alterações dos lançamentos contábeis sem a necessidade de fazer a efetivação.**

Para isso segue abaixo o passo a passo do processo de como habilitar a pergunta: "Mostra Lançamento Contábil" na rotina de Acompanha Custos:

**-Atenção:** caso utilize o conceito de processamento de saldos em fila, considerar validar se o seu ambiente esta devidamenteo configurado para apresentação da tela de lançamentos na jornada de fechamento: <https://tdn.totvs.com/display/public/PROT/CTBA193+Reprocessamento+de+Saldos+por+fila+-+P12>

**1. Pré-Condições**

Nas configurações de parâmetros, selecione a opção **Mostra lançamentos contábeis** juntamente com a opção **Gerar lançamento contábil** e salve esta configuração antes de iniciar seu fechamento.

Ao término do processamento da etapa de Contabilização, caso existam lançamentos contábeis inconsistentes, estes serão apresentados em tela para que seja possível realizar os ajustes e prosseguir com seu fechamento sem que seja necessário sair do Acompanha Custos, acessar o módulo de Contabilidade e efetuar os ajustes por outra rotina.

**Para que esta integração ocorra com sucesso os seguintes critérios devem ser atendidos:**

**Campos necessários**

|  |  |  |
| --- | --- | --- |
| **Tabela** | **Campo** | **Descrição** |
| CT2 | CT2\_PROCES | Código do processo de contabilização |
| CT2 | CT2\_INCONS | Inconsistências na contabilidade |
| CT2 | CT2\_INCDET | Detalhes das inconsistências |

*Caso os campos ainda não existam em sua base de dados será necessário executar o pacote de dicionário da Expedição Contínua do módulo de Contabilidade para criação dos mesmos:*

**[Pacotes de Atualização - Contabilidade](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)**

**Programas X Datas**

|  |  |
| --- | --- |
| **Programa** | **Data do RPO maior ou igual a** |
| CTBA102 | 17/10/2023 |
| CTBA105 | 15/09/2023 |
| CONA100A | 11/10/2023 |
| CTBXATU | 15/09/2023 |

*Caso os programas acima estejam com datas inferiores em seu RPO será necessário executar o pacote de programas da Expedição Contínua do módulo de Contabilidade.*

|  |  |
| --- | --- |
| MATA038 | 23/01/2024 |
| MATA330 | 23/01/2024 |

*Caso os programas acima estejam com datas inferiores em seu RPO será necessário executar o pacote de programas da Expedição Contínua do módulo de Estoque.*

**[Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21454771216663)**

**2. Exemplo do processo:**

![](https://tdn.totvs.com/download/attachments/820561391/showCTBA102.gif?version=1&modificationDate=1705668101743&api=v2)

**3. Observações:**

**3.1** O processo anterior em relação aos lançamentos contábeis inconsistentes continua funcionando.  
Portanto, caso seu fechamento com contabilização seja configurado com a opção Mostra lançamentos contábeis desmarcada, a jornada de fechamento seguirá sem exibir os lançamentos contábeis e pode-se, caso desejado, utilizar a opção para gerar pré-lançamentos caso o lançamento contábil tenha alguma inconsistência e realizar a efetivação destes lançamentos pelo módulo de Contabilidade.

**3.2 Bloqueio de perguntas**

A pergunta **Mostra lançamentos contábeis** está preparada para aceitar a configuração de bloqueio de alteração de perguntas pela rotina CFGA540 (grupo de perguntas MTA330).

As informações acima consta no link abaixo:

[Ajuste de lançamentos contábeis inconsistentes](https://tdn.totvs.com/pages/releaseview.action?pageId=820561391)

**Saiba mais:**

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

[*Mais sobre a configuração da nova jornada de fechamento*](https://tdn.totvs.com/display/public/PROT/Acompanha+Custos)
