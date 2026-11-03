---
article_id: 8890844378263
category: SIGAACD - Automação e Coleta de Dados
content_hash: 3979138468b529ab92da852b6f140307017f702c5c51b1ba9cf0bcc243e1b6ec
fetched_at: '2026-06-28T22:39:12.690671+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - É possível estabelecer
  a tag InactiveTimeout para ociosidade na sessão VTDEBUG?
type: support-article
updated_at: '2025-12-17T14:46:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8890844378263-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-%C3%89-poss%C3%ADvel-estabelecer-a-tag-InactiveTimeout-para-ociosidade-na-sess%C3%A3o-VTDEBUG
---

É possível configurar a tag InactiveTimeout para ociosidade na sessão VTDEBUG em ambientes TELNET, ajustando a chave na seção [TELNET]. Essa tag define o tempo máximo de inatividade da conexão, medido entre envios e recebimentos de dados, com valores mínimos de 60 segundos. Após o tempo configurado, ocorre desconexão, que não é exibida na tela, mas encerra a aplicação ao retornar o foco ao VTDEBUG.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37090026611735) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
É possível estabelecer a tag InactiveTimeout para ociosidade na sessão VTDEBUG?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Sim é possível efetuar essa configuração.

Para ambientes TELNET a chave **InactiveTimeOut** deve ser configurada na seção [TELNET].

**Qual a funcionalidade dessa tag InativeTimeOut?**

Indica o tempo máximo que a conexão pode ficar inativa. Essa contagem de tempo leva em consideração apenas os tempos entre envio e recebimento de dados, se o processo tiver alguma rotina que pode demorar o processamento, levar em consideração esse tempo que a interface ficará sem enviar/receber dados.

**Exemplo:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8890763712279)

Após o período configurado, a desconexão irá ocorrer, **se houver interação na sessão**.

* Diferente do SmartClient Desktop, na tela do VTDEBUG não é exibida a tela de desconexão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8890860104983)

* Contudo, ao voltar o foco para a janela do VTDEBUG, ele encerra a aplicação.
* Falando de FOCO, sempre que o foco for alternando entre qualquer outra aplicação e o VTDEBUG, o contador de timeout é reiniciado, por exemplo tentar acessar outro menu dentro do mesmo, ocorrera a desconexão.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8890863052567)

* O valor é definido em segundos. Contudo, a inatividade considera o "minuto cheio" da inatividade. Por exemplo, quando configurado 90 segundos a desconexão será realizada em 1,5 minuto.
* Apenas valores superiores a 60 segundos são aceitos. Assim, qualquer valor inferior a essa quantidade será interpretado como 60 segundos.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre ACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360002469152-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
