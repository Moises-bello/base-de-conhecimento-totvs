---
content_hash: dec9d0b6a51048521fb0cc2eb0f604c0d353abad63aceb663670e015c69d336e
fetched_at: '2026-06-29T00:12:10.307662+00:00'
page_id: '953002044'
product: rm
source: tdn-rm
title: Grupo I05g - Grupo Credito Presumido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953002044
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo I05g - Grupo Credito Presumido** | | | | | | | | | | | | |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo da Aplicação** | **Mais Informações** |
| 104.07 | I05g | gCred | Grupo de informações sobre o Crédito Presumido | G | I01 |  | 0-4 |  |  |  |  | Grupo gerado se o campo "Tipo de Crédito" do código de ajuste for igual a "Crédito Presumido". |
| 104.08 | I05h | cCredPresumido | Código de Benefício Fiscal de Crédito Presumido na UF aplicado ao item | E | I05g | C | 1-1 | 8,10 |  | DCODIGOAJUSTE.CODAJUSTE | Código Ajuste | Código de Benefício Fiscal de Crédito Presumido na UF - Gerada conforme a tag <cBenf> |
| 104.09 | I05i | pCredPresumido | Percentual do Crédito Presumido | E | I05g | N | 1-1 | 3v2-4 |  | DCODIGOAJUSTE.CODFRMALIQUOTA | Fórmula Alíquota | Percentual do Crédito Presumido - Será gerada com o valor do Campo Fórmula de Alíquota informado no cadastro do Código de Ajuste.  Exemplo fórmula:  *DECL NAT;* *DECL ALIQ;*  *SETVAR(NAT,TABNATITEM('CODNAT','V'));* *SETVAR(ALIQ,TABNATITEM('ALIQICMS','V'));*  *Se ((NAT >'6.102') AND (ALIQ = 12))* *ENTAO* *8.40* *SENAO* *((NAT >'6.102') AND (ALIQ = 4))* *ENTAO* *3* |
| 104.10 | I05j | vCredPresumido | Valor do Crédito Presumido | E | I05g | N | 1-1 | 13v2 |  |  | Valor do Item x Alíquota Informada | Valor do Crédito Presumido - Será o resultado do cálculo (Valor do Item x (Valor Percentual da Fórmula / 100)) |

Observação

Este grupo está disponível à partir da versão 12.1.2406
