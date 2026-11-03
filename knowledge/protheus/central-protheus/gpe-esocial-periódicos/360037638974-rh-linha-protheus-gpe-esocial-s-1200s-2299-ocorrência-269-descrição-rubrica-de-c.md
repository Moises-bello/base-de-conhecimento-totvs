---
article_id: 360037638974
category: GPE - eSocial - Periódicos
content_hash: 7c12fbca053e97d3d5b54f491fb5bb40d6f597cab0339774302530dcf157737b
fetched_at: '2026-06-28T22:45:08.859083+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Ocorrência 269 - Descrição:
  Rubrica de código X e Identificador de tabela Y não existe no cadastro do empregador
  para o período ''AAAA-MM'''
type: support-article
updated_at: '2025-07-22T20:52:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037638974-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Ocorr%C3%AAncia-269-Descri%C3%A7%C3%A3o-Rubrica-de-c%C3%B3digo-X-e-Identificador-de-tabela-Y-n%C3%A3o-existe-no-cadastro-do-empregador-para-o-per%C3%ADodo-AAAA-MM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27420996680343)Tempo aproximado para leitura: **00:02:00min  
  
Ocorrência**S-1200/S-2299 - Ocorrência 269 - Descrição: Rubrica de código X e Identificador de tabela Y não existe no cadastro do empregador para o período 'AAAA-MM'.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27420996683287)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**A inconsistência é apresentada no envio do evento S-1200 ou S-2299 quando o código de Rubrica informado em um desses eventos não existe na base de dados do RET (Governo) ou que o início de vigência não abrange o período que está sendo enviado.  
Isso pode ocorrer por não ter enviado o evento S-1010 ao RET (Governo) ou devido ao inicio de validade do evento S-1010 ser posterior ao período de referência do evento que está tentando transmitir.  
  
Em muitos casos pode ocorrer junto a inconsistência de código 933, para saber mais acesse:  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Ocorrencia 933 - O somatório dos Proventos deve ser maior ou igual ao somatório dos Descontos no Demonstrativo de Pagamento X. Valor Encontrado: -Y](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023120571)  
  
Por exemplo, para enviar um evento S-1200 em 10/2024 é necessário existir um evento S-1010 com inicio de validade anterior ou igual a 10/2024, caso contrário o RET (Governo) vai rejeitar o S-1200 informando que a Rubrica informado não existe na base de dados do RET (Governo).  
  
Esse mesmo cenário é muito comum em Rescisões Complementares, suponha que uma Rescisão Complementar calculada em 10/2024 está pagamento diferenças relacionadas aos períodos de 03/2024 e 04/2024, todas as rubricas que compõem o evento devem constar na base de dados do governo o cadastro dentro do período de vigência  
  
**Solução**Envie para o governo uma nova rubrica com o campo inicio de validade que deve ser igual ou anterior ao período de referência do evento S-1200/S-2299 que está tentando transmitir.  
  
Para saber mais sobre como ajustar incidência e validade de rubricas no governo, TAF e GPE acesse:  
[MP - GPE - eSocial - S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512) **Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
