---
content_hash: d05186ba5160fc68ffefe196c7eff438b323f89b07c223de7ee11bb61f22effc
fetched_at: '2026-06-29T00:05:53.225156+00:00'
page_id: '1068927390'
product: rm
source: tdn-rm
title: Entendendo os Resultados e Corrigindo Erros
type: documentation
url: https://tdn.totvs.com/display/LRM/Entendendo+os+Resultados+e+Corrigindo+Erros
version: 18
---

Esta seção descreve como o TOTVS Automação apresenta os resultados de cada execução Cypress e como usar essas informações para identificar e corrigir problemas. O sistema foi projetado para traduzir erros técnicos do Cypress em linguagem de negócio. Você não precisa saber ler logs de terminal para entender o que aconteceu.

solid#21cafc1dashedO que o TOTVS Automação  mostra após uma execução

Ao abrir o resultado de uma execução Cypress no TAT, você verá um painel de relatório dividido em seções. O que aparece depende do resultado:

| Situação | O que é exibido |
| --- | --- |
| Execução falhou **antes** de rodar qualquer teste | Mensagem de falha descrevendo em qual etapa de preparação o problema ocorreu |
| Execução concluída, **todos os testes passaram** | Painel de relatório com resumo e lista de testes aprovados |
| Execução concluída, **alguns testes falharam** | Painel de relatório completo com resumo, lista de aprovados, detalhes de cada falha e guia de diagnóstico |

solid#21cafc1dashedSeção 1 - Painel de Resumo

### Seção 1 - Painel de Resumo

O topo do relatório exibe três contadores visuais:

* **Passaram -** quantidade de testes que foram concluídos com sucesso
* **Falharam -** quantidade de testes que encontraram algum problema
* **Total -** número total de testes executados
* **Barra de aprovação -** percentual de testes bem-sucedidos em relação ao total

Use essa visão para ter a dimensão geral da execução antes de mergulhar nos detalhes.

solid#21cafc1dashedSeção 2 - Testes Aprovados (expansível)

### Seção 2 - Testes Aprovados (expansível)

Lista todos os testes que passaram, agrupados por **módulo** (o nome do arquivo ou grupo de testes). Útil para confirmar que as partes saudáveis do sistema continuam funcionando corretamente, mesmo quando há falhas em outras áreas.

solid#21cafc1dashedSeção 3 - Detalhes das Falhas

### Seção 3 - Detalhes das Falhas

Esta é a seção mais importante quando algo deu errado. Para cada teste que falhou, o TOTVS Automação exibe um cartão com quatro informações:

| Campo | O que significa |
| --- | --- |
| **Categoria** | Classificação automática do tipo de problema (ver tabela abaixo) |
| **Resumo** | Descrição simplificada do que falhou, em linguagem acessível |
| **Dica** | Sugestão de ação para corrigir o problema |
| **Mensagem original** | Texto técnico gerado pelo Cypress. Útil para quem tem acesso ao código dos testes |

As falhas são agrupadas pelo **módulo** a que pertencem, facilitando identificar se o problema está concentrado em uma área específica da aplicação.

solid#21cafc1dashedSeção 4 - Guia de Diagnóstico por Categoria

O TOTVS Automação classifica automaticamente cada falha em uma de sete categorias. Use esta tabela como referência para entender o que cada categoria significa e o que fazer:

| Categoria | O que indica | Como agir |
| --- | --- | --- |
| ⏰ **Lentidão / Regra de Negócio** | O teste esperou por uma ação ou resposta que não ocorreu no tempo esperado | Verificar se a aplicação está respondendo normalmente; pode indicar lentidão no servidor ou uma regra de negócio que alterou o comportamento esperado |
| 🔍 **Elemento Não Encontrado** | O teste tentou interagir com um botão, campo ou seção que não estava disponível na tela | Verificar se a interface foi alterada recentemente; se o caminho de navegação até aquele ponto ainda é válido |
| 👁 **Falha de UI/Validação** | O teste verificou um valor ou texto esperado e encontrou algo diferente | Verificar se os dados de teste estão corretos e se a lógica de exibição da aplicação foi alterada |
| 🔗 **Falha de Integração** | A aplicação fez uma chamada a um serviço externo ou interno que retornou erro | Verificar se os serviços que a aplicação consome estão disponíveis e respondendo corretamente |
| 🌐 **Falha de Navegação** | O teste tentou acessar uma página que não carregou ou redirecionou inesperadamente | Verificar se o endereço base da aplicação está correto na variável `BASE_URL` e se a página existe |
| 🔒 **Problema de Permissão** | O teste acessou uma área que retornou erro de acesso negado | Verificar se as credenciais ou o perfil de usuário usado nos testes têm permissão para a ação que está sendo testada |
| ⚠️ **Erro Interno do Sistema** | Falha inesperada que não se encaixa nas categorias anteriores | Verificar a **Mensagem original** para obter detalhes técnicos; pode indicar problema no próprio script de teste |

solid#21cafc1dashedFluxo de Correção - Passo a Passo

### Fluxo de Correção - Passo a Passo

Ao receber uma execução com falhas, siga esta sequência:

#### Etapa 1 - Identifique se é falha de preparação ou falha de teste

**A atividade marcou como "Falhou" (vermelho) e não há painel de relatório?** → A falha ocorreu **antes** de qualquer teste ser executado. Veja a mensagem de erro da atividade. Ela descreve em qual etapa de preparação o problema aconteceu. Consulte o [Diagnóstico de Falhas de Preparação](#diagnóstico-de-falhas-de-preparação) abaixo.

**A atividade marcou como "Concluída" e há painel de relatório com falhas?** → A preparação foi bem-sucedida. Os testes rodaram, mas alguns encontraram problemas. Vá para a [Etapa 2](#etapa-2--leia-a-categoria-e-a-dica-de-cada-falha).

#### Etapa 2 - Leia a categoria e a dica de cada falha

No painel de relatório, abra a seção de falhas e leia o **Resumo** e a **Dica** de cada cartão de erro. Na maioria dos casos, a combinação de categoria + dica é suficiente para identificar a causa sem precisar olhar para o código.

**Exemplo prático - Falha de Navegação:**

`Categoria: Falha de Navegação`

`Resumo:` cy.visit() falhou ao carregar a página

Dica: Verifique se o endereço base da aplicação está correto e se o servidor está acessível

→ Ação: revisar o valor de `BASE_URL` nas Variáveis de Ambiente da atividade.

**Exemplo prático - Elemento Não Encontrado:**

`Categoria: Elemento Não Encontrado`

`Resumo: Timed out retrying after 4000ms: Expected to find element`

Dica: Verifique se o elemento existe na tela no momento esperado; a interface pode ter mudado

→ Ação: verificar se a interface da aplicação foi alterada desde que o teste foi criado.

#### Etapa 3 - Use o Guia de Diagnóstico integrado

O painel de relatório inclui um **Guia de Diagnóstico** expansível com orientações para cada categoria de erro. Ele complementa as dicas individuais com descrições mais detalhadas do que pode ter causado o problema e como investigar.

#### Etapa 4  - Corrija e reexecute

Dependendo do que identificou:

| Causa identificada | Onde corrigir |
| --- | --- |
| `BASE_URL` incorreta | Variáveis de Ambiente da atividade no TAT |
| Token Git expirado | Credencial Git no TAT |
| Filtro de arquivos errado | Campo "Filtro de arquivos de teste" da atividade |
| Variável de ambiente ausente | Adicionar novo par chave-valor na atividade |
| Interface da aplicação mudou | Atualizar os scripts de teste no repositório e reexecutar |
| Serviço externo indisponível | Verificar a disponibilidade do serviço e reexecutar |

Após corrigir, acione a execução novamente. O TAT gerará um novo relatório completo para a nova tentativa.

solid#21cafc1dashedDiagnóstico de Falhas de Preparação

### Diagnóstico de Falhas de Preparação

Quando a falha ocorre antes dos testes, a mensagem exibida pelo TAT indica qual etapa específica do processo de preparação encontrou o problema. O processo de preparação tem cinco etapas sequenciais:

Se qualquer etapa falhar, as seguintes não são executadas. A mensagem de erro aponta diretamente para a etapa com problema.

| Mensagem de falha | Causa | Como corrigir |
| --- | --- | --- |
| "verificação do Node.js falhou" | Node.js não está instalado ou não está acessível no servidor | Solicitar à equipe de infraestrutura a instalação do Node.js no e |
| "verificação do npm falhou" | npm não está disponível (normalmente instalado junto com o Node.js) | Verificar se o Node.js foi instalado corretamente; reinstalar se necessário |
| "Node.js instalado no ambiente é incompatível" | A versão do Node.js no servidor é muito antiga para o Cypress configurado no projeto | Para que a execução do Cypress funcione sem problemas no ambiente *On-Premises*, é fundamental garantir que a versão do Node.js instalada na sua máquina seja compatível com a versão do Cypress que você pretende utilizar. Se você está **começando um projeto do zero**, siga o passo a passo da [Documentação Oficial de Instalação do Cypress](https://docs.cypress.io/app/get-started/install-cypress#Nodejs) para garantir que tudo seja configurado corretamente desde o início. Agora, se você **já possui um projeto em andamento** e precisa atualizar ou verificar a compatibilidade atual, consulte o [Guia de Migração do Cypress](https://docs.cypress.io/app/references/migration-guide) |
| "Permissão negada ao instalar dependências" | O processo de execução não tem permissão de escrita na pasta do projeto | Solicitar à equipe de infraestrutura que ajuste as permissões de acesso à pasta |
| "Não foi possível acessar o registry do npm" | O servidor não tem acesso à internet ou ao servidor de pacotes | Verificar a conectividade do Agent com a internet; pode exigir configuração de proxy |
| "Falha ao instalar o Cypress" | Incompatibilidade de versão entre Node.js e a versão do Cypress definida no `package.json` | Alinhar a versão do Cypress no `package.json` com a versão do Node.js disponível no servidor |
| Falha na clonagem do repositório (origem Git) | Git não instalado, token expirado, URL incorreta ou branch inexistente | Verificar se o Git está instalado no servidor; revisar os dados da Credencial Git no TAT |

> **Clientes PaaS:** falhas de preparação relacionadas à infraestrutura (Node.js, npm, Git, permissões, rede) devem ser reportadas à equipe responsável pelo ambiente gerenciado — não são ajustes que você faz no TAT.

solid#21cafc1dashedDiagnóstico: Testes passam localmente mas falham no TOTVS Automação

Este é um dos cenários mais comuns. As causas mais frequentes são:

| Diferença | Verificação sugerida |
| --- | --- |
| **Endereço da aplicação** diferente | Confirme que a variável `BASE_URL` aponta para o ambiente correto (homologação vs. produção vs. local) |
| **Credenciais de acesso** diferentes | Verifique se o usuário e senha usados nos testes existem e têm acesso no ambiente do Agent |
| **Dados de teste** ausentes | Alguns testes dependem de dados específicos no banco; verifique se esses dados existem no ambiente de execução |
| **Versão da aplicação** diferente | O Agent pode estar apontando para uma versão diferente da que você testou localmente |
| **Conectividade** do Agent | O servidor pode não conseguir acessar serviços que sua máquina local acessa sem problema |

solid#21cafc1dashedReferência Complementar - Erros Comuns do Cypress

Além das mensagens simplificadas exibidas pelo TOTVS Automação, você também pode consultar a documentação oficial do Cypress com exemplos de erros comuns e orientações adicionais de correção:

[Documentação Oficial de Erros do Cypress](https://docs.cypress.io/app/references/error-messages)

Essa referência pode ajudar principalmente quando:

* a mensagem original do Cypress precisar de uma análise mais detalhada;
* o problema envolver comportamento específico do framework;
* houver necessidade de validar exemplos técnicos semelhantes ao erro encontrado na execução.

Importante: na maioria dos cenários, o próprio painel do TAT já traduz o problema em linguagem mais acessível, indicando a categoria da falha, o resumo do erro e sugestões práticas de correção. A documentação oficial do Cypress funciona como um material complementar para aprofundamento e investigação adicional quando necessário.

solid#21cafc1dashedVeja também:

* [Guia de Experiência - Atividade Cypress no TOTVS Automação de Testes](https://tdn.totvs.com/pages/viewpage.action?pageId=1068171448)
* [Origem do Repositório - Estratégias de Armazenamento do usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=1067056872)
