---
article_id: 360028706011
category: RH - Integração de Titulo
content_hash: 641927da390d4d75f63c1ff8288b8db6aa25690ef491d37d1d7b6a1dbcfffd59
fetched_at: '2026-06-28T22:43:36.224632+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar um título rateado por centro de custos
type: support-article
updated_at: '2025-07-15T20:33:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028706011-RH-Linha-Protheus-GPE-Como-criar-um-t%C3%ADtulo-rateado-por-centro-de-custos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33489796013207)**Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como criar um título rateado por centro de custos  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Versão 12.1.17  
  
**Solução**  
Acesse **Miscelânea-> Títulos-> Definição:**1) O título criado deverá ser configurado com o "Agrupamento: Centro de Custo". Lembrando que ao clicar no campo Definir título, será possível incluir a verba e tabela de busca para geração do título.  **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029141712)**

Em nosso exemplo , usaremos uma verba de crédito de vale transporte (verba 997)e a busca na tabela SRC**\***:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029142032)**

2) Após lançamento e cálculo da verba na folha de pagamento, verificamos os valores e seu respectivo centro de custos:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029143311)

4) Acesse **Miscelânea -> Títulos -> Geração:**Configure a geração do título de acordo com a data de pagamento (data de cálculo da folha no cadastro de períodos), competência e código do título:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029142892)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029143851)

5) Acesse **Miscelânea -> Títulos -> Manutenção:**Os títulos gerados por centro de custo serão apresentados na Manutenção de títulos de acordo com os valores de folha de pagamento:

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029143432)**

**\*A busca de tabela na definição de título segue o seguinte conceito:  
SRC -** Movimento de folha aberto (Movimento do Período) **SRD -** Movimento de folha fechado (Histórico de Movimentos)

**Importante:**  
Quando a definição de títulos for com o agrupamento "Centro de custos", na geração de títulos referentes ao INSS, será necessário validar se existe pagamento de salário família ou maternidade , pois considerando que refere-se ao título de um centro de custos específico, os valores superiores destas verbas não farão abatimento nos valores dos demais centros de custos. Desta forma, o título será gerado apenas com o valor de terceiros , uma vez que este valor não se enquadra no abatimento das verbas de compensação do INSS. 

**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
