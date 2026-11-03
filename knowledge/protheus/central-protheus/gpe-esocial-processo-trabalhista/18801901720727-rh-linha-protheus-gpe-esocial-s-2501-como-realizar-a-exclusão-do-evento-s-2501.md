---
article_id: 18801901720727
category: GPE - eSocial - Processo Trabalhista
content_hash: d78a7aefd86aa639102af5758be455faefe22df930a64323cfd6eb50f9a0ba3c
fetched_at: '2026-06-28T22:45:00.572134+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2501 - Como realizar a exclusão do
  evento S-2501
type: support-article
updated_at: '2024-10-28T20:00:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18801901720727-RH-Linha-Protheus-GPE-eSocial-S-2501-Como-realizar-a-exclus%C3%A3o-do-evento-S-2501
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18801908913687) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como realizar a exclusão do evento S-2501?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A exclusão de um evento **S-2500 não pode ser efetuada se houver um evento S-2501** que faça referência a ele. Ou seja, para a exclusão do evento S-2500 deve-se excluir, primeiramente, o(s) evento(s) S-2501 a ele vinculado(s).  
  
A geração do XML será executado e enviado ao TAF/Middleware através da rotina de Geração de Processos Trabalhistas (GPEM038) no módulo SIGAGPE.  
  
Acesse a rotina GPEM038 - Eventos Processos Trabalhistas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18801888386583)

1. Informe a **data inicial e final** de acordo com o **número da sentença** e deve abranger o mesmo mês.  
2. Selecione o evento S-3500 e a filial  
3. Clique em filtro, para selecionar o processo que deseja realizar a exclusão do S-2501  
4. Após preencher os parâmetros, clique em Processar e verifique o *log* gerado  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
