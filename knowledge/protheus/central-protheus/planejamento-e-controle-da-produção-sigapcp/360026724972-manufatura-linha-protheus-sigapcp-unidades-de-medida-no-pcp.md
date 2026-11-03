---
article_id: 360026724972
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 32d6ebe5b9bcafc41ff0b146d0dd3ebb3cfef4fa8a16f2430767f9f4f3c9599f
fetched_at: '2026-06-28T22:42:47.094291+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Unidades de medida no PCP
type: support-article
updated_at: '2021-11-03T13:10:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026724972-Manufatura-Linha-Protheus-SIGAPCP-Unidades-de-medida-no-PCP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:45 min****Dúvida**Como o **PCP - Planejamento e controle da produção** trabalha com as unidades de medida?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
O **PCP** sempre considera a 1ª unidade de medida informada na rotina **MATA010 - Atualização de Produtos**, no campo **Unidade**. A 2ª unidade de medida informada no campo **Seg. Un. Medi.** desta rotina é opcional.  
  
A 1ª unidade de medida é considerada a unidade de medida padrão, e é utilizada em todos os movimentos, desde a compra até a venda. A 2ª unidade de medida é utilizada em transações em que as partes trabalham com unidades de medidas distintas, sendo obtidas a partir do fator de conversão determinado.  
  
Quando utilizada a segunda unidade de medida, as demais rotinas que consideram esta informação, também utilizam os campos **Fator Conv.** e **Tipo de Conv** da rotina **MATA010** para fazer a conversão.

* **Fator de conversão**: valor a ser aplicado na 1ª unidade de medida para obter a segunda unidade de medida, conforme o tipo de conversão.
* **Tipo de conversão**: determina como é obtida a segunda unidade de medida, se multiplicada ou dividida a 1ª unidade de medida pelo fator de conversão.

**Exemplo**  
1ª Unidade de Medida = 3 Kg  
    Fator de Conversão = 1000  
    Tipo de conversão = Multiplicação  
  
2ª Unidade de Medida = 3000 gramas  
    O Sistema controla o saldo nas 2 unidades, mas o custo unitário reflete o valor na unidade padrão.  
  
**Importante**  
Caso o produto não possua um fator de conversão fixo, como por exemplo, quando sofre variações por fatores físicos como umidade, calor, etc., é possível informar a quantidade nas duas unidades de medida, digitando diretamente seus valores, sem o cadastramento do fator de conversão.
