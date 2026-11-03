---
article_id: 12132665388695
category: eSocial - Relatórios
content_hash: 86a28a91390962c79e1233b773733871485d9b40821ef46078806bf41944bbfd
fetched_at: '2026-06-28T22:47:04.901502+00:00'
product: rm
section_id: 1500000861002
source: central-rm
title: RH - RM - FOP - eSocial - Relatório de Conferência INSS Patronal
type: support-article
updated_at: '2024-09-24T17:24:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12132665388695-RH-RM-FOP-eSocial-Relat%C3%B3rio-de-Confer%C3%AAncia-INSS-Patronal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21709702598295) Tempo aproximado para leitura: **00****:04:00 min****Dúvida**Como configurar e gerar o Relatório de Conferência de INSS Patronal para identificação de divergências entre Folha de Pagamento e Governo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da versão 12.1.2209.151 e Superiores.   
  
**Solução**Esta funcionalidade têm como objetivo apoiar na identificação de possíveis divergências entre os valores de INSS calculados utilizando as incidências dos eventos/verbas existentes no envelope de pagamento com o valores retornados do RET através do evento S-5011, auxiliando também na conferência dos valores de: Segurados, Deduções Salário Família e Maternidade da DARF de INSS.  
  
Os dados apresentados são originados da comparação dos valores de INSS encontrados na Folha de pagamento contra os valores retornados pelo Governo através do evento S-5011-Informações das Contribuições Sociais Consolidadas por Contribuinte.

Abaixo segue documentação com orientações de como configurar e gerar o relatório:

      • [Relatório de Conferência INSS Patronal](https://tdn.totvs.com/pages/releaseview.action?pageId=714242305#1-1)

**Importante**1. Para o funcionamento do relatório para usuários que utilizam TAF é necessário a atualização da versão do TAF para obter os totalizares após o envio do fechamento;

2. A configuração para usuários Middleware ou TAF é a mesma, o que diferencia uma da outra é o caminho para acessar a configuração;

* Para os usuários que utilizam Middleware o parâmetro está localizado em **Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com Middleware;**
* Para os usuários que utilizam TAF o parâmetro está localizado em **Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com TAF.**

3. O governo disponibilizou recentemente o leiaute S-1.2, em que é enviado através do S-1000. Além disto, que ele é totalizado no S-5012 e, o valor calculado do PIS é retornado através da TAG <tpCR>830102</tpCR> (que é o código da receita de PIS/PASEP). Porém, o governo ainda não apresentou nenhuma validação no MOS/Leiaute do eSocial com as devidas informações do cálculo e validação do PIS. Com isto, não foi desenvolvido no produto as validações para considerar no relatório o valor do PIS/PASEP. Neste caso, será necessário o usuário desconsiderar o valor de PIS/PASEP do relatório Patronal.  
  
**Saiba mais**Para mais informações acesse:[Relatório de Conferência INSS Patronal - Depósito do montante em juízo](https://tdn.totvs.com/pages/releaseview.action?pageId=866540777)
