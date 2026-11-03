---
article_id: 30488590981271
category: Originação de Grãos (OG)
content_hash: 776c19367c250c016117470afc0477addc5b00dc0fed3f64c5f4b17eeffb9fc4
fetched_at: '2026-06-28T22:45:44.974749+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Tabela de Serviços OGA135 no SIGAAGR
type: support-article
updated_at: '2025-06-24T20:44:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30488590981271-Agro-Linha-Protheus-AGR-Tabela-de-Servi%C3%A7os-OGA135-no-SIGAAGR
---

A rotina tabela de serviços **OGA135** permite definir uma tabela de serviço com data de vigência, e vincular itens de serviços de armazenagem. Este registro da tabela de serviços é informado no contrato de deposito de terceiro **OGA260**, que posteriormente conforme parametrização será usado para realizar os cálculos de serviços **OGA262** de armazenagem que incidem sobre o contrato.

Após cadastrar a tabela de serviço **OGA135** definindo o período em que ela estará ativa, é possível via opção do menu **“Outras Ações > Serviços**”, incluir um ou mais registros para os itens da tabela de serviço **OGA135I**.    
  
Entre os campos de parametrização podemos citar:

|  |  |
| --- | --- |
| Ord. Cálculo | Indica a ordem do serviço no momento de realizar os cálculos de armazenagem. |
| Despesa | Indica o código da despesa. |
| Fator Gerador | Indica o momento que será considerado para gerar os custos de armazenagem. Os valores aceitos são:  0 - Entrada (Gera pela nota fiscal de entrada).  1 - Saída (Gera pela nota fiscal de saída).  2 - Saldo (Gera a partir do saldo do produto no armazém na data de cálculo). |
| Tipo de Cobrança | Indica se a cobrança será realizada gerando um valor a receber ou retenção de um volume de mercadoria. Os valores aceitos são:  0 - Valor  1 - Retenção |
| Perc Retenção | Indica o percentual de retenção quando o tipo de cobrança é igual a **1 - Retenção**. |
| Tipo de Retenção | Indica o tipo de retenção quando o tipo de cobrança é igual a **1 - Retenção**. Os valores aceitos são:  0 - Quebra técnica (utilizado para identificar a retenção quando se dá por quebra técnica).  1 - Cobrança (utilizado para identificar que a cobrança do serviço será por meio da retenção da mercadoria). |
| Valor Tarifa | Indica o valor da tarifa que será cobrado pelo serviço quando o tipo de cobrança é por valor. |
| Per. Cobrança | Indica o período que será realizado para cobrança do serviço. Informação utilizada para cálculo do serviço de armazenagem. Os valores aceitos são:  0 - Diário  1 - Quinzenal  2 - Mensal |
| Cob.Per.Par | Indica a regra que deve ser adotada quando ocorrerem períodos parciais. Os valores aceitos são:  0 - Livre (considera apenas o período fechado. Por exemplo: Caso o período de cálculo esteja dentro 2,5 quinzenas, será cobrado por 2 quinzenas.)  1 - Cheia (considera o período cheio. Por exemplo: Caso o período de cálculo esteja dentro 2,5 quinzenas, será cobrado por 3 quinzenas.)  2 - Proporcional (considera o período proporcional. Por exemplo: Caso o período de cálculo esteja dentro 2,5 quinzenas, será cobrado por 2,5 quinzenas.).  Não é aceito para fator gerador Saldo quando Per. Cobrança quinzenal ou mensal. |
| Aprovação | Indica se deverá haver aprovação do serviço após o cálculo. Os valores aceitos são:  0 - Automática  1 - Manual |

O cadastro de serviços também permite definir tarifa por resultado de análise. Esses dados podem ser informados na tabela inferior do cadastro. Deve-se informar o código do desconto, a faixa **%** da análise e o valor da tarifa ou percentual de retenção.

**Para mais informações:**<https://tdn.totvs.com/pages/releaseview.action?pageId=516644407>

<https://tdn.totvs.com/display/PROT/Armazenagem>
