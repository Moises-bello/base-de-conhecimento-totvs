---
article_id: 4409115260311
category: MIDDLEWARE eSocial
content_hash: 6fa3909012ff62ca34052796a4cdf6de3d7e5b4e5d856315026948b08e8c1f40
fetched_at: '2026-06-28T22:43:04.995158+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - Como realizar a importação
  ao middleware dos eventos transmitidos pelo TAF
type: support-article
updated_at: '2025-07-21T20:32:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409115260311-RH-Linha-Protheus-GPE-eSocial-Middleware-Como-realizar-a-importa%C3%A7%C3%A3o-ao-middleware-dos-eventos-transmitidos-pelo-TAF
---

**Dúvida**Como realizar a importação ao Middleware dos eventos transmitidos pelo TAF?  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Acesse a rotina de importação:  
Caminho SIGAGPE: Miscelânea > eSocial > Middleware > Monitor (GPEM017B);  
  
A rotina **GPEM017B** foi criada para efetuar a importação dos registros do TAF/TSS para a tabela de fila de eventos RJE.  
A 1ª tela do *Wizard* contém apenas o descritivo da rotina, avisos e o botão para abertura da documentação técnica.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409114941847)  
  
A 2ª tela do *Wizard* contém lista de opções dos registros/eventos que estão disponíveis para importação. 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409099625367)  
  
A 3ª tela do *Wizard* contem opções para a importação dos registros, como número de threads, filtro por período de/até e filtro por filiais.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409114990487)  
  
**Observações**:  
O controle de geração por *multi thread* não será utilizado para a importação das tabelas T3M e V3N; para os demais, somente será ativado caso o número de registros a serem importados seja superior a 2500.  
O filtro por período de/até apenas será utilizado para os eventos de tabela (eventos S-1000, S-1005, S-1010, S-1020) e para os eventos periódicos (S-1200, S-1210, S-1280, S-1298, S-1299). Para os eventos de tabelas, o filtro será efetuado sobre o início da validade, campo XXX\_DTINI (onde XXX é a tabela do evento).  
O filtro por filial não será utilizado para a importação da tabela T3M.  
  
**Documentação relacionada:**  
[RH - Linha Protheus - GPE - eSocial - Middleware - O registro do evento S-XXXX com ID: XXXXX não foi encontrado no TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409114239255)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)  
[TAF - CONFIGURAÇÃO - TAF do Futuro – Erros para configurar ou acessar a rotina do TAF do Futuro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405166201623-TAF-CONFIGURA%C3%87%C3%83O-TAF-do-Futuro-Erros-para-configurar-ou-acessar-a-rotina-do-TAF-do-Futuro)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
