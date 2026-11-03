---
article_id: 4405166201623
category: TAF - eSocial - eSocial do Futuro
content_hash: c06bdb0208dfc17f4303cc9f7119932803f48ca09bd7e0e1de3639513abeef86
fetched_at: '2026-06-28T22:45:15.861440+00:00'
product: protheus
section_id: 1500001537001
source: central-protheus
title: RH - Linha Protheus - TAF - CONFIGURAÇÃO - Erros para configurar ou acessar
  a rotina do Painel E-social
type: support-article
updated_at: '2024-11-14T20:49:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405166201623-RH-Linha-Protheus-TAF-CONFIGURA%C3%87%C3%83O-Erros-para-configurar-ou-acessar-a-rotina-do-Painel-E-social
---

Tempo aproximado para leitura: **05:00 min****Ocorrência**

O Painel E-social apresenta erros ao tentar configura-lo ou quando tento acessar a rotina.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração (TAFA552A) - Todas as versões  
  
**Causa**

Os incidente costumam ocorrer pela falta de algumas configurações obrigatórias, ou configuração errada do Painel E-social.  
  
**Solução**

Independente do erro que venha a apresentar o Painel E-social, seja na configuração ou após a instalação, quando acessar a rotina, orientamos que seja avaliado as informações do passo a passo que vamos apresentar.

**1. Pré-requisitos para configuração do Painel E-social:**

Verifique em seu ambiente se os pré-requisitos para correto funcionamento do Painel E-social foram atendidos.

* **Binário atualizado Lobo Guará (LG).**

**Appserver:** <https://suporte.totvs.com/portal/p/10098/download#detail/947528>

**Smartclient:** <https://suporte.totvs.com/portal/p/10098/download?e=947510>

*Como atualizar o appserver e o smartclient:*

<https://tdn.totvs.com/pages/releaseview.action?pageId=224123650>

* **Ambiente atualizado com o último acumulado, incluindo o menu, para que a opção “Painel E-social” fique disponível.**

*Como atualizar o TAF:*

[Automação Fiscal - Atualização - Expedição contínua no TAF (eSocial)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4484557005207)

* **Possuir um serviço HTTP configurado.**

*Como configurar um serviço HTTP:*

Acrescente a seção [HTTP] no appserver.ini onde o Painel E-social será configurado, essa seção precisa ser exclusiva para o Painel E-social.

Se já possuir serviços configurados, como por exemplo o serviço do Meu RH, a porta HTTP pode ser a mesma, sendo necessário ajustes na seção [HTTP]:

* Migre as configurações da sessão HTTP para uma sessão com IP e Porta.
* Inclua as configurações do Painel E-social na sessão HTTP.

Conforme o exemplo abaixo:

**Apenas o Meu RH:**

**![](https://tdn.totvs.com/download/attachments/625757000/image2020-4-16_17-32-4.png?version=1&modificationDate=1624399624113&api=v2)**

**Meu RH e Painel E-social:**

![](https://tdn.totvs.com/download/attachments/625757000/image2020-4-16_15-38-33.png?version=1&modificationDate=1624399624080&api=v2)

* **Possuir um serviço REST configurado.**

```
Atenção: Clientes, que já possuirem a Porta Multi-Protocolo (MPP) ativada, a criação do   
serviço REST não é necessária.
```

*Como configurar um serviço REST:*

A porta utilizada para o serviço REST, precisa ser exclusiva para o Painel E-social.

Acrescente as seções que listamos abaixo no appserver.ini onde o Painel E-social será configurado:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412250040855)

**IMPORTANTE:**

Orientamos criar **um appserver.ini separado** para o Painel E-social.

Clientes Cloud (T-Cloud) do TOTVS, precisam solicitar a configuração do Painel E-social á área do CLoud:

[Automação Fiscal - Como solicitar suporte TOTVS para o produto, TSS ou Cloud](http://hc/pt-br/articles/4413617765783)

**2. Como criar um appserver.ini separado da aplicação, exclusivo para os serviços do Painel E-social:**

Entre na raiz de instalação do Protheus, copie a pasta "appserver", renomeie a pasta copiada:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412240955159)

Abra para edição o arquivo appserver.ini localizado dentro da pasta copiada, será o appserver.ini para os serviços do Painel E-social.

* Altere o nome do Ambiente (ENVIRONMENT);
* Altere o numero da porta TCP;
* Pode ser mantido o direcionamento para o rpo da aplicação, desta forma, somente um rpo precisa ser atualizado;
* Exclua todos os serviços desnecessários para o Painel E-social, como Schedule, Help, WS, app, etc.;
* Certifique-se de deixar a estrutura necessária para o correto funcionamento do Painel E-social.

                \*\*Utilize as **portas** que **liberou** para os serviços HTTP (**[HTTP]**), REST (**[HTTPREST]**)e as                                 configurações do seu ambiente;

                \*\*Abaixo somente o trecho do appserver.ini referente ao Painel E-social;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405165858327)

**Pontos de Atenção:**

* Verifique se o caminho na chave **RootPath** no grupo **[ENVIRONMENT]** está apontando para o **“rpo”** correto;
* Verifique se o caminho na chave **PATH** no grupo **[HTTP]** está apontando para a pasta “**http-root”**;
* Se possuir a chave **PrepareIn** dentro do grupo **[HTTPURI]** mantenha a chave comentada;
* A chave **PrepareIn** dentro do grupo **[TAF\_CFGJOB],** mantenha como **ALL**, pois dessa forma, o sistema vai ler todos os grupos de empresa;
* Certifique-se que a chave **JOBS** dentro do grupo **[TAF\_CFGJOB]** contém os dois Jobs**: HTTPJOB e TAF\_CFGJOB**

**3. Acesse o menu Painel E-social:**

Pelo menu principal do TAF: **Atualizações > Eventos Esocial > Painel E-social**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17024142391063)

Ao **acessar a rotina Painel E-social** pela primeira vez, a pasta **http-root será criada** dentro da pasta **Protheus Data,** onde ficará armazenado os artefatos da rotina.

Não é possível fazer download dos artefatos, eles são criados ao acessar a rotina.

**4. Configure os parâmetros do Painel E-social:**

Pelo configurador **(SIGACFG)** verifique se os parâmetros abaixo foram criados:

* MV\_BACKEND – Receberá no campo conteúdo a URL do serviço REST ([http://](http://ipportarest/)[IP:PORTAREST/rest](http://ipportarest/))
* MV\_GCTPURL – Receberá no campo conteúdo a URL do serviço HTTP (http://SEUIP:PORTAHTTP)
* MV\_TAFPO – Informará se possui mais módulos do Protheus, deixando o campo conteúdo com .T. em caso positivo ou .F., caso não possua;

Caso não possua um ou mais parâmetros, os mesmos podem ser criados pelo configurador:

Segue exemplos para conferir e criar os parâmetros:

**MV\_BACKEND:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405158224919)**

**MV\_GCTPURL:**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405158242839)**

**MV\_TAFPO:**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405165931799)**

**Pontos de Atenção:**

Insira nos parâmetros MV\_BACKEND (REST) e MV\_GCTPURL (HTTP) as portas liberadas para os respectivos serviços REST e HTTP, as mesmas que inseriu no appserver.ini onde o Painel E-social foi configurado.

*Exemplo:*

**REST**: *http://localhost:**8080**/rest*

**HTTP**: *http://192.168.15.26:**8083***

**5. Teste as URL´s dos serviços HTTP e REST:**

*Como testar:*

**HTTP:**

Pelo navegador de internet que utiliza, digitar o **endereço HTTP (URL)** que está no parâmetro **MV\_GCTPURL,**após a URL do parâmetro, insira /time.apl

Se não existir **bloqueios** de ***Firewall, antivírus, ou na VPN***, será apresentado o horário atual.

**REST:**

Pelo navegador de internet que utiliza, digitar o **endereço REST (URL)** que está no parâmetro **MV\_BACKEND**;

Será aberta uma página com informações das **API´s** *(**Application-Programming Interface, ou Interface de Programação de Aplicação).*

**6. Se o erro na rotina do Painel E-social persistir:**

Abra um ticket para o suporte TOTVS TAF Esocial, e anexe as informações abaixo:

* Descrição do momento que o erro ocorre;
* Print do erro;
* Cópia do arquivo **appserver.ini** onde o Painel E-social está configurado;
* **Print** ou a **tabela SX6** com os parâmetros: MV\_BACKEND, MV\_GCTPURL e MV\_TAFPO;
* Habilite a chave **fwlogmsg\_debug=1** no arquivo **appserver.ini** dentro do grupo [**ENVIRONMENT]** (ambiente);
* Após habilitar, **renomeie** o **console.log** existente. **Gere o erro** no Painel E-social, e encaminhe para o suporte o **novo arquivo console.log**

**Saiba Mais:**

Consulte nossas FAQ´s:

[TAF - ATUALIZAÇÃO - Como configurar o TAF do Futuro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051595774)

[TAF - CONFIGURAÇÃO - Erro ao abrir o TAF do Futuro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055855973)
