---
article_id: 360062679833
category: Financeiro - Contas a Receber
content_hash: fb5a9912da59cc6fab59e72d329428342225eff57c395603888281c37b157fcc
fetched_at: '2026-06-28T22:38:14.171811+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN – FINA811 - Erro Falha
  de autenticação no envio de carta de cobrança
type: support-article
updated_at: '2026-02-10T19:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062679833-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA811-Erro-Falha-de-autentica%C3%A7%C3%A3o-no-envio-de-carta-de-cobran%C3%A7a
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37735567040535)**Tempo aproximado para leitura: **00:04:00 min**

**Ocorrência**  
No módulo Financeiro, ao tentar enviar uma carta de cobrança pela rotina **FINA811**, ocorre o erro de falha de autenticação.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA811 - Todas as versões.  
  
**Causa**  
O erro é decorrente da configuração de e-mail no módulo Configurador, que não reconhece as novas definições necessárias para o correto funcionamento da rotina FINA811. As informações da TAG **MAIL** no arquivo **APPSERVER.INI** não estão sendo interpretadas pelo ambiente, o que ocasiona a falha no envio de e-mails.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar a pasta **BIN** / **APPSERVER**.  
2. Faça um backup do arquivo **APPSERVER.INI.**  
3. Abra o arquivo **APPSERVER.INI** e localize a TAG "**MAIL**", conforme a imagem abaixo.  
![flavio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002281962)  
4. Apague a TAG MAIL com todos os componentes dentro da TAG "**MAIL".**  
5. Salve o arquivo **APPSERVER.INI.**  
6. Acesse o **Configurador > Ambiente > E-mail/Proxy > Configurar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38307062348439)

Na próxima tela, apenas clique em avançar sem alterar nada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38307084668311)

**Importante**

|  |
| --- |
| Obs. 1: atualmente a maioria dos provedores SMTP utilizam uma porta diferente da padrão, geralmente usam a 465 ou 587. Essa porta deve ser informada no campo do endereço do SMTP, logo após o endereço, utilizando :###  Obs. 2: o Gmail utiliza a porta 465 quando a segurança utilizada é a SSL e a porta 587 quando a segurança é a TLS (o tipo de segurança será configurado na próxima tela da configuração de E-mail/Proxy) |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38307084670487)

Clicar em Avançar para continuar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38307084671383)

Por fim, clicar em Finalizar.

7. Após a validação mencionada acima, revise os demais parâmetros listados a seguir e realize novamente os testes.

![](https://totvssuporte.zendesk.com/attachments/token/9mY4K7GaIVDioLNnILHcCyrHj/?name=inline801107563.png)

**Saiba mais**

[Carta de Cobrança](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)

[Financeiro - Carta de Cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/sections/35058223754903-Financeiro-Carta-de-Cobran%C3%A7a)
