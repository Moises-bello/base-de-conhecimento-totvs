---
article_id: 360024412872
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: aaf1803bce1d9c46d3b108ab94a324250a3e89f7d027fc302877b99ae7506bb7
fetched_at: '2026-06-28T22:39:19.288319+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como Parametrizar
  o Protheus Com Cálculo de DIFAL Pela Diferença das Alíquotas Quando Não Existe Cálculo
  do ICMS Próprio? '
type: support-article
updated_at: '2021-09-23T20:13:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024412872-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Parametrizar-o-Protheus-Com-C%C3%A1lculo-de-DIFAL-Pela-Diferen%C3%A7a-das-Al%C3%ADquotas-Quando-N%C3%A3o-Existe-C%C3%A1lculo-do-ICMS-Pr%C3%B3prio
---

**Dúvida**Como Parametrizar o Protheus Com Cálculo de DIFAL Pela Diferença das Alíquotas Quando Não Existe Cálculo do ICMS Próprio?   
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
   
**Solução**  
Para que o sistema efetue o cálculo do Difal pela diferença das alíquotas quando não existe o cálculo do ICMS Próprio, será necessário configurar o cadastro de TES conforme abaixo:   
   
Cadastro de TES  
  
Calcula ICMS = Sim  
L. Fiscal de ICM = Isento  
Sit Trib ICM = (Utilizar um CST de isenção de ICMS conforme orientação do setor Fiscal)  
  
No pedido de venda será calculado o ICMS mesmo sendo isento, o calculo é demonstrado para que o valor do DIFAL seja calculado e demonstrado para conferencia.  
  
A isenção do ICMS será gravada no Livro Fiscal conforme configuração de TES descrita acima e, consequentemente essa isenção não será considerada na apuração do ICMS gerando valor ICMS para pagamento.

Também não terá impactos no XML e impressão da Danfe.
