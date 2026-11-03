---
article_id: 360034833693
category: GPE - eSocial - Periódicos
content_hash: bb0729f3aa499a46a49f8b1112461b11258bbae4f7eadceff510e23f296378fb
fetched_at: '2026-06-28T22:45:08.800923+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2298 - Como funciona a Reintegração
  para envio ao eSocial
type: support-article
updated_at: '2025-07-22T20:50:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034833693-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2298-Como-funciona-a-Reintegra%C3%A7%C3%A3o-para-envio-ao-eSocial
---

**Dúvida**Como funciona a Reintegração para envio ao eSocial?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O primeiro passo é entender **[Quando deve ser enviado o evento S-2298 (Reintegração)?](http://tdn.totvs.com/pages/releaseview.action?pageId=347447951)** de Reintegração, para mais informações acesse o artigo publicado por nossa Consultoria de Segmentos através do link: **<http://tdn.totvs.com/x/j6K1F>**.  
  
Após entender a diferença entre os tipos de reintegração, o próximo passo é executar a rotina do Protheus que realiza a reintegração do Trabalhador no ambiente da Folha de Pagamento do GPE, neste caso há duas opções e independente de qual selecionar será gerado um evento S-2298 de Reintegração para o TAF. Para entender mais sobre as opções de Reintegração no GPE e como executar a rotina, acesse: **[GPEA810 - Reintegração funcionário P12](http://tdn.totvs.com/pages/viewpage.action?pageId=387286318)**.  
  
Conforme o primeiro artigo menciona, há casos em que o Empregador deve enviar o evento S-1200 e S-1210 de todo o período em que o Trabalhador esteve afastado de suas funções em razão do desligamento, para essa situação é possível realizar cálculo da Folha de Pagamento dos períodos que o Trabalhador estava desligado através da rotina de **[Retificação da Folha de Pagamento](http://tdn.totvs.com/pages/releaseview.action?pageId=451266813)**.  
  
A rotina de **[Retificação da Folha de Pagamento](http://tdn.totvs.com/pages/releaseview.action?pageId=451266813)** não calcula valores automaticamente, somente o que for informado nos lançamentos mensais do roteiro **RTF**, ou seja, se eu preciso pagar dias de salário mensal eu tenho que informar a Verba de salário mensal nos lançamentos mensais e o Sistema calculará a Folha de Pagamento.  
  
Após calculado o roteiro **RTF** é possível acessar a rotina de integração dos Eventos Periódicos do GPE e gerar uma carga do evento S-1200 referente ao período que o roteiro foi criado/calculado.  
  
Já o evento **S-1210** será gerado no período atual da Folha de Pagamento conforme data de Pagamento utilizada no cadastro do roteiro **RTF**, ou seja, se em **08/2019** eu cálculo uma Retificação da Folha de Pagamento de **05/2019** com data de pagamento em **30/08/2019**, o evento **S-1210** que levará a informação do pagamento será o de período de referência **08/2019**. Para mais informações sobre esse conceito acesse o artigo: [RH - Linha Protheus - GPE - eSocial - S-1200/S-2299/S-1210 - Conteúdo do Evento x Regime de Apuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027707032-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-S-1210-Conte%C3%BAdo-do-Evento-x-Regime-de-Apura%C3%A7%C3%A3o)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
