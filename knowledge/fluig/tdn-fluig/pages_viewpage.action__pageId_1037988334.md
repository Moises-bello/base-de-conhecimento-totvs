---
content_hash: 91a7e450f044fb0e7f6386b88a7bd6b1414121930e32865af1d428222f2f747b
fetched_at: '2026-06-28T21:35:17.276403+00:00'
page_id: '1037988334'
product: fluig
source: tdn-fluig
title: Iniciar um processo a partir de página publica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1037988334
version: 3
---

# Objetivo

---

Essa documentação tem por objetivo abranger todas as etapas isoladas que existem para iniciar uma solicitação no TOTVS Fluig via página pública utilizando widget, e API REST pública com codificação em Java.

## Contextualização

---

* Nesta documentação precisaremos criar uma widget personalizada, uma página pública e um processo básico.

## Criando um processo

---

01. Para criar um processo simples (início, atividade e fim) siga os passos da documentação [Plataforma | Editor de processos](https://tdn.totvs.com/pages/viewpage.action?pageId=860245005#Plataforma%E2%9D%99Editordeprocesso-Verdiagramadoprocesso) no **passo 01** do item **Ver diagrama do processo**.

## Criando uma widget

---

01. Baixe o **[exemplo](https://git.fluig.com/projects/SAMPLES/repos/exemplo-iniciar-processo-publico-com-widget-e-api-service/browse)** e siga as instruções contidas no arquivo **[README.md](http://README.md)**. Ao fazer isso, serão gerados dois artefatos iguais aos exemplificados abaixo, que precisarão ser adicionados na Central de componentes. Saiba mais detalhes sobre como adicionar um componente na central **[aqui](https://tdn.totvs.com/x/voL5DQ)**.

#f2f2f2#f2f2f2

Recomendamos a alteração dos arquivos abaixo conforme as instruções:

**[Activate.java](https://git.fluig.com/projects/SAMPLES/repos/exemplo-iniciar-processo-publico-com-widget-e-api-service/browse/api-start-public-process/api-rest-start-public-process/src/main/java/com/totvs.startpublicprocess/activate/oauth/Activate.java)**

* APP\_KEY = será o usuário que será criado.

#000000#f2f2f2

É possível conferir mais detalhes sobre o Activate [aqui](https://tdn.totvs.com/x/bS6QGg).

**[component.xml](https://git.fluig.com/projects/SAMPLES/repos/exemplo-iniciar-processo-publico-com-widget-e-api-service/browse/api-start-public-process/api-rest-start-public-process/src/main/resources/component.xml)**

* Informações relacionadas à título, descrições, versões, categorias e desenvolvedor.
#f2f2f2#f2f2f2

Recomendamos a alteração dos arquivos abaixo conforme a instrução:

**[startPublicProcess.js](https://git.fluig.com/projects/SAMPLES/repos/exemplo-iniciar-processo-publico-com-widget-e-api-service/browse/widget-start-public-process/src/main/webapp/resources/js/startPublicProcess.js):**

* tenantId = 1; código da empresa

* processId = 'private-process'; código do processo

* targetAssigneeUserCode = 'adm'; usuário que será o solicitante.

**[Aplication.info](https://git.fluig.com/projects/SAMPLES/repos/exemplo-iniciar-processo-publico-com-widget-e-api-service/browse/widget-start-public-process/src/main/resources/application.info)**

* Informações relacionadas à título, descrições, versões, categorias e desenvolvedor.

## Criando uma página pública

---

Após a criar o processo, é necessário criar uma página pública contendo um botão para iniciar uma solicitação. No **TOTVS Fluig**, há duas formas de criar uma página pública, sendo uma **NO-CODE** sem a necessidade de códigos, e uma segunda via codificação, sendo esta a forma que utilizaremos nesta documentação.

### Via interface da plataforma

---

* Para criar uma página no TOTVS Fluig, acesse o **Painel de controle**  agrupador **Personalização**  **Minhas páginas**.

Dica

Para mais detalhes e passo a passo sobre como criar uma página, acesse [Plataforma | Criar página](https://tdn.totvs.com/x/fYP5DQ) no **passo 08** do item Criar página.

### Via codificação

* Uma segunda forma seria a **via codificação**, sendo esta a forma que utilizaremos nesta documentação. Neste exemplo, usaremos a API REST para Processos, em específico: **POST - /v2/processes/{processId}/start**. Você pode conferir mais detalhes da API **[aqui](https://apps.fluig.io/process-management/swagger-ui/#/Processes/start)**.

## Adicionando a widget na página

---

**01.** A página será apresentada em modo de edição para incluir a widget que foi criada anteriormente pelo artefato.

**02.** Localize a widget na seção **Personalizado** no agrupador de widgets no lado esquerdo, e arraste-a para a área de construção ou clique sobre a mesma. No caso deste exemplo de uso utilizamos o nome: Iniciar solicitação de um processo público.

**03.** Após a inclusão da widget, clique em **Publicar**, insira uma breve descrição e clique em **Publicar página**.

**04.** Para acessar a página pública basta acessar a URL da sua empresa adicionando o identificador utilizado no momento da criação da página. Ficando como no exemplo: <FLUIG\_URL>/iniciar-processo-via-publica
