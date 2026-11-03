---
article_id: 360058847774
category: Treinamento (SIGATRM)
content_hash: e17c41768ec7251aa50591a53434152a4363b721c3b87fb1fd31ecd5da548dbd
fetched_at: '2026-06-28T22:43:02.532862+00:00'
product: protheus
section_id: 206971527
source: central-protheus
title: RH - Linha Protheus - TRM - Configuração para envio de Email no modulo SIGATRM
type: support-article
updated_at: '2024-06-21T17:06:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058847774-RH-Linha-Protheus-TRM-Configura%C3%A7%C3%A3o-para-envio-de-Email-no-modulo-SIGATRM
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23543300091671) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Configuração para envio de *e-mail* no módulo SIGATRM  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Treinamento - todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Configurar os parâmetros abaixo:  
**MV\_TRMMAIL** - Define se ao realizar a baixa de um treinamento envia *email* de conclusão de curso aos funcionários  
**MV\_EMCONTA** - Conta *e-mail***MV\_EMSENHA** - Indica qual a senha da conta utilizada para envio dos *e-mails*  
**MV\_RELSERV** - Servidor *smtp e-mail*  
**MV\_RELACNT** - Conta a ser utilizada no envio de *e-mail* para os relatórios  
**MV\_RELAUTH** - Servidor de *e-mail* necessita de autenticação? = .T.  
**MV\_RELSSL** - Define se o envio e recebimento de *e-mails* utilização conexão segura  
**MV\_RELTLS** - Informe se o servidor de *SMTP* possui conexão do tipo segura  
  
2. Verificar se os campos na aba **Cadastrais** do cadastro do funcionário estão preenchidos:  
**RA\_EMAIL** - Email Princ   
**RA\_TPMAIL** - Tipo E-Mail   
**RA\_RECEMAIL** - Receb E-mail  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23543272837655)  
  
Fontes e funções, já compiladas no RPO padrão, relacionadas ao processo:  
**- TRMA060** - Função - **Tr060Email** - Envia *e-mail* de confirmação para funcionários  
**- RHLIBGEN** - Função - **Rh\_Email** - Envia *e-mail* para funcionários  
  
3 - Nas perguntas da geração da Reserva de Treinamento tem o item: **Envia email confirmação?**Seleciona o item desejado para o envio.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24343313495191)  
  
4. Após es configurações acima, o sistema envia ao funcionário *e-mails* de confirmações relacionado ao modulo **SIGATRM.****Saiba Mais**[**Como configurar o E-mail de Workflow de solicitações do MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055230453)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
