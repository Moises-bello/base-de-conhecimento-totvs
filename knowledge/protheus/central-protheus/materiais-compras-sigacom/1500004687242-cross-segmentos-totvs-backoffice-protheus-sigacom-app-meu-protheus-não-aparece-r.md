---
article_id: 1500004687242
category: Materiais - Compras (SIGACOM)
content_hash: b9ff550bff0d43dde838a1da31ef3c1eaeec36bf573438417d80dbdf947d92f2
fetched_at: '2026-06-28T22:41:14.203086+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - APP Meu Protheus não
  aparece registros para aprovação
type: support-article
updated_at: '2022-05-03T13:36:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004687242-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-APP-Meu-Protheus-n%C3%A3o-aparece-registros-para-aprova%C3%A7%C3%A3o
---

**Dúvida**As aprovações não aparecem?

Não é possível realizar a aprovação?

**Ambiente**Protheus – Compras – A partir da versão 12.1.17

**Configurador**: Ter a rotina **Event Viewer** no módulo implantada e funcional.

**Lib**: A lib com a funcionalidade precisa ser igual ou superior a **20180216.**

**Solução**

**Passo 1:** Verificar se o seu appserver.ini do rest está configurado corretamente conforme a seguir:

**APP MEU PROTHEUS**

**[HTTPV11]**

SOCKETS=HTTPREST

ENABLE=1

**[HTTPREST]**

Port=**porta do cliente**

URIs=HTTPURI

Security=1

**[HTTPURI]**

URL=/rest

PrepareIn=**99,01** **(OBS: Supondo que possuo o grupo de empresa 99 e a filial 01, este seria o exemplo de preenchimento PrepareIn=99,01**

**Caso o cliente possua várias filiais em seu grupo de empresa, poderá preencher apenas com o código do grupo PrepareIn=99 neste caso o sistema entenderá que o APP irá funcionar para todas as filiais dentro deste grupo.**

**Poderá configurar também como PrepareIn=ALL , nesta configuração o APP irá atender todas as empresas e filiais que possuir no sigamat, mas esta configuração utiliza mais licenças, então o cliente deverá verificar o que melhor o atende.)**

Instances=1,2,1,1

CORSEnable=1

AllowOrigin=\*

**[HTTPJOB]**

MAIN=HTTP\_START

ENVIRONMENT=**Ambiente do cliente**

**[OnStart]**

JOBS=HTTPJOB

RefreshRate=120

**Passo 2:** Verificar se está com a última versão do aplicativo do celular;

**Passo 3:** Verificar se está com a última atualização do Mobile;

Basta acessar o portal da central de atualizações e pesquisar por MOBILE:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006219921/mceclip0.png)

**Passo 4:** Verificar se possui o serviço PURCHASEORDERAPPROVAL habilitado em seu serviço do REST:

Entre no navegador de internet, digite: [http:/**/localhost:17115**/rest](http://localhost:17115/rest) faça a busca (CTRL+F) e digite **PURCHASEORDERAPPROVAL:**

OBS: **LocalHost** < Verificar aonde está hospedado a sua porta (provavelmente IP)

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4499584982807/mceclip0.png)**

Caso não encontre aplique a expedição contínua do módulo de Compras disponível no portal.

**Passo 5:** A aba de aprovações aparece em seu aplicativo? **![](https://totvssuporte.zendesk.com/attachments/token/bzeO79HsEz6qTJAt8XxWvyNys/?name=inline1184816145.png)**

**Passo 6:** Logar com usuário que esteja cadastrado como **APROVADOR** no Protheus e verificar se possui as liberações na rotina MATA094 (Liberação de Documentos), caso possuir aprovações pendentes para este usuário os registros deverão aparecer no aplicativo.

**Passo 7:** Verificar se o usuário está cadastrado em algum evento:

7.1: Acesse o módulo **Configurador (SIGACFG)**

7.2: Acesse a rotina**Usuário > Senhas > Usuários.**

7.3: Pesquise pelo usuário que será alterado.

7.4: Selecione o usuário e clique em alterar.

7.5: Selecione a aba **Restrições de Acesso > Aba Acessos**.

7.6: Habilite a permissão **174 - Acesso a inscrição nos Eventos do Event Viewer.**

**![](https://tdn.totvs.com/download/attachments/307838137/GIF%2028-09-2020%2013-17-52.gif?version=1&modificationDate=1601310008753&api=v2 "Linha Microsiga Protheus > Guia de uso - Meu Protheus > GIF 28-09-2020 13-17-52.gif")**

**Passo 8:** Verificar se o parâmetro **MV\_MINGKEY** está devidamente configurado com o token conforme documentação: [APP MEU PROTHEUS](https://tdn.totvs.com/display/public/PROT/Guia+de+uso+-+Meu+Protheus#configuracao-configuracao-usuario)

O token é enviado junto a sua solicitação de alias do mingle: <https://mingle.totvs.com.br/landpage/>

Passo a passo para preenchimento do parâmetro:

![](https://tdn.totvs.com/download/attachments/307838137/GIF%2029-09-2020%2018-52-36.gif?version=1&modificationDate=1601417831553&api=v2 "Linha Microsiga Protheus > Guia de uso - Meu Protheus > GIF 29-09-2020 18-52-36.gif")

**Passo 9:** Mesmo após todas as configurações se entender que o problema ainda persiste, habilite as tags abaixo no appserver.ini onde o REST está configurado (ambiente teste para validação):

FWTRACELOG=1

FWLOGMSG\_DEBUG=1

**Obs**: colocar na TAG do ENVIRONMENT

Após habilitar reinicie seus serviços, limpe o console.log localizado na pasta appserver (EXEMPLO): C:\TOTVS\PROTHEUS27\protheus\bin\appserver e envie o arquivo para o suporte após nova tentativa de acesso.

**ATENÇÃO:** Caso realize a troque de Filial para listar os pedidos e a lista não for carregada, atualizar de forma manual a lista, este comportamento é esperado do **APP MEU PROTHEUS**.

***Saiba Mais :***

[Guia de uso - Meu Protheus](https://tdn.totvs.com/display/public/PROT/Guia+de+uso+-+Meu+Protheus#tudo-sobre-funcionalidades-interfaces)  
[Cross Segmento - Totvs Backoffice Protheus - SIGACOM - Como anexar documento no pedido de compras e visualizar no aplicativo Meu Protheus ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412680424727-Cross-Segmento-Totvs-Backoffice-Protheus-SIGACOM-Como-anexar-documento-no-pedido-de-compras-e-visualizar-no-aplicativo-Meu-Protheus-?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS) 

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
