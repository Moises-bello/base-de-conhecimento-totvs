---
content_hash: 4a4830cf934fedc9bc9b26655077be130208d34ad5a2e7d1669b3d77ad4d86df
fetched_at: '2026-06-29T00:05:53.142491+00:00'
page_id: '1067056872'
product: rm
source: tdn-rm
title: Origem do Repositório - Estratégias de Armazenamento do usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1067056872
version: 17
---

A atividade Cypress do TOTVS Automação de Testes (TAT) permite executar projetos de teste utilizando duas estratégias diferentes de armazenamento do código: **Projeto Local** ou **Repositório Git**.

## Por que isso importa?

Cada abordagem atende a necessidades específicas do usuário, da equipe e do ambiente de execução. Entender quando utilizar cada opção é fundamental para facilitar a manutenção, reduzir gargalos operacionais e melhorar a governança da sua automação.

solid#21cafc1dashed1. Projeto Local

Na opção Local, o projeto Cypress já está disponível diretamente no Agent de execução. O TAT consome os arquivos de um diretório existente no servidor ou na máquina onde o Agent está instalado.

### Como funciona o fluxo

### Quando utilizar o Projeto Local?

* O usuário está iniciando na automação de testes.
* Os testes ainda estão em fase de desenvolvimento ou prototipação.
* Existe apenas **um responsável** pela criação e manutenção.
* O ambiente de execução é simples ou isolado.
* O foco principal é realizar validações rápidas sem burocracia de versionamento.

### Benefícios e Pontos de Atenção

| **Benefício** | **Descrição** |
| --- | --- |
| **Simplicidade** | Configuração rápida e direta, ideal para os primeiros testes. |
| **Agilidade** | Alterações no código podem ser feitas e testadas imediatamente. |
| **Independência** | Não depende de plataformas Git, credenciais ou internet para clonagem. |

| **Ponto de Atenção** | **Impacto na Operação** |
| --- | --- |
| **Alterações manuais** | Editar código direto no servidor pode gerar perda de rastreabilidade. |
| **Ausência de versionamento** | Não há histórico de mudanças; alterações acidentais são difíceis de reverter. |
| **Colaboração limitada** | Múltiplos analistas trabalhando no mesmo servidor geram conflitos e dificultam a sincronização. |

solid#21cafc1dashed2. Repositório Git

Na opção Git, o projeto Cypress fica armazenado em um repositório remoto (como Azure DevOps, GitHub, GitLab). O TAT realiza automaticamente o clone do projeto antes de cada execução.

### Quando utilizar o Git?

* O projeto possui **manutenção contínua** e é oficializado.
* Existe mais de um analista colaborando no mesmo conjunto de testes.
* Os testes fazem parte de uma esteira de Integração Contínua (CI/CD).
* Há necessidade rigorosa de versionamento, governança e auditoria de código.

### Benefícios do Git

| **Benefício** | **Descrição** |
| --- | --- |
| **Versionamento** | Histórico completo de quem alterou, quando alterou e por quê. |
| **Colaboração Segura** | Equipes trabalham em paralelo via *branches* sem sobrescrever o trabalho alheio. |
| **Código Centralizado** | O código-fonte fica seguro na nuvem, não dependendo de backups manuais do servidor. |
| **Garantia de Atualização** | O TAT sempre clona a versão mais recente e validada da *branch* principal. |

solid#21cafc1dashed3. Comparativos de Decisão

## Comparativos de Decisão

### Local vs Git - Qual origem escolher?

| Critério | Caminho Local | Repositório Git |
| --- | --- | --- |
| **Velocidade para começar** | Rápido: apenas informe o caminho | Requer cadastro de credencial primeiro |
| **Atualização automática** | Manual: precisa copiar arquivos no servidor | Automática — sempre clona a versão mais recente |
| **Ideal para** | Desenvolvimento, testes rápidos, Cypress Studio | Processos contínuos, integração, equipes |
| **Trabalho em equipe** | Difícil: dependente do servidor específico | Centralizado no repositório |
| **Rastreabilidade de mudanças** | Sem histórico nativo | Histórico completo via Git |
| **Manutenção a longo prazo** | Pode se tornar difícil de gerenciar | Organizado e versionado |
| **Recomendação do TAT** | Para validações e início rápido | **Melhor prática para uso contínuo** |

> O TOTVS Automação não proíbe o uso de `Local,` é uma opção válida e funcional. A recomendação de `Git` existe para cenários onde a rastreabilidade, a colaboração e a automação contínua fazem a diferença no dia a dia.

### Jornada de Evolução Recomendada

Não é necessário escolher uma opção e ignorá-la para sempre. A melhor prática para o ciclo de vida de um projeto de testes geralmente segue este fluxo de maturidade:

1. **Início:** Desenvolvimento e Validação Inicial `(Origem: Local)`
2. **Estabilização:** Publicação no repositório `(Transição)`
3. **Maturidade:** Versionamento, CI/CD e Manutenção Colaborativa `(Origem: Git)`
solid#21cafc1dashedResumo de Boas Práticas

Independentemente da origem escolhida, siga estas recomendações para garantir a saúde da sua automação:

* **Valide localmente primeiro:** Sempre execute e valide os testes na sua própria máquina antes de enviá-los para o servidor do TOTVS Automação ou para o Git.
* **Proteja dados sensíveis:** Utilize o recurso de Variáveis de Ambiente do TOTVS Automação para senhas e tokens; nunca os deixe fixos (`hardcoded`) no código Cypress.
* **Organize por módulos:** Separe os testes em pastas lógicas para facilitar a manutenção e a execução segmentada.
* **Evite o "Código em Produção":** Mesmo usando origem Local, evite o hábito de editar testes críticos diretamente no servidor de produção sem um backup.
* **Documente as mudanças:** Ao usar Git, crie mensagens de *commit* claras e documente mudanças estruturais para o resto da equipe.

solid#21cafc1dashedVeja também:

* [Guia de Experiência - Atividade Cypress no TOTVS Automação de Testes](https://tdn.totvs.com/pages/viewpage.action?pageId=1068171448)
* [Entendendo os Resultados e Corrigindo Erros](https://tdn.totvs.com/display/LRM/Entendendo+os+Resultados+e+Corrigindo+Erros)
