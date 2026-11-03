---
content_hash: 8dcbb888dda9ed01888c9d5c2d5e73d7ca59d7f4440b0dff370072652ed82bdf
fetched_at: '2026-06-29T00:10:47.818942+00:00'
page_id: '560654804'
product: rm
source: tdn-rm
title: DT- MP 936 – Indenização - Tratamento SEFIP/GRRF/FOLHA ANALÍTICA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560654804
version: 5
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | SEFIP / GRRF / Folha Analítica |
| **Situação/Requisito:** | Ao demitir funcionário que estava afastado ou com processo de redução Covid 19, e o mesmo for demitido antes do prazo da estabilidade, ele terá direito a indenização, portanto o valor da indenização, terá que ser levado para a GRRF com incidência em FGTS, conforme o novo manual da Caixa.Como o evento é tratado por fórmula, não tem codigo de cálculo, se colocar incidência em FGTS no evento, ao gerar a SEFIP, o validador da Caixa irá realizar o desconto de INSS, por não se tratar de uma verba indenizatória. |
| **Solução/Implementação:** | Foi criado o Código de Cálculo 440 - MULTA POR DEMISSÃO EM PERÍODO DE ESTABILIDADE Evento do tipo valor que deve ser calculado manualmente ou por fórmula pelo usuário. Quando existir o evento na rescisão, o valor será informado como verba indenizatória na GRRF.  **Observação:**  Não foi criado um código de cálculo específico para diferença, como o controle será manual, o usuário deverá criar um outro evento com o mesmo código de cálculo 440 e informar como evento de diferença no evento da rescisão original. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-11701](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-11701) e [FOPROTINAS01-12572](https://jiraproducao.totvs.com.br/browse/FOPROTINAS01-12572) |
| **Documento de Referência:** | [Código de Cálculo 440 - MULTA POR DEMISSÃO EM PERÍODO DE ESTABILIDADE](https://tdn.totvs.com.br/pages/viewpage.action?pageId=560653919) |
| **Pacote:** | N/A |
