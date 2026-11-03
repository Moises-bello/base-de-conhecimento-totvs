---
article_id: 14838088296855
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 832c18dfb9e1f5ad70ed1b2822a228df7bc3f0fc39d5ea49ddec6fdffb738010
fetched_at: '2026-06-28T22:45:20.957350+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração de e-mail no Diagnóstico
type: support-article
updated_at: '2026-06-26T12:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14838088296855-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-de-e-mail-no-Diagn%C3%B3stico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23702288065687) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como realizar a configuração de e-mail, para que seja verificado na tela de diagnóstico, se o e-mail está cadastrado e se o serviço SMTP está configurado corretamente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Diagnostico (TAFDIAG) - Todas as Versões  
  
**Solução**Siga as orientações abaixo para realizar a configuração:

**\*\*Importante:** somente é possível configurar usuário **administrador.**

1. Entre no configurador do Protheus SIGACFG:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26594783898903)

2. Acesse o menu Base de Dados > Dicionário > Base de Dados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14835382627863)

2.  Pesquise e analise se os parâmetros listados abaixo estão preenchidos corretamente:

MV\_RELSERV

MV\_RELACNT

MV\_RELPSW

**Exemplo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14835493788695)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14835504185751)

**3. MV\_RELSERV**

Insira no campo conteúdo, o **endereço do seu servidor**, IP ou Localhost:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14837802168599)

**4. MV\_RELACNT**

Insira no campo conteúdo, o **endereço de e-mail** do administrador.

**\*\*Atenção:** o e-mail utilizado, precisa estar informado no cadastro do usuário, no SIGACFG.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14837873002391)**

4.1 Como verificar se o e-mail está cadastrado no usuário administrador:

Pelo SIGACFG entre no menu: **Usuário> senhas> Usuários,**

Abra o registro do usuário administrador e verifique se o campo "e-mail" está preenchido, este e-mail deve ser utilizado na configuração do parâmetro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14843076944151)

**5. MV\_RELPSW**

Insira no campo conteúdo, a **senha que utiliza no e-mail.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14838073836695)**

6. Após configurar os parâmetros, faça logoff (saia e entre no sistema novamente) para que as alterações sejam efetivas.

7. Entre no TAF, na rotina **Diagnostico:** Atualizações > Configs. TAF > Diagnóstico

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14845337585943)

8. Será apresentada mensagem, na cor Verde, que o servidor e e-mail foram configurados corretamente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14845427957783)

**Documentações Relacionadas:**

[MP - FRAME - Configurar o SMTP para envio de relatórios por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071)
