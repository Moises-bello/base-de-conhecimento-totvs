---
article_id: 360056648973
category: RH - Soluções para error.log
content_hash: 7c193c254c4e4d61d6fdea5c164963e41d75a1e9652012468ee45334e21216be
fetched_at: '2026-06-28T22:44:09.005169+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH- Linha Protheus - GPE - Error log na inclusão de Funcionário - InterFunctionCall:cannot
  find function A240VARALFA in AppMap on
type: support-article
updated_at: '2022-10-19T13:13:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056648973-RH-Linha-Protheus-GPE-Error-log-na-inclus%C3%A3o-de-Funcion%C3%A1rio-InterFunctionCall-cannot-find-function-A240VARALFA-in-AppMap-on
---

**Ocorrência**  
Ao vincular atestado ao Funcionário, através da rotina **GPEA240**, é gerado ***error log**: **"InterFunctionCall:cannot find function A240VARALFA in AppMap on {|a,b,c,d| FWInitCpo(a,b,c),lRet:=((Vazio() .or. aContAfaVal()) .And. (!vazio().or.(a240VarAlfa().and.aContAfaVal().and.a240Numdias()))),FWCloseCpo(a,b,c,lRet),lRet }(PROTHEUSFUNCTIONMVC.PRX)******"*.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - à partir da versão 12.1.17  
  
**Causa**Este erro ocorre devido ao campo **R8\_CONTAFA** estar com suas propriedades fora do padrão  
  
**Solução  
1.**Acessar o dicionário de dados do ambiente que apresenta o error.log e verificar se o campo **R8\_CONTAFA** da tabela **SR8** está de acordo com o padrão demonstrado abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/7avj2uGO7ZL2sUqwTbaK7sCOo/?name=inline-799239935.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/tneNaGTwyR2N2lcNGcxxVCS3r/?name=inline328340418.png)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092712154/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094937333/mceclip1.png)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092712254/mceclip2.png)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092712354/mceclip3.png)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092712374/mceclip4.png)  
  
Acessando em opções deste campo e em modo de edição deve ficar  com conteúdo do padrão: **Gp240VerEdit()**, imagem abaixo:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092712414/mceclip5.png)  
  
Já ao clicar em validações, no padrão o campo **R8\_CONTAFA** está com a informação: **Vazio() .or. aContAfaVal()**, conforme imagem abaixo:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092712474/mceclip6.png)  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094937473/mceclip7.png)  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094937513/mceclip8.png)  
  
**Saiba mais:**  
[RH Expedição Contínua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
