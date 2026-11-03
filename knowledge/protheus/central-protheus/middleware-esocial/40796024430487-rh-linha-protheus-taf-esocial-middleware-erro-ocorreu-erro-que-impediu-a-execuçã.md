---
article_id: 40796024430487
category: MIDDLEWARE eSocial
content_hash: 325053da08294bb7b7ad6db2f8ced136d939581ba12546c564246f9a540f6cd6
fetched_at: '2026-06-28T22:43:04.940242+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Middleware - Erro Ocorreu erro que impediu
  a execução do processo. System.AggregateException: One or more errors occurred'
type: support-article
updated_at: '2026-05-28T16:50:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40796024430487-RH-Linha-Protheus-TAF-eSocial-Middleware-Erro-Ocorreu-erro-que-impediu-a-execu%C3%A7%C3%A3o-do-processo-System-AggregateException-One-or-more-errors-occurred
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40795980057367) Tempo aproximado para leitura: 00**:02:25 min**  
  
**Ocorrência**  
Ao realizar a transmissão ou atualização do certificado digital no RM Middleware é apresentado o erro Ocorreu erro que impediu a execução do processo. System.AggregateException: One or more errors occurred  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Todas as versões.  
  
**Causa**  
O erro ocorre pode ocorrer por várias causas:

Serviços TAF\_WS e TSS parados

Erro de comunicação com o banco de dados

Parametrização errada dos endereços no RM

Bloqueio das portas dos serviços  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se os serviços TAF\_WS, TSS e Dbaccess estão em execução. Caso estejam, reinicie os mesmos

2. Verifique no RM em Configurações - Parametrizador - eSocial - Integração com Middleware se o endereço e porta estão configurados corretamente, conforme exemplo abaixo:

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40796024399383)

3. Caso esteja correto, abra um chamado com a equipe de suporte anexando os arquivos: console.log e appserver.ini dos serviços TAF\_WS e TSS - [RH - Linha Protheus - TAF - eSocial - Middleware - Enviar arquivo console.log](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26598043057175-RH-Linha-Protheus-TAF-eSocial-Middleware-Enviar-arquivo-console-log) e o print da tela do parametrizador do Middleware

**Saiba Mais**

**Para saber mais consulte os links abaixo:**

[**eSocial | Protheus - Entregas Legais**](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[**MOS - Manual de Orientação eSocial**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[**Perguntas Frequentes site eSocial**](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

**Para conhecimento dos eventos futuros, acessa a nossa página**[**TOTVS Informa**](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "Eventos"**

**Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:**[**Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus)
