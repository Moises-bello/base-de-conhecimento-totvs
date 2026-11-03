---
content_hash: 8d2902252402b52af6f5004e58cfa145fe9f1074310ff70783727214ecc52fb8
fetched_at: '2026-06-29T00:05:47.223895+00:00'
page_id: '1008229564'
product: rm
source: tdn-rm
title: Importação de Ambientes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008229564
version: 7
---

# O que é?

A **Importação de Ambientes** do TOTVS Automação de Testes é a funcionalidade que permite **recriar ou atualizar ambientes existentes** a partir de um arquivo gerado pela exportação de ambientes.

Ela é utilizada para **trazer para o sistema configurações, variáveis e credenciais** previamente exportadas de outra base, garantindo **padronização e compatibilidade** entre diferentes instalações da ferramenta.

# Para que serve?

A Importação de Ambientes foi criada para **facilitar a transferência e a manutenção de configurações**, tornando o processo de implantação e atualização mais ágil e seguro.

Com essa funcionalidade, é possível:

* Adicionar novos ambientes a partir de arquivos exportados;
* Atualizar ambientes existentes, reaproveitando variáveis já definidas;
* Garantir consistência entre bases diferentes da ferramenta;
* Evitar retrabalho, importando configurações padronizadas em vez de criá-las manualmente.

# Exemplo de Uso

Como cadastrarComo Utilizar1- Navegação para Importar

 1. Navegue no menu do TOTVS Automação de Testes e clique em **Ambientes.**

 2. Clique no botão **Importar ambientes.**

2- Preenchimento dos CamposModo de importaçãoCriar novo ambiente

Selecione essa opção quando você quiser **adicionar um ambiente completamente novo** ao sistema.

* Um **novo registro de ambiente** será criado.
* É ideal para **importar ambientes de outro local**, como de uma filial, homologação ou backup anterior.
* Todas as variáveis e configurações do arquivo importado serão **incluídas como um novo ambiente**.

  *Exemplo:*

  Você exportou o ambiente "Homologação RM" de outra base e quer adicioná-lo no seu sistema atual.  
  Escolha **Criar novo ambiente**, importe o arquivo `.json` e pronto o novo ambiente será criado sem substituir nada existente.

Ao selecionar **Criar novo ambiente** no Modo de importação, o sistema solicita:

Grupo

* **Grupo:** escolha o [grupo](https://tdn.totvs.com/pages/viewpage.action?pageId=680234913#Cria%C3%A7%C3%A3odeumgrupo-1729228565) ao qual o novo ambiente será vinculado.

Credencial de Banco de Dados

* **Credencial do Banco de Dados:** selecione a [credencial](https://tdn.totvs.com/pages/viewpage.action?pageId=947302624) padrão que será usada para conectar no banco de dados.

importar em ambiente existente

Use essa opção quando você quiser **atualizar as variáveis** um ambiente que já existe no sistema.

* O sistema pedirá que você **escolha qual ambiente existente será atualizado**.
* As **variáveis** não existentes serão **incluídas** e as que já existem serão apresentadas como **conflitos** no resultado e não serão importadas.
* É ideal quando você tem uma **versão mais recente** do ambiente exportada e quer aplicar as atualizações.

Ao escolher Importar em ambiente existente, será exibido:

Selecionar Ambiente

Ao selecionar a opção "**Importar em ambiente existente"**, a ferramenta interpreta que o arquivo de importação contém dados que devem ser **aplicados sobre um ambiente já cadastrado** no sistema.

Nesse modo, o campo "**Selecionar ambiente"** é exibido para que o usuário escolha **qual ambiente existente receberá a atualização**.  
A partir dessa seleção, a ferramenta **associa o arquivo importado ao ambiente indicado**, aplicando as informações correspondentes **sem criar um novo registro**, ou seja, **somente o ambiente selecionado é atualizado**.

Durante o processo, o sistema realiza uma verificação detalhada das variáveis contidas no arquivo de importação:

* **Variáveis novas:** são **incluídas automaticamente** no ambiente selecionado.
* **Variáveis já existentes:** são **detectadas como conflitos** e **não sobrescritas**, preservando o valor atual.

Ao final da importação, o sistema exibe um **relatório de resultado**, listando todas as variáveis adicionadas, bem como as que **entraram em conflito** e foram **ignoradas**.

* Exemplo de exportação de múltiplos projetos:

*Exemplo de variáveis em conflito*

*Exemplo de variáveis com sucesso*

3- Selecione os arquivos

Esse campo recebe o arquivo **.json** gerado na **exportação de ambientes** do TOTVS Automação de Testes, contendo todas as informações necessárias para recriar a estrutura do ambiente.

Você pode **clicar na área destacada** para escolher o arquivo ou **arrastá-lo diretamente** para o campo.  
O sistema valida automaticamente o formato e **aceita apenas arquivos .json**.

Exemplo práticoExemplo prático

## Exemplo prático:

## **Cenário 1: Importação de um novo ambiente**

**Exemplo prático:**  
O usuário recebe um arquivo `Ambientes_Homologacao.zip` contendo todos os ambientes de homologação. Ao importar um desses ambientes:

* O sistema cria um **novo ambiente** com todas as configurações do arquivo.
* Todas as variáveis e configurações serão replicadas no novo ambiente.

**Validação pós-importação:**  
Após a importação, o usuário deve acessar o novo ambiente e conferir se todas as variáveis, credenciais e configurações estão corretas. Pode-se executar um teste rápido para validar que os projetos vinculados funcionam conforme esperado.

## **Cenário 2: Importação em um ambiente existente**

**Exemplo prático:**  
O usuário já possui um ambiente chamado `Produção` e deseja atualizar suas configurações usando o arquivo `Produção_Backup.json`:

* Variáveis que não existam no ambiente atual serão adicionados.
* Variáveis que existam no ambiente serão apresentadas como conflitos e não serão importadas.

**Resultado da importação:**

* O ambiente é atualizado com as novas variáveis.

**Validação pós-importação:**

* Acesse o ambiente atualizado e confira se todas as variáveis e configurações estão corretas.
* Execute os projetos vinculados para garantir que todas as dependências funcionem sem erros.

---

# Saiba mais

Sempre ao importar projetos de teste verifique também se está importando o ambiente relacionado com suas variáveis e configurações.

Sempre que possível, **importe primeiro os ambientes** antes de importar projetos de teste, garantindo que as variáveis e conexões necessárias já estejam configuradas.

# FAQ

**P: Quando importo em um ambiente existente todos os dados são sobrescritos?**

R: Para compartilhar configurações entre diferentes bases ou instalações do TOTVS Automação de Testes; para migrar ambientes entre filiais ou entre homologação e produção; e para reaproveitar configurações já existentes em novos projetos ou contextos.

**P: O que preciso validar após importar um ambiente?**

R: Confirme se todas as variáveis e configurações foram importadas corretamente. Execute um teste rápido para garantir que os projetos funcionem conforme esperado. Revise os grupos e permissões associados ao ambiente, caso aplicável.

**P: Posso editar o arquivo .json antes de importar?**

R: Sim, mas **não é recomendado**. Qualquer modificação incorreta pode gerar erros de leitura ou incompatibilidades na estrutura.  
O ideal é realizar alterações diretamente na ferramenta eexportar novamente o arquivo atualizado.
