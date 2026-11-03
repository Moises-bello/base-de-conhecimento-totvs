---
content_hash: 8741429ae8a994bf68ebe7804a80eb239afee55364ea4666dbf671d58b705270
fetched_at: '2026-06-29T00:05:47.237662+00:00'
page_id: '1008231280'
product: rm
source: tdn-rm
title: Cache Centralizado - RM.Host.Cache
type: documentation
url: https://tdn.totvs.com/display/LRM/Cache+Centralizado+-+RM.Host.Cache
version: 9
---

# Sumário

---

Sumário|Revisão|Download dos arquivos

# 1 Introdução

      Este documento é um guia da utilização do executável **RM.Host.Cache** para utilização de **Cache centralizado utilizando Garnet** nos produtos da linha TOTVS RM. Dentre os benefício que o cache centralizado traz estão: racionalização de recursos de memória e eliminação de chaves duplicadas em instancias distintas de servidores de aplicação.

Download: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1233739>

---

## 1.1.  Instalação Automática do RM.Host.Cache

Após os download do instalador é necessário seguir os passos da execução.

**Passo a passo para realizar a execução:**

false.1° Passo:

Inserir caminho onde a pasta do arquivo será adicionada.

2° Passo:

Inserir a porta que o serviço irá utilizar

3° Passo:

Aguardar conclusão da instalação

4° Passo:

Após instalação, a pasta "rm-host-cache" será criada e o serviço RMHostCache será instalado na porta adicionada e iniciado automaticamente.

## 1.2.  Instalação manual do RM.Host.Cache no Windows

Pode ser executado ou instalado como serviço Windows;

* Pelo executável, basta iniciar o aplicativo.

* Para instalar como serviço é necessário abrir a linha de comando (CMD) como administrador e executar os comandos abaixo:

|  |
| --- |
| ``` sc create <NomeDoServiço> binPath= "C:\caminho\para\seu\aplicativo.exe" start= auto DisplayName= "<Nome de Exibição>" sc description <NomeDoServiço> "Descrição do serviço" sc failure <NomeDoServiço> actions= restart/60000/restart/60000/restart/60000 reset= 86400 sc start <NomeDoServiço>  Exemplos: sc create RMHostCache binPath= "C:\RM\RMHostCache\win-x64\publish\RM.Host.Cache.exe" start= auto DisplayName= "RM Host Cache" sc description RMHostCache "Cache centralizado do RM" sc failure RMHostCache actions= restart/60000/restart/60000/restart/60000 reset= 86400 sc start RMHostCache ```   **Exemplo:** |

## 1.3.  Instalação manual do RM.Host.Cache no Linux

Pode ser executado pelo terminal ou instalado como serviço;

* Para executar o aplicativo pelo terminal é necessário executar os seguintes comandos:

|  |
| --- |
| ``` cd <Diretório do aplicativo> ./<NomeDoAplicativo> ```   **Exemplo:** |

* Para instalar como serviço é necessário abrir o terminal e executar os comandos abaixo:

|  |  |
| --- | --- |
| **Criar arquivo do serviço:**  `sudo nano /etc/systemd/system/RM.Host.Cache.service`  **Adicionar as informações abaixo no arquivo e salvar (Ctrl + O):**   | [Unit] Description=`<Descrição do Aplicativo>` After=network.target  [Service] ExecStart=`<Diretório do Aplicativo>` WorkingDirectory=`<Diretório do Aplicativo>` Restart=always RestartSec=10 User=root StandardOutput=[append:/var/log/RM.Host.Cache.log](http://append/var/log/RM.Host.Cache.log)  [Install] WantedBy=multi-user.target | | --- |   **Exemplo:**  **Iniciar o serviço:**  sudo systemctl daemon-reload sudo systemctl enable RM.Host.Cache sudo systemctl start RM.Host.Cache  **Verificar se esta rodando:**  `systemctl status RM.Host.Cache` |

## 1.4.  Configuração do RM.Host.Cache

      O executável **RM.Host.Cache** é iniciado com base nas configurações do seu arquivo próprio de configuração "appsettings.json"

* **Mode:** Define a origem e o destino do tráfego de rede sendo:
  + Loopback (127.0.0.1): Somente local. O tráfego não sai da máquina e não é visível na rede.
  + Any (0.0.0.0): Global (dependendo da configuração do firewall).
* **Port:** Porta onde o serviço/executável será iniciado.

## 1.5.  Configuração no RM

a) Edite o arquivo RM.Host.Service.exe.config / RM.Host.exe.config e insira a tag abaixo.

|  |
| --- |
| ``` <add key="KVSCacheConfig" value="127.0.0.1:3278"/> ``` |

O **IP** adicionado em **value** deve ser o IP do servidor onde o RM.Host.Cache foi inicializado.

b) Reinicie o RM.Host.Service.exe / RM.Host.exe Realize esta configuração em todos os Servidores de App e Servidores de Job.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.2602 ou Superior

false

Cache Centralizado - **RM.Host.Cache**

falsefalse

**Status:** Em Andamento

false

**Data:**

false

**Autores:**

false 250
