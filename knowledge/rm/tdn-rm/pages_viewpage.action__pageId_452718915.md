---
content_hash: c9934a8468434fb7ede1a7156eff37a88692400df46945b5189c7536b5bf2391
fetched_at: '2026-06-29T00:10:02.456994+00:00'
page_id: '452718915'
product: rm
source: tdn-rm
title: Código de Cálculo 191 - INSS Retificação SEFIP - 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718915
version: 2
---

Este código de cálculo corresponde ao valor do INSS 13º Salário referente ao mês a ser retificado.   
 Poderá ser do tipo "Desconto" ou "Provento", nunca poderá ser do tipo "Base de Cálculo", e não poderá ter incidência em: FGTS 13º Salário, INSS 13º Salário, Est. Cálc. INSS 13º ou Est. Cálc. FGTS 13º.  
 O sistema não calcula este código de cálculo, o usuário deverá digitar o valor ou utilizar fórmula de cálculo.  
 Quando o código de cálculo for do tipo "Desconto", deverá marcar a opção "Est. Cálc. IRRF 13º".  
 Somente será desconto quando o funcionário receber um valor a menor em meses anteriores e na movimentação atual o usuário lançar o pagamento da retificação de 13º Salário.  
 Quando o código de cálculo for do tipo "Provento", deverá marcar a opção "IRRF 13º Salário" e "Informe Rend.".  
 Somente será provento quando o funcionário receber um valor a maior em meses anteriores e na movimentação atual o usuário lançar o desconto da retificação de 13º Salário.

**Observações**

1°) Quando utilizar fórmula de cálculo no evento com código de cálculo 191, a fórmula deverá calcular o valor do INSS utilizando a tabela de cálculo do mês em que se refere a retificação, observando o teto da tabela.

2°) O sistema utiliza este código de cálculo na DIRF e "Informe de Rendimentos" no campo "Décimo Terceiro Salário".

3°) O evento de IRRF 13º Salário sobre a retificação 13º Salário, deverá ser calculado manualmente ou através de fórmula e terá o código de cálculo 106 quando for desconto e código de cálculo 052 quando for provento.  
    
 **Dica**  
    
 Criar um evento de INSS Retificação SEFIP 13º Salário para cada competência a que a retificação se referir.  
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
