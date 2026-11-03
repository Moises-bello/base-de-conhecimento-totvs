---
article_id: 30630645722135
category: Originação de Grãos (OG)
content_hash: 8e78970b57770fe0097137cc715ebfd3bc839187e34cf6ae2773ead18b8dc90c
fetched_at: '2026-06-28T22:45:41.164288+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Para adicionar cláusulas no select que traz os
  Lotes para selecionar
type: support-article
updated_at: '2025-07-08T19:45:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30630645722135-Agro-Linha-Protheus-AGR-Para-adicionar-cl%C3%A1usulas-no-select-que-traz-os-Lotes-para-selecionar
---

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agronegócio |
| **Módulo:** | Gestão de Agronegócio |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA870A | Função chamada a partir da opção alterar/incluir a rotina AGRA870 | |
| **Ponto de entrada:** | AG870AA8 |
| **País(es):** | Todos |
| **Pacote:** | 12.1.23 e superior. |

## **Ponto de Entrada:**

| **Localização:** | AGRF4LOTE() |
| **Programa Fonte:** | AGRA870A |
| **Função:** | Permitir adicionar cláusulas no select que traz os lotes para serem selecionados |
| Parâmetros: | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | PARAMIXB[1] | caractere | Consulta | Não | | PARAMIXB[2] | caractere | Pedido | Não | | PARAMIXB[3] | caractere | Item | Não | | PARAMIXB[4] | caractere | Produto | Não | |
| **Retorno:** | |  |  |  | | --- | --- | --- | | **Tipo** | **Descrição** | **Obrigatório** | | caractere | Retorne a variável concatenada às cláusulas que foram adicionadas | Não | |

**Exemplo:**

|  |
| --- |
| `<``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>FUNÇÃO DO USUÁRIO AG870AA8()</``font``></``font``><``font``></``font``>`  `<``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`  `//personalizações</``font``></``font``><``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`  `cQuery += "E B8_SALDO > 0"</``font``></``font``><``font``></``font``>`  `<``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`  `RETORNAR cQuery</``font``></``font``>` |
