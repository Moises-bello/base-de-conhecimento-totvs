---
article_id: 360039052094
category: GPE - eSocial - Carga Inicial
content_hash: 842b4f6fad8e7b50e1401521efaee1aa3c4435a281f8e995d6907e315dace552
fetched_at: '2026-06-28T22:45:03.249157+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 - Como configurar para o eSocial
  a verba de ID 0232 (INSS Férias Mês Seguinte)
type: support-article
updated_at: '2026-04-09T19:44:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039052094-RH-Linha-Protheus-GPE-eSocial-S-1010-Como-configurar-para-o-eSocial-a-verba-de-ID-0232-INSS-F%C3%A9rias-M%C3%AAs-Seguinte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39638261605527) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como configurar para o eSocial a verba de ID **0232** (INSS Férias Mês Seguinte)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
A verba de ID **0232** é gerada quando o parâmetro **MV\_DINSSFM** está com conteúdo **S**. Esse parâmetro serve para chumbar no cálculo o desconto do INSS do mês seguinte, para que no próximo mês não exista o recalculo desse valor. Vale ressaltar que não existe **INSS** de Férias para o **Governo**, o INSS é único. O que existe é o entendimento diferente por parte das empresas de como isso será demonstrado para o trabalhador no recibo de pagamento.  
Para o **eSocial** a verba de ID **0232** não deve ter incidência de **Previdência,**portanto o campo no cadastro de verbas **(aba eSocial) CD.INC.CP** **deve ficar com código** **00**.   
Devido ela ser uma verba de desconto que ocorre nas férias do trabalhador sobre os dias de férias do mês seguinte, não altera-se a base de contribuição do mês.  
No próximo mês o sistema vai somar as verbas da folha e ferias mês seguinte (que vira férias mês) e deduzir o que já foi descontado, para gerar a nova base de salário contribuição respeitando o Teto para recolhimento do **INSS**.  
  
**Obs.:** A configuração das Verbas/Rubricas com relação a Natureza e as Incidências Tributárias é algo particular de cada Empresa e que deve ser analisado em conjunto com o departamento Jurídico e Contábil, mas a lógica é que a na aba eSocial essa Verba/Rubrica esteja com o código de incidência condizente com a aba incidência.  
Não podemos orientar sobre o preenchimento das incidências legais das verbas, isso porque pode existir diferenças entre empresas, sindicatos, súmulas, etc.  
O próprio governo não fornece nenhum material com orientação para incidências de verbas, somente em casos muito específicos.  
  
**Entenda Mais:**

* [Conceito do cálculo de folha com Férias partidas utilizando o parâmetro MV\_DINSSFM= S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017956652)
* [Quais são as formas de cálculo para cada configuração do parâmetro MV\_DINSSFM?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016451652)

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[Artigos S-1010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051971613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)
