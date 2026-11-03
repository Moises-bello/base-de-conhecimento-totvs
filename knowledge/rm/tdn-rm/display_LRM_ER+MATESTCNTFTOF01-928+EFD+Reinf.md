---
content_hash: 7f07ed5eba4c9c8fa55a873565117fbb594e57f7d3eeae39da60c56fd64d9838
fetched_at: '2026-06-29T00:08:44.503926+00:00'
page_id: '309035191'
product: rm
source: tdn-rm
title: ER MATESTCNTFTOF01-928 EFD Reinf
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATESTCNTFTOF01-928+EFD+Reinf
version: 97
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATESTCNTFTOF01 | **IRM/EPIC1** | MATESTCNTFTOF01-928 |
| **Requisito/Story/Issue1** |  | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | ( x ) Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Detalhar as alterações necessárias no sistema TOTVS Gestão de Estoque, Compras e Faturamento que permitirão o envio de informações para o sistema TOTVS Gestão Fiscal, para geração da rotina EFD Reinf.

## 

## Definição da Regra de Negócio

Parâmetros Tipo de Movimento

1. Na etapa **Fis - Outros Dados** deverá ser criado um CheckBox para o usuário definir se o tipo de movimento é para lançamento de repasses recebidos. Esse parâmetro deve-se chamar **Recebimento de Repasse** e deverá ser exibido somente nos tipos de movimento 1.2.xx.

Esse parâmetro servirá para definir se no item de movimento será apresentada a opção de definir os tipos de repasse, opção que será detalhada no próximo tópico.

2. Criar consistência ao salvar o tipo de movimento para não permitir que o mesmo tipo de movimento tenha tributos do tipo (DTRIBUTO.TIPOTRIBFISC) "INSS" e "FUNRural".

Tela de Edição do Item de Movimento

1. Em **Integrações | Fiscal**, deverá ser criado o ComboBox **Tipo de Repasse** em que o usuário deverá definir qual o tipo de repasse está sendo recebido. Esse ComboBox somente será apresentado em movimentos do tipo 1.2.xx e deverá ser exibido quando o parâmetro **Recebimento de Repasse** estiver marcado. Nesse ComboBox deverão ser apresentadas as seguinte opções:

* 1 - Patrocínio;
* 2 - Licenciamento de marcas e símbolos;
* 3 - Publicidade;
* 4 - Propaganda;
* 5 - Transmissão de espetáculos.

Na tabela onde será inserida essa informação, pode ser gravado apenas o código de cada tipo de repasse, pois apenas esse código é que será necessário para geração dos dados do EFD Reinf.

2. Em **Tributos e Valores | Valores**, deverão ser criados novos campos do tipo valor, tamanho 9:

* **Dedução de Materiais/Equipamentos**;
* **Percentual de Dedução de Materiais/Equipamentos**;
* **Dedução de Alimentação**;
* **Percentual de Dedução de Alimentação**;
* **Dedução de Transporte**;
* **Percentual de Dedução de Transporte**.

Esses campos serão exibidos no item de movimento conforme definição do parâmetro **Dedução** (Etapa 36 - Item - Valores Financeiros) do tipo de movimento. Deve ser obedecida a seguinte regra:

* Se o parâmetro for igual a "Não Usa", os campos não deverão ser exibidos;
* Se o parâmetro for igual a "Usa Percentual", deverão ser exibidos apenas os campos de percentual das deduções;
* Se o parâmetro for igual a "Usa Valor", deverão ser exibidos apenas os campos de valor das deduções;
* Se o parâmetro for igual a "Usa Ambos", deverão ser exibidos os campos de valor e de percentual das deduções.

Esses campos poderão ser preenchidos manualmente pelo usuário na edição do movimento ou serão preenchidos pelo TOP quando da geração do movimento através da integração entre os sistemas. Caso sejam preenchidos pelo TOP somente poderão ser alterados pelo usuário se no cadastro do usuário logado, em **Permissões por Tipo de Movimento**, para o tipo de movimento acessado a permissão **Alterar Item Integrado** estiver marcada.

3. Em **Tributos e Valores | Valores**, deverão ser criados dois novos campos do tipo valor, tamanho 9:

* **Retenção de Subcontratados**;
* **Percentual de Retenção de Subcontratados**.

Esses campos serão exibidos no item de movimento conforme definição do parâmetro **Retenção**(Etapa 36 - Item - Valores Financeiros) do tipo de movimento. Deve ser obedecida a seguinte regra:

* Se o parâmetro for igual a "Não Usa", os campos não deverão ser exibidos;
* Se o parâmetro for igual a "Usa Percentual", deverão ser exibidos apenas os campos de percentual das deduções;
* Se o parâmetro for igual a "Usa Valor", deverão ser exibidos apenas os campos de valor das deduções;
* Se o parâmetro for igual a "Usa Ambos", deverão ser exibidos os campos de valor e de percentual das deduções.

Esses campos poderão ser preenchidos manualmente pelo usuário na edição do movimento ou serão preenchidos pelo TOP quando da geração do movimento através da integração entre os sistemas. Caso sejam preenchidos pelo TOP somente poderão ser alterados pelo usuário se no cadastro do usuário logado, em **Permissões por Tipo de Movimento**, para o tipo de movimento acessado a permissão **Alterar Item Integrado** estiver marcada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Tabelas Utilizadas**

* TTRBMOV - Tributos do Movimento / Item de Movimento
* TITMMOV - Item de Movimento

## Dicionário de Dados

|  |  |
| --- | --- |
| **Campo** | RECREPASSE |
| **Tipo** | DLOGICONULL |
| **Tamanho** | 2 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Parâmetro para indicar se o movimento será utilizado para laçamento de repasse de verbas destinada a clubes de futebol. |
| **Título** | Recebimento de Repasse |
| **Picture** | NA |
| **Help de Campo** | Indica se o movimento será utilizado para laçamento de repasse de verbas destinada a clubes de futebol. |

|  |  |
| --- | --- |
| **Campo** | TIPOREPASSE |
| **Tipo** | SMALLINT |
| **Tamanho** | 2 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Indicativo do Tipo de Repasse que está sendo recebido pelo clube de futebol. |
| **Título** | Tipo de Repasse |
| **Picture** | NA |
| **Help de Campo** | Indica o Tipo de Repasse que está sendo recebido pelo clube de futebol. |

|  |  |
| --- | --- |
| **Campo** | DEDUCAOMATEQUIP |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9,4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Valor da Dedução de Materiais e/ou Equipamentos. |
| **Título** | Dedução de Materiais/Equipamentos |
| **Picture** | NA |
| **Help de Campo** | Valor da Dedução de Materiais e/ou Equipamentos. |

|  |  |
| --- | --- |
| **Campo** | PERCENTDEDUCAOMATEQUIP |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9,4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Percentual da Dedução de Materiais e/ou Equipamentos. |
| **Título** | Percentual de Dedução de Materiais/Equipamentos |
| **Picture** | NA |
| **Help de Campo** | Percentual da Dedução de Materiais e/ou Equipamentos. |

|  |  |
| --- | --- |
| **Campo** | DEDUCAOALIMENT |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9,4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Valor da Dedução de Alimentação. |
| **Título** | Dedução de Alimentação |
| **Picture** | NA |
| **Help de Campo** | Valor da Dedução de Alimentação. |

|  |  |
| --- | --- |
| **Campo** | PERCENTDEDUCAOALIMENT |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9,4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Percentual da Dedução de Alimentação. |
| **Título** | Percentual de Dedução de Alimentação |
| **Picture** | NA |
| **Help de Campo** | Percentual da Dedução de Alimentação. |

|  |  |
| --- | --- |
| **Campo** | DEDUCAOTRANSP |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9,4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Valor da Dedução de Transporte. |
| **Título** | Dedução de Transporte |
| **Picture** | NA |
| **Help de Campo** | Valor da Dedução de Transporte. |

|  |  |
| --- | --- |
| **Campo** | PERCENTDEDUCAOTRANSP |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9,4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Percentual da Dedução de Transporte. |
| **Título** | Percentual de Dedução de Transporte |
| **Picture** | NA |
| **Help de Campo** | Percentual da Dedução de Transporte. |

|  |  |
| --- | --- |
| **Campo** | RETENCAOSUBCONT |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9,4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Valor de Retenção de Subcontratados. |
| **Título** | Retenção de Subcontratados |
| **Picture** | NA |
| **Help de Campo** | Valor de Retenção de Subcontratados. |

|  |  |
| --- | --- |
| **Campo** | PERCENTRETENCAOSUBCONT |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9,4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Percentual de Retenção de Subcontratados. |
| **Título** | Percentual de Retenção de Subcontratados |
| **Picture** | NA |
| **Help de Campo** | Percentual de Retenção de Subcontratados. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
