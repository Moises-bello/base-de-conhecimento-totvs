---
article_id: 37783114711447
category: Financeiro - Carta de Cobrança
content_hash: 321edbcf4f0d94207427f3bfa526872b74b0517d4db5342fd647c0bfea9a93ad
fetched_at: '2026-06-28T22:37:28.941794+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA811 - Como alterar a senha
  do e-mail?
type: support-article
updated_at: '2026-01-19T18:46:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37783114711447-Cross-Segmentos-Backoffice-Linha-Protheus-FINA811-Como-alterar-a-senha-do-e-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37783114686871) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Como alterar a senha do e-mail?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA811 - Todas as versões.

**Solução**  
Para realizar a atualização da senha do e-mail utilizado para o envio de boletos, é necessário seguir os procedimentos descritos abaixo:

**1.** Acesse o **Configurador > Ambiente > E-mail/Proxy > Configurar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37783130845847)

Na próxima tela, apenas clique em avançar sem alterar nada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37783114689431)

**Importante**

|  |
| --- |
| Obs. 1: atualmente a maioria dos provedores SMTP utilizam uma porta diferente da padrão, geralmente usam a 465 ou 587. Essa porta deve ser informada no campo do endereço do SMTP, logo após o endereço, utilizando :###  Obs. 2: o Gmail utiliza a porta 465 quando a segurança utilizada é a SSL e a porta 587 quando a segurança é a TLS (o tipo de segurança será configurado na próxima tela da configuração de E-mail/Proxy) |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37783130849175)

Clicar em Avançar para continuar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37783114691863)

Por fim, clicar em Finalizar.

A execução do processo realizará a atualização dos parâmetros listados abaixo, incorporando as novas informações configuradas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37783114692887)

Caso o servidor de e-mail exija autenticação por senha, será necessário também ajustar os parâmetros adicionais relacionados à autenticação, conforme descrito a seguir:

| Parâmetro | Parâmetro Relacionado | Descrição |
| --- | --- | --- |
| MV\_RELAUSR | MV\_FINACNT | Usuário para autenticação no servidor de e-mail (caso o servidor exija) |
| MV\_RELAPSW | MV\_FINPSW | Senha para autenticação no servidor de e-mail (caso o servidor exija) |

**Saiba mais**

[Envio de boleto - Visão geral - Gmail](https://tdn.totvs.com/pages/releaseview.action?pageId=635983295)
