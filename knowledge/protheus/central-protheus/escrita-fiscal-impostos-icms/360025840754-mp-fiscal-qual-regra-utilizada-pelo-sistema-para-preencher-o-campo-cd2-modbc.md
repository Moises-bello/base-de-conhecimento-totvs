---
article_id: 360025840754
category: Escrita Fiscal - Impostos - ICMS
content_hash: da6e733eb8f268ad03ae5a8344c24c8729fced9bf3ac287d0e2ff694a8051b31
fetched_at: '2026-06-28T22:39:26.067599+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: MP - FISCAL - Qual regra utilizada pelo sistema  para preencher o campo CD2_MODBC?
type: support-article
updated_at: '2021-04-28T21:23:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025840754-MP-FISCAL-Qual-regra-utilizada-pelo-sistema-para-preencher-o-campo-CD2-MODBC
---

**[Remover as instruções entre colchetes]**  
 **Dúvida** Qual regra utilizada pelo sistema para preencher o campo CD2\_MODBC?  
   
 **Ambiente**Protheus – A partir da versão 11.80]  
  
**Solução**

Regra para o ICMS PROPRIO com pauta:

 Se ele tiver valor de pauta e F4\_PAUTICM = 2 , MODBC = 1

Se não tiver cálculo de pauta,MODBC = 2

 Regra para o ICMS ST com pauta :

 Não é pauta, é somente ST = MODBC = 3

Se tiver pauta do ST, e o valor da pauta maior que zero, MODBC = 5

Se tiver pauta e o valor menor que zero, MODBC = 0

Se tiver cálculo de st, e não tiver pauta, ele gera MODBC = 4

  Informação do manual contribuinte NFe 3.10:

Tag : modBCST

Descrição: Modalidade de determinação da BC do ICMS ST

0=Preço tabelado ou máximo sugerido;

1=Lista Negativa (valor);

2=Lista Positiva (valor);

3=Lista Neutra (valor);

4=Margem Valor Agregado (%);

5=Pauta (valor);
