---
article_id: 9687263117591
category: PONTO ELETRÔNICO
content_hash: aeac3282a28a4bbed3c15d5dce3807f7262068293fdda04268565c633ce7542e
fetched_at: '2026-06-28T22:44:36.643427+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Não está apresentando os motivos ao incluir
  marcação de ponto pelo App Meu RH
type: support-article
updated_at: '2026-06-19T15:23:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9687263117591-RH-Linha-Protheus-Meu-RH-N%C3%A3o-est%C3%A1-apresentando-os-motivos-ao-incluir-marca%C3%A7%C3%A3o-de-ponto-pelo-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27658746781719) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Não está apresentando os motivos ao incluir marcação de ponto, pelo *App* Meu RH  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH - Todas as versões  
  
**Solução**  
Quando tentamos **incluir uma marcação de ponto**, pelo **Meu RH**, tanto via navegador quanto via celular, temos o retorno de um erro "***Object Object***", assim como o print abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9687125530135)  
  
Os erros com referência ao "***Object Object***", ocorre por conta de numa falha de conectividade e/ou acessibilidade de **algum serviço REST, com a interface**, a tela da aplicação, neste caso, a inclusão de marcações de ponto eletrônico.  
  
Quando temos esse tipo de erro, **não** gera nenhum ***THREAD ERROR*** no ***consolelog***do appserver.  
  
Para casos como estes, **os fontes do Meu RH, precisam estar obrigatoriamente atualizados**, em especial, no caso das marcações de ponto, os fontes **RHNP06 e RHNP06F**.  
  
Segue pacote para atualização:  
12.2310: <https://suporte.totvs.com/portal/p/10098/download#detail/1123885>  
12.2410: <https://suporte.totvs.com/portal/p/10098/download?e=1170810>  
12.2510: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1221795>   
  
Uma outra verificação, será acessando o módulo **16 - SIGAPON e, na rotina Atualizações -> Cadastro de Ponto -> Motivos de Manutenção**, verificar se os motivos estão cadastrados corretamente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27658776994711)  
  
**Saiba mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
