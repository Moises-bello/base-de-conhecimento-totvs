---
content_hash: 40dd8042cc690a5ec57e4e0eb770556c35dc0cf87e374b242393222ed6904550
fetched_at: '2026-06-29T00:06:02.657414+00:00'
page_id: '198948409'
product: rm
source: tdn-rm
title: FIN - Posição Financeira Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198948409
version: 23
---

Funcionalidade cujo objetivo é disponibilizar o acesso à posição financeira da empresa em um determinado dia. Será apresentado o estado de um Lançamento em data específica, ou seja, os valores para o Lançamento serão apresentados como uma "fotografia" do registro naquele determinado momento. Isso será feito a partir de um histórico de alterações do Lançamento que armazenará parte dos dados do mesmo quando realizado determinados processos. Histórico quanto a entidades vinculadas: Retenções ( tributos), Valores de integração, Rateio por centro de Custo, Rateio por departamento, Vínculo entre Lançamentos, Retenção Acumulada, Retenção Acumulada Rateio e Retenção de IRRF também será armazenado.

Necessário habilitar o controle de histórico de alterações. Através do Menu Utilitários - Outros, acessar o processo "Habilitação do Controle de Histórico de Alterações de Lançamentos / Extratos de Caixa, marcar a opção "Habilita controle de Histórico de Alteração". Será criado um registro para cada Lançamento Financeiro não cancelado. 

|  |  |
| --- | --- |
| **Objetivo da tela:** | *Parametrizador para realizar o controle do histórico de alterações e realizar a carga inicial do histórico.* |

**Outras Ações/Ações Relacionadas:**

|  |  |
| --- | --- |
| **Ação:** | **Descrição:** |
| *Habilita controle de Histórico de Alteração* | *O Controle de Histórico será habilitado para todas as coligadas.* |
| *Desabilita controle de Histórico de Alteração* | **Todos os registros de histórico de alteração de lançamentos e extratos de caixa já existentes serão excluídos da base de dados.** |

Após habilitar o controle de histórico, os processos abaixo quando executados irão criar um registro de histórico referente a alteração no Lançamento Financeiro:

* Incluir Lançamento
* Alterar lançamento
* Alteração Global de Lançamento
* Alteração do Valor do IRRF no Lançamento
* Geração de Lançamentos de INSS
* Geração de Lançamentos de IRRF
* Cancelar Lançamento
* Cancelar Transação de Cartão de Crédito/Débito
* Excluir Lançamento
* Reajuste de Valores de Integração ( Integração módulo Gestão Imobiliária)
* Baixa de Lançamento
* Baixa de Lançamento com fatura
* Baixa com Cheque
* Baixa por perda financeira
* Cancelamento de Baixa
* Emissão / Recebimento de cheque
* Cancelamento de cheque
* Incluir fatura
* Cancelar fatura
* Efetivação de acordo
* Cancelamento de acordo efetivado
* Desconto de duplicata
* Efetivar desconto de duplicata
* Devolver desconto de duplicata
* Vincular Lançamentos ( incluir ou remover vínculos)
* Remessa de pagamento
* Retorno bancário
* Inclusão de Tributo pelo EFD Fiscal
* Atualização de valores de integração ( Integração módulo Gestão Imobiliária)
* Alteração Conta Caixa e Convênio do Boleto
* Alteração Data Vencimento Boleto
* Edição de boleto via interface ( código de barras, IPTE, nosso número e forma de pagamento)
* Conversão de Boletos
* Remover código de barras do Boleto
* Cancelamento Boleto
* Desvincular lançamentos do Boleto
* Contabilizar baixados ( Lançamentos)
* Retenções Acumuladas

Novas funções de fórmula para trazer a Posição Financeira do Lançamento numa data específica foram criadas, será possível pesquisar a posição dos Lançamentos baseado no histórico de alterações.

**Principais Campos e Parâmetros:**

|  |  |
| --- | --- |
| **Campo:** | **Descrição** |
| *Habilitação Histórico de Alterações* | *Parametrizador para realizar o controle do histórico de alterações e realizar a carga inicial do histórico.* |
| *Histórico de Alterações* | **Será possível visualizar parte dos dados do histórico no Lançamento Financeiro.** |
| *Posição Financeira* | **Será possível pesquisar a posição dos lançamentos numa data especifica baseado no histórico de alterações** |
| *TABLANPF* | **Valor de um campo de lançamento numa determinada data.** |
| *TABLANRATCCUPF* | **Valor de um campo do rateio por centro de custo do lançamento numa determinada data.** |
| *TABLANRATDEPPF* | ***Valor de um campo do rateio por departamento do lançamento numa determinada data.*** |
| *VALORLIQUIDOPF* | ***Valor líquido do lançamento numa determinada data.*** |
| *VALORINTEGRACAOLANPF* | ***Valor de um valor de integração do lançamento numa determinada data.*** |

 Informações Complementares
