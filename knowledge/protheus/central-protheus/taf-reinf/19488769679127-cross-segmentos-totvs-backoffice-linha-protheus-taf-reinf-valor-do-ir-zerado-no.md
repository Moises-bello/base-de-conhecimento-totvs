---
article_id: 19488769679127
category: TAF - REINF
content_hash: 86afbf873333f13c0fd9bc2dd6437fa9f923a5b0000e0f433932604c0e7492db
fetched_at: '2026-06-28T22:41:34.927563+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - TAF - REINF - Valor do
  IR zerado no Painel Reinf
type: support-article
updated_at: '2024-01-05T15:06:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19488769679127-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-TAF-REINF-Valor-do-IR-zerado-no-Painel-Reinf
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20346148758807) Tempo aproximado para leitura: **00:03:00min****Ocorrência**Ao efetuar a integração dos documentos para gerar os eventos R-4010 ou R-4020 para o TAF, o Painel Reinf está demonstrando os valores zerados de base e valor do IR.  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Linha Protheus - TOTVS Automação Fiscal - Todas as versões  
  
**Causa**

O incidente pode ocorrer devido ao seguinte:

* erro de integração dos registros T013, T154 ou T158
* vinculo do código do tributo na rotina incorreta
* utilização do parâmetro **MV\_TAFDT40** de forma incompleta

1- Inicialmente verificar se os layouts T013, T154 e/ou T158 foram integrados corretamente ao TAF:

Cross Segmentos - Backoffice Protheus - TAF - REINF - Como consultar o gerenciador de integração

Caso tenha ocorrido erros nessa etapa, o IR não será demonstrado no painel, sendo necessário corrigir os erros de integração e posteriormente reintegrar os dados. Isso pode ocorrer se no painel for demonstrado somente o PGT sendo que o IR é na emissão.

2 - Verificar se o IR está demonstrado na rotina correta: Caso a nota fiscal possua IR, o título vinculado a essa nota não possua o código 12 do IR, mas sim os códigos do**Pis e Cofins** por exemplo, o painel reinf não irá demonstrar o valor do IR do documento. Se o IR for no pagamento, é necessário que no Pagamento seja utilizado o código 28 - IR pagamento, se for utilizado o código 12 também ficará incorreto e não será exibido.

3 - **MV\_TAFDT40**: Se o parâmetro estiver habilitado para considerar o IR pela contabilização mas os campos do documento **LEM\_DTCONT**  e **C20\_DTCONT** estiverem vazios, os documentos com IR não serão exibidos no Painel Reinf. Esse parâmetro deve ser habilitado para uso em conjunto com os campos citados  **preenchidos**.
