---
content_hash: fb9b1b397fea455983c6f7378a567d56d6606220dcce52295c246cf7e0beeb5f
fetched_at: '2026-06-29T00:09:17.458115+00:00'
page_id: '421388603'
product: rm
source: tdn-rm
title: FIN - Integração contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388603
version: 8
---

**AVP**

Evento contábil

Define evento contábil de provisão e reversão de juros.

Indexador

Define o indexador de ajuste a valor presente.

Valor relevante

Define o valor mínimo original para que o lançamento tenha AVP calculado.

Dias longo prazo

A rotina filtrará apenas os lançamentos que possuírem entre a sua data de emissão e sua data de vencimento um prazo maior ou igual ao valor informado neste campo.

Tabela que define o AVP

Define a tabela do AVP (tipo de documento ou cliente/fornecedor). Ao selecionar um dos dois será disponibilizado no cadastro correspondente a opção "usar ajuste a valor presente'.

**Contab. Financeiro**

Tabela default para evento

Define qual será a tabela default de evento: Nenhuma, Seção, Portador, Centro de despesa, Natureza de gasto, Contratos vendor ou Tipo documento.

Tabela opcional vendor

Define qual será a tabela default de vendor: Nenhuma, Seção, Portador, Centro de despesa, Natureza de gasto ou Contratos vendor.

Copia número contábil sem alfanumérico

Define que o número contábil será copiado considerando apenas os números e desconsiderando as letras.

**Contab. Lançamento**

Regerar contabilização

Define que a contabilização será regerada quando houver alteração em lançamentos originários.

Rateio c. custo default para rateio contábil

Define que o rateio contábil será gerado através do rateio por centro de custo do lançamento. Caso haja uma configuração no evento contábil para o rateio gerencial, estando esse parâmetro marcado, o rateio por centro de custo do lançamento irá sobrescrever o rateio do evento para o rateio do lançamento.

Rateio por centro de custo com prioridade sobre o rateio do evento

Define que o rateio gerencial contábil será gerado através do rateio por centro de custo do lançamento, e, no caso de insucesso, será gerado através do rateio do evento contábil.

Preencher filial, departamento e centro de custo na contabilização através do lançamento

Define que para esses valores serão utilizados os dados do lançamento, caso contrário irá utilizar o default contábil.

Permite contabilizar com o valor contábil menor do lançamento

Define que será permitido informar lançamentos contábeis com valor contábil menor que o valor do lançamento na contabilização de inclusão e baixa.

Campos do lançamento que afetam a contabilização

Criado parâmetro para definir os campos que afetam a contabilização do lançamento financeiro, nesse parâmetro o usuário definirá quais são os campos que afetarão a contabilização do lançamento. Dessa forma, caso algum campo dessa entidade seja alterado, a contabilização será regerada apenas se o campo estiver parametrizado. Hoje, o sistema permite que o usuário opte por regerar a contabilização, quando algum campo é alterado.

**Observações:**

O parâmetro "Campos do lançamento que afetam a contabilização" será habilitado somente se o parâmetro "Regerar Contabilização" estiver marcado.

O parâmetro "Considerar alteração dos valores opcionais, multa, juros, capitalização e desconto ao regerar contabilização" foi descontinuado, e a lista de campos marcados que afetam a contabilização do lançamento financeiro será inicializada se esse parâmetro estiver marcado ou não.

**Procedimento para Utilização**

Para configuração do sistema acesse o caminho abaixo, para definição de quais campos afetarão a contabilização dos lançamentos financeiros:  
Ambiente  TOTVS Gestão Financeira | Parâmetros | Integração Contábil | Contabilização | Contab. Lançamento| Campos do lançamento que afetam a contabilização (Define se a alteração dos campos será considerada para regerar contabilização):

| * Capitalização mensal * Centro de custo * Centro de despesa * Conta Caixa * Contratos Vendor * Departamento * Filial * Multa ao Dia * Natureza do gasto * Portador * Rateio de Centro de Custo * Rateio de Departamento * Seção * Tipo de Documento | * Valor da Capitalização * Valor da Multa * Valor do Desconto * Valor dos Juros * Valor Opcional 1 * Valor Opcional 2 * Valor Opcional 3 * Valor Opcional 4 * Valor Opcional 5 * Valor Opcional 6 * Valor Opcional 7 * Valor Opcional 8 * Valor Original |
| --- | --- |

**Contab. Inclusão**

Default contábil no lançamento

Define o default contábil do lançamento (contábil, baixa contábil, a contabilizar, default do cliente/fornecedor).

Número contábil na inclusão

Define o número contábil na inclusão (número do documento, referência e segundo número).

Permite data de inclusão contábil anterior à emissão do lançamento

Define que será possível incluir data de inclusão anterior à data de emissão do lançamento.

**Contab. Inclusão a pagar**

Data default de inclusão a pagar

Define data default de inclusão a pagar (sistema, vencimento, emissão, previsão de baixa e digitação).

**Contab. Inclusão a receber**

Data default de inclusão a receber

Define data default de inclusão a receber (sistema, vencimento, emissão, previsão de baixa e digitação).

Estorno contab. Inclusão

Data default de estorno da inclusão

Define a data default de estorno de inclusão de lançamento financeiro (sistema, contab. Inclusão e digitação).

**Contab. Baixa**

Permite data de baixa anterior à contabilização de inclusão

Define permissão para data de baixa ser anterior à contabilização de inclusão.

Buscar número do documento no lançamento faturado

Define que o número documento da baixa será buscado no lançamento.

Não contabilizar baixa com valor zero

Define que baixas de valor zero não serão contabilizadas.

Usar o default do evento contábil de baixa contábil apenas nos lançamentos gerados pelo financeiro

Define que o evento contábil de baixa contábil será utilizado apenas para lançamentos gerados no Financeiro.

Carregar automaticamente contabilização antes de efetuar a baixa de lançamentos na tela de baixa

Define que a baixa só será concluída se a contabilização estiver válida no formulário de baixa.

Não contabilizar a baixa de vinculados

Define se os lançamentos de nota de crédito e/ou devolução não serão contabilizados ao serem baixados vinculados aos lançamentos financeiros.

Número contábil da baixa

Define o default do número contábil da baixa: (Número do cheque, número contábil da inclusão, número do documento, número do mov. RM Nucleus, segundo número ou referência.

**Contab. Baixa pagar**

Data default de baixa a receber

Define a data default de baixa a receber (sistema, baixa, vencimento, emissão, previsão de baixa, cheque, inclusão, digitação ou comp. cheque).

**Contab. Baixa receber**

Data default de baixa a receber

Define a data default de baixa a receber (sistema, baixa, vencimento, emissão, previsão de baixa, cheque, inclusão, digitação ou comp. cheque).

**Estorno contab. Baixa**

Data default de estorno de baixa

Define a data default de baixa a receber (sistema, digitação ou contab. Baixa).

**Contab. Extrato**

Default contábil no extrato

Define o default contábil no extrato de caixa (não contábil, contábil, a contabilizar).

Usar contabilização de mútuo

Define se utilizará os recursos de contabilização de mútuo.

Observação: Quando essa opção está marcada é habilitado a coluna 'Coligada' na visão de Convênio.

Inverte o default contábil de mútuo para extrato de saque

Define que será invertido o default contábil de mútuo para o extrato de saque.

Data default do extrato   

* Contabilização

Define data default de contabilização do extrato (sistema, vencimento, emissão ou compensação).

* Estorno

Define data default de estorno (sistema ou contab. Extrato).

Evento contábil CPMF

Define evento contábil para CPMF.

Campos do extrato que afetam a contabilização

Com esse parâmetro o usuário definirá quais são os campos que afetarão a contabilização do extrato. Dessa forma, caso algum campo seja alterado, a contabilização será regerada apenas se o campo estiver parametrizado.

Para configuração do sistema acesse o caminho abaixo, para definição de quais campos afetarão a contabilização do extrato de caixa:  
Ambiente  TOTVS Gestão Financeira | Parâmetros | Integração Contábil | Contabilização | Contab. Extrato | Campos do extrato que afetam a contabilização:

| * Centro de custo * Centro de despesa * Contratos Vendor * Departamento * Filial * Natureza do gasto * Portador * Seção * Valor |
| --- |

**Observação:**

A regeração ocorre apenas se a contabilização for gerada de forma automática (através de eventos contábeis, por exemplo). Caso a contabilidade tenha sido incluída ou alterada manualmente, a alteração destes campos **não**implicará na regeração da contabilidade.

**Lote**

Define os lotes de inclusão, estorno, pagamento eletrônico, estorno de pagamento eletrônico, Cobrança, Estorno de cobrança, baixa, estorno de baixa, débito automático, estorno de débito automático, Inclusão Liquidação Duvidosa e Estorno Liquidação Duvidosa para lançamentos a pagar, receber, extrato, AVP e aplicação financeira.
