---
content_hash: c0206c5966fec7a00cada9bf8898f987d94e151e80b8c5833ca227c59050183b
fetched_at: '2026-06-29T00:06:25.471034+00:00'
page_id: '224397440'
product: rm
source: tdn-rm
title: ER_PCREQ-8879_Mapa Resumo (Redução Z)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224397440
version: 138
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-8879 | **Subtarefa1** | PDR\_CP\_MOV010-37 |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS do Mapa Resumo - Redução Z. Este adapter irá viabilizar o recebimento da mensagem de Mapa Resumo (Redução Z) gerado pelo PDV PROTHEUS.

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de recebimento de Mensagens Únicas TOTVS para integração do Mapa Resumo (Redução Z), estando o adapter de envio desta mesma mensagem fora do escopo do requisito.

 A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Redução Z | Inclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Fiscais\ Mais...\ Redução Z | - |

A Redução Z permite que o usuário, por exigência legal, informe diariamente os totais acumulados de cada contador ao término do expediente. 

**Tabelas Utilizadas**

* TREDUCAOZ – Redução Z
* TREDUCAOZITEM – Item da Redução Z
* TCUPOMFISCAL – Cupom Fiscal
* TCUPOMFISCALITM – Itens de Cupom Fiscal
* TTRIBUTACAOECF – Tributação ECF

**Entidades de Integração**

* DataServer envolvido
  + MovReducaoZData
* Transformação
  + Id: Reduction
  + Versão: 1\_001
* SourceCode (Evento)
  + GUID: c68d7d06-46c4-40f1-8e9d-245c45244eab

### Regras de Integridade

**Inclusão de Redução Z**

A inclusão de Redução Z no RM considera como obrigatórios a informação dos seguintes dados: Ponto de Venda, Número da Redução, Série e Cliente.

* O Ponto de Venda será enviado na mensagem única Reduction\_1.001 na tag ***StationSalePointInternalId***. Ao receber a mensagem deve-se buscar na tabela De-Para qual é o código do ponto de venda do RM.
* Número da Redução:  será considerado o valor enviado pelo PDV Protheus na tag ***ReductionCode***.
* Série: como esta informação não é trafegada na mensagem será buscado a Série do Ponto de Venda.
* Cliente: como esta informação não é enviada pelo PDV Protheus na mensagem, é necessário cadastrar o Cliente/Fornecedor Default nos Parâmetros de Integração Frente de Loja do TOTVS Gestão de Estoque, Compras e Faturamento. Acesse  RM menu BackOffice >> Gestão de Estoque, Compras e Faturamento >> Ambiente >> Configuração >> Parâmetros >> 04.03 - Integrações >> 04.03.04 - Frente de Loja.

Além dos campos obrigatórios acima o campo Contador Não Sujeito ICMS receberá como valor default zero.

**Itens de Redução Z**

Estes dados são gerados com base nas seguintes informações recebidas da mensagem única:

* Lista de Alíquotas(*ListOfAliquot*)
  + Nesta lista serão enviados os valores tributados de ICMS e ISS, onde na tag *AliquotCode* será enviado o código da tributação ECF e na tag *AliquotBase* será enviado o valor base da alíquota informada.
* Valor de Substituição tributária (TaxReplacementValue);
* Valor de Isentos (FreeValue);
* Valor de Não Tributado (UntaxedValue).

O PDV Protheus deverá enviar os Códigos dos Tributos ECF utilizados nos Cupons para que os Itens de Redução Z seja gerados corretamente.

**Cálculo da Redução Z**

Devido ao recálculo do rateio de descontos e acréscimos pode haver diferenças de arredondamento entre o valor líquido de alguns itens e assim gerando diferenças nos totalizadores de Tributação ECF, mas não nos valores absolutos do cupom.

Caso esta diferença ocorra no Cálculo da Redução Z o processo de "Recalculo dos Totalizadores Parciais" deve ser executado e posteriormente reexecutar o Cálculo da Redução Z.

**Ponto de Atenção**

* **Valor dos Acréscimos:**os acréscimos aplicados aos cupons fiscais nas vendas, devem ser enviados na Redução Z para que o cálculos dos valores sejam feitos corretamente. Para isso o PDV Protheus deve somar os acréscimos aplicados aos cupons enviados na Redução Z e enviar esta informação na tag "***IncreasesValue***'.
* **Grande Total (GT):** O grande total enviado deverá considerar os acréscimos.
* **Acréscimo Financeiro:**Devido os dois pontos listados acima e considerando que o Protheus somente utiliza acréscimos no Cupom Fiscal e não nos seus itens, o campo "IncreasesValue" será mapeado para o campo "Acréscimos Financeiros" do RM.

### Opcional

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

## Mapeamento dos Campos

**Mensagem:** Reduction\_1\_000

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da empresa. | TREDUCAOZ | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial |  |  |
| **CompanyInternalId** | InternalId da chave completa de empresa do produto |  |  |
| **InternalId** | InternalId de Integração | TREDUCAOZ | CODCOLIGADA|IDREDUCAOZ |  |
| **MovementDate** | Data do Movimento | TREDUCAOZ | DATAMOVIMENTO |  |
| **ReductionCode** | Código da Redução | TREDUCAOZ | NUMEROREDUCAO |  |
| **InitialValue** | Grande Total Final do dia anterior | TREDUCAOZ | GRANDETOTALANT | Valor default Zero, caso não seja enviado na mensagem. |
| **FinalValue** | Grande Total Final do dia | TREDUCAOZ | GRANDETOTAL |  |
| **InitialCounter** | Número do Cupom Inicial do Dia | TREDUCAOZ | COOANT |  |
| **FinalCounter** | Número do Cupom Final do Dia | TREDUCAOZ | COO |  |
| **ValueCancellations** | Valor Total de Cancelamento | TREDUCAOZ | CANCELAMENTOS |  |
| SalesValueNet | Valor Contábil | -- | -- | Não utilizado no RM. |
| **TaxReplacementValue** | Valor Substituição Tributária | TREDUCAOZITEM | TOTALPARCIAL | Quando enviado o valor preencher o total parcial do Item de Redução Z e utilizar como código de tributação ECF o valor fixo **F1**. |
| **DiscountValue** | Valor de Descontos | TREDUCAOZ | DESCONTOS |  |
| **FreeValue** | Valor de Isentos | TREDUCAOZITEM | TOTALPARCIAL | Quando enviado o valor preencher o total parcial do Item de Redução Z e utilizar como código de tributação ECF o valor fixo **I1**. |
| **UntaxedValue** | Valor de Não Tributado | TREDUCAOZITEM | TOTALPARCIAL | Quando enviado o valor preencher o total parcial do Item de Redução Z e utilizar como código de tributação ECF o valor fixo **N1**. |
| **CounterCode** | Contador de Ordem de Operação | TREDUCAOZ | COORZ |  |
| ValueOfOthersReceivables | Valor de Outros Recebimentos | -- | -- | Não utilizado no RM. |
| AmountOfTaxDue | Valor do Imposto Devido | -- | -- | Não utilizado no RM. |
| IssValue | Valor Base do ISS | -- | -- | Não utilizado no RM. Os valores de ISS serão mapeados pela lista de alíquotas (*ListOfAliquotType)*. |
| CounterReset | Contador de Ordem de Reinicio | -- | -- | Não utilizado no RM. |
| **IssueDateReduction** | Data de Emissão da Redução | TREDUCAOZ | DATAREDUCAO |  |
| **StationSalePointCode** | Código Ponto de Venda | TREDUCAOZ | PONTOVENDA |  |
| **StationSalePointInternalId** | InternalId do Ponto de Venda | TREDUCAOZ | CODCOLIGADA|PONTOVENDA |  |
| **Increases**Value**** | Valor dos Acréscimos da Venda | TREDUCAOZ | ACRESCIMOSFIN |  |
| **ListOfAliquot\ListOfAliquotType** | Lista de Alíquotas da Redução Z |  |  | As informações desta lista serão preenchidas para cada tipo de alíquota ICMS e ISS. Ver AliquotType. |
| AliquotType | | | |  |
| **AliquotCode** | Identificador da Base ICMS | TREDUCAOZITEM | TRIBUTACAOECF |  |
| **AliquotBase** | Valor da Base ICMS | TREDUCAOZITEM | TOTALPARCIAL |  |

* Somente os campos marcados em negrito são tratados no Adapter.

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
