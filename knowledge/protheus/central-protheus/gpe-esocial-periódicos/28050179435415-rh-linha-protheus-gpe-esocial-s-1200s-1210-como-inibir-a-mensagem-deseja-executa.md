---
article_id: 28050179435415
category: GPE - eSocial - Periódicos
content_hash: e3f3f6c18899add267cd1b1a8ce6d4a00144109c5bb967c4823829338cb9e17a
fetched_at: '2026-06-28T22:45:07.338920+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200/S-1210 - Como inibir a mensagem:
  "Deseja executar o processamento em segundo plano?"'
type: support-article
updated_at: '2025-07-23T14:56:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28050179435415-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Como-inibir-a-mensagem-Deseja-executar-o-processamento-em-segundo-plano
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28050148197271) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como inibir a mensagem: "Deseja executar o processamento em segundo plano?"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Criação do parâmetro **[MV\_RHSCHED](https://tdn.totvs.com/pages/releaseview.action?pageId=881567117)** que controla a execução automática e aparecimento de mensagem de confirmação para execuções em segundo plano.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28050148199191)

O parâmetro tem por padrão o preenchimento: 0,0,0,0 e deve ser estar disponível a partir da versão 2510.  
**Em versões anteriores, ele pode ser criado manualmente através do configurador.**   
Nele, devemos informar o que desejamos deixar como padrão quanto à execução das rotinas **GPEM034, GPEM650, GPEM670 e GPEM110** (nessa ordem e separados por vírgula).  
  
As opções disponíveis são:  
**0**: Sempre mostrar a pergunta;  
**1**: Sempre executar em segundo plano;  
**2**: Nunca executar em segundo plano.  
  
Como informado acima, o parâmetro tem por padrão o preenchimento: 0,0,0,0  
Neste caso, ele mostrará a pergunta para execução em segundo plano nas quatro rotinas.  
  
Caso queira, por exemplo, que nunca mostre a pergunta de execução em segundo plano em nenhuma das rotinas citadas acima, devemos deixar o parâmetro preenchido com: 2,2,2,2  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28050179410327)  
  
**Boletim técnico**: <https://tdn.totvs.com/pages/releaseview.action?pageId=881567117>  
  
**Saiba Mais**Para saber mais, consulte os links abaixo:  
[EVENTOS PERIÓDICOS ESOCIAL - Processamento em Segundo Plano](https://tdn.totvs.com/pages/releaseview.action?pageId=852891868)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
