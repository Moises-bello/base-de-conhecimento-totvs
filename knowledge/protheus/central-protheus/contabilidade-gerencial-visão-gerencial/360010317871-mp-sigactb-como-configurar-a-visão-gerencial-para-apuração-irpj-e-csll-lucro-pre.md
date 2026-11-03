---
article_id: 360010317871
category: Contabilidade Gerencial - Visão Gerencial
content_hash: cebecd57d4e0f7a2062a182bc615bfb51449ac8ab9e2f3b80fad3b794da19826
fetched_at: '2026-06-28T22:40:50.702353+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: MP-SIGACTB -COMO CONFIGURAR A VISÃO GERENCIAL PARA APURAÇÃO IRPJ E CSLL LUCRO
  PRESUMIDO
type: support-article
updated_at: '2021-04-28T15:23:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010317871-MP-SIGACTB-COMO-CONFIGURAR-A-VIS%C3%83O-GERENCIAL-PARA-APURA%C3%87%C3%83O-IRPJ-E-CSLL-LUCRO-PRESUMIDO
---

**Dúvida**Como tratar Visão gerencial para extrair informações para Apuração Lucro Presumido?  
  
   
 **Ambiente**Microsiga Protheus  – Financeiro – A partir da versão 11.80  
  
   
**Solução**

É recomendado utilizar a rotina VISÃO GERENCIAL, pois vários elementos que compõem a base de cálculo do lucro presumido são retirados das classificações e resultados contábeis, sendo inviável somente utilizar os dados fiscais.

Esclareço ainda que "VISÃO GERENCIAL" é uma rotina do módulo Contabilidade Gerencial

Determinação do valor a recolher dos impostos IRPJ e CSLL através da visão gerencial  configurada e gerada através do ambiente Contabilidade Gerencial.   
   
  Por esta operação necessitar do uso de sintaxes específicas da Visão Gerencial, em função da necessidade de fórmulas, é recomendável que a configuração da visão seja realizado por um analista conhecedor.

Os impostos são definidos com base no resultado da empresa apurado através do DRE, conforme exemplo abaixo:  
   
  
Abaixo exemplo :  
   
 Demonstração do Resultado do Exercício – 20x3  
  
 Valor (R$)  
   
 (=) Receita Bruta de Vendas  R$ 120.000,00  
(-) ICMS sobre Vendas  (R$ 21.600,00)  
(-) PIS e COFINS sobre Vendas (R$ 11.100,00)  
(=) Receita Líquida de Vendas R$ 87.300,00  
(-) CMV (líquido do ICMS, PIS e COFINS) (R$ 29.100,00)  
(=) Lucro Bruto R$ 58.200,00  
(-) Despesas operacionais (R$ 25.500,00)  
(=) Lucro antes do IRPJ e CSLL R$ 32.700,00  
(-) Provisão para IRPJ e CSLL (15% + 9%) (R$ 7.848,00)  
(=) Lucro Líquido Exercício R$ 24.852,00

Segue link com mais informações :

<http://tdn.totvs.com/pages/releaseview.action?pageId=6068417>

<http://tdn.totvs.com/pages/releaseview.action?pageId=6068442>

<http://tdn.totvs.com/pages/releaseview.action;jsessionid=A7315EE26753D27CE6DDE87D5FCA3C35?pageId=95618076>
