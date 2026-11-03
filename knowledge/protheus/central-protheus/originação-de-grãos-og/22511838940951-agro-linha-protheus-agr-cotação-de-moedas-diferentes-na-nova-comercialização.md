---
article_id: 22511838940951
category: Originação de Grãos (OG)
content_hash: 892dd0a244c0a0afba75f24dae63f7575cbeaa3998b7fca80118789c9c82afba
fetched_at: '2026-06-28T22:45:38.895845+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Cotação de Moedas Diferentes na Nova Comercialização
type: support-article
updated_at: '2025-06-24T11:31:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22511838940951-Agro-Linha-Protheus-AGR-Cota%C3%A7%C3%A3o-de-Moedas-Diferentes-na-Nova-Comercializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22511808732183) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Como funciona uma estrutura de **Cotação de Moedas Diferentes** **na Nova Comercialização**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**A fixação de preço ou de componente podem ocorrer em outra moeda e assim sendo o sistema realiza as conversões de cotação necessárias.  
Na tabela de componentes, o valor que deve ser informado é na moeda do componente. Caso ela seja diferente da moeda do contrato, ocorre a conversão utilizando a taxa do campo Cotação. O valor convertido é exibido no campo **R$ / UN - UN é a unidade de medida do componente que é exibida dinamicamente**.  
O componente de resultado sempre assume a moeda que foi definida para o contrato e nesse caso, caso hajam componentes que fazem parte da sua formação com moedas diferentes, a conversão também é realizada.  
Já na regra fiscal do contrato, quando este é definido como interno, mas a moeda do contrato é em dólar os valores são apresentados nas seguintes moedas:

| Moeda do Contrato | Valor Fixado | Valor Faturamento | Valor Financeiro |
| --- | --- | --- | --- |
| US$ | US$ | R$ | R$ |
