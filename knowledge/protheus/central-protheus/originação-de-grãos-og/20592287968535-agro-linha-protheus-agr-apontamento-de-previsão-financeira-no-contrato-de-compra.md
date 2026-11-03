---
article_id: 20592287968535
category: Originação de Grãos (OG)
content_hash: 6909ff129c745e5c8c0db4e4fcada15efc9181daf145d1f0366da2195a3b4b9c
fetched_at: '2026-06-28T22:45:37.002056+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Apontamento de previsão financeira no contrato
  de compra
type: support-article
updated_at: '2025-01-07T14:10:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20592287968535-Agro-Linha-Protheus-AGR-Apontamento-de-previs%C3%A3o-financeira-no-contrato-de-compra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20592287923863) Tempo aproximado para leitura: **00:01:300 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para inserir uma **previsão financeira** é apresentada a ocorrência **Apontamento de previsão financeira no contrato de compra**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para inserir uma **previsão financeira** no Sistema.  
  
**Solução**  
Para que seja possível incluir uma **previsão financeira** no contrato existem duas formas:  
A primeira forma é acessando a pasta **Financeiro** e inserindo uma linha, a regra é que o valor total seja igual ao valor total do contrato. Podem ser incluídas quantas linhas forem necessárias.

![PREV.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20592287926679)

A outra forma é pela opção de **Composição de Preços**. Para isso é necessário cadastrar um componente de preço por meio da rotina **OGA410 - Componentes de Preço**.

![PREV1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20592248891543)

Ao acessar a rotina **OGA280** ou **OGA290** e selecionar a opção de **Composição de Preços**, das **Outras Ações**, serão exibidos os componentes de preço cadastrados, de acordo com as demais informações do contrato.

![PREV2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20592248903575)

Após informar a composição de preço para o contrato será incluída a previsão financeira na pasta  
**Financeiro**.

![PREV3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20592287938071)
