---
content_hash: 8e5a31cd46b5e207568193998f52e9f0cdc9f0d87ae0b838b7e97137812c1fed
fetched_at: '2026-06-29T00:09:12.340113+00:00'
page_id: '417695323'
product: rm
source: tdn-rm
title: Utilizando o DBMonitor
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+o+DBMonitor
version: 27
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Este documento objetiva esclarecer como configurar o DBMonitor.

# Introdução:

---

O DBMonitor é uma ferramenta que fornece o monitoramento visual do seu banco de dados.

Ele executa o rastreio por componente de eventos do banco de dados, como Commit, Rollback, execução da instrução SQL e etc.

Atenção

O DBMonitor funciona somente para bancos de dados **Oracle**.

O DBMonitor é um aplicativo de terceiros (Devart) no qual disponibilizamos em nosso ambiente para facilitar o monitoramento do banco de dados.

O DBMonitor precisa ser executado na mesma máquina que o serviço que será monitorado.

# Configuração:

---

Para que o DBMonitor funcione, é necessário seguir os passos abaixo:

* Habilitar nos parâmetros globais do sistema a opção DbMonitor.

     Menu Ambiente | Parâmetros | Parâmetros Globais  
  
Acesse a guia Oracle e marque a opção Habilitar DbMonitor

Atenção

O DBMonitor **exibe** informações sensíveis como a *ConnectionString*do Banco de Dados, então sugerimos que está opção seja habilitada realmente quando existir a necessidade de realizar o monitoramento do Banco de Dados.

A partir da versão **12.1.34**, as informações da *ConnectionString* **NÃO serão mais visualizadas.**

É necessário reiniciar a aplicação após habilitar/desabilitar o parâmetro.

* Após habilitar o DbMonitor é necessário colocar a tag <add key="**DBMONITORENABLED**" value="True" /> no arquivo .Config do aplicativo que deseja monitorar o banco de dados (Exemplos: RM.Host.Service.exe.config, RM.Host.exe.config, RM.Host.JobRunner.exe.config) e reiniciar o serviço do host.

No exemplo estarei habilitando o DbMonitor no RM.Host.Exe.

xml










]]>

 Após estes passos basta inicializar o DBMonitor.exe que os dados serão exibidos.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.22 ou Superior

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

falseDownload

 O Arquivo executável do DbMonitor é disponibilizado no caminho C:\totvs\RM.NET\dbMonitor

250
