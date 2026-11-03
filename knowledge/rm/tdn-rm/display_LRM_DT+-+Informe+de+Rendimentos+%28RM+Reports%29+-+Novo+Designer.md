---
content_hash: 4a84457081a4f904b25357fb8b1015c075296f7b978dbb6eb09bffb752eaf91e
fetched_at: '2026-06-29T00:11:25.647608+00:00'
page_id: '714234519'
product: rm
source: tdn-rm
title: DT - Informe de Rendimentos (RM Reports) - Novo Designer
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Informe+de+Rendimentos+%28RM+Reports%29+-+Novo+Designer
version: 24
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | RM Reports |
| País: | Brasil |
| Release: | a partir da **12.1.2209.169** |
| Issue: | [DRHROTRM-4062](https://jiraproducao.totvs.com.br/browse/DRHROTRM-4062 "View this issue") |

## **02. SITUAÇÃO/REQUISITO**

Modernizar o design do leiaute do Informe de Rendimentos, trazendo melhor experiência no produto e mais satisfação aos nossos usuários. 

## **03. SOLUÇÃO**

Disponibilizado o novo modelo do Informe de Rendimentos gerado através do menu **Anuais | DIRF/Informe de Rendimentos:**

Relatório "FOPREL0008 - Informe de rendimentos - NOVO MODELO"

**Observações:**

* Devido a necessidade de reformulação do quadro 7 (Informações complementares), criamos a tabela **PDIRFCOMPLEMENTO**, onde as informações passam a ser armazenadas em colunas ou invés serem armazenada em apenas um campo, assim a impressão das informações desde campo ficarão alinhadas, semelhante aos demais campos.  Lembrando que, essa tabela é preenchida durante o processamento do Informe de Rendimentos, quando marcadas as opções **"Lançar Valores para o Gerador de Relatórios"** e **"Deletar Ano de Referência"**.

* O informe de rendimentos que já esta processado e disponibilizado no portal antes da implementação, será exibido no leiaute antigo, devido não existir dados na tabela PDIRFCOMPLEMENTO. Caso deseje exibir esse informe no novo leiaute, deverá regera-lo para que a tabela seja preenchida.

## **04. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719351)

[DT - Informe de Rendimentos - Usar Responsável da DIRF em Arquivo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=735439697)
