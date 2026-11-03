---
content_hash: 7228eeb7d9276c83fd9098fccc4c6792156aad1ff62b72a726764abf935688c5
fetched_at: '2026-06-29T00:05:47.168534+00:00'
page_id: '1008226448'
product: rm
source: tdn-rm
title: Exportação de Projetos de Teste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008226448
version: 8
---

# O que é?

É a extração de **um** ou **mais** Projetos de Testes em um arquivo compactado contendo todas as **atividades, casos de teste e configurações**.  
Esse recurso facilita o **compartilhamento, backup e reutilização** de projetos entre diferentes ambientes ou bases locais.

# Para que serve?

A exportação foi criada para simplificar o processo de transferência e padronização de projetos, garantindo que o conteúdo possa ser reutilizado de forma prática e segura.

Com ela, é possível:

* Mover projetos entre diferentes ambientes ou bases de dados;
* Enviar projetos completos para outros analistas ou equipes;
* Fazer backup preventivo dos projetos;
* Garantir padronização e reaproveitamento das automações já criadas.

# Exemplo de Uso

Como cadastrarComo Utilizar1- Navegação para Exportar 

 1. Navegue no menu do TOTVS Automação de Testes e clique em Atividades  → Projetos → Projetos de Teste.

 2. Na tabela exibida, selecione o projeto que deseja exportar e clique no botão **Exportar** para gerar o arquivo .**zip** com todas as atividades e casos de teste do projeto selecionado.

* Exemplo de exportação de múltiplos projetos:

*Exemplo utilizando todos os Projetos selecionados*

*Exemplo utilizando projetos específicos selecionados*

Exemplo prático

## Exemplo Prático

Atenção

Cuidado ao exportar atividades que contenham dados sensíveis.

### Cenário 1: Backup de Projetos de Teste

Quando o usuário precisa realizar o backup dos projetos de teste existentes antes de aplicar grandes alterações no ambiente ou nos próprios projetos, a exportação garante uma cópia de segurança dos casos de teste, atividades e configurações, permitindo restaurar o estado anterior caso algo saia do esperado.

Por que fazer isso:  
A exportação como forma de backup é uma medida preventiva essencial. Ela permite restaurar rapidamente os projetos originais em caso de falhas, erros de configuração ou inconsistências após modificações significativas.

### Cenário 2: Reutilização de projetos em diferentes ambientes

Quando a equipe de testes já possui um conjunto de automações e precisa utilizá-lo em outro ambiente do TOTVS Automação de Testes  por exemplo, em uma filial ou em um ambiente de homologação a exportação permite gerar um pacote portátil do projeto, que pode ser facilmente importado em outro ambiente, mantendo toda a estrutura original, incluindo casos de teste, atividades e configurações.

Para que fazer isso:  
Essa funcionalidade facilita o compartilhamento e a reutilização de projetos de teste entre diferentes ambientes, evitando retrabalho e garantindo padronização nos processos de automação.

---

# Saiba mais

Antes de exportar,verifique se o projeto está completo e atualizado, garantindo que todas as atividades e casos de teste estejam funcionando corretamente. Isso assegura que o arquivo gerado reflita o estado real do projeto e evite falhas ao importar posteriormente

Ao exportar apenas o projeto, lembre-se de que as configurações de ambiente (como variáveis, credenciais e dependências externas) não são incluídas.

Ao exportar apenas o projeto, lembre-se de que as configurações de ambiente (como variáveis, credenciais e dependências externas) não são incluídas.  
Se o projeto depender de um ambiente específico, exporte também o ambiente correspondente para garantir que todas as execuções funcionem corretamente após a importação.

# FAQ

**P: Quando devo usar a Exportação?**

R: Backup preventivo antes de grandes alterações no sistema ou nos projetos; Compartilhamento de projetos entre diferentes equipes, clientes ou filiais; Migração de ambiente, como de homologação para produção; Reutilização de fluxos já prontos em novos contextos.

**P: Posso reutilizar um arquivo de exportação antigo?**

R: Sim, desde que o formato do projeto e a versão do sistema sejam compatíveis com o ambiente atual, além de garantir que todos os arquivos foram exportados em um único pacote, ou seja, não é possível importar simultaneamente arquivos gerados em diferentes importações.

ATENÇÃO: Muito cuidado ao importar arquivos antigos de exportação em uma base de dados populada - essa ação pode sobrepor atualizações e versões mais atuais dos projetos de testes.
