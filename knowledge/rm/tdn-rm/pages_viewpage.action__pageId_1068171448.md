---
content_hash: acfa1cc077f38b04faf54b5b63a58446f8180f8d23219acc42a7d75f6f422ca2
fetched_at: '2026-06-29T00:05:53.187081+00:00'
page_id: '1068171448'
product: rm
source: tdn-rm
title: Guia de Experiência - Atividade Cypress no TOTVS Automação de Testes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068171448
version: 66
---

## Para quem é este guia?

## Este documento orienta quatro perfis diferentes de usuários na configuração da Atividade Cypress dentro do TOTVS Automação de Testes (TAT). Independentemente do seu ponto de partida — seja criando seus primeiros testes, integrando um repositório existente, gravando fluxos sem escrever código ou atuando em um ambiente gerenciado sem acesso ao servidor — as seções abaixo têm um caminho traçado para você.

solid#21cafc1dashedSumário de Navegação por Perfil

### Escolha sua jornada:

| Quero... | Meu perfil | Vá para | |
| --- | --- | --- | --- |
| Criar meus primeiros testes e configurar tudo agora | **Do Zero** | .\*Do Zero - Meus Primeiros Testes Cypressnonefalse | |
| Integrar um repositório Git já existente | **Especialista** | .\*Especialista - Repositório Git e Page Object Modelnonefalse | |
| Gravar testes sem escrever código | **Não Técnico** | .\*Não Técnico - Gravação com Cypress Studiononefalse | |
| Usar o TAT como serviço, sem acesso ao servidor | **PaaS** | .\*PaaS - Sem Acesso ao Servidornonefalse | |
| Consultar todos os campos da tela | **Qualquer perfil** | .\*Referência Completa dos Campos da Interfacenonefalse | |
| Entender o que escolher (Studio vs POM) | **Qualquer perfil** | .\*Cypress Studio vs Page Object Model - Como criar testes?nonefalse | |
| Criar um Token de Acesso Pessoal (PAT) no Git | **Qualquer perfil** | .\*Como Criar um Token de Acesso Pessoal (PAT) no Git.\*Para quem é este guia? Este documento orienta quatro perfis diferentes de usuários na configuração da Atividade Cypress dentro do TOTVS Automação de Testes (TAT). Independentemente do seu ponto de partida — seja criando seus primeiros testes, integrando um repositório existente, gravando fluxos sem escrever código ou atuando em um ambiente gerenciado sem acesso ao servidor — as seções abaixo têm um caminho traçado para você. Escolha sua jornada: Perfil: Do Zero - Meus Primeiros Testes Cypress Passo 1 - Prepare o ambiente de testes no servidor Passo 2 - Crie um arquivo de teste simples Passo 3 - Configure a Atividade no TAT Perfil: Especialista - Repositório Git e Page Object Model Por que usar Git como origem? Passo 1 - Cadastre a Credencial Git no TOTVS Automação Passo 2 - Configure a Atividade no Totvs Automação Page Object Model - A Estrutura Recomendada Estrutura sugerida de repositório: Dica sobre o Filtro de Arquivos de Teste Perfil: Não Técnico - Gravação com Cypress Studio O que é o Cypress Studio? Passo 3 - Configure no TAT usando Caminho Local Limitações do Studio para o Longo Prazo Perfil: PaaS - Sem Acesso ao Servidor Passo 1 - Crie os testes na sua máquina Passo 2 - Publique os testes em um repositório Git Passo 3 - Crie um Token de Acesso (PAT) na plataforma Git Passo 4 - Cadastre a Credencial Git no TAT Passo 5 - Configure a Atividade Cypress no TAT Como Criar um Token de Acesso Pessoal (PAT) no Git O que o TOTVS Automação de Testes (TAT) faz automaticamente para você Referência Completa dos Campos da Interface Campos de Cabeçalho (comuns a todas as atividades) Campos de Configuração Cypress Campos de Variáveis de Ambiente (Parâmetros Customizados) Cypress Studio vs Page Object Model - Como criar testes? Veja também:nonefalse | |

solid#21cafc1dashedAntes de Começar - Pré-Requisitos no Servidor de Execução

O servidor onde os testes serão executados (o **agente de execução**) precisa ter os componentes abaixo instalados antes da primeira execução. Esses componentes **não são instalados pelo TAT** — é responsabilidade da equipe que configura o servidor garantir que estejam disponíveis.

| Componente | Instalado pelo TAT? | Observação |
| --- | --- | --- |
| Node.js | Não | Deve estar instalado e acessível no servidor. Sem ele, a atividade falha imediatamente. |
| npm | Não | Normalmente incluído junto com o Node.js. |
| Git | Não | Obrigatório quando a origem do repositório for `Git`. O TAT executa o clone via Git — se não estiver instalado, a clonagem falhará. |
| Cypress | Sim | Instalado automaticamente pelo TAT no diretório do projeto a cada execução. |

Clientes PaaS: se você utiliza o TAT como serviço gerenciado, esses pré-requisitos já estão garantidos pela equipe de infraestrutura responsável pelo ambiente. Você não precisa se preocupar com esta seção.

A primeira execução poderá ser mais lenta que as seguintes, pois o sistema baixa o Cypress e as dependências do projeto. Nas execuções sequênciais, esse passo é ignorado automaticamente.  
  
Informações complementares sobre a instalação do Cypress também podem ser obtidas através do [site oficial](https://www.cypress.io/install).

solid#21cafc1dashed1. Criando seus Primeiros Testes

## Perfil: Do Zero - Meus Primeiros Testes Cypress

Este perfil é para você se**:** ainda não tem um repositório ou estrutura de testes e quer começar a validar fluxos de interface o mais rápido possível.

### Passo 1 - Prepare o ambiente de testes no servidor

No servidor de execução (o agente do TOTVS Automação), abra um terminal e execute:

```

```

powershell

```

```

> O comando `npx cypress open` cria automaticamente a estrutura de pastas sugerida pelo Cypress na primeira execução, incluindo a pasta `cypress/e2e/` onde seus arquivos de teste ficarão.

Após este passo, você terá em mãos um **caminho de pasta,** anote-o. É ele que será informado no TOTVS Automação.

### Passo 2 - Crie um arquivo de teste simples

 {
it('abre a página inicial', () => {
cy.visit('https://meusite.com')
cy.contains('Bem-vindo')
})
})]]>
> Não precisa dominar a sintaxe agora. O objetivo é ter algo funcional para validar o fluxo completo no TOTVS Automação, Porém, quando quiser expandir seus cenários e entender o que cada comando faz, recomendamos a leitura do guia oficial: [Escrevendo seu primeiro teste no Cypress](https://docs.cypress.io/app/end-to-end-testing/writing-your-first-end-to-end-test)

### Passo 3 - Configure a Atividade no TAT

No TAT, ao criar a Atividade Cypress, preencha da seguinte forma:

| Campo | O que informar |
| --- | --- |
| **Origem do repositório** | `Local` |
| **Caminho local** | Caminho absoluto da pasta raiz do projeto Cypress (ex.: `C:\projetos\meus-testes` ou `/home/usuario/meus-testes`) |
| **Navegador** | `Electron` — é a opção mais simples, já vem embutida no Cypress, sem instalação extra |
| **Execução visual** | Desativado (execução em segundo plano) — ative só se precisar ver o navegador abrir |
| **Filtro de arquivos de teste** | Deixe em branco para executar todos, ou informe `cypress/e2e/**/*.cy.ts` para padronizar |

Dica para CrescerComeçar com `Local` é válido para desenvolvimento e testes rápidos. Quando seus testes estiverem estáveis e você quiser integrá-los a um processo automatizado, migrar para o perfil **Especialista** com `Git` é o próximo passo natural — sem perder nenhuma configuração do TAT, só troca a origem.solid#21cafc1dashed2. Estruturando Testes com Git e POM

## Perfil: Especialista - Repositório Git e Page Object Model

Este perfil é para você se**:** já tem um repositório de testes estruturado (ou quer criar um com boas práticas) e precisa que o TOTVS Automação busque os scripts diretamente do Git a cada execução.

## Por que usar Git como origem?

Quando a origem é `Git`, o TOTVS Automação clona o repositório automaticamente antes de cada execução, garantindo que a versão mais atual dos testes seja sempre a que roda. Isso elimina a necessidade de copiar arquivos manualmente para o servidor.

| Vantagem | Descrição |
| --- | --- |
| Sempre atualizado | Cada execução parte do estado atual da branch configurada |
| Rastreabilidade | Todo teste tem histórico de alterações no repositório |
| Trabalho em equipe | Vários analistas colaboram no mesmo conjunto de testes |

## Passo 1 - Cadastre a Credencial Git no TOTVS Automação

Antes de configurar a atividade, você precisa registrar as informações de acesso ao repositório. Acesse **Credenciais → Nova Credencial → Repositório Git** e preencha:

| Campo | O que informar |
| --- | --- |
| **Nome de exibição** | Um nome descritivo, como "Git - Testes de Regressão QA" |
| **URL do repositório** | Endereço HTTPS do repositório (ex.: `https://github.com/empresa/testes-cypress.git`) |
| **Branch** | Nome da branch de trabalho (ex.: `main`, `develop`, `homologacao`) |
| **Token de acesso pessoal (PAT)** | Token gerado na plataforma Git com permissão de leitura ao repositório |

> O token (PAT) é gerado nas configurações da sua conta no GitHub, GitLab, Gitea ou similar (consulte a documentação oficial do [GitHub](https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) ou do [GitLab](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)  para o passo a passo exato). Quando o token expirar, basta atualizá-lo na credencial, todas as atividades que a referenciam passarão a usar o novo valor automaticamente. Para um guia detalhado sobre o cadastro de credenciais, consulte o documento [Credencial de Repositório Git](https://tdn.totvs.com/credencial-git.md).

## Passo 2 - Configure a Atividade no TOTVS Automação

| Campo | O que informar |
| --- | --- |
| **Origem do repositório** | `Git` |
| **Credencial Git** | Selecione a credencial cadastrada no passo anterior |
| **Navegador** | `Chrome -` opção mais confiável para testes de interface reais |
| **Execução visual** | Desativado (headless) - recomendado para execuções em servidor |
| **Filtro de arquivos de teste** | Use padrões por módulo: `cypress/e2e/financeiro/**/*.cy.ts` |

## Page Object Model - A Estrutura Recomendada

Para times que mantêm testes ao longo do tempo, o [Page Object Model (POM)](https://martinfowler.com/bliki/PageObject.html) é a abordagem que mais reduz o esforço de manutenção. A ideia central: quando a interface muda, você ajusta em um só lugar o objeto de página e todos os testes que o usam são corrigidos automaticamente.

## Estrutura sugerida de repositório:

> Cada "página" da aplicação tem um arquivo correspondente em `support/pages/`. Os testes em `e2e/` apenas orquestram as ações definidas nesses objetos. Resultado: testes legíveis em linguagem de negócio, manutenção localizada.

### Dica sobre o Filtro de Arquivos de Teste

O campo **Filtro de arquivos de teste** aceita padrões flexíveis. Use essa flexibilidade para criar atividades especializadas no TOTVS Automação:

| Cenário | Filtro sugerido |
| --- | --- |
| Todos os testes | *(deixar em branco)* |
| Só testes de login | `cypress/e2e/login.cy.ts` |
| Módulo de RH completo | `cypress/e2e/rh/**/*.cy.ts` |
| Testes críticos marcados | `cypress/e2e/**/*.smoke.cy.ts` |

solid#21cafc1dashed3. Criando Testes sem Código

## Perfil: Não Técnico - Gravação com Cypress Studio

Este perfil é para você se: quer criar testes de interface sem escrever código, gravando os passos diretamente no navegador.

## O que é o Cypress Studio?

O [Cypress Studio](https://docs.cypress.io/app/guides/cypress-studio) é um recurso nativo do Cypress que permite **gravar ações em tempo real** enquanto você navega pela aplicação. Você clica, preenche campos e navega normalmente, o Studio transforma cada ação em um passo de teste automaticamente.

* O Cypress Studio exige que o Cypress seja executado em **modo visual** (com o navegador aberto).

Dica para o futuro:Comece salvando seus testes localmente. Conforme você ganha familiaridade, recomendamos evoluir para o uso de um **repositório Git**. Isso trará vantagens como histórico de versões e facilidade para trabalho em equipe! Para entender melhor as vantagens dessa transição, consulte nosso [Comparativo de Decisão: Local vs Git.](https://tdn.totvs.com/pages/viewpage.action?pageId=1067056872)

No servidor ou na sua máquina local, instale o Cypress conforme descrito no "Perfil: Do Zero". Crie uma pasta dedicada para os testes gravados.

**Passo 2 - Grave seus testes com o Cypress Studio**

Abra o Cypress no modo visual (`npx cypress open`) e execute o arquivo de teste onde deseja gravar. Certifique-se de que o teste seja executado até o fim com sucesso (sem erros). Em seguida, passe o mouse sobre o nome do teste no painel de comandos (*Command Log*) e clique em **Edit in Studio**. Dentro do ambiente do Studio:

1. **Execute as ações** que deseja automatizar interagindo normalmente com a sua aplicação do lado direito (navegar, clicar, preencher campos).
2. O Studio traduzirá cada interação em comandos do Cypress e os exibirá em tempo real no painel de código.
3. **Adicione validações:** Clique com o botão direito do mouse sobre qualquer elemento na tela para adicionar validações (assertions) manuais, ou simplesmente revise e aceite as recomendações inteligentes sugeridas automaticamente pelo *Studio AI* enquanto você interage.
4. Clique em **Save** no painel do Studio para gravar os comandos gerados diretamente no seu arquivo de teste.

> **Nota:** Os testes gravados são funcionais e podem ser editados posteriormente por alguém com conhecimento técnico, se necessário.

### Passo 3 - Configure no TAT usando Caminho Local

Após gravar e salvar os testes, configure a Atividade Cypress no TAT:

| Campo | O que informar |
| --- | --- |
| **Origem do repositório** | `Local` |
| **Caminho local** | Pasta onde os testes gravados foram salvos |
| **Navegador** | `Chrome -`mais confiável para gravações do Studio |
| **Filtro de arquivos de teste** | Informe o arquivo específico gravado, ex.: `cypress/e2e/meu-teste-gravado.cy.ts` |

### Limitações do Studio para o Longo Prazo

O Studio é excelente para **validações rápidas** e para **criar a base de testes** sem depender de desenvolvimento. Para cenários de uso contínuo, considere que:

* Testes gravados tendem a ser mais sensíveis a mudanças de interface.
* A manutenção é manual: cada alteração na aplicação pode exigir regravar partes do teste.
* Para processos críticos e equipes que mantêm testes ao longo do tempo, o "Perfil: Especialista com POM" oferece mais robustez.

solid#21cafc1dashed4. Executando Testes em Ambiente Gerenciado

## Perfil: PaaS - Sem Acesso ao Servidor

Este perfil é para você se: utiliza o TAT como serviço gerenciado (modelo PaaS) e não tem acesso direto ao servidor de execução. Nesse cenário, a origem `Local` **não está disponível** para você, o único caminho é o `Git`, pois é o mecanismo pelo qual o TAT busca seus scripts sem precisar que você envie arquivos ao servidor.

Boas notícias:Você não precisa instalar nada no servidor. O próprio TAT cuida da instalação do Cypress e das dependências antes de cada execução. O que você precisa fazer está inteiramente na sua própria máquina e na interface do TAT.

### Passo 1 - Crie os testes na sua máquina

Você vai trabalhar **na sua própria máquina** para criar e validar os testes. O servidor de execução só entra em cena quando você acionar a atividade no TAT.

Se ainda não tem testes prontos, use o **Cypress Studio** para gravá-los sem escrever código:

1. Instale o Node.js na sua máquina (apenas uma vez): acesse [nodejs.org](https://nodejs.org/pt-br) e baixe a versão LTS.
2. Crie uma pasta para o projeto, abra um terminal dentro dela e execute:

   ```
   npm install cypress --save-dev
   npx cypress open
   ```
3. Grave os testes com o Cypress Studio (consulte o [Perfil "Não Técnico"](#perfil-3-não-técnico--gravação-com-cypress-studio) para o passo a passo detalhado).

> Aqui o Node.js é instalado apenas na **sua máquina local** para você poder criar e visualizar os testes. No servidor gerenciado, as dependências necessárias para execução já estão provisionadas.

Se você já tem testes prontos em uma pasta, pode pular direto para o próximo passo.

### Passo 2 - Publique os testes em um repositório Git

Os testes precisam estar em um repositório Git acessível via HTTPS. Se não tiver um, crie gratuitamente no [GitHub](https://github.com), [GitLab](https://gitlab.com) ou outro serviço compatível.

Envie os arquivos do projeto Cypress para o repositório. O TAT vai clonar esse repositório antes de cada execução, garantindo que sempre rode a versão mais atual.

> **Importante:** certifique-se de que o repositório contém um arquivo `package.json` na pasta raiz. Ele é necessário para que o TAT instale as dependências automaticamente no servidor.

### Passo 3 - Crie um Token de Acesso (PAT) na plataforma Git

Para que o TAT possa clonar o repositório, você precisará de um token de acesso pessoal com permissão de leitura:

| Plataforma | Onde gerar |
| --- | --- |
| **GitHub** | Configurações → Developer Settings → Personal Access Tokens → Tokens (classic) → permissão `repo` |
| **GitLab** | Configurações do Usuário → Access Tokens → escopo `read_repository` |
| **Gitea** | Configurações → Aplicações → Gerar Token de Acesso |

> Guarde o token gerado. Ele é exibido uma única vez na maioria das plataformas.

### Passo 4 - Cadastre a Credencial Git no TAT

No TAT, acesse **Credenciais → Nova Credencial → Repositório Git** e preencha:

| Campo | O que informar |
| --- | --- |
| **Nome de exibição** | Identificação fácil, ex.: "GitHub - Meus Testes Cypress" |
| **URL do repositório** | Endereço HTTPS do repositório (apenas HTTP/HTTPS — SSH não é suportado) |
| **Branch** | Branch onde seus testes estão (ex.: `main`) |
| **Token de acesso pessoal (PAT)** | Token gerado no passo anterior |

### Passo 5 - Configure a Atividade Cypress no TAT

| Campo | O que informar |
| --- | --- |
| **Origem do repositório** | `Git -`único caminho disponível sem acesso direto ao servidor |
| **Credencial Git** | Selecione a credencial criada no passo anterior |
| **Navegador** | `Electron -`mais indicado para ambientes gerenciados, pois já vem embutido no Cypress sem instalação extra |
| **Execução visual** | Desativado (headless) - execução em segundo plano, adequada para servidores sem interface gráfica |
| **Filtro de arquivos de teste** | Deixe em branco para executar todos, ou informe o caminho do arquivo específico |

solid#21cafc1dashed5. Criando um Token de Acesso Pessoal (PAT)

## Como Criar um Token de Acesso Pessoal PAT no Git

Sempre que você utilizar a origem **Git** para seus testes (seja no perfil Especialista ou PaaS), o TOTVS Automação de Testes (TAT) precisará clonar o seu repositório. Para que isso ocorra com segurança, é exigido um **Token de Acesso Pessoal (PAT)** com permissão de leitura.

Siga o caminho correspondente à plataforma que sua equipe utiliza para gerar o token:

* **[GitHub](https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens):** Acesse `Configurações` → `Developer Settings` → `Personal Access Tokens` → `Tokens (classic)`. Gere um novo token e certifique-se de marcar a permissão **`repo`**.
* **[GitLab](https://docs.gitlab.com/user/profile/personal_access_tokens/):** Acesse `Configurações do Usuário` (ou *Preferences*) → `Access Tokens`. Crie um novo token marcando o escopo **`read_repository`**.
* **[Gitea](https://docs.gitea.com/development/api-usage):** Acesse `Configurações` → `Aplicações` → clique em `Gerar Token de Acesso`.

 Guarde o token gerado em um local seguro. Por motivos de segurança, a maioria das plataformas exibe o token apenas uma vez logo após a criação. Quando o seu PAT expirar, basta gerar um novo e atualizar o campo na Credencial já cadastrada no TOTVS Automação. Todas as atividades vinculadas passarão a usar o novo token automaticamente.solid#21cafc1dashedO que o TAT faz automaticamente para você

## O que o TOTVS Automação de Testes (TAT) faz automaticamente para você

Ao acionar a execução, o TOTVS Automação realiza as seguintes etapas sem qualquer intervenção:

1. Clona o repositório Git configurado na credencial
2. Instala o Cypress no diretório clonado
3. Executa os testes no navegador configurado
4. Gera e apresenta o relatório consolidado com os resultados

Quando o PAT expirar, basta gerar um novo token na plataforma Git e atualizar o campo na Credencial cadastrada no TAT. Todas as atividades que referenciam essa credencial passarão a usar o novo token automaticamente na próxima execução.solid#21cafc1dashed6. Campos da Interface no TOTVS Automação de Testes

## Referência Completa dos Campos da Interface

Esta seção serve como referência rápida para todos os campos disponíveis no formulário da Atividade Cypress.

### Campos de Cabeçalho (comuns a todas as atividades)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| **Nome** | Sim | Identificação da atividade no sistema. |
| **Versão** | Sim | Controle de versão da atividade. Permite manter múltiplas versões ativas simultaneamente. |
| **Descrição** | Sim | Texto livre para documentar o propósito da atividade. |

### Campos de Configuração Cypress

| Campo | Obrigatório | Opções / Formato | Descrição |
| --- | --- | --- | --- |
| **Origem do repositório** | Sim | `Local` | `Git` | Define de onde os scripts de teste serão obtidos. |
| **Caminho local** | Quando origem = Local | Caminho absoluto (ex.: `C:\testes` ou `/home/testes`) | Pasta raiz do projeto Cypress no servidor. |
| **Credencial Git** | Quando origem = Git | Lista de credenciais cadastradas | Credencial de acesso ao repositório Git. Deve ser cadastrada antes em **Credenciais → Repositório Git**. |
| **Navegador** | Sim | `Chrome` | `Firefox` | `Edge` | `Electron` | Navegador usado para executar os testes. Chrome, Firefox e Edge devem estar instalados no servidor. Electron é embutido no Cypress. |
| **Execução visual** | Sim | Ativado / Desativado | Quando **ativado**, o navegador abre de forma visível (modo *headed*). Quando **desativado**, a execução ocorre em segundo plano (modo *headless*). |
| **Filtro de arquivos de teste** | Não | Padrão glob (ex.: `cypress/e2e/**/*.cy.ts`) | Define quais arquivos de teste serão executados. Aceita múltiplos padrões. Se vazio, todos os arquivos encontrados serão executados. |

### Campos de Variáveis de Ambiente (Parâmetros Customizados)

Cada variável de ambiente é um par chave-valor repassado diretamente ao Cypress durante a execução. Nos scripts de teste, o valor é acessado via referência ao nome da variável.

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| **Chave** | Sim (por linha) | Nome da variável que os scripts de teste reconhecerão. |
| **Valor** | Não | Conteúdo da variável. Pode usar a sintaxe `{nomeDaVariavel}` para referenciar variáveis do Ambiente de Execução vinculado. |

**Exemplo de uso com referência a variável de ambiente:**

| Chave | Valor configurado | Comportamento |
| --- | --- | --- |
| `BASE_URL` | `{urlHomologacao}` | O TAT substitui `{urlHomologacao}` pelo valor configurado no Ambiente de Execução antes de iniciar os testes. |
| `SENHA_ADMIN` | `{senhaAdmin}` | Evita expor senhas diretamente na configuração da atividade. |
| `TIMEOUT` | `15000` | Valor fixo, sem substituição dinâmica. |

solid#21cafc1dashed7. Escolhendo entre Cypress Studio e Page Object Model

## Cypress Studio vs Page Object Model - Como criar testes?

| Critério | Cypress Studio (Gravação) | Page Object Model (Código) |
| --- | --- | --- |
| **Conhecimento técnico exigido** | Mínimo: gravar ações no navegador | Médio — exige familiaridade com código |
| **Velocidade de criação** | Rápida para testes simples | Exige mais tempo inicial |
| **Manutenção quando a UI muda** | Pode exigir regravar trechos | Ajuste em um único lugar (objeto de página) |
| **Legibilidade dos testes** | Menor, devido à geração automática de código. | Testes leem como cenários de negócio |
| **Reutilização de passos** | Passos duplicados por teste | Passos compartilhados entre testes |
| **Escalabilidade** | Difícil de manter em suítes grandes | Estrutura organizada por módulo |
| **Ideal para** | Validações pontuais, onboarding, protótipos | Suítes de regressão, processos críticos |
| **Recomendação do TAT** | Para início rápido e usuários não-técnicos | **Melhor prática para testes duráveis** |

> Não há exclusividade: você pode começar com Studio e, quando os testes estiverem provados como úteis, pedir ao time técnico que os estruture em POM para facilitar a manutenção futura.

solid#21cafc1dashedResumo das Boas Práticas

| Prática | Por quê |
| --- | --- |
| Use `Git` como origem para processos contínuos | Garante que a versão mais atual dos testes sempre rode, sem intervenção manual |
| Prefira `Electron` para execuções em servidor sem interface gráfica | É o único navegador embutido — não requer instalação adicional no agent |
| Use `{variavel}` nos Parâmetros Customizados | Permite reutilizar a mesma atividade em diferentes ambientes sem duplicar configurações |
| Organize filtros por módulo em atividades separadas | Facilita identificar qual área falhou e reduz o tempo de execução por ciclo |
| Mantenha o `package.json` do projeto atualizado | Evita falhas na etapa de instalação automática de dependências |
| Centralize credenciais Git no TAT | Quando o token expirar, basta atualizar em um lugar — todas as atividades se beneficiam |

solid#21cafc1dashedVeja também:

* [Origem do Repositório - Estratégias de Armazenamento do usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=1067056872)
* [Entendendo os Resultados e Corrigindo Erros](https://tdn.totvs.com/display/LRM/Entendendo+os+Resultados+e+Corrigindo+Erros)

---
