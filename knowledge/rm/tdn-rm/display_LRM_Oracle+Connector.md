---
content_hash: 2bc5b18b9d91904cc6b4e49e6d9f87cb654acc565ed28548c01cdd89a30b59bd
fetched_at: '2026-06-29T00:05:49.846351+00:00'
page_id: '1042908602'
product: rm
source: tdn-rm
title: Oracle Connector
type: documentation
url: https://tdn.totvs.com/display/LRM/Oracle+Connector
version: 5
---

# 📘 MANUAL DO USUÁRIO

O **Oracle Connector** é uma ferramenta desenvolvida para facilitar o gerenciamento de **Pluggable Databases (PDBs)** em ambientes Oracle, com foco específico na administração de instâncias para o sistema **Totvs RM**.

A aplicação automatiza tarefas complexas de banco de dados por meio de uma **interface gráfica amigável**, simplificando operações administrativas.

---

# 🔌 1. Conexão com o Banco de Dados

Esta é a primeira etapa para utilizar o sistema.  
A área de conexão permite configurar como a aplicação se comunicará com o servidor Oracle.

false

## ⚙️ Campos de Configuração

**Servidor/Instância:**  
Campo para inserir o endereço do servidor e a instância (CDB).  
Exemplo: `localhost/ORCL` ou `192.168.0.10/CDB1`.  
O sistema mantém um histórico das últimas conexões utilizadas.

**Usuário e Senha:**  
Credenciais de acesso ao banco.  
Recomenda-se o uso de usuários com privilégios elevados (ex: SYS).

**AS SYSDBA:**  
Checkbox obrigatória para a maioria das operações administrativas (criar, clonar e deletar PDBs).  
Conecta com privilégios de administrador do sistema.

**Salvar Inst. / Salvar Usu.:**  
Permite memorizar o servidor e o usuário para o próximo uso.  
Por segurança, a senha não é salva.

**Caminho Backup:**  
Define o diretório no servidor onde os arquivos de backup (.dmp) serão gravados.

false

⚠️ **Importante:**  
Este deve ser um caminho absoluto válido dentro do servidor onde o Oracle está rodando.  
Exemplo: `C:\Oracle\Backups` ou `/u01/backups`.

# 🗂️ 2. Gerenciamento de PDBs

Após conectar, a lista de PDBs será carregada na grade principal.  
Selecione um PDB na lista para habilitar os botões de ação descritos abaixo.

false

## 🔄 Atualizar

Recarrega a lista de PDBs, exibindo o status atual (**OPEN\_MODE**) de cada banco.

Use esta função para:

* Verificar se uma operação foi concluída
* Conferir mudanças de estado

---

## 🐑 Clonar (Clonagem Local)

Cria uma cópia exata de um PDB existente na mesma instância.

### 🔄 Processo

O sistema:

* Solicita o nome do novo PDB
* Coloca o PDB de origem em modo **READ ONLY** temporariamente (se necessário)
* Realiza a cópia
* Reabre ambos os bancos

### 📌 Uso

Ideal para criar ambientes de teste rápidos baseados em uma base de produção ou homologação.

---

## 🌐 Clonagem Remota

Permite copiar um PDB de um servidor para outro servidor diferente.

### ⚙️ Requisitos

É necessário possuir pelo menos **2 conexões salvas** na lista de servidores (origem e destino).

### 🔄 Processo Automatizado

O sistema:

* Cria usuários de clonagem (**C##CLONE\_USER**) na origem e no destino
* Configura automaticamente o **Database Link** necessário
* Realiza a transferência e criação do PDB no servidor de destino

---

## 🚦 Estado

Altera o modo de operação do PDB selecionado.

### Opções disponíveis:

**READ WRITE (Open):**  
Modo normal de uso. O banco está aberto para leitura e escrita.

**READ ONLY:**  
O banco está acessível apenas para leitura.  
Obrigatório para algumas operações de clonagem manual.

**MOUNTED (Closed):**  
O banco está montado, porém fechado para conexões de usuários.

---

## 📦 Backup RM

Ferramenta específica para backup lógico de ambientes **Totvs RM**.

### 💾 O que faz

Executa um **Data Pump Export (expdp)** focado especificamente no schema RM.

### ⚙️ Automação

* Filtra automaticamente estatísticas problemáticas
* Gera o arquivo `.dmp` no diretório configurado em **Caminho Backup**

---

## ♻️ Restaurar

Cria um **NOVO PDB** a partir de um arquivo de backup (.dmp).

### 🎯 Foco Totvs RM

Além de importar os dados, a função prepara todo o ambiente necessário para o Totvs RM:

* Cria automaticamente as Tablespaces padrões (RM\_DADOS, RM\_INDICES, etc.)
* Cria os usuários de sistema (RM, TOTVSAUDIT, etc.)
* Aplica permissões (Grants) e sinônimos específicos exigidos pelo sistema RM

false

⚠️ **Atenção:**  
O arquivo `.dmp` selecionado no seu computador deve estar acessível pelo servidor Oracle (ex: em uma pasta local do servidor ou em um compartilhamento de rede mapeado da mesma forma).

## ❌ Deletar

Exclui permanentemente um PDB e todos os seus arquivos de dados (Datafiles).

🔍 **Segurança:**  
Exige confirmação explícita do usuário.  
O sistema se encarrega de fechar o PDB antes de excluí-lo.

# 🛠️ 3. Outras Funcionalidades

## 🔗 Copiar String de Conexão

Ao clicar com o botão direito em um PDB na lista, é possível copiar a **Connection String sugerida**.

Isso facilita a configuração de:

* Arquivos `.config`
* Conexões em outras ferramentas (como SQL Developer)

---

## 📜 Logs de Operação

Na parte inferior da janela, um painel de logs exibe em tempo real:

* Todas as ações executadas
* Comandos SQL enviados
* Respostas do servidor

É útil para auditoria e para análise de eventuais erros de processo  
(ex: *"Table or view does not exist"*).

---

false

## 🧩 Nota Técnica

Esta aplicação foi construída para rodar em ambientes **Windows** e requer o **Oracle Client** ou drivers gerenciados instalados/embutidos para comunicação com o banco de dados.
