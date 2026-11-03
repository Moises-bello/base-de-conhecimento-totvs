---
article_id: 22541881521687
category: Originação de Grãos (OG)
content_hash: d717e8357abb0fd2b158786d9ca7238393faebcad4593199073be497e36a5f83
fetched_at: '2026-06-28T22:45:38.891635+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Cotação de Moedas diferentes na Nova Comercialização
type: support-article
updated_at: '2024-07-10T14:23:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22541881521687-Agro-Linha-Protheus-AGR-Cota%C3%A7%C3%A3o-de-Moedas-diferentes-na-Nova-Comercializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22541881470999) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como funciona uma estrutura **Cotação de Moedas diferentes na Nova Comercialização**?

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os pré-requisitos:

A **fixação de preço** ou de componente podem ocorrer em outra **moeda** e assim sendo o Sistema realiza as conversões de cotação necessárias.

Na tabela de componentes, o valor que deve ser informado é na moeda do componente. Caso ela seja diferente da **moeda do contrato**, ocorre a conversão utilizando a taxa do campo **Cotação**. O valor convertido é exibido no campo **R$ / UN - UN é a unidade de medida do componente** **que é exibida dinamicamente**.

O componente de resultado sempre assume a **moeda** que foi definida para o contrato e nesse caso, hajam componentes que fazem parte da sua formação com **moedas** diferentes, a conversão também é realizada.

Já na **regra fiscal do contrato**, quando este é definido como interno, mas a **moeda do contrato** é em dólar os valores são apresentados nas seguintes **moedas**:

| **Moeda do Contrato** | **Valor Fixado** | **Valor Faturamento** | **Valor Financeiro** |
| --- | --- | --- | --- |
| US$ | US$ | R$ | R$ |
