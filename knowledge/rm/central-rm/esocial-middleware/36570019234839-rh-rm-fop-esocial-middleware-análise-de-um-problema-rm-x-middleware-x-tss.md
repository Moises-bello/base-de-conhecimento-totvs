---
article_id: 36570019234839
category: eSocial - Middleware
content_hash: 6e8a77feee7a2979aa0be8358581692efdf23fcd0d239e59868d42769a4b2a6b
fetched_at: '2026-06-28T22:47:05.493127+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: RH - RM - FOP - eSocial - Middleware Análise de um problema RM x Middleware
  x TSS
type: support-article
updated_at: '2026-05-27T21:08:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36570019234839-RH-RM-FOP-eSocial-Middleware-An%C3%A1lise-de-um-problema-RM-x-Middleware-x-TSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36570019232151) Tempo aproximado para leitura: 05:00 **min**  
  
**Dúvida**  
Como analisar um problema de integração entre RM x Middleware x TSS  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial  
  
**Solução**  
Breve explicação sobre a integração dos eventos utilizando Middleware

O middleware é um serviço que faz a conexão entre o ERP e o TSS/Governo. Para que os eventos do eSocial trafeguem do middleware até o TSS, é necessário um webservice. Esse webservice precisa ser, obrigatoriamente, um serviço do Protheus (chamado Appserver TAF), conforme imagem abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36569990917143)

Quando temos um problema nas integrações, primeiramente precisamos avaliar os arquivos de log dos serviços de webservices (Appserver TAF) e (Appserver TSS). Depois avaliar tambem a versão da release e extrato de fontes conforme o passo a passo abaixo

1- Passo

Acessar o smartclient/webapp do Appserver TAF e no Programa Inicial digitar "MYRELEASE". Printar a informação gerada para envio ao suporte

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36569990917271)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36569990917399)

2- Passo

Gerar os logs do "Appserver TAF" e "Appserver TSS" conforme os links abaixo

[RM - Como gerar log do "Appserver TAF"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026026133-RM-Como-habilitar-e-gerar-o-Fwtracelog-no-console-log-do-protheus)

[RM - Como gerar log do "Appserver TSS"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007834222-Cross-Segmentos-TSS-Procedimento-para-ativar-os-logs-de-comunica%C3%A7%C3%A3o-do-TSS)

Saiba Mais

[RH - RM - FOP - eSocial - Middleware: Certificado Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009264782-RH-RM-FOP-eSocial-Middleware-Certificado-Digital)

[Passos para ativação do Middleware, configuração do Relatório de Conferência e Edição de XML](https://tdn.totvs.com/pages/releaseview.action?pageId=563428854#passos--1208117187)
