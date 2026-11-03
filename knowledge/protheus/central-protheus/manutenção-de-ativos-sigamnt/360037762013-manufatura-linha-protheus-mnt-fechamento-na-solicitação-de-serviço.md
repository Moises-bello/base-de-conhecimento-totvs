---
article_id: 360037762013
category: Manutenção de Ativos (SIGAMNT)
content_hash: 6fbd005487b94fb77eaafa42f69fed3194224fa8a59bd372a7afc883331d409b
fetched_at: '2026-06-28T22:42:33.194175+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Fechamento na solicitação de serviço
type: support-article
updated_at: '2021-07-05T20:59:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037762013-Manufatura-Linha-Protheus-MNT-Fechamento-na-solicita%C3%A7%C3%A3o-de-servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Qual o conceito da rotina **Fechamento - MNTA290** no processo de **Solicitação de Serviço - MNTA280**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**O conceito da rotina é o fechamento das **Solicitações de Serviço - S.S.** quando não se faz necessária a criação de uma ordem de serviço para a mesma.  
  
Deve ser utilizada para o fechamento de **S.S.** quando não há necessidade da abertura de uma ordem de serviço, ou seja, o problema pelo qual foi aberta foi resolvido sem a necessidade de outros recursos.  
  
Se houver necessidade de abrir ordem de serviço para a **Solicitação - MNTA280**, ela não pode ser fechada através desta rotina, somente através da finalização da ordem de serviço nos**Retornos de OS - MNTA400** ou **Retorno Mod 2 -MNTA435**.  
  
É permitido somente fechar solicitações que não estão vinculadas à ordens de serviço.  
  
Envia uma pesquisa de satisfação de atendimento da **S.S.** para que o solicitante da **S.S.** responda. O envio do *Workflow* depende diretamente do preenchimento do parâmetro **MV\_NGSSWRK - Identifica se no módulo de Solicitação de Serviços será utilizado envio de mensagens por Workflow**. Se ele estiver igual a **S**, o W*orkflow* após seleção da opção **Fechamento**.  
  
**Importante**  
Parâmetros relacionados ao *Workflow*:

* **MV\_NGWFHT -** **Indica o IP - Internet Protocol e a Porta para a comunicação HTTP - HyperText Transfer Protocol do Workflow**
* **MV\_NGWFLG -****Indica se gera log especifico do processamento do Workflow*****.***Valores do parâmetro: **0 – Desabilita**; **1 – Habilita**.

Com o preenchimento desses parâmetros, pode-se optar por responder à pesquisa via navegador *browser* internet.
