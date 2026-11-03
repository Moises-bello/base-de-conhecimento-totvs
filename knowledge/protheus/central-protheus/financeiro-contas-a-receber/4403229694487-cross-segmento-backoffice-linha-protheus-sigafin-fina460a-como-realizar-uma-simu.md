---
article_id: 4403229694487
category: Financeiro - Contas a Receber
content_hash: c75a83f4fb0f67475e1d51c876b488a90edf474e0f5b759bca636c8a886d14d0
fetched_at: '2026-06-28T22:38:12.846527+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA460A - Como realizar
  uma simulação de liquidação a Receber
type: support-article
updated_at: '2021-12-02T17:14:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403229694487-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA460A-Como-realizar-uma-simula%C3%A7%C3%A3o-de-liquida%C3%A7%C3%A3o-a-Receber
---

**Dúvida**Como realizar uma simulação de liquidação a Receber?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA460A - Todas as versões  
  
**Solução**

Na inclusão da Simulação irá apresentar os parâmetros iniciais da rotina **FINA460**, para seleção dos títulos.

Ao **salvar** a a Simulação irá gravar somente a simulação e ao **Efetivar Simulação**, irá gravar a simulação e gerar a liquidação.

Caso a **Simulação** seja alterada, será criada uma nova versão nas tabelas envolvidas.

A Simulação que estiver **bloqueada**, **cancelada**, **gerada** ou **encerrada** não pode sofrer alteração.

Grave a liquidação dos títulos selecionados e gera os novos conforme dados da simulação.

Caso exista mais de uma versão para o mesmo processo de simulação, as demais simulações terão status alterado para **Encerrada**.

Todos os campos estarão disponíveis apenas para visualização.

**Botão Bloquear**

Altera o status da Simulação para bloqueado.

**Estorno bloqueio**

Altera o status da Simulação para Ativo.

**Encerramento/Cancelamento de uma Simulação**

Uma simulação somente é exibida como **Encerrada**/**Cancelada** (Legenda Preta) quando a mesma for efetivada (se tornou uma liquidação/gerada), em seguida essa liquidação é cancelada (através da rotina **FINA460** - opção **Cancelar**) e ao final ser selecionada a opção **Cancelar** a simulação.

**Exemplos**

1) **Simulação Efetivada**/**Liquidação Gerada**:

![](https://tdn.totvs.com/download/attachments/305930204/image2019-9-30_15-6-46.png?version=1&modificationDate=1569866806253&api=v2)

2) Ao cancelar a liquidação, é exibida a pergunta relacionada as simulações: "**Deseja cancelar as simulações desta liquidação?**"

![](https://tdn.totvs.com/download/attachments/305930204/image2019-9-30_15-8-37.png?version=1&modificationDate=1569866917113&api=v2)

3) Respondendo sim, as simulações utilizadas desse processo serão canceladas/**encerradas** e não poderão ser mais utilizadas.

![](https://tdn.totvs.com/download/attachments/305930204/image2019-9-30_15-26-19.png?version=1&modificationDate=1569867980200&api=v2)

Segue as legendas da rotina **Simulação de liquidação a Receber**:

|  |  |
| --- | --- |
| **Cor** | **Descrição** |
|  | Simulação Bloqueada |
|  | Simulação Vigente |
|  | Simulação Vencida |
|  | Simulação Gerada |
|  | Simulação Encerrada/Cancelada |

**Saiba Mais**<https://tdn.totvs.com/pages/releaseview.action?pageId=305930204>
