---
article_id: 360045760493
category: GPE - eSocial - Periódicos
content_hash: 91b4705cacd52ec8b2584b9f54a633834f9fd230e21b3d69fcc866fc69769e37
fetched_at: '2026-06-28T22:45:07.598178+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1000 - Inconsistência do RET - 130
  - E necessário existir informação cadastral do empregador para o período. Ação Sugerida:
  Verificar se ja foi enviado um evento de cadastramento do empregador'
type: support-article
updated_at: '2025-07-21T14:15:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045760493-RH-Linha-Protheus-GPE-eSocial-S-1000-Inconsist%C3%AAncia-do-RET-130-E-necess%C3%A1rio-existir-informa%C3%A7%C3%A3o-cadastral-do-empregador-para-o-per%C3%ADodo-A%C3%A7%C3%A3o-Sugerida-Verificar-se-ja-foi-enviado-um-evento-de-cadastramento-do-empregador
---

**Ocorrência**Inconsistência do RET - **130** - E necessário existir informação cadastral do empregador para o **periodo**.  
**Ação Sugerida:** Verificar se ja foi enviado um evento de cadastramento do empregador.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**O evento que está sendo transmitido para o governo (RET) tem o período de validade inicial (**Per. Ini Vld**) inferior ao cadastro do empregador (S-1000) que já está no governo (RET).   
  
No exemplo abaixo demonstro um **S-1000** com a data de **01/2017** e um **S-1020** com data de **10/2016**. Nesse cenário o governo retornaria com a ocorrência 130 já que como o S-1000 é o primeiro evento do **eSocial** não é possível enviar o S-1020 com data inferior.  
  
S-1000 (Empregador Matriz) com o período de validade inicial (**Per. Ini Vld**) 01/2017![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063761553)  
  
S-1020 (Lotação) com o período de validade inicial (**Per. Ini Vld**) 10/2016  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062859094)  
  
**Solução**Analise qual evento está com o período de validade inicial (**Per. Ini Vld**) incorreto e ajuste. Caso seja o evento **S-1000** acesse no **sigataf** o caminho atualizações > configs. taf > complemento cadastral, ajuste o período e envie para o governo o evento S-1000 de retificação.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063761553)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
