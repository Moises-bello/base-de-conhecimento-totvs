---
article_id: 11270158408215
category: GPE - eSocial - Carga Inicial
content_hash: 2201289edd3ab4310c4da79237a56933d2a8b5aa7f38cdab7d2d4e62ab05f7ec
fetched_at: '2026-06-28T22:45:03.122379+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Criação do ID de cálculo 1903 para dedução
  de base de INSS no cálculo de férias
type: support-article
updated_at: '2024-07-25T11:24:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11270158408215-RH-Linha-Protheus-GPE-eSocial-Cria%C3%A7%C3%A3o-do-ID-de-c%C3%A1lculo-1903-para-dedu%C3%A7%C3%A3o-de-base-de-INSS-no-c%C3%A1lculo-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484677569047) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Criação do ID de cálculo 1903 para dedução de base de INSS no cálculo de férias.  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Quando o parâmetro MV\_DINSSFM está configuração **N** e há cálculo de férias partidas, a base de INSS fica menor do que o valor gerado na verba do ID 1870, pois a base de INSS considera as verbas de férias do mês seguinte, que não possuem incidência para contribuição patronal **11**, portanto não são consideradas na geração do ID 1870.

Devido a isso, o relatório **TAFR120** apresenta uma divergência na conferência.  
[Automação Fiscal - RELATÓRIO - Acessando o Painel de Conferência de INSS no novo painel do TAF Full](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057414373?source=search)  
  
Implementada a geração da verba do ID de cálculo **1903** no cálculo de férias normais e coletivas, contendo a diferença entre a base de INSS (verbas dos ID 0013 e 0014) e a verba do ID 1870, de modo que o relatório TAFR120 não apresente divergências na conferência.  
  
Deverá ser criado manualmente uma verba e vinculá-la ao ID de cálculo 1903. A verba deverá ser do **tipo 4** (Base Desconto) e a **natureza** de rubrica deve ser **9901**.  
  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
