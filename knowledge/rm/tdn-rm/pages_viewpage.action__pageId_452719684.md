---
content_hash: c46f343e2d537734b210098b75df703907324de21aed1991d64ae0feafc10386
fetched_at: '2026-06-29T00:10:09.498687+00:00'
page_id: '452719684'
product: rm
source: tdn-rm
title: Código de Cálculo 188 - INSS Retificação SEFIP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719684
version: 2
---

Este código de cálculo corresponde ao valor do INSS referente ao mês a ser retificado.   
 Poderá ser do tipo "Desconto" ou "Provento", nunca poderá ser do tipo "Base de Cálculo", e não poderá ter incidência em: FGTS, INSS, Estorna FGTS ou Estorna INSS  
 O sistema não calcula este código de cálculo, o usuário deverá digitar o valor ou utilizar fórmula de cálculo.  
 Quando o código de cálculo for do tipo "Desconto", deverá marcar a opção "Estorna IRRF" ou "Est. Cálc. IRRF de Férias".  
 Somente será desconto quando o funcionário receber um valor a menor em meses anteriores e na movimentação atual o usuário lançar o pagamento da retificação.  
 Quando o código de cálculo for do tipo "Provento", deverá marcar a opção "IRRF" e "Informe Rend." ou "IRRF Férias" e "Informe Rend.".  
 Somente será provento quando o funcionário receber um valor a maior em meses anteriores e na movimentação atual o usuário lançar o desconto da retificação.

**Observações**

1) Quando utilizar fórmula de cálculo neste evento, a fórmula deverá calcular o valor do INSS utilizando a tabela de cálculo do mês em que se refere a retificação, observando o teto da tabela.

2) O sistema utiliza este código de cálculo na DIRF e "Informe de Rendimentos" no campo "Contribuição Previdenciária Oficial".

3) Quando marcar a opção "Est. Cálc. IRRF de Férias" ou "IRRF Férias", o IRRF Férias deverá ser calculado manualmente ou através de fórmula e deverá ter o código de cálculo 107 quando for desconto e código de cálculo122.

**Dica**

Criar um evento de INSS Retificação SEFIP para cada competência a que a retificação se referir.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
