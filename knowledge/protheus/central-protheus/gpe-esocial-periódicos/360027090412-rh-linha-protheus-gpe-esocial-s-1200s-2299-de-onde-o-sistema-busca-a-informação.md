---
article_id: 360027090412
category: GPE - eSocial - Periódicos
content_hash: cd979663027c106626fb92128582ff501dd4f114cede344a58adb7549c6ba824
fetched_at: '2026-06-28T22:45:08.822797+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - De onde o Sistema busca
  a informação de Contribuição Substituída para integrar a tag indSimples
type: support-article
updated_at: '2025-07-22T20:51:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027090412-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-De-onde-o-Sistema-busca-a-informa%C3%A7%C3%A3o-de-Contribui%C3%A7%C3%A3o-Substitu%C3%ADda-para-integrar-a-tag-indSimples
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27420972835863)Tempo aproximado para leitura: **00:02:00min****Dúvida**De onde o Sistema busca a informação de Contribuição Substituída para integrar a tag indSimples ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Solução**De acordo com o leiaute vigente do eSocial no evento S-1200 e S-2299 há campos destinados as **Informações relativas a remuneração do trabalhador no período de apuração**e entre eles deve-se informar o **Indicador de Contribuição Substituída** (**indSimples**).  
  
No leiaute existe a seguinte descrição para esse campo:  
  
**Indicador de Contribuição Substituída:**   
**Valores válidos:**  
**1**- Contribuição substituída integralmente  
**2**- Contribuição não substituída  
**3**- Contribuição não substituída concomitante com contribuição  
  
**Validação:** O preenchimento do **campo é obrigatório** apenas no caso das empresas **enquadradas no regime de tributação Simples Nacional**, com tributação previdenciária substituída e não substituída (classTrib em S-1000 = [03]). **Para os demais empregadores, não deve ser informado.**  
O Protheus vai integrar essa informação nos eventos indicados de acordo com o preenchimento do campo **Id.Contb.Sub**. da **tabela S037** do GPE, localizada no menu em *Atualizações > Definições de Cálculo > Manutenção de Tabelas.*  
  
Se sua Empresa não se enquadra nas situações descritas no leiaute do eSocial versão 1.0 esse campo deverá ficar vazio.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026938891)  
  
Abaixo é possível verificar onde essa informação fica localizada no evento S-1200 visualizado através da rotina do TAF.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026922552)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
