---
article_id: 26897176315671
category: SIGAACD - Automação e Coleta de Dados
content_hash: c4ab911baa0c50f0a93ca639e41c383413b875035e54e3a4540cc452bcca3ec0
fetched_at: '2026-06-28T22:39:11.400473+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - App Meu Coletor de
  Dados - Não existe licença disponivel no License Server para atender a requisição
  nesse momento
type: support-article
updated_at: '2025-12-30T21:17:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26897176315671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-App-Meu-Coletor-de-Dados-N%C3%A3o-existe-licen%C3%A7a-disponivel-no-License-Server-para-atender-a-requisi%C3%A7%C3%A3o-nesse-momento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26897176283287) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O que avaliar quando, ao configurar o App Meu Coletor de Dados e tentar acessá-lo, ocorrer o erro "Internal Server Error"?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
Abaixo serão descritos os passos a serem seguidos para mitigar a existência de erros de configuração, caso execute todos os passos e o app continuar retornando o erro, nos forneça:

* Evidencia dos passos que executou;
* Gerar o Console.log no AppServer.ini do REST com as chaves abaixo:

  ```
  [environment]
  FWLOGMSG_DEBUG=1
  FWTRACELOG=1

  [General]
  MAXSTRINGSIZE=10
  LogHttpFuncs=1 (Para analisar erros no REST)

  --- Para verificar problemas na licença---

  [environment]
  LSDebug=2
  FWTRACELOG=1
  ```

**Análises a serem realizadas:**

**Passo 1** - Verificar a versão do License Server do ambiente (em caso de dúvidas referente à atualização, acionar o Cloud (caso tenha o ambiente hospedado no Cloud) ou Framework (caso tenha ambiente  o ambiente hospedado localmente);

**Passo 2** - Avaliar em qual etapa ocorre o erro. Se é em um processo específico no App ou se seria no primeiro acesso (caso esteja em implantação);

**Passo 3** - Estando em implantação do App, revisar todas as configurações necessárias:

* Se possui licença TOTVS T, TOTVS I ou TOTVS FULL conforme documentação: [Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Qual licença utilizar no aplicativo Meu Coletor de Dados?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411627803415--Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Qual-licen%C3%A7a-utilizar-no-aplicativo-Meu-Coletor-de-Dados?source=search)
* Se o REST está configurado conforme exemplo abaixo:

```
[HTTPV11]
Enable=1
Sockets=HTTPREST

[HTTPREST]
Port=8080 (porta configurada para o REST do cliente) 
IPsBind=
URIs=HTTPURI
Security=1 

[HTTPURI] 
URL=/rest (este é o endpoint a ser colocado na primeira tela de acesso do aplicativo) 
PrepareIn=ALL 
Instances=2,5,1,1 
CORSEnable=1 
AllowOrigin=*
Module=46 (obrigatória para uso do App Meu Coletor de Dados)

[HTTPJOB]
MAIN=HTTP_START 
ENVIRONMENT=environment (nome do ambiente do cliente)

[ONSTART]
jobs=HTTPJOB 
RefreshRate=30
```

**OBS:** **É imprescindível que todas as chaves e tags citadas acima existam no ambiente (apenas mude para o seu contexto os dados que são pontuais, por exemplo: Port e Environment)**

**Observação importante sobre a tag INSTANCES:** Esta tag define quantas instâncias ficarão disponíveis para o serviço do REST. Ela deve ser adaptada de acordo com o número de licenças que o cliente deseja utilizar no serviço. TDN com detalhes da tag: <https://tdn.totvs.com/display/tec/Instances>

**Passo 4 (opcional) -** Via Assistente de Configuração do Mobile, certifique-se de que não há nenhuma informação faltante na configuração do AppServer.ini

Para saber mais sobre como utilizar este recurso, veja esta documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=620785607#interfaces-acesso>

**Passo 5** - Verificar se houve o primeiro cadastro de Operador (ACDA010)

Configuração de Operador:  
- Acessar o modulo Estoque/Custos  
- Acessar o Menu > Atualizações > ACD> Operadores  
- Clique Incluir  
- Informe os campos obrigatórios

![image2019-2-19_8-16-59.png](https://tdn.totvs.com/download/attachments/464945570/image2019-2-19_8-16-59.png?version=1&modificationDate=1552075909463&api=v2)

**Passo 6** - Revisar no Configurador (Usuários -> senhas -> usuário -> aba restrições de acesso na parte superior -> aba ambientes) se o modulo 46- SIGAACD está com *checkbox* marcado no usuário  
do qual foi cadastrado o operador vinculado a ele

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26897161061911)

**Passo 7**- Testar no navegador a comunicação do Endereço, Porta e o Endpoint. Exemplo: https://localhost:8080/rest. Deve retornar algo, se não acessar, revisar endereço, protocolo (http/https), porta e endpoint

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26897161064343)

**Passo 8-** Certifique-se de que o aplicativo está em sua ultima versão (2.0.1)

![Exibindo image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEV8xms6qm5YvYThOciJRKqyfrFowkITvKmMrFZBQfFbZ8UG2fFlq4f3Ll3TLZdzTvn56fGkpNEli1Ei6BzoFiWF0m6aeamJLTW4VZEZf3FY80iKKV8KSEywJoiLp2Ri2x4ziaOhAbaYxY2DWsj%2F9YtaZWJ0yyPb9jiD2Q6spqIwbFambfZB%2B9VQNRNasPqwURiYoz8wdakk1tHJgARhgWYVpyanK6dcGENU8KDO3OgtAOgH9YehxsUDXR9XeeAMGUdy6rXNOoI0sk6ztBJcI2ElZnAmy%2FUbXmVDUKDRckW4OMW8kCrf0eMd4ZvnGv7TvV%2FVgPFpaT%2Fa2BoR34yFMcYILu0Pl1jM18wQuBC9WQVRkgbvgUvigIX7I5b1i8FwCTER5oUebKTm3NuiBWJXuCn3x%2BlBCBZM0dgVkNbS0dX5%2BCoHcNFIt2IIWfpCddXYZLaJLSqfhzBr5EZvvAnpMGCqTuU1YyK5dry%2B5Ch7LveGceCQcIA9kpCknSIZBxFVe2wDKoBT302aab1zQgRf0HxUSeiCRzojPvpjHdcqTx9h22o41P2yEeF4x7xakzC1&sz=w1294-h960)

**Passo 9** - Superado o passo 6, ao inserir novamente a Conexão, Endereço, Porta e Endpoint, o acesso deve ser feito com sucesso

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26897176292119)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
