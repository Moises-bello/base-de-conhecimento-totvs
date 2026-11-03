---
content_hash: 86002a16f242a8e02b94c394c89e6620d223b1f7a0794ba6b79b9c3f3282bfea
fetched_at: '2026-06-29T00:05:51.670589+00:00'
page_id: '1052750469'
product: rm
source: tdn-rm
title: 2.9 - Cypress
type: documentation
url: https://tdn.totvs.com/display/LRM/2.9+-+Cypress
version: 79
---

## O que é?

Uma Atividade Cypress permite executar testes automatizados diretamente na interface web de uma aplicação, simulando as ações de um usuário real — como clicar em botões, preencher formulários, navegar entre páginas e validar se as informações estão sendo exibidas e validadas corretamente.  
Ao executar uma atividade Cypress, o sistema instala automaticamente as dependências necessárias do projeto (como Cypress e o reporter de relatórios), executa os testes no navegador escolhido e gera um relatório detalhado com os resultados, indicando quais testes passaram e quais falharam.

Antes de utilizar a atividade Cypress, é necessário que o Agent de execução já possua o Node.js e o npm instalados. O sistema não instala esses componentes, apenas verifica se estão disponíveis. Caso não estejam, a atividade falhará. Para mais detalhes, consulte a seção Preparação do ambiente Cypress.

## Para que serve?

* Serve para automatizar/orquestrar a execução de testes de interface web (E2E) de forma simples e integrada ao TAT
* Executar suítes de testes Cypress em diferentes navegadores (Chrome, Firefox, Edge, Electron).
* Filtrar e organizar os arquivos de teste específicos (spec files) para execução. Passar variáveis de ambiente customizadas para os testes.
* Obter relatórios detalhados de sucesso e falha com categorização automática dos erros.
* Utilizar variáveis de ambiente do TOTVS Automação de Testes dentro dos parâmetros da atividade (substituição dinâmica com {variavel}).
* Integrar a atividade em Projetos de Teste, combinando-a com outras atividades em um fluxo sequencial.

Antes de executar qualquer teste na atividade Cypress do TOTVS Automação de Testes, valide se o seu teste Cypress está funcionando corretamente fora da Sistema.

## Exemplo de Uso

Como cadastrarPrepraração do ambiente Cypress Usuário PaaS

 Como o TAT é executado em um ambiente gerenciado em nuvem (PaaS), **você não precisa instalar ou configurar nada no servidor**. A plataforma já entrega o Node.js, npm, Git e os navegadores prontos para uso a cada execução. Sua única responsabilidade é garantir que seu código (os testes) e o arquivo `package.json` estejam corretos no repositório Git.

1. Responsabilidade do Usuário (Preparação Manual)

## 1. Responsabilidade do Usuário (Preparação Manual)

Antes da primeira execução, é obrigatório garantir que os seguintes componentes estejam instalados e acessíveis no **PATH** do sistema operacional do Agent.

| Componente | Obrigatório | Como verificar | Observação |
| --- | --- | --- | --- |
| Node.js | Sim | `node --version` | Runtime necessário para execução do Cypress. Recomenda-se versão LTS (v18+ ou v20+) |
| npm | Sim | `npm --version` | Gerenciador de pacotes do Node.js (instalado junto com o Node.js) |
| Git | Condicional | `git --version` | Necessário apenas quando a fonte do projeto for um repositório Git |
| Navegador | Condicional | — | Chrome, Firefox ou Edge devem estar instalados. Electron já vem com o |

O sistema não realiza a instalação desses componentes. Ele apenas verifica se estão disponíveis.  
Caso alguma verificação falhe, a atividade será encerrada com erro e nenhuma etapa seguinte será executada.  
Informações complementares sobre a instalação do Cypress também podem ser obtidas através do [site oficial](https://www.cypress.io/install).2. Responsabilidade do Sistema (Preparação Automática)

## 2. Responsabilidade do Sistema (Preparação Automática)

A cada execução da atividade Cypress, o sistema realiza automaticamente a preparação do ambiente dentro do diretório do projeto.

### Etapas executadas automaticamente pelo executor de atividades Cypress do TOTVS Automação de Testes (TAT):

| Ordem | Etapa | Comando | Descrição |
| --- | --- | --- | --- |
| 1 | Verificação do Node.js | `node --version` | Valida se o Node.js está acessível (não realiza instalação) |
| 2 | Verificação do npm | `npm --version` | Valida se o npm está acessível (não realiza instalação) |
| 3 | Instalação das dependências | `npm install` | Instala os pacotes definidos no `package.json` |
| 4 | Instalação do Cypress | `npm install cypress` | Garante que o Cypress esteja disponível no projeto |
| 5 | Execução dos testes | `npx cypress runz` | Executa os testes automatizados |

3. Observação de Performance

## 3. Observação de Performance

Na primeira execução, o processo pode levar mais tempo devido ao download completo das dependências.

Nas execuções seguintes:

* O `npm` reutiliza o diretório `node_modules`
* As instalações são ignoradas quando os pacotes já existem
* O tempo de execução é significativamente reduzido
4. Estrutura do Diretório do Projeto

## 4. Estrutura do Diretório do Projeto

As dependências são instaladas no diretório do projeto Cypress (e não no Agent):

```

```

5. Fluxo de Execução

## 5. Fluxo de Execução

A execução é sequencial e bloqueante. Se qualquer etapa falhar, o processo é interrompido.

6. Visão Geral de Responsabilidades

## 6. Visão Geral de Responsabilidades

| Ação | Responsável | Local de execução | Quando ocorre |
| --- | --- | --- | --- |
| Instalar Node.js e npm | Usuário | Agent (PATH do sistema) | Antes da primeira execução |
| Instalar Git (Opcional) | Usuário | Agent (PATH do sistema) | Antes da execução (se aplicável) |
| Instalar navegador (A escolha) | Usuário | Agent | Antes da execução |
| Criar Teste `package.json` | Usuário | Projeto Cypress | Na criação do projeto de testes |
| Verificar Node.js e npm | Sistema | — | A cada execução |
| Instalar dependências | Sistema | `node_modules` do projeto | A cada execução |
| Instalar Cypress | Sistema | Projeto | A cada execução |

7. Solução de Problemas

## 7. Solução de Problemas

| Erro | Causa | Solução |
| --- | --- | --- |
| `node: command not found` | Node.js não instalado ou fora do PATH | Instalar Node.js e reiniciar o Agent |
| `npm: command not found` | npm não acessível | Reinstalar Node.js e reiniciar o Agent |
| `npm ERR! failed to install` | Falha na instalação de dependências | Verificar internet, permissões e `package.json` |
| Git não encontrado | Git não instalado | Instalar Git e reiniciar o Agent |
| `fatal: repository not found` | URL incorreta ou falta de permissão | Validar URL, branch e permissões (PAT) |
| Falha ao abrir navegador no Cypress | Navegador não instalado | Instalar o navegador configurado (Chrome, Edge ou Firefox) no Agent de execução ou utilizar o Electron, que já vem embutido no Cypress |

Informações complementares sobre a instalação do Cypress também podem ser obtidas através do [site oficial](https://www.cypress.io/install).

Como Cadastrar 1. Navegação para o cadastro

1.   Navegue no menu do TOTVS Automação de Testes e clique em: Atividades → Web → Cypress.  
2.   Na tabela que será mostrada, clique no botão verde em destaque para iniciar o cadastro.

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Origem do Repositório

Define a origem do projeto Cypress que será utilizado na execução dos testes. Este campo determina como o sistema acessa o código-fonte.

| Opção | Descrição |
| --- | --- |
| **Local** | Utiliza um diretório já existente no Agent de execução. O projeto Cypress deve estar previamente disponível no caminho informado. Indicado para **desenvolvimento local**, testes rápidos ou cenários onde o código já está disponível no servidor. |
| **Git** | Realiza a clonagem automática do repositório antes de cada execução. O código-fonte é obtido diretamente de um repositório remoto. Indicado para **integração contínua, versionamento** e cenários com atualizações frequentes no código. |

Caminho Local

Define o caminho absoluto do diretório onde o projeto Cypress está localizado no Agent de execução.

* Campo **obrigatório** quando a origem for **Local**
* Campo **ignorado** quando a origem for **Git**

**Regras de validação (para o caminho Local):**

* Deve ser um caminho absoluto válido (Windows ou Linux)
* Não pode ser nulo, vazio ou conter apenas espaços
* Não pode conter caracteres inválidos do sistema operacional (ex.: `*`, `|`)

**Exemplos válidos:**

| Sistema | Exemplo |
| --- | --- |
| Windows | `C:\cypress-tests` |
| Windows | `D:\projetos\meu-projeto-cypress` |

Configuração para Fonte Git

### Configuração para Fonte Git

Ao utilizar a origem **Git**, deve-se informar uma credencial contendo os dados de acesso ao repositório.

* Para saber como selecionar uma credencial, consulte a documentação sobre [Credenciais de Repositório Git](https://tdn.totvs.com/pages/viewpage.action?pageId=1065229898)**.**

| Campo | Descrição | Exemplo |
| --- | --- | --- |
| **Repository URL** | URL completa do repositório (protocolo HTTPS). | `https://dev.azure.com/org/projeto/_git/repo-cypress` |
| **Branch** | Nome da branch a ser utilizada. | `main`, `develop`, `staging` |
| **Personal Access Token (PAT)** | Token de autenticação com permissão de leitura no repositório. | PAT do Azure DevOps ou GitHub |

1. Selecione o repistório de origem.
2. Selecione a Credencial Git.
3. Clique em "TESTAR" para testar a conexão da sua credencial GIt.

Ao selecionar a opção **Git**, é obrigatório vincular uma **Credencial de Repositório Git** à atividade.

O sistema também valida se o Git está instalado no Agent de execução. Caso não esteja disponível, a execução será interrompida com erro.

O Personal Access Token (PAT) é utilizado exclusivamente no processo de clonagem e não é exibido nos logs, garantindo a proteção das credenciais. Para entender como selecionar e gerenciar esse recurso, consulte a documentação de [Credenciais de Repositório Git.](https://tdn.totvs.com/pages/viewpage.action?pageId=1065229898)

Filtro de Arquivos de Teste (Spec Files)

### Filtro de Arquivos de Teste (Spec Files)

Permite definir quais arquivos de teste serão executados.  
Caso não informado, todos os testes configurados no `cypress.config.js` serão considerados.

Os filtros são enviados via parâmetro `--spec` e aceitam múltiplos valores separados por vírgula.

Extensões suportadas

### Extensões suportadas

| Extensão | Exemplo |
| --- | --- |
| `.js` | `cypress/e2e/login.js` |
| `.jsx` | `cypress/e2e/login.jsx` |
| `.ts` | `cypress/e2e/login.ts` |
| `.tsx` | `cypress/e2e/login.tsx` |
| `.mjs` | `cypress/e2e/login.mjs` |
| `.cjs` | `cypress/e2e/login.cjs` |
| `.cy.js` | `cypress/e2e/login.cy.js` |
| `.cy.ts` | `cypress/e2e/login.cy.ts` |
| `.spec.js` | `cypress/e2e/login.spec.js` |
| `.spec.ts` | `cypress/e2e/login.spec.ts` |

**Exemplos válidos:**

* `cypress/e2e/login.cy.js`
* `cypress/e2e/login.cy.js,cypress/e2e/cadastro.cy.js`
* `cypress/e2e/**/*.cy.ts`
Navegador

### Navegador

Define o navegador utilizado na execução dos testes. O valor selecionado é repassado ao Cypress via parâmetro `--browser`.

| Navegador | Valor | Requer instalação | Observação |
| --- | --- | --- | --- |
| **Chrome** | `chrome` | Sim | Recomendado para testes E2E |
| **Firefox** | `firefox` | Sim | Utilizado para testes de compatibilidade |
| **Edge** | `edge` | Sim | Pré-instalado no Windows 10+ |
| **Electron** | `electron` | Não | Embutido no Cypress, ideal para execução headless |

Em ambientes sem interface gráfica, utilize o **Electron** ou execução em modo headless.Execução Visual (Headed)

### Execução Visual

Define se a execução dos testes será realizada com interface gráfica.

| Estado | Argumento | Comportamento |
| --- | --- | --- |
| **Habilitado** | `--headed` | Executa com navegador visível. Indicado para **depuração** |
| **Desabilitado** | — | Executa em modo headless. Indicado para **automação em servidores** |

O modo visual requer ambiente com interface gráfica disponível.Parametros customizaveis

### Parâmetros Customizados

Em cenários onde é necessário realizar autenticação na aplicação por exemplo, recomenda-se **não informar credenciais diretamente na atividade**.

Utilize variáveis do **Ambiente de Execução** para proteger dados sensíveis e facilitar a reutilização entre ambientes. Exemplo de Configuração

| Chave | Valor configurado | Descrição |
| --- | --- | --- |
| `USUARIO` | `{loginUsuario}` | Usuário obtido dinamicamente do ambiente |
| `SENHA` | `{}` | Senha protegida, não exposta na atividade |
| `EMPRESA` | `{codigoEmpresa}` | Identificador da empresa (tenant) |

Restrições

* A **Chave é obrigatória**
* Não é permitido utilizar **chaves duplicadas**  
  (ex.: `BASE_URL` e `base_url` são consideradas iguais)
* Alguns nomes são **reservados pelo Cypress** e não podem ser utilizados  
  (ex.: `--browser`, `--spec`, `--record`, entre outros)
* O sistema exibirá uma mensagem caso algum parâmetro seja inválido
Exemplo Prático Exemplo Prático - Login Fluig

## Exemplo Prático -  Login no Fluig

Considere um cenário em que um analista de testes precisa validar o fluxo de **login do portal Fluig** após uma atualização de versão.  
O objetivo é garantir que usuários válidos consigam acessar o sistema e que validações de autenticação funcionem corretamente.

## Preparação do Ambiente

Antes da execução, o ambiente deve estar devidamente configurado:

* Portal Fluig acessível
* Agent do TOTVS Automação de Testes em execução
* Node.js e npm instalados no Agent

### Configuração da Atividade

| Campo | Valor | Descrição |
| --- | --- | --- |
| **Nome** | `Cypress - Login Fluig` | Identificação da atividade |
| **Versão** | `1.0.0` | Versão compatível com o cenário |
| **Origem do Repositório** | `Local` | Utiliza projeto disponível no Agent |
| **Caminho Local** | `C:\fluig\cypress-tests` | Diretório do projeto Cypress |
| **Navegador** | `Chrome` | Navegador utilizado na execução |
| **Execução Visual** | `Desabilitado` | Execução em modo headless |
| **Filtro de Arquivos de Teste** | `cypress/e2e/login.cy.ts` | Executa apenas os testes de login |

### Parâmetros Customizados

| Chave | Valor | Descrição |
| --- | --- | --- |
| `BASE_URL` | `http://{fluigexemplohost}:8080/portal` | URL do portal definida pelo ambiente |
| `USUARIO` | `{fluigUsuario}` | Usuário obtido do ambiente |
| `SENHA` | `{fluigSenha}` | Senha protegida |

As credenciais não devem ser informadas diretamente na atividade.  
Utilize variáveis do Ambiente de Execução para garantir segurança e evitar exposição nos logs.

### Ambiente de Execução

As variáveis utilizadas devem estar previamente configuradas no ambiente vinculado à atividade:

| Variável | Valor |
| --- | --- |
| `fluigHost` | <http://fluig-exemplo.local:8080/portal/home> |
| `fluigUsuario` | `EXEMPLO` |
| `fluigSenha` | `EXEMPLO@Flu1g` |

### Exemplo do códico Cypress Utilizado:

 {
beforeEach(() => {
// Ignorar erros de cross-origin e widgets Fluig (esperados)
cy.on('uncaught:exception', (e) => {
if (
e.message.includes('cross-origin') ||
e.message.includes('utilities') ||
e.message.includes('Blocked a frame') ||
e.message.includes('Rendering of widgets')
) {
return false
}
})
})
it('deve realizar o login com credenciais válidas e validar a página inicial', () => {
// ── Configuração das Variáveis ───────────────────────────────────────────
const fluigHost = 'http://fluig-exemplo.local:8080/portal/home'
const fluigUsuario = 'EXEMPLO'
const fluigSenha = 'EXEMPLO@Flu1g'
// Montagem da URL baseando-se no padrão anterior do Fluig
const urlLogin = `http://${fluigHost}:8080/portal/home`
// ── 1. Acesso à tela de Login ────────────────────────────────────────────
cy.visit(urlLogin)
cy.title().should('eq', 'Login')
// ── 2. Preenchimento de Credenciais e Autenticação ───────────────────────
cy.get('#username').should('be.visible').type(fluigUsuario)
cy.get('#password').should('be.visible').type(fluigSenha, { log: false }) // log: false oculta a senha no Cypress runner
cy.get('#submitLogin').click()
// ── 3. Validação do Sucesso no Login ─────────────────────────────────────
cy.title().should('eq', 'TOTVS Fluig Plataforma - Home')
cy.url().should('include', '/portal/p/')
})
})]]>

### Execução da Atividade

Ao executar a atividade, o sistema realiza:

1. Acesso ao diretório local configurado
2. Preparação do ambiente de execução
3. Substituição das variáveis `{fluigHost}`, `{fluigUsuario}` e `{fluigSenha}`
4. Execução do arquivo de teste configurado
5. Geração do relatório de execução

### Resultado da Execução

* Login com usuário válido — **Sucesso**
* Validação de credenciais inválidas — **Sucesso**

> **Resumo:** 0 falhas em 2 testes executados

### Análise

O resultado confirma que o fluxo de **login do Fluig** está funcionando corretamente após a atualização, permitindo avançar para a validação de outros cenários do sistema.

---

## Experiência do Usuário 📖:

* [Guia de Experiência - Atividade Cypress no TOTVS Automação de Testes](https://tdn.totvs.com/pages/viewpage.action?pageId=1068171448)
* [Origem do Repositório - Estratégias de Armazenamento do usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=1067056872)
* [Entendendo os Resultados e Corrigindo Erros](https://tdn.totvs.com/display/LRM/Entendendo+os+Resultados+e+Corrigindo+Erros)

---

# Saiba mais

Planeje os Filtros de Arquivos de Teste de forma organizada, agrupando testes por módulo ou funcionalidade. Isso permite executar apenas os testes relevantes para cada cenário, reduzindo o tempo de execução e facilitando a identificação de falhas.

Utilize variáveis de ambiente nos Parâmetros Customizados para tornar a atividade reutilizável entre diferentes ambientes (desenvolvimento, homologação, produção) sem necessidade de duplicar a atividade.

Configure o navegador adequado para o cenário de teste. Chrome é o mais utilizado e recomendado, mas Electron oferece melhor performance em modo headless e não requer instalação adicional no Agent.

Ao utilizar a fonte Git, certifique-se de que o Personal Access Token possui permissões de leitura no repositório e que a branch informada existe. Isso garante que o sistema consiga clonar o repositório sem erros. Clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=1065229898) e saiba mais sobre as **Credenciais de Repositório Git**.

Mantenha o package.json do projeto Cypress sempre atualizado com as dependências necessárias. Isso evita falhas na etapa de instalação automática de dependências.

Mantenha o package.json do projeto Cypress sempre atualizado com as dependências necessárias. Isso evita falhas na etapa de instalação automática de dependências.

# FAQ

**P:** Posso executar testes Cypress em qualquer navegador?

**R:** A atividade suporta Chrome, Firefox, Edge e Electron. O navegador escolhido deve estar instalado no Agent de execução, exceto o Electron, que já vem embutido no Cypress.

**P:** Preciso instalar o Cypress manualmente no Agent?

**R:** Não. O sistema instala o Cypress automaticamente no diretório do projeto a cada execução. O que você precisa instalar manualmente é o Node.js e o npm — o Cypress e suas dependências são responsabilidade do sistema.

**P:** Qual a diferença entre usar fonte Local e Git?

**R:** A fonte Local utiliza um diretório já existente no Agent — ideal para desenvolvimento e testes rápidos. A fonte Git clona o repositório automaticamente antes de cada execução — ideal para integração contínua e ambientes onde o código pode mudar entre execuções.

**P:** Posso executar apenas alguns testes específicos?

**R:** Sim! Utilize o campo Filtro de Arquivos de Teste para definir quais arquivos serão executados. Você pode informar caminhos específicos como cypress/e2e/[login.cy](http://login.cy).ts ou utilizar padrões como cypress/e2e/rh/\*\*/\*.cy.ts para executar todos os testes de um módulo.

**P:** Como passo informações sensíveis (senhas, tokens) para os testes?

**R:** Utilize variáveis de ambiente nos Parâmetros Customizados. Em vez de colocar a senha diretamente, use a sintaxe {variavel} (ex.: {senhaAdmin}). O valor real será obtido do Ambiente de Execução vinculado à atividade, sem expor dados sensíveis na configuração.

**P:** O que acontece se o Node.js não estiver instalado no Agent?

**R:** A atividade falhará na etapa de preparação com uma mensagem indicando que a verificação do Node.js falhou. O sistema não instala o Node.js — apenas verifica se ele está disponível. Certifique-se de que Node.js e npm estejam instalados e acessíveis no Agent antes da primeira execução.

**P:** A primeira execução demora mais que as seguintes?

**R:** Sim. Na primeira execução, o sistema precisa baixar todas as dependências do projeto (incluindo o Cypress). Nas execuções seguintes, o npm detecta que os pacotes já existem e pula a instalação, tornando o processo mais rápido.
