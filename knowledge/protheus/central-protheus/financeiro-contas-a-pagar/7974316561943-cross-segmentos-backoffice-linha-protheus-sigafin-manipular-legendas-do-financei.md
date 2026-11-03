---
article_id: 7974316561943
category: Financeiro - Contas a Pagar
content_hash: cd6ec07ac3b67b58a900fe3cc3ac67a4cdb9e9138df988de2fd8a605b28c68cd
fetched_at: '2026-06-28T22:38:09.788791+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Manipular legendas
  do financeiro '
type: support-article
updated_at: '2022-08-29T20:53:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7974316561943-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Manipular-legendas-do-financeiro
---

O retorno desse ponto de entrada substituirá as regras do padrão.

Lembrando que as regras de legenda são consideradas na ordem do array retornado.

A primeira regra atendida definirá a cor que será atribuída.

Atenção para com a ordem das regras e conflitos.

É chamado para retornar as regras de legendas e quando acionado o botão de **Legendas** mostrada a tela:

![](https://tdn.totvs.com/download/thumbnails/572211290/image2020-11-16_10-42-59.png?version=1&modificationDate=1605538053697&api=v2)

**Parâmetros**

| Nome | Descrição |
| --- | --- |
| nReg | Com valor: Abrir a telinha de legendas ### Sem valor: Retornar as regras |
| cAlias | SE1 ou SE2, dependendo da rotina utilizada |
| aRegras | Regras do Padrão |
| aLegendas | Legendas do Padrão |

**Retorno**

| Nome | Descrição |
| --- | --- |
| aRet | Array com todas as regras de legendas.  Estrutura do array: 1º posição: Regra  2ª posição: Cor |

**Exemplo de utilização:**

**FINALEG**

|  |
| --- |
| `#INCLUDE``"PROTHEUS.CH"`    `User Function FINALeg()`    `Local nReg := PARAMIXB[``1``]``// Com valor: Abrir a telinha de legendas ### Sem valor: Retornar as regras`  `Local cAlias := PARAMIXB[``2``]``// SE1 ou SE2`  `Local aRegras := PARAMIXB[``3``]``// Regras do padrão`  `Local aLegendas := PARAMIXB[``4``]``// Legendas do padrão`  `Local aRet := {}`  `Local nI :=``0`    `/*`  `Sem Recno --> Retornar array com as regras para o Browse colocar as cores nas colunas.`  `Com Recno --> Chamada quando acionado botão Legendas do browse -> Abrir telinha de Legendas (BrwLegenda)`  `*/`  `If nReg = Nil`    `/*`  `aRegras passado contém as regras do padrão`  `O array retornado deverá conter todas as regras, do padrão e customizadas.`    `Dicas:`  `Lembrando que as regras de legenda são consideradas na ordem do array retornado.`  `A Primeira regra atendida definirá a cor que será atribuída.`  `Atenção para com a ordem das regras e com regras conflitantes.`  `A Última regra do padrão, caso não atenda a nenhuma condição anterior é a .T. -> BR_VERDE -> Título em aberto`  `*/`  `If cAlias =``"SE1"`    `/*`  `Exemplo: adicionar uma regra de legenda "mais prioritária" que as do padrão`  `*/`  `aAdd(aRet,{``"!Empty(E1_PORTADO) .AND. Empty(E1_NUMBOR)"``,``"BR_LARANJA"``})`    `/*`  `Regras do padrão para retorno`  `*/`  `For nI :=``1` `To Len(aRegras)`  `aAdd(aRet,{aRegras[nI][``1``],aRegras[nI][``2``]})`  `Next nI`    `Else``// SE2`    `/*`  `Exemplo para retornar as mesmas regras do padrão sem alteração`  `*/`  `aRet := aRegras`    `Endif`      `Else``// Abrir telinha de Legendas (BrwLegenda)`    `If cAlias =``"SE1"`    `aAdd(aLegendas,{``"BR_LARANJA"``,``"Título em Portador"``})`    `Else``// SE2`  `/*`  `Adicionar a cor e descrição de legendas para SE2 aqui. Exemplo:`  `Aadd(aLegendas, {"BR_AMARELO", "Titulo aguardando liberacao"}) //Titulo aguardando liberacao`  `*/`  `Endif`    `BrwLegenda(cCadastro,``"Legenda"``, aLegendas)`    `Endif`    `Return aRet` |

**Saiba Mais**[FINALEG](https://tdn.totvs.com/display/public/PROT/FINALEG+-+Manipula+legendas+financeiro) [- Manipula legendas financeiro](https://tdn.totvs.com/display/public/PROT/FINALEG+-+Manipula+legendas+financeiro)
