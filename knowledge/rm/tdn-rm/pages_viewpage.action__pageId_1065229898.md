---
content_hash: a66ab5c5efe77fb6de92200fb550186f9c753d1a7c9ea32f5619dd5a6fe90054
fetched_at: '2026-06-29T00:05:53.083997+00:00'
page_id: '1065229898'
product: rm
source: tdn-rm
title: 2- Repositórios Git
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1065229898
version: 5
---

## O que é

Uma **Credencial de Repositório Git** armazena as informações necessárias para que o TOTVS Automação de Testes acesse um repositório Git remoto de forma autenticada.

Ela é utilizada em atividades Cypress configuradas com **Origem do Repositório = Git**.

## Para que serve

Permite que o sistema:

* Acesse repositórios Git públicos ou privados
* Clone automaticamente o projeto de testes antes de cada execução
* Utilize sempre a versão mais atualizada dos testes
* Elimine a necessidade de manter cópias locais do projeto no agente

## Exemplo de Uso

Como cadastrarComo Cadastrar 1. Início de Cadastro 

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Credenciais → Repositório Git**

 2. Clique em **Adicionar (+)** para cadastrar uma nova credencial

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposURL do Repositório

#### URL do Repositório

Endereço completo do repositório Git (obrigatoriamente em HTTPS).

| Provedor | Exemplo |
| --- | --- |
| Azure DevOps | `https://dev.azure.com/org/projeto/_git/repositorio` |
| GitHub | `https://github.com/usuario/repositorio.git` |
| GitLab | `https://gitlab.com/usuario/repositorio.git` |
| Bitbucket | `https://bitbucket.org/usuario/repositorio.git` |

 URLs no formato SSH (`git@...`) não são suportadas.Branch (opcional)

#### Branch

Nome da branch a ser clonada.

**Exemplos:**

* `main`
* `develop`
* `staging`
* `release/1.0.0`Recomenda-se utilizar branches estáveis para execuções automatizadas.
Token de Acesso Pessoal (PAT)

#### Token de Acesso Pessoal (PAT)

Token utilizado para autenticação no repositório.

* Substitui usuário e senha
* Deve possuir permissão de leitura

### Geração do Token

**Azure DevOps**

1. Acesse o perfil → *Personal Access Tokens*
2. Clique em **New Token**
3. Defina escopo **Code (Read)**
4. Gere e copie o token

**GitHub**

1. Acesse *Settings → Developer settings → Personal access tokens*
2. Clique em **Generate new token**
3. Selecione o escopo `repo`
4. Gere e copie o token

**GitLab**

1. Acesse *Settings → Access Tokens*
2. Selecione o escopo `read_repository`
3. Gere e copie o token

O token não é exibido nos logs e deve ser armazenado com segurança  
Tokens possuem validade e devem ser atualizados antes do venciment

## Solução de Problemas

| Erro | Causa | Solução |
| --- | --- | --- |
| Git não encontrado | Git não instalado | Instalar e reiniciar o agente |
| Repository not found | URL inválida | Validar o endereço |
| Falha de autenticação | Token inválido/expirado | Gerar novo token |
| Branch não encontrada | Nome incorreto | Validar a branch |
| URL inválida | Uso de SSH | Utilizar HTTPS |

---

# Saiba mais

Utilize nomes descritivos para suas credenciais, incluindo o nome do projeto e o ambiente. Isso facilita a identificação quando houver várias credenciais cadastradas (ex.: Cypress - Testes Fluig - Produção, Cypress - Testes RH - Homologação).

Crie tokens com permissão mínima necessária (apenas leitura de código). Evite tokens com permissões amplas como escrita, exclusão ou administração do repositório.

Fique atento à validade do token. Recomenda-se criar lembretes para renovação antes do vencimento. Quando o token expira, todas as atividades Cypress vinculadas à credencial deixam de funcionar.

Prefira utilizar branches estáveis como main, master ou staging. Branches de desenvolvimento podem conter testes incompletos ou instáveis, comprometendo os resultados da execução.

Uma mesma credencial pode ser reutilizada em várias atividades Cypress. Se diversas atividades utilizam testes do mesmo repositório (mas com filtros de arquivos diferentes), basta vincular a mesma credencial a todas elas.

Caso o repositório mude de endereço ou a branch seja renomeada, atualize a credencial imediatamente para evitar falhas nas próximas execuções.

# FAQ

**P**: **Posso reutilizar a mesma credencial?**

**R:** Sim. Pode ser utilizada em múltiplas atividades.

**P:** **O que acontece quando o token expira?**

**R:** A execução falha ao clonar o repositório. Atualize o token.

**P:** **Preciso instalar o Git no agente?**

**R:** Sim. O Git deve estar disponível no PATH.

**P:** **Funciona com repositórios privados?**

**R:** Sim, desde que o token tenha permissão de leitura.

P: **O token aparece nos logs?**

R: Não. O sistema protege automaticamente as credenciais.
