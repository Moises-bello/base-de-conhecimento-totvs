---
article_id: 25510214148119
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 8a2a7a4e174303bf3f59a31c34274c5c758c025bd72e0e647dfda42436da1f3e
fetched_at: '2026-06-28T22:47:29.470880+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH- Como as licenças no Meu RH são consumidas
type: support-article
updated_at: '2026-05-12T12:35:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25510214148119-RH-RM-Meu-RH-Como-as-licen%C3%A7as-no-Meu-RH-s%C3%A3o-consumidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25510214108439) Tempo aproximado para leitura: **00:08:14 min**  
  
**Dúvida**  
Como as licenças no Meu RH são consumidas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**

O Meu RH consome as licenças de **slot**:

* **4177** - Agrupador Ondemand RH
* **4001** - TOTVS I
* **4000** - TOTVS FULL
* **4099** - CAMPANHA TOTVS / Licença Especifica TOTVS
* **4016** - ID INTERA COMPLETAO
* **3098** - APP MEU RH

Caso ainda não possua nenhuma das licenças, **entre em contato com o seu ESN (Executivo de Soluções de Negócio) para aquisição e maiores informações.**  
  
Em relação a **quantidade de licenças**, seu**Gerente de Contas** pode ser acionado, pois deve ser avaliada a infraestrutura, picos de acessos, entre outros detalhes intrínsecos de cada ambiente. Este levantamento deve ser feito por um arquiteto de soluções, que deve direcionar essa demanda junto ao Gerente da conta para verificar a **quantidade de licenças necessárias para atender a Empresa.**

O ideal também é monitorar o consumo das licenças listadas anteriormente em tempo real, utilizando o monitor de licenças conforme a documentação [**Framework - Linha RM - Frame - Monitorar uso de licenças em tempo real**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9218011037079) quando a tela do Meu RH fica totalmente em branco ou retorna algum erro referente a licenças.  
  
No que cabe ao **consumo das licenças**, vale lembrar que a arquitetura do **Meu RH** usa o serviço ***API/REST,*** onde o consumo da licença ocorre **durante** o **período em que a*****API*** está **processando a resposta** para a **requisição**.  
  
**Uma página do Meu RH utiliza em média de 3 a 7 requisições/threads** simultaneamente, sendo possível em tempo real, acompanhar o Monitor do LS, **01 única licença atenderá somente 01 requisição,**mas com a comunicação REST, e o uso de *token* para validar as API's, o processo de ***login*** realmente, utilizará **entre 3 a 7 requisições API's diferentes e "ao mesmo tempo"** para:  
  
- criação do *token;*  
- validação do *login*;  
- carregar a página inicial;  
- funcionalidades que o usuário tem acesso.  
  
**Importante**  
Essa informação sobre o consumo de 3 a 7 licenças no login pode parecer alarmante à primeira vista. No entanto, isso não significa que, caso 1.000 funcionários utilizem o app, seria necessário contratar entre 3.000 e 7.000 licenças.  
Devido ao comportamento de "**consumo temporário e liberação imediata"** das licenças, a recomendação continua sendo manter uma **relação de 1 para 1**, ou seja, uma licença por usuário.   
  
Para o funcionamento do **Meu RH**, mesmo para testes, é necessário um mínimo de **10 licenças para funcionamento.**  
  
Outra observação é que os processos não precisarão ser executados todos ao mesmo tempo, entrará em uma espécie de fila de processamento, sendo que, enquanto houverem licenças disponíveis, as requisições consomem uma nova *thread* e por consequência uma nova licença, e executa o processamento.  
  
Exemplo, caso um cliente adquira 100 licenças TOTVS I e somente um funcionário acesse o Meu RH, como o processo do *login* são 4 ou mais operações distintas (execução de 4 API's), para agilizar o processo de *login*, **o sistema pode utilizar entre 3 a 7 licenças, momentaneamente**, para fazer as requisições de uma só vez.  
  
Importante ressaltar que, **neste momento do*****login*****somente,** mais licenças são consumidas, porém estas são liberadas entre **1 e 4 minutos após o consumo/*****login !***  
  
O *token* por sua vez, serve para que **não seja necessário realizar uma validação de*****login*****a toda requisição e que o usuário logado "prendesse" a licença.**  
  
Quando um novo botão é apertado em tela, uma nova requisição *API* é disparada ao *REST*, e o *token* é enviado no corpo da comunicação para validar se o *REST* pode responder àquela requisição ou não.  
  
Quando nenhuma requisição está em processamento, ou seja, o funcionário está logado, mas não está navegando, mesmo que ainda não tenha dado o *timeout*, nenhuma licença será consumida.  
  
Esta é a regra sobre o consumo das licenças para o Meu RH, tendo somente o adendo que a TOTVS I é a licença que consegue responder requisições *REST*, por isso que ela é utilizada e vendida para o Meu RH, pois o App funciona totalmente através de *API's/REST.*  
  
Devido à **estrutura do serviço REST**, que atende à requisições apenas, **o usuário logado no Meu RH não consome nenhuma requisição/thread**, enquanto não realiza nenhuma ação no aplicativo (clicar sobre algum item do Menu ou em tela).   
  
**Saiba Mais**

[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000860702-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
