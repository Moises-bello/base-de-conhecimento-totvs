---
content_hash: bddda51ac48a2a3dfbf0102750e06cdfa7b074e49f7237347404445f66eaa763
fetched_at: '2026-07-02T19:24:23.399634+00:00'
page_id: '448600268'
product: protheus
source: tdn-tec
title: Seção [BTMonitorAppD] - Chave ApplicationNodeName
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448600268
version: 10
---

Define o nome do nó na camada de aplicação de uma aplicação instrumentada pelo BTMonitor no controlador do AppDynamics.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| não preenchido (Padrão) | Gera o nome do nó a partir do conteúdo de outras chaves da configuração do BTMonitor e do AppServer. |
| <texto\_definido\_pelo\_usuário> | Usa <texto\_definido\_pelo\_usuário> como nome do nó, respeitando as observações listadas. |

## Observações

* **Como regra geral, nomes de nós devem ser únicos.** No entanto, nós que residem em diferentes camadas e máquinas diferentes (hosts) podem ter nomes de nós duplicados;
* Dentro de uma aplicação, os nomes dos nós devem sempre ser únicos nos seguintes casos:

  + se os nós residem na mesma camada, mas em máquinas diferentes;
  + se os nós residem na mesma máquina, mas em diferentes camadas;
  + nomes de nós e nomes de máquinas devem ser únicos. Quando um nó é registrado em um controlador, aquele é associado à máquina onde está, e não pode ser movido para outra máquina sem mudar o nome do nó;
  + nós em agentes baseados em proxy podem ter nomes duplicados na mesma camada e mesma máquina;
* O tamanho máximo do nome do nó deve ser de 500 caracteres;
* Além de números e caracteres em caixa alta e baixa, os seguintes caracteres especiais podem ser usados:
* Caso o nome do nó não seja preenchido, este será gerado no seguinte formato:

  --]]>
* Onde as partes do nome do nó serão:

  | Parte do nome do nó | Origem |
  | --- | --- |
  | ``` <nome_da_máquina> ``` | Nome da máquina (computador) |
  | ``` <nome_da_camada> ``` |  |
  | ``` <número_da_porta_com_zeros_à_esquerda> ``` | O primeiro dos seguintes valores de chave:  ou , preenchido com zeros à esquerda até 5 posições,  ou , preenchido com zeros à esquerda até 5 posições,  ou `00000`, cinco zeros, indicando ausência de valor de porta adequado. |

## Exemplos

* Caso o **nome do nó seja fornecido**: define o nome do nó como **SomeNodeName01** na camada de aplicação SomeTierName01 da aplicação instrumentada SomeApplicationName01:
* Caso o **nome do nó não seja fornecido**: define o nome do nó como **SomeServerMachineName-**SomeTierName01-01234****a partir do nome da máquina **SomeServerMachineName**, do nome da camada **SomeTierName01** e da **porta TCP 1234**:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
