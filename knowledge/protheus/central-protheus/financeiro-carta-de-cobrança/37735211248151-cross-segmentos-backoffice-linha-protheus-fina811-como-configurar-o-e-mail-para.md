---
article_id: 37735211248151
category: Financeiro - Carta de Cobrança
content_hash: 2d026f59d26a0467b49b0d3c5ccaef71a71a43ef328974d22a487c13bc66fbc3
fetched_at: '2026-06-28T22:37:28.956978+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA811 - Como configurar o e-mail
  para envio do boleto de cobrança?
type: support-article
updated_at: '2026-01-16T20:30:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37735211248151-Cross-Segmentos-Backoffice-Linha-Protheus-FINA811-Como-configurar-o-e-mail-para-envio-do-boleto-de-cobran%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37735234809623) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como configurar o e-mail para envio do boleto de cobrança?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA811 - Todas as versões.  
  
**Solução**

A rotina de envio de cartas de cobrança permite a cobrança de títulos em atraso, a vencer ou em situações específicas, por meio de cartas eletrônicas e/ou físicas.

O processo considera critérios configuráveis, como período, situação de cobrança, atualização de juros e multas e modelo de texto.

Também disponibiliza relatório para acompanhamento das cobranças realizadas, com os respectivos clientes e títulos.

1º Configurar o layout da carta de cobrança.

No cabeçalho do cadastro são informados o método de envio da carta, os textos que a compõem (texto principal, saudação e conclusão), bem como a definição da posição do endereço para cartas impressas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37735211221143)

No rodapé da rotina estão disponíveis duas abas destinadas à configuração dos campos do Contas a Receber (tabela SE1) que serão exibidos na carta de cobrança, como número do título, valor e data de vencimento.

Nessa mesma seção, também são definidas as regras personalizadas para o envio das cartas, por meio da inclusão de expressões de filtro, seguindo o mesmo padrão utilizado nos filtros de tela (browse) do Protheus, com a tabela de Clientes (SA1) devidamente posicionada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37735211225239)

2º Configurar as informações referentes ao e-mail e senha.

A seguir, apresenta-se o procedimento para configuração do envio de relatórios por e-mail, contemplando as definições de **E-mail/Proxy**, utilizando como exemplo uma conta do **Gmail**.

Para a utilização de outros provedores de e-mail (SMTP), recomenda-se consultar as informações junto ao respectivo provedor e realizar a substituição dos dados nos campos correspondentes.

**1.** Acesse o **Configurador > Ambiente > E-mail/Proxy > Configurar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37735234811031)

Na próxima tela, apenas clique em avançar sem alterar nada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37735234812311)

**Importante**

|  |
| --- |
| Obs. 1: atualmente a maioria dos provedores SMTP utilizam uma porta diferente da padrão, geralmente usam a 465 ou 587. Essa porta deve ser informada no campo do endereço do SMTP, logo após o endereço, utilizando :###  Obs. 2: o Gmail utiliza a porta 465 quando a segurança utilizada é a SSL e a porta 587 quando a segurança é a TLS (o tipo de segurança será configurado na próxima tela da configuração de E-mail/Proxy) |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37735211228055)

Clicar em Avançar para continuar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37735211228439)

Por fim, clicar em Finalizar.

**Importante**

Por meio deste processo, serão alimentados os parâmetros listados a seguir. Contudo, para o pleno e correto funcionamento da rotina, é necessário o preenchimento de outros parâmetros adicionais, conforme detalhado na documentação apresentada abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37735234816535)

**Para envio das cartas por e-mail são utilizados os seguintes parâmetros:**

| **Parâmetro** | | **Definição** |
| --- | --- | --- |
| **FINA811** **<= 23/08/2022** | **FINA811** **> 23/08/2022** |
| MV\_RELSERV | | Nome do servidor de envio de e-mail |
| MV\_RELACNT | MV\_FINACNT | Conta a ser utilizada no envio de e-mail |
| MV\_RELPSW | MV\_FINPSW | Senha da conta de e-mail |
| MV\_RELFROM | MV\_FINFROM | E-mail utilizado no campo FROM no envio do e-mail |
| MV\_RELBODY | | Determina o assunto padrão no envio do e-mail. Será usado quando o campo FWP\_TXTASS não for preenchido |
| MV\_RELAUTH | | Determina se o servidor exige autenticação |
| MV\_RELAUSR | MV\_FINACNT | Usuário para autenticação no servidor de e-mail (caso servidor assim exigir) |
| MV\_RELAPSW | MV\_FINPSW | Senha para autenticação no servidor de e-mail (caso servidor assim exigir) |

Para mais informações:

[Parâmetros de configuração para o envio da carta de cobrança](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)

Após a conclusão das configurações, será possível realizar o envio das cartas de cobrança.

A seguir, disponibiliza-se o manual contendo o procedimento completo para execução da rotina.

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA811 - Como realizar o envio da carta de cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6777494398231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA811-Como-realizar-o-envio-da-carta-de-cobran%C3%A7a)

**Saiba mais**

[Envio de boleto - Visão geral - Gmail](https://tdn.totvs.com/pages/releaseview.action?pageId=635983295)
