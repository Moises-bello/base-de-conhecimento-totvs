---
content_hash: f0e4399d7fc28e7e5dc656ee6e6e17771aa6efd2b22b10ccad672f7defb8e5b8
fetched_at: '2026-06-28T21:35:17.494830+00:00'
page_id: '1072001314'
product: fluig
source: tdn-fluig
title: 'Integração Fluig x RM: Requisição de Alteração de dados Funcionais'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1072001314
version: 8
---

## Introdução

---

Esta documentação visa orientar a configuração e desenvolvimento da integração entre Fluig e RM, focando na automatização do processo de requisições de alteração de dados funcionais. Isso garante que modificações cadastrais no RM passem por um fluxo de aprovação estruturado no Fluig, incluindo validações, aprovação da liderança e rastreabilidade. O material aborda o fluxo funcional, configuração de ambientes, APIs REST/SOAP e boas práticas, servindo como referência técnica e operacional para equipes diversas na manutenção, evolução da solução e sua aplicabilidade à outras situações em que a integração se fizer necessária.

## Pré-requisitos

---

Para o correto funcionamento da integração entre Fluig e RM, é necessário que os ambientes estejam previamente configurados e atendam aos requisitos mínimos descritos abaixo.

### Requisitos do Ambiente RM:

* **Serviço RM.Host:** Deve estar ativo e configurado conforme a [documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17383402763287-RH-RM-FOP-Como-Habilitar-Webservice-via-RM-Host).
* **APIs no RM:** As APIs REST e SOAP precisam estar habilitadas no ambiente TOTVS RM conforme a [documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36972742937623-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebService-Integra%C3%A7%C3%A3o-RM-com-aplicativos-terceiros).
* **Comunicação de Rede:** O firewall deve permitir a comunicação entre o servidor Fluig e o servidor RM.
* **Usuário:** Necessidade de um usuário configurado para a integração e com permissão nos módulos a serem utilizados.

### Requisitos do Ambiente Fluig:

* **Gestão de Acessos:** O usuário deve possuir as permissões necessárias no Painel de Controle para realizar ajustes técnicos no ambiente.
* **APIs REST/SOAP:** Habilitação do acesso e consumo de APIs externas (do RM) via Fluig. Recomenda-se utilizar ferramentas como o Postman para a validação dos endpoints.
* **Desenvolvimento:** Acesso ao ambiente com o [Fluig Studio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27663340938519-Fluig-Plataforma-DES-Como-realizar-a-configura%C3%A7%C3%A3o-inicial-do-Fluig-Studio-para-come%C3%A7ar-a-criar-projetos) devidamente configurado para desenvolvimento do processo.

## Passo 1: Cadastre os serviços no servidor fluig

---

A utilização do cadastro de serviços no Fluig possibilita a centralização das credenciais e da URL base de integração diretamente no Painel de controle. Esta configuração mitiga o risco de exposição de senhas no código-fonte e simplifica processos de manutenção decorrentes de eventuais alterações no endereço do ERP. Além de constituir a base de segurança da integração, essa prática otimiza a gestão de atualizações de usuários e senhas, eliminando a necessidade de intervenções diretas em linha de código.

#f2f2f2#f2f2f2

Acesse a documentação de apoio: [Plataforma ❙ Serviços](https://tdn.totvs.com/pages/releaseview.action?pageId=243660796).

É necessário informar os dados da conexão com o RM do seu ambiente.

falsesamplePasso 1

* Acesse o Fluig com usuário **Administrador**;
Passo 2

* Selecione o tipo de serviço **Rest**;
Passo 3

* Preencha os campos conforme seu ambiente:
  + **Nome:** Será utilizado também nas chamadas no código.
  + **Descrição:** Para facilitar a identificação do serviço
  + **Domínio:** Endereço da url no RM
  + **Tipo de autenticação:**Neste exemplo utilizamos a Basic.

Dica: Tipos de autenticação

Acesse a documentação de apoio para entender sobre os tipos de autenticação:

Passo 2: Configure o projeto no eclipse

---

Para o desenvolvimento, utilizamos como ferramenta base o **Eclipse 2019-09R**, integrado ao plugin Fluig Studio em versão compatível com a do servidor. A configuração do ambiente deve seguir estas diretrizes:

#f2f2f2#f2f2f2

Acesse a documentação de apoio: [Guia de instalação Fluig Studio](https://tdn.totvs.com/pages/releaseview.action?pageId=73078179).

falsesamplePasso 1

* Instale o plugin do Fluig studio em **Help ➔ Install New Sotfware**.

Passo 2

* Abra a perspectiva do Fluig em **Window ➔ Perspective ➔** **Open Perspective ➔ Other ➔** **Fluig**.

Passo 3

* Crie o Servidor e insira os dados conforme seu ambiente:

Passo 3: Elabore o formulário e vincule ao processo 

---

Para garantir a eficácia da integração, é muito importante o preenchimento dos campos obrigatórios do RM no formulário. Adicionalmente, estruturaremos o processo BPM utilizando SwingLines para acomodar os níveis de aprovação requeridos; neste cenário prático, configuraremos um nível além da etapa do RH.

#f2f2f2#f2f2f2

Acesse as documentações de apoio:

* [Como criar um diagrama no fluig Studio](https://tdn.totvs.com/display/public/fluig/Como+criar+um+diagrama+no+fluig+Studio#1-4)
* [Configuração de Processos com Componentes Avançados (BPMN 2.0)](https://tdn.totvs.com/pages/releaseview.action?pageId=126714181)
falsesamplePasso 1

* Crie um novo Formulário em **New ➔ Formulário**.

Passo 2

* Crie um novo processo em **New ➔ Diagrama Fluig**.

Passo 3

* Construa o diagrama conforme a imagem abaixo:

Passo 3

* Insira os campos no formulário:

js1form\_altera\_dados\_funcionaistrue


### Alteração de Dados Funcionais

[#### Identificação](#panelIdentificacao)

Requisitante:

Funcionário:

Previsão:

Justificativa:

[#### Dados Atuais do Funcionário](#panelDadosFunc)

Função de Origem:

Hierarquia Origem:

##### Tabela Salarial

Nivel Salarial de Origem:

Faixa Salarial de Origem:

Salario de Origem:

[#### Proposta de Alteração](#panelPropAlt)

Função Proposta:

Hierarquia Destino:

Nivel

Faixa

Percentual

Salario

Gerar Substituição

Motivo de Mudança de Função:

Motivo de Mudança de Salario:
