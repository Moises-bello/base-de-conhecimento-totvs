---
content_hash: 9ce7fc288656434f256217a2d826ad1f5272a731e72c5e8a73a2409a60f7923f
fetched_at: '2026-06-29T00:11:25.589190+00:00'
page_id: '712493078'
product: rm
source: tdn-rm
title: Constantes - TOP
type: documentation
url: https://tdn.totvs.com/display/LRM/Constantes+-+TOP
version: 21
---

As constantes do sistema são caracteres simples ou numerais que são usados para representar o status de um movimento, cotação, produto ou outros registros no sistema, quando este é gravado no banco de dados. Em alguns casos uma mesma constante pode representar status distintos, dependendo da parametrização do recurso ou processo do sistema. Conhecer o significado de cada um dos status e quando eles são atribuídos é importante na execução de algumas tarefas, como ao criar um filtro, executar uma sentença ou gerar um relatório gerencial.

Constantes de Contrato - Tabela MCNT

* **Tipos de finalidades de contratos**

Define o tipo de finalidade que os contratos possuem, gravando na tabela **MCNT** no campo **CNTMATERIAL**.

| Constante | Representação |
| --- | --- |
| S | Prestação de serviços |
| M | Fornecimento de material |
| F | Parcelas fixas |
| C | Marco contratual |
| I | Contrato de Insumo |
| X | Extra-Histograma |

* **Periodicidade do contrato**

Localizado na tabela **MCNT** e no campo **PERIODICIDADEMED**, Separa a periodicidade do contrato em relação aos dias, se ele será único, semanal quinzenal etc.

| Constante | Representação |
| --- | --- |
| 0 | Personalizada |
| 1 | Única |
| -7 | Semanal |
| 7 | Semanal corridos |
| -15 | Quinzenal |
| 15 | Quinzenal corridos |
| 30 | Mensal |
| 365 | Anual |
| -10 | Dezena |
| 10 | Dezena corridos |

* **Tipo de reajuste de contrato**

Na tabela **MCNT** e no campo **TIPOREAJUSTE** Informa se o contrato sofrerá algum tipo de reajuste, se sim define qual o tipo dele:

| Constantes | Representação |
| --- | --- |
| 0 | Sem Reajuste |
| 1 | Por Contrato |
| 2 | Por item associado |

* **Periodicidade do reajuste**

Se for definido um reajuste como vimos acima, a periodicidade informa se será de 30 dias (Mensal) ou de 365 dias (um ano). Localizado na tabela **MCNT** no campo **PERIODOREAJUSTE.**

| Constantes | Representação |
| --- | --- |
| 30 | Mensal |
| 365 | Anual |

* **Tipo de retenção de medição**

Gravando na tabela **MCNT** e no campo **TIPORETMEDICAO,** armazena o tipo da medição de contrato selecionada pelo usuário.

| Constantes | Representação |
| --- | --- |
| 0 | Sem Reajuste |
| 1 | Mensal |
| 2 | Anual |

* **Status de contrato**

Na tabela **MCNT** no campo **STATUS**, guarda a informação se o contrato determinado possui algum status definido, e se sim, cita os tipos abaixo:

| Constantes | Representação |
| --- | --- |
| 0 | Em andamento |
| 1 | Em negociação |
| 2 | Paralisado |
| 3 | Cancelado |
| 4 | Concluído |
| 5 | Sem status definido |

* **Tipo de medição contrato**

Define o tipo da medição do contrato pelo valor, quantidade ou percentual. Armazenado na tabela **MTRFMED**e no campo **CAMPOMEDIDO.**

| Constantes | Representação |
| --- | --- |
| V | Valor medido |
| Q | Quantidade medida |
| P | Percentual medido |

* **Tipo periodo de contrato**

Define qual o tipo de periodo que está sendo criado para o contrato. Gravando na tabela **MPDO** no campo **PERIODOMED.**

| Constantes | Representação |
| --- | --- |
| 0 | Periodo |
| 1 | Periodo Complementar |
| 2 | Período Estornado |
| 3 | Período de Reajuste |

* **Tipo de situações de contrato**

Informa em qual situação o contrato foi definido na sua criação. Armazenando na tabela **MCNT** e no campo **TIPO.**

| Constantes | Representação |
| --- | --- |
| P | A Pagar |
| R | A Receber |

* **Classificação de período de contrato**

Na tabela **MPDO** no campo **CLASSIFICACAO**, esta constante define que um contrato possui 3 tipos de classifcações em relação ao seu período, sendos elas:

| Contantes | Representação |
| --- | --- |
| 0 | Classificação Normal |
| 1 | Classificação de Conferência |
| 3 | Classificação de Reajuste |

* **Tipo de item de contrato**

No campo **TIPOITEMCONTRATO** da tabela **MCNT,** é definido se o item de contrato é de tarefa ou serviço.

| Contantes | Representação |
| --- | --- |
| T | Tarefa |
| S | Serviço |

* **Tipos de aplicação de reajuste por item associado**

Informa o tipo de valor do reajuste de cada item associado ao projeto. Tabela **MCNT** e campo **TIPOAPLICRJT.**

| Constantes | Representação |
| --- | --- |
| 0 | Valor Unitário Inicial |
| 1 | Valor Atual |

* **Tipo de periodo adicional** **de contrato**

No campo **PERIODOMED** na tabela **MED,** é possível adicionar um periodo adicional no contrato, e ele é definido em três tipos: complementar, estornado ou de reajuste.

| Constantes | Representação |
| --- | --- |
| C | Periodo Complementar |
| E | Período Estornado |
| R | Período de Reajuste |

* **Status de movimento de origem**

Atualiza o status de movimento da origem do contrato. Localizado na tabela **MCNTMOVORIGEM** e no campo de **STATUS.**

| Constantes | Representação |
| --- | --- |
| 0 | Inativo |
| 1 | Ativo |

* **Status de abatimento de contrato**

No campo **STATUSABATIMENTODefine** da tabela **MCNTABATIMENTO,** mostra como está o processo de abatimento de um determinado contrato.

| Constantes | Representação |
| --- | --- |
| 0 | Abatimento Realizado |
| 1 | Abatimento Cancelado |

Constantes de Tarefas - Tabela MTAREFA

* **Tipo desmembramento de tarefa**

No campo **TIPODESMEMBRAMENTO** e na tabela **MTAREFA,** é verifiado se houve algum tipo desemembramento em uma determinada tarefa no projeto, sãos listadas em 3 tipos de categorias:

| Constantes | Representação |
| --- | --- |
| 0 | Nenhum |
| 1 | Tarefa original |
| 2 | Etapa criada |
| 3 | Tarefa desmembrada |

Constantes de Projeto - Tabela MPRJ

* **Status do projeto**

Informa em qual etapa de processamento o atual projeto está. Localizado na tabela **MPRJ** no campo **POSICAO.**

| Constantes | Representação |
| --- | --- |
| 0 | Indefinido |
| 1 | Em Andamento |
| 2 | Paralisado |
| 3 | Concluído |
| 4 | A Executar |
| 5 | Em Negociação |
| 6 | Revisado |
| 7 | Cancelado |
| 8 | Em restauração |

* **Tipo de projeto**

Na mesma tabela **MPRJ**porém no campo **TIPOPRJ.**Informa se o projeto escolhido possui o tipo "principal", "licitação", "revisão" ou "rodada de negociação".

| Constantes | Representação |
| --- | --- |
| 0 | Projeto Principal |
| 1 | Projeto Licitação |
| 2 | Projeto Revisão |
| 3 | Rodada de Negociação |

* **Fase de um projeto**

No campo **TIPOFASE** da tabela de projeto **MPRJ**, determina se um projeto irá possuir um controle de fases ou não. Caso se tiver será listadas as opções abaixo:

| Constantes | Representação |
| --- | --- |
| 0 | Sem Controle de Fases |
| 1 | Orçamento |
| 2 | Venda |
| 3 | Planejamento |
| 4 | Execução |

* **Tipo de revisão do projeto**

Verifica o tipo da revisão associada ao projeto selecionado. Tabela **MPRJ** e campo **TIPOREVISAO.**

| Constantes | Representação |
| --- | --- |
| H | Horizontal |
| V | Vertical |
| J | Juncao |
| T | Transformar Fase do Projeto |

* **Tipo de recurso**

Tabela **MCONTROLEREVISAO**campo **TIPOREC.**

| Constantes | Representação |
| --- | --- |
| C | Composição |
| I | Insumo |
| T | Tarefa |
| A | Filtro de Select trazendo todos DE-Para |
| P | Preço de insumo |
| M | Prioridade de projeto |
| G | Grupo de Custo |
| D | Disciplina |

* **Indicativo de Prestação de Serviços**

Indicativo de Prestação de Serviços em Obra de Construção Civil. Localizado no campo **INDPRESTSRV**na tabela **MPRJ.**

| Constantes | Representação |
| --- | --- |
| 0 | Não se aplica |
| 1 | Não é obra de construção civil ou não está sujeita a matrícula |
| 2 | Obra de Construção Civil - Empreitada Total |
| 3 | Obra de Construção Civil - Empreitada Parcial |

* **Tipo de projeto**

Campo **TPPRJ**da tabela **MPRJ.**

| Constantes | Representação |
| --- | --- |
| 0 | Próprio |
| 1 | Terceiros |
