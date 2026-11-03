---
content_hash: 527a71a6246afb6b445c393911ef6a2ab02902dab2d6fe6fdbd1894002027203
fetched_at: '2026-06-29T00:08:06.575264+00:00'
page_id: '236593839'
product: rm
source: tdn-rm
title: Configurando Impressora para acesso Network Service Account em Windows Server
  2008
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurando+Impressora+para+acesso+Network+Service+Account+em+Windows+Server+2008
version: 31
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é demostrar o processo de configuração de impressora em servidores de Job.

# Introdução:

---

       Para geração de alguns relatórios contábeis e financeiros é necessário a instalação de uma impressora nos servidores que executam Job. Nesta configuração é necessário que o usuário configurado no "RM. Host" possua permissão de acesso a impressora.

falseObservação:

As configurações abaixo também se aplicam para ambientes locais.

      Para realizar a configuração da impressora execute os passos do processo a seguir.

falseObservação:

É necessário instalar o serviço do Host com um usuário que seja administrador de rede.

# Processo de configuração da impressora Windows Server 2008:

---

falseConfiguração Impressora:

**Processo de Configuração:**

1º Passo:

* Acesse a Ferramenta “Server Manager” do Windows

2º Passo:

**Instale a role Print Services:**

* Acesse "Roles | Add Roles".

* Em seguida selecione "Server Roles" e marque a opção "Print and Document Services".

* Selecione a opção "Confirmation" e clique em "Install".

* Clique em "Results" e confirme que a instalação foi realizada com sucesso.

3º Passo:

* Acesse "Administrative Tools", selecione a opção "Print Management". Em seguida remova todas as impressoras locais.

4º Passo:

* Depois de remover as impressoras adicione uma nova acessando "Printer | Add Printer".

5º Passo:

* Marque a opção "add a new printer using an existing port" e selecione a porta "LPT1: (Printer Port)".

6º Passo:

* Marque a opção "Use an existing printer driver on the computer" e selecione a opção "Microsoft XPS document writer".

7º Passo:

* Desmarque a opção "Share this printer"

8º Passo:

* Acesse a propriedade da impressora criada e adicione permissão para o usuário "Network Service" ou o usuário utilizado para iniciar o serviço RM.

9º Passo:

* Acesse o Painel de Controle / Dispositivos e Impressoras. Selecione a impressora criada e a defina como padrão, em seguida reinicie o Serviço do RM.

# Processo de configuração da impressora Windows Server 2012:

---

falseConfiguração Impressora:

**Processo de Instalação:**

1º Passo:

**Acesso:**

* Acesse a Ferramenta “Server Manager” do Windows

2º Passo:

**Instalar a role Print Services:**

* Clique em "Add roles and features".

* Em seguida ao ser carregada a tela selecione "Server Roles" e marque a opção "Print and Document Services (Installed)".

* Na tela seguinte de "Add Roles and Features Wizard", marque a opção "include management tools (if applicable)" e clique em "Add Features".

3º Passo:

**Remover todas as impressoras já configuradas no Windows:**

* Acesse o painel de controle e abra a ferramenta "Administrative Tools".

* Selecione a opção "Print Management".

* Selecione a opção "Printers" e remova todas as impressoras instaladas. Feito isso Reinicie a micro.

4º Passo:

**Adicionar impressora local no servidor:**

* Para adicionar uma impressora acesse "Printer | Add Printer".

* Marque a opção "add a new printer using an existing port" e selecione a porta "LPT1: (Printer Port)".

* Marque a opção "Use an existing printer driver on the computer" e selecione a opção "Microsoft XPS document writer".

* Desmarque a opção "Share this printer"

* Avance a etapa "Printer Found" e finalize o processo.

5º Passo:

**Liberar permissão de segurança para (“Todos | Everyone” da rede) e para (“Network Service” da máquina loca) para impressora adicionada.**

* Acesse a propriedade da impressora, criada e adicione permissão para o usuário "Network Service" ou o usuário utilizado para iniciar o serviço RM.  
    
  Exemplos do processo abaixo:

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** Configuração de Impressora

falsefalse

**Status:** Finalizado

false

**Data:** 12/05/2016

false

**Autores:**
