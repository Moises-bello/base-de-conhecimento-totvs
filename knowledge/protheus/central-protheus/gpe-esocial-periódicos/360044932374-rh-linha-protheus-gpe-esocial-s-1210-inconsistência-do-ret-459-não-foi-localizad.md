---
article_id: 360044932374
category: GPE - eSocial - Periódicos
content_hash: 9600a4fe46cb7daaa82098019621aaf9f8a29ce96077fc7ec5889534da8cf173
fetched_at: '2026-06-28T22:45:08.975872+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência do RET - 459
  - Não foi localizado um evento para o recibo de entrega informado ou o mesmo foi
  excluído/retificado
type: support-article
updated_at: '2024-10-31T22:02:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044932374-RH-Linha-Protheus-GPE-eSocial-S-1210-Inconsist%C3%AAncia-do-RET-459-N%C3%A3o-foi-localizado-um-evento-para-o-recibo-de-entrega-informado-ou-o-mesmo-foi-exclu%C3%ADdo-retificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27476594886807)Tempo aproximado para leitura: **00:01:00min  
  
Ocorrência**Ocorrencia 459 - Nao foi localizado um evento para o recibo de entrega informado ou o mesmo foi excluido/retificado. Acao Sugerida: Devera existir um Evento ja recebido, "Ativo" (nao excluido ou retificado), com numero de recibo de entrega igual ao informado no campo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27476601700887)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**   
Esse erro de retorno ocorre quando é enviado um evento S-1210 retificando o registro anterior porém o registro anterior já foi excluído do eSocial ou o **número do recibo** que está sendo informado no evento de retificação não é o número que consta no eSocial para o evento original.  
  
**Solução**1. Verificar no eSocial se existe o evento S-1210 para o período e CPF que esta sendo retificado;  
  
2. Caso não exista, provavelmente o evento foi excluído diretamente no site do governo.  
OBS: É de responsabilidade do cliente verificar se o evento foi excluído diretamente no site do eSocial pois o suporte não tem acesso ao ambiente do governo para realizar essa verificação.   
  
3. Caso o evento não esteja no eSocial, deve ser excluído o evento no Protheus e gerar o evento S-3000, após realizar o ajuste de protocolo no evento S-3000 pela rotina >Atualizações >Eventos Esocial >Não periódicos >Exclusão de eventos após selecionar o evento e >Outras Ações >Ajuste de recibo;  
  
Para maiores informações acesse: [TAF - FUNCIONALIDADES - Como realizar ajuste de recibo do e-Social no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-TAF-FUNCIONALIDADES-Como-realizar-ajuste-de-recibo-do-e-Social-no-TAF)  
  
4. Caso o evento que esta sendo enviado retificando esteja no eSocial, deve ser verificado se o numero de protocolo do evento que esta no governo é o mesmo que esta no TAF.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
