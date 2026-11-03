---
content_hash: 061f8092cd6a72a1a9a8386e4654186cd96f2a70000c8ba602756cef13ad84d0
fetched_at: '2026-06-29T00:11:49.734952+00:00'
page_id: '837861728'
product: rm
source: tdn-rm
title: DT - S-1260 - Desconsiderar a comercialização do indicador igual a 3
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=837861728
version: 8
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1260 - Desconsiderar a comercialização do indicador igual a 3 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9678](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9678) |

## **02.** **LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2306.251
* 12.1.2310.191
* 12.1.2402.128 e superiores.

## **03.****SITUAÇÃO/REQUISITO**

De acordo com o MOS, conforme descrito abaixo no item 1.4 quando a comercialização isenta ocorrer com empresa adquirente, o produtor rural não é obrigado a enviar o "S-1260 - Comercialização da Produção Rural Pessoa Física", neste caso, quem deverá enviar a informação será o segurado especial que comercializar.

***"1.4. Quando o produtor rural pessoa física contribuinte individual e o segurado especial comercializarem produção rural isenta com adquirente produtor rural pessoa física ou segurado especial, os que comercializarem devem enviar o evento S-1260 com ({tpComerc}=7). Nesse caso, a responsabilidade pelo recolhimento do Senar é do produtor rural ou segurado especial que comercializa. Todavia, quando a comercialização de produção rural isenta ocorrer com empresa adquirente ou com intermediário Pessoa Física, o produtor rural pessoa física contribuinte individual não é obrigado a enviar este evento e o segurado especial que comercializar, caso opte por enviar este evento, deve fazê-lo usando ({tpComerc}=3. Nesses casos, a responsabilidade pela retenção e pelo recolhimento da contribuição para o Senar é do adquirente, que cumprirá suas obrigações por meio do envio do evento R-2055 na EFD-Reinf. "***

## **04.****SOLUÇÃO**

Possibilidade de não enviar dados no S-1260 quando a empresa não está obrigada a realizar esse envio, visto que, nesse caso, é o adquirente quem é responsável por recolher e reportar os dados.

Diante dessa situação, desenvolvemos o parâmetro "**Desconsiderar o indicador de comercialização igual a 3 no evento S-1260 pessoa jurídica não inscrita no PAA**". Ao ativá-lo, os movimentos serão excluídos da geração do S-1260 nos casos em que a venda é feita para uma pessoa jurídica adquirente não optante pelo Programa de Alimentação do Trabalhador (PAA).

**ATENÇÃO**: Essa implementação foi solicitada pelo time de MATERIAIS, que realizou alterações no serviço responsável por fornecer as informações do evento S-1260, conforme issue [DRMMATERIAIS-2436](https://jiraproducao.totvs.com.br/browse/DRMMATERIAIS-2436).

## **05. DEMAIS INFORMAÇÕES**

[S-1260](https://tdn.totvs.com.br/pages/releaseview.action?pageId=479829352)
