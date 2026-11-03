---
content_hash: 5fc46bc65644a85d281a73730fec0cbfcc8852a7441d259a008f67483f7fca2c
fetched_at: '2026-06-28T21:35:27.051455+00:00'
page_id: '458754182'
product: fluig
source: tdn-fluig
title: Iniciar uma solicitação a partir de uma página pública utilizando Forms
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458754182
version: 25
---

Atenção

Os aplicativos **Pages Beta**, **Forms Beta** e **Tasks Beta** foram descontinuados e o **suporte** padrão e oficial da TOTVS será mantido apenas até **Junho de 2023**.

Depois desse período, clientes que ativaram e estão usando os aplicativos continuarão tendo acesso a eles, porém, sem direito ao suporte.

O exemplo demonstrado nessa página utilizou os recursos Forms e Pages do menu Soluções que vinham junto com a plataforma Fluig na atualização 1.6.5 Liquid.

Esta página foi revisada para considerar as configurações da **atualização 1.6.5 (Liquid)**.

# Índice

trueÍndicenone

# Objetivo

Este guia tem o propósito de mostrar como iniciar uma solicitação de processo a partir de uma página pública por meio de um formulário público. Vamos apresentar um exemplo e detalhar todos os passos da integração.

# Passo a passo

O caso de uso selecionado é o de recrutamento de novos colaboradores. Você pode conferir mais informações sobre essa aplicação por meio [desse webinar](https://youtu.be/KW2HK8H32YQ).

Confira a seguir os passos necessários para realizar essa configuração.

## Configuração do processo

O primeiro passo é definir qual o processo que deve ser iniciado. Você pode utilizar um processo já existente ou configurar um novo, caso necessário.

Para verificar como criar o processo, verifique a documentação sobre [Adicionar processo](http://tdn.totvs.com/display/HF/Configurar+processos#Configurarprocessos-Adicionarprocesso).

Neste exemplo, vamos criar um processo simples, porém sua empresa pode evoluir o fluxograma para atender completamente as necessidades.

Atenção!

Não se esqueça de configurar o formulário do seu processo! E fique atento ao nome dos campos do formulário, iremos precisar dele nos próximos passos.

## Configuração do serviço

O segundo  passo para iniciar uma solicitação é por meio do cadastro do serviço REST de processos. Lembrando que se deseja fazer integração de um formulário com outro serviço é possível, basta cadastrar o serviço desejado.

Para verificar como criar o serviço, verifique a documentação sobre [Adicionar serviço](http://tdn.totvs.com/pages/viewpage.action?pageId=243660796#Servi%C3%A7os-Adicionarservi%C3%A7o).

No caso do exemplo, será utilizado um serviço REST configurado conforme a seguir.

Serviços01Configuração02Arquivo Swagger

Para recuperar a informação do arquivo Swagger, siga os passo abaixo:

1. Acesse a URl do seu ambiente TOTVS Fluig Plataforma e adicionar /api-rest. Ex: <http://suaempresa.fluig.com/api-rest>
2. Selecione o serviço que deseja, nesse caso utilizamos o de Process Management. Ver imagem abaixo:

Após acessar a página, copiar a URL e adicionar ao final a *swagger.json.* O resultado final será algo semelhante a: <http://suaempresa.fluig.com/process-management/swagger-ui/swagger.json>

03Domínio

No campo Domínio você adicionará a URL do Fluig Plataforma da sua empresa junto com a Base URL que você pode recuperar na página do serviço (Process Management).

04Tipo de autenticação

Nosso exemplo utiliza o tipo de autenticação Rest oAuth 1, porém [nessa documentação](http://tdn.totvs.com/pages/releaseview.action?pageId=239041233)são apresentados os detalhes de cada autenticação para atender a sua necessidade. Ao selecionar autenticação do tipo Rest oAuth 1 é preciso preencher algumas informações (Consumer Key, Consumer Secret, Token de acesso e Token Secret).

Acesse [essa documentação](http://tdn.totvs.com/display/public/fluig/Fluig+API)para saber onde encontrar essas informações.

URL de teste de serviço

A URL de teste de serviço não é uma informação obrigatória, porém serve para testar se as configurações do serviço estão corretas. A única particularidade é que precisa ser um método GET.

## Configuração da operação

No terceiro passo é realizada a inclusão da operação que será necessária para integrar com o formulário.

Para verificar como criar a operação, verifique a documentação sobre [Adicionar operação](http://tdn.totvs.com/pages/viewpage.action?pageId=394220928#Opera%C3%A7%C3%B5es-Adicionaropera%C3%A7%C3%A3o).

No exemplo dessa documentação, será incluída a operação de iniciar solicitação de processos.

Operação01Configuração02Operação do serviço

As operações são os métodos retornados da documentação Swagger da API, cadastrado no serviço selecionado. No caso será escolhida a operação start, que é o método de inicialização de uma solicitação de processo.

03Parâmetros de entrada e saída

Os parâmetros também são recuperados da documentação Swagger e o campo Label permite que sejam definidos nome mais amigáveis, que irão aparecer na integração do formulário, facilitando assim o entendimento de usuários das áreas de negócio.

## Configuração do formulário

Nesse 4º passo será apresentada a configuração do formulário, que inclui torná-lo público e integrado com a operação de iniciar a solicitação.

Para verificar como criar o formulário, verifique a documentação sobre [Construção de formulário](http://tdn.totvs.com/display/HF/Forms#Forms-Construirumformul%C3%A1rio).

No exemplo dessa documentação, foi criado um formulário com alguns campos. Na configuração dos campos, foram definidas as informações como obrigatórias:

Forms01Configuração02Marcar como público

Como o formulário será adicionado a uma página pública, é necessário realizar a configuração para torná-lo formulário público. Basta acessar as configurações de segurança do formulário e defini-lo como público.

03Vincular a operação

Nessa mesma aba de configurações é realizada a inclusão da operação a ser integrada, basta selecionar a operação desejada (no caso, aquela de *start*) e configurar os campos para a integração. Serão preenchidos apenas os campos necessários para a integração, que são o **codigoProcesso** com o valor do código de processo a ser iniciado (nesse caso o código de processo é o do processo criado no passo 1), o parâmetro **targetState**(código da atividade que se encontra após a atividade inicio), o parâmetro **targetAssignee** (pessoa responsável pela atividade) e os campos que serão preenchidos no formulário público e enviados para o formulário do processo.

Após configurar os campos é possível definir as mensagens relacionadas a integração.

## Configuração da página

O último passo é configurar a página pública, arrastando os componentes e personalizando o layout de acordo com a identidade da empresa.

Para verificar como criar a página, verifique a documentação sobre [Adicionar página](http://tdn.totvs.com/display/HF/Pages+Beta#PagesBeta-Adicionarp%C3%A1gina).

E para que a solução fique completa, basta adicionar o formulário criado no passo 4. Para fazer isso, siga os passos a seguir:

Page01Pages

Arraste um componente de Conteúdo externo para a página.

02Forms

Acesse o seu formulário e acione a opção Compartilhar URL, para copiar a URL do formulário para a área de transferência.

03Pages

Volte na tela de configuração da página e insira a URL do formulário na configuração do componente de Conteúdo externo.

# Conheça mais: Webinar

Assista ao *webinar* gravado pelo time da plataforma Fluig, para obter mais detalhes sobre o funcionamento deste procedimento:

800450
