---
article_id: 20609694150935
category: Materiais - Compras (SIGACOM)
content_hash: fcf9b67bbd0ac2b51716a703ba66e9ba0a7e839418f668ebe16ae4c5078fbfc1
fetched_at: '2026-06-28T22:41:25.461266+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM: O campo D1_CLASFIS
  está sendo alterado quando há informações no campo DT_CLASFIS na Nota'
type: support-article
updated_at: '2024-06-13T19:43:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20609694150935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-campo-D1-CLASFIS-est%C3%A1-sendo-alterado-quando-h%C3%A1-informa%C3%A7%C3%B5es-no-campo-DT-CLASFIS-na-Nota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20609720584471) Tempo aproximado para leitura: **00h05 min****Dúvida**O que fazer quando o campo D1\_CLASFIS alterar as informações mantendo o que está no campo DT\_CLASFIS ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução**

Será necessário realizar a criação do Parâmetro MV\_COLCLAS para que possa definir como será a gravação do campo CLASFIS (D1 e FT) quando o documento for de origem Importador XML.

* Se MV\_COLCLAS = 0 (Default) → Igual SDT
* Se MV\_COLCLAS = 1 → Somente origem igual SDT
* Se MV\_COLCLAS = 2 →  Não busca na SDT e mantem o que esta na SD1

**Criação do Parâmetro:**

**Acessar o Configurador / Dicionário / Base de Dados.**

1. Clicar em **Parâmetros**;

2. Clicar em **Incluir**;

![](https://tdn.totvs.com/download/attachments/699814909/image2021-7-30_16-38-52.png?version=1&modificationDate=1658521076240&api=v2)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20609824560151)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20609826340119)

 **Tabela 2:**

| Campo: | Aba: | Valor: |
| --- | --- | --- |

| **Filial:** | Informações | Preencher este campo, caso o controle dos parâmetros seja por Filial |
| **Nome var:** | Informações | MV\_COLCLAS |
| **Tipo:** | Informações | 3 - Numérico |
| **Conteúdo:** | Informações | 0 |
|  | | |
| **Descrição: Cont. Descriç Cont. Descriç** | Descrição | Define situação tributaria quando integrada com importador XML |

***Obs:***

Este parâmetro estará disponível automaticamente a partir do release 12.1.22.10, porém poderá ser criado manualmente

***Saiba Mais:***

[DT Campo D1\_CLASFIS altera conteúdo quando a nota tem DT\_CLASFIS](https://tdn.totvs.com/pages/releaseview.action?pageId=699814909)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Erros (Códigos)](https://tdn.totvs.com/pages/releaseview.action?pageId=271663193)

[Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML'](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
