---
article_id: 33477926410519
category: Originação de Grãos (OG)
content_hash: 5033a4d871f7ce9d5893105239b5a5f95f5d134883e16da90000203bd6973420
fetched_at: '2026-06-28T22:45:41.109646+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - OGX00401 PE Ajuste na classificação do romaneio
type: support-article
updated_at: '2025-11-03T20:46:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33477926410519-Agro-Linha-Protheus-AGR-OGX00401-PE-Ajuste-na-classifica%C3%A7%C3%A3o-do-romaneio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33477928043799) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como funciona **OGX00401 PE Ajuste na classificação do romaneio**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Visão Geral:**  
O ponto de entrada **OGX00401()** esta disponível nas chamadas da função **OGX004DESC()** executada nas rotinas do **Romaneio** **OGA250/OGA251/AGRA500** e **Amostras Avulsas - OGA180**.

O ponto de entrada **OGX00401()** permite realizar ajustes nos itens de classificação do romaneio, podendo adequar o calculo do resultado conforme uma necessidade especifica.

| **Localização:** | OGX004DESC |
| **Programa Fonte:** | OGX004 |
| **Função:** | OGX00401()  | aRetPe := ExecBlock("OGX00401",.F.,.F.,{aRetorno, NJJ\_TABELA, NJJ\_PSSUBT, aItens, lRecursivo }) | | --- | | |  | |
| **Parametros:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | aRetorno | Array | Itens de classificação do romaneio(NJK)  aRetorno[1][1] := NJK\_CODDES  aRetorno[1][2] := NJK\_BASDES  aRetorno[1][3] := NJK\_PERDES  aRetorno[1][4] := NJK\_READES  aRetorno[1][5] := NJK\_QTDDES  aRetorno[1][6] := ""  aRetorno[1][7] := NNK\_TABALT  aRetorno[1][8] := NNJ\_GRUPO  aRetorno[1][9] := NNJ\_DESREL  aRetorno[1][10] := NNJ\_FORMUL | Sim | | cTabela | Caracter | Tabela de classificação/descontos | Sim | | nPsSubt | Numérico | Peso bruto do romaneio | Sim | | aItens | Array | Itens de classificação/descontos  aItens[1][1] := NJK\_CODDES  aItens[1][2] := NJK\_BASDES | Sim | | lRecursivo | Logical | Se repete(NNJ\_GRUPO=1), para avaliação desconto agrupador | Sim | |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | aRetPe | Array | Retorno  do array no mesmo padrão do parametro aRetorno com os ajustes realizados. | Sim | |

**Exemplo de Utilização:**

Abaixo segue um exemplo do ponto de entrada.

![EMPL.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33477926392983)
