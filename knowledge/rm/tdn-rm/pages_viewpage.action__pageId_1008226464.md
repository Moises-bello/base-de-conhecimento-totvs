---
content_hash: 299d03f5ccc12f8dc05b4dfa124eb59b04aeff1633cee57a6d60ecac44691fbc
fetched_at: '2026-06-29T00:05:47.176134+00:00'
page_id: '1008226464'
product: rm
source: tdn-rm
title: Importação de Projetos de Teste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008226464
version: 12
---

# O que é?

A **Importação de Projetos de Teste** permite que você traga para o TOTVS Automação de Testes projetos previamente exportados de outros ambientes ou bases, de forma prática e segura.  
Com essa funcionalidade, é possível recriar todo o projeto, incluindo suas **atividades, casos de teste e configurações,** a partir de um arquivo `.json` gerado no processo de exportação.

# Para que serve?

A importação foi criada para facilitar oreaproveitamento, padronização e compartilhamento de Projetos de Teste entre diferentes ambientes da ferramenta.

Com ela, você pode:

* Reutilizar projetos prontos sem precisar recriá-los manualmente;
* Mover projetos de teste entre diferentes ambientes ou bases;
* Restaurar backups de projetos exportados anteriormente;
* Garantir consistência e compatibilidade nos testes automatizados entre múltiplas instalações da ferramenta.

# Exemplo de Uso

Como cadastrarComo Utilizar1- Navegação para Importar

 1. Navegue no menu do TOTVS Automação de Testes e clique em Atividades  → Projetos → Projetos de Teste.

 2. Clique no botão **Importar projetos de teste.**

2- Preenchimento dos CamposVersão para importação

Caso o projeto ou atividades não existam, será aplicada a versão selecionada. Se já existirem, será mantida a versão atual.

* Selecione a versão compatível com o ambiente para garantir a importação correta.

Caso seu ambiente utilize versões diferentes do sistema RM, recomenda-se escolher a mesma versão usada nos projetos originais. Se isso não for possível, utilize uma versão padrão compatível com o ambiente atual para garantir uma importação estável e sem inconsistências.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Credencial do Banco de Dados para importação 

Ao importar um projeto de teste, é necessário selecionar uma [Credencial de Banco de Dados](https://tdn.totvs.com/display/LRM/1+-+Banco+de+Dados). Essa credencial representa as informações de conexão que serão utilizadas para acessar o banco durante a execução das atividades e validações do projeto.

Grupo para importação

* Selecione o [grupo](https://tdn.totvs.com/pages/viewpage.action?pageId=680234913#Cria%C3%A7%C3%A3odeumgrupo-1729228565) que terá acesso aos Projetos de Teste importado.

3- Selecione os arquivos

Após definir a Versão para importação →  Credencial de banco de dados → Grupo de importação. Selecione o arquivo do projeto que será importado.

Esse campo recebe o arquivo **.json** gerado na exportação de projetos do TOTVS Automação de Testes, contendo todas as informações necessárias para recriar o projeto como atividades, casos de teste e configurações.

Você pode **clicar na área destacada** para escolher o arquivo ou **arrastá-lo diretamente** para o componente.  
O sistema valida automaticamente o formato e aceita apenas arquivos **.json**.

Exemplo prático

## Exemplo Prático

Antes de importar projetos, **verifique se o ambiente correspondente também foi exportado**. Isso garante que variáveis, recursos e dependências sejam corretamente restaurados após a importação. Sem o ambiente, parte dos testes pode falhar por falta de configuração compatível.

## Importação de Projetos de Teste

### 1. Acesso à tela

No menu lateral, acesse Projetos → Importar Projetos de Teste.  
Clique em Importar para abrir o modal de importação.

### 2. Preenchendo o modal

* Credencial de Banco de Dados: selecione a credencial configurada no seu ambiente atual.
* Grupo: defina o grupo de usuários que terão permissão para visualizar e editar o projeto importado.
* Arquivo de Importação: anexe o arquivo `.json` exportado de outro ambiente ou de um backup local.

### Cenário 1: Importação de novos projetos de teste

**Exemplo prático:**  
Quando ousuário recebe um pacote de projetos de teste exportados do TOTVS Automação de Testes por exemplo, o arquivo `ProjetosERP_Export.zip` contendo os casos de teste do ERP Financeiro, é possível importar esse conteúdo no ambiente atual.

1. Resultado da importação:

   * O sistema criará automaticamente um novo projeto de teste, com suas atividades, casos de teste e recursos personalizados.
   * O caso de teste será vinculado ao novo projeto criado.
   * Os recursos de execução serão importados e ajustados automaticamente conforme o ambiente atual.
   * Os mocks precisarão ser regravados manualmente, garantindo que o comportamento simulado esteja atualizado.
2. Validação pós-importação:

   * Após a importação, execute o projeto para validar se todos os fluxos funcionam corretamente.

### Cenário 2: Importação de projetos de teste já existentes

Quando o usuário já possui um projeto existente  por exemplo, o “Portal de Vendas” e precisa atualizá-lo com novas atividades e correções usando o arquivo `PortalVendas_Backup.json`, é possível realizar a importação mantendo os dados principais.

1. Durante a importação:

   * Se o sistema identificar um projeto já existente, será exibido o modal de substituição, perguntando se deseja substituir os dados existentes.
   * As atividades com o mesmo identificador terão seus dados atualizados.
   * O mock de comparação não será importado se já existir um mock local, ele será mantido.
   * Se houver casos de teste duplicados, o sistema criará novos casos de teste independentes, sem vínculo com o projeto antigo.
   * Os recursos e parâmetros de execução serão ajustados automaticamente conforme o ambiente.
2. Resultado da importação:

   * O projeto "Portal de Vendas" é atualizado com as novas atividades e correções.
   * O mock anterior permanece preservado.
   * O sistema exibirá uma mensagem confirmando a atualização bem-sucedida.
3. Validação pós-importação:

   * Execute novamente o projeto para validar as alterações.

---

# Saiba mais

A Importação de Projetos de Teste permite integrar projetos de diferentes ambientes do TOTVS Automação de Testes, garantindo portabilidade e reaproveitamento dos casos de teste, atividades e configurações.

Verifique o ambiente antes da importação: sempre confirme se o ambiente correspondente ao projeto foi exportado. Isso evita falhas de execução causadas por variáveis ausentes.

Após a importação, valide os projetos importados para identificar quais atividades de comparação de banco de dados necessitam do preenchimento dos Mocks. Em seguida, revise e atualize os Mocks, garantindo que o comportamento simulado esteja consistente com os dados e o ambiente atual.

# FAQ

**P: O que preciso validar após importar um projeto?**

R: Execute o projeto importado para confirmar que as atividades, fluxos e recursos estão funcionando corretamente. Regrave os Mocks das atividades de comparação de banco de dados. Além disso, se o projeto depender de variáveis de ambiente, importe também o ambiente correspondente.

**P: O que acontece se eu importar um projeto que já existe?**

R: O sistema exibirá uma mensagem de substituição perguntando se deseja atualizar o projeto existente. O projeto, sub-projetos e atividades serão sobrescritas com os novos dados, enquanto os mocks locais serão preservados.
