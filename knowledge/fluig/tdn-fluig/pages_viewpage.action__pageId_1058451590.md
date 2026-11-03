---
content_hash: 4fcce4cc9c12ed286b67bec7dffc51c223ccb926301258590bfc2512f2e65f59
fetched_at: '2026-06-28T21:35:17.406754+00:00'
page_id: '1058451590'
product: fluig
source: tdn-fluig
title: 'Integração Fluig x Protheus: Centro de custo'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058451590
version: 34
---

## Introdução

---

Este é um exemplo inicial e simplificado para fornecer a compreensão fundamental do conceito e da mecânica da integração entre o TOTVS Fluig e o TOTVS Protheus. Ao dominar este fluxo, você terá a base necessária para evoluir o conceito e personalizar essa lógica para atender a outros cenários de negócio. 

## Pré-requisitos

---

Antes de iniciar o desenvolvimento, verifique se o seu ambiente atende aos seguintes requisitos de acesso e versão:

* **Versão Mínima do Protheus:** Certifique-se de que o Protheus esteja na versão **12.1.21** ou superior. Você pode verificar isso abrindo o Protheus, acessando o SIGACFG e, em seguida, **Ajuda** > **Sobre**.
* **Acesso à API REST do Protheus:**

+ Obtenha a **URL base** do REST do Protheus (exemplo: http://[seu\_localhost]:[8084]/[rest]).
+ O endpoint específico para **Centro de Custo** é /api/ctb/v1/cost-center (disponível a partir do Protheus 12.1.21).
+ Consulte a documentação completa da API em: [api.totvs.com.br](https://api.totvs.com.br/apidetails/CostCenter_v1_000.json).

* **Credenciais de Acesso:** Você precisará de um **usuário e senha** válidos do Protheus com as permissões necessárias para acessar a API.

novo-usuariotrue1Validar versão API2Validar versão Protheus

## Passo 1: Cadastre o serviço REST no Fluig

---

O serviço REST centraliza as credenciais e a URL base da integração diretamente no painel do Fluig. Isso evita que você deixe senhas expostas no código e facilita a manutenção caso o endereço do ERP mude no futuro. É a fundação segura da nossa integração.

#f2f2f2#f2f2f2

Acesse a documentação de apoio: [Plataforma ❙ Serviços](https://tdn.totvs.com/pages/releaseview.action?pageId=243660796).

falsenovo-usuariotrue1Passo 1

* Acesse o Fluig com um usuário administrador.
2Passo 2

* Vá em **Painel de Controle** **➔** **Serviços** e clique em **Adicionar Novo Serviço**.
3Passo 3

* Selecione o tipo **REST**.
4Passo 4

* Preencha os campos exatamente assim:
  + **Nome do Serviço:** API\_PROTHEUS\_REST (Este é o ID que usaremos no código).
  + **Descrição:** API Protheus Rest.
  + **Domínio:** http://[seu\_localhost]:[8084]/[rest] (mude os [parâmetros] de acordo com seu ambiente).
  + **Autenticação:** Selecione **BASIC** e insira as credenciais do Protheus.
5Passo 5

* Em **URL para teste**, insira /api/ctb/v1/cost-center e salve.
6Passo 6

* Nas **Propriedades** da atividade **Integração**, vá na aba **Geral** e marque a Execução como **Automatizada**. Configure as tentativas

#f2f2f2#f2f2f2

exemplo

5 tentativas a cada 30 minutos).

6Passo 6

* Na lista de serviços, clique em **Testar**. O Fluig deve retornar o JSON com os centros de custo.

## Passo 2: Configure o projeto no eclipse

---

O Eclipse com o plugin do Fluig Studio é a nossa principal ferramenta de desenvolvimento. Precisamos conectar a IDE ao servidor do Fluig para criar e exportar os arquivos do projeto diretamente para o ambiente.

#f2f2f2#f2f2f2

Acesse a documentação de apoio: [Guia de instalação Fluig Studio](https://tdn.totvs.com/pages/releaseview.action?pageId=73078179).

falsenovo-usuariotrue1Passo 1

* No Eclipse, acesse **Window** **➔** **Open Perspective** **➔** **Other** **➔** **Fluig**.
2Passo 2

* Na aba **Fluig Servers**, clique com o botão direito e vá em **New** **➔** **Fluig Server**.
3Passo 3

* Após inserir os dados do servidor (host, porta, usuário e senha), efetue um clique duplo para confirmar o status como **Disponível**.
4Passo 4

* Crie o projeto: **File** **➔** **New** **➔** **Projeto Fluig** e nomeie como **fluig\_protheus**.

## Passo 3: Crie o dataset customizado (GET)

---

Datasets no Fluig são scripts escritos em JavaScript executados no backend que consultam dados (APIs, Web Services e entre outros...) e os padronizam em linhas e colunas. Vamos criar um para consumir o serviço REST do Protheus e buscar os centros de custo disponíveis. É esse dataset que alimentará a nossa interface depois.

#f2f2f2#f2f2f2

Acesse a documentação de apoio: [Desenvolvimento de Datasets](https://tdn.totvs.com/display/public/fluig/Desenvolvimento+de+Datasets).

falsenovo-usuariotrue1Passo 1

* No Eclipse, clique com o botão direito no projeto e selecione **New** **➔** **Dataset customizado Fluig**.
2Passo 2

* Nomeie como **ds\_get\_costcenter\_protheus**.
3Passo 3

* Escreva o script :

jsds\_get\_costcenter\_proteus.jstrue 0) {
            for (var i = 0; i < jsonResponse.items.length; i++) {
                var item = jsonResponse.items[i];                
                dataset.addRow(new Array(
                 item.InternalId,
                 item.CompanyInternalId,
                 item.CompanyId,
                 item.RegisterSituation,
                 item.Class,
                 item.Code,
                 item.Name
                ));
            }
        }
    } else {
        var errorMsg = "Erro desconhecido durante a integracao.";
        try {
            var parseResult = JSON.parse(vo.getResult());
            var parseError = JSON.parse(parseResult.errorMessage);
            errorMsg = parseError.detailedMessage;
        } catch (e) {
            errorMsg = vo.getResult();
        }
        
        dataset.addRow(new Array(
            status,
            errorMsg,
            "", "", "", "", ""
        ));
    }
  
    return dataset;
}
function onMobileSync(user) {}]]>4Passo 4

* Exporte para o servidor, para isso, clique com o botão direito no arquivo: **Export** **➔** **Exportar para servidor Fluig**.
5Passo 5

* Após, teste no Eclipse na aba **Visualização de Dataset**, digite **ds\_get\_costcenter\_protheus** e clique em **Finish**.

Dica

**Paginação:** Se a base for grande, adicione parâmetros de paginação (page, pageSize) no endpoint. Consulte este e outros parâmetros na documentação oficial da API do Protheus: [api.totvs.com.br](https://api.totvs.com.br/apidetails/CostCenter_v1_000.json)

**Dataset Offline:** Isso faz o Fluig salvar os dados do ERP no próprio Fluig, assim poupando o Protheus de requisições excessivas. Acesse a documentação: [Sincronização de datasets](https://tdn.totvs.com/pages/releaseview.action?pageId=212899013)

## Passo 4: Modele o processo BPMN

---

O diagrama BPMN desenha o fluxo de trabalho visualmente e orquestra a execução da integração no Fluig. Vamos usar uma **Atividade de Serviço** automatizada para fazer a comunicação com o ERP, e um **Evento de Erro** para desviar o processo caso a API do Protheus rejeite o envio. 

#f2f2f2#f2f2f2

Acesse as documentações de apoio:

* [Como criar um diagrama no fluig Studio](https://tdn.totvs.com/display/public/fluig/Como+criar+um+diagrama+no+fluig+Studio#1-4)
* [Configuração de Processos com Componentes Avançados (BPMN 2.0)](https://tdn.totvs.com/pages/releaseview.action?pageId=126714181)
falsenovo-usuariotrue1Passo 1

* No Eclipse, vá em **New** **➔** **Diagrama Fluig** e nomeie como **centro\_de\_custo**.
2Passo 2

* Renomeie a Pool para **Centro de Custo**.
3Passo 3

* Crie duas raias (Swimlanes): **Solicitante** e **TOTVS Protheus**.
4Passo 4

* Configure as atividades:
  + Arraste uma **Atividade de Serviço** para a raia do TOTVS Protheus e nomeie como **Integração**;
  + Arraste um **Evento Intermediário de Captura de Erro** (ícone de raio) para as bordas da atividade de Integração;
  + Crie uma atividade comum na raia do Solicitante chamada **Manutenção**;
  + Crie um componente Fim raia do TOTVS Protheus chamado **Fim**.
5Passo 5

* Ligue o fluxo:
  + **Início** ➔ **Integração**
  + **Captura de Erro** ➔ **Manutenção**
  + **Manutenção** ➔ **Integração**
  + **Integração** ➔ **Fim**
6Passo 6

* Nas **Propriedades** da atividade **Integração**, vá na aba **Geral** e marque a Execução como **Automatizada**.
7Passo 7

* Salve o diagrama.

## Passo 5: Crie o formulário com campo zoom

---

O formulário é a interface HTML onde o usuário vai interagir com os dados. Vamos utilizar um componente nativo do Fluig, que cria um campo de busca dinâmico consumindo o Dataset criado no **passo 3**. É a ponte visual entre o usuário e a tabela do Protheus.

#f2f2f2#f2f2f2

Acesse a documentação de apoio: [Formulários - Campo Pesquisa (zoom)](https://tdn.totvs.com/pages/releaseview.action?pageId=872686733)

falsenovo-usuariotrue1Passo 1

* Clique com o botão direito no projeto: **New** **➔** **Formulário**. Nomeie o arquivo como **form\_costcenter**.
2Passo 2

* Adicione os seguintes campos no HTML do formulário.

xmlform\_costcenter.htmltrue
    

### Dados do Centro de Custo (Protheus)

Centro de Custo

Codigo

Descricao

Classe
                            
                                Selecione...
                                1 - Sintetico
                                2 - Analitico

Centro de Custo Bloqueado?
                            
                                Selecione...
                                1 - Bloqueado
                                2 - Nao bloqueado
