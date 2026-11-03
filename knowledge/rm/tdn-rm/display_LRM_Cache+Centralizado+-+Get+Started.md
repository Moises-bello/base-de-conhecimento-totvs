---
content_hash: 2fb1d3c458eb7549a46c9f0d1cc2320da44af23dde743a3634bd7877faa74f48
fetched_at: '2026-06-29T00:08:54.980074+00:00'
page_id: '348295831'
product: rm
source: tdn-rm
title: Cache Centralizado - Get Started
type: documentation
url: https://tdn.totvs.com/display/LRM/Cache+Centralizado+-+Get+Started
version: 21
---

# Sumário

---

Sumário|Revisão|Download dos arquivos

# Revisão

---

|  |  |  |
| --- | --- | --- |
| Versão do Documento | Modificação | Autor / Revisor |
| 1.0 - 28/03/2018 | Criação do documento | / |
| 1.1 - 02/04/2018 | Alteração do documento | / |

.panelContent, .panelContent p, .panelContent p span{
color: white !important;
background: #202020 !important;
}
]]>

# 1 Instalação

---

## 1.1.  Instalando o Docker

---

|  |
| --- |
| **Windows Server 2016 ou Windows 10** |
| **a)** Clique no link e baixe o instalador : **[download.docker.com/win/stable/Docker for Windows Installer.exe](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe).** |
| **b)** Siga as instruções do **Wizard,** aceite a licença, e então prossiga com a instalação. Em seguida clique em **Finish** |
| **c)** No menu **iniciar,** execute o programa **Docker for Windows** |
| **d)** Quando o ícone da **baleia** aparecer na **barra de status,** o **Docker** está rodando e pronto para ser usado. |
| **e)** **Certifique que o container seja linux,** a instalação padrão sobe o docker em container windows. |

Veja mais sobre "Instalando Docker no Windows 7"

|  |
| --- |
| **Windows 7** |
| **a)** Clique no link e baixe o instalador: **[download.docker.com/win/stable/DockerToolbox.exe](https://download.docker.com/win/stable/DockerToolbox.exe)** |
| **b)** Siga as instruções do **Wizard,** prossiga com a instalação.Em seguida clique em **Finish** |
| **c)** No menu **iniciar,** execute o programa **Docker Quickstart Terminal** |
| **d)** Aguarde até que você veja uma tela como esta |
| **e)** Após isso, abra o **Oracle VirtualBox,** selecione o **SO Default** instalado juntamente com o **Docker,** clique em **configurações.** |
| **f)** No menu **Rede,** vá em **Adaptador 1,** clique no **botão "Redirecionamento de Portas".** |
| **g)** Adicione uma linha com as **"rules" (regras)** do **Redis.** |

## 1.2.  Rodando o Redis via Docker

---

a) Abra uma sessão do Powershell (window + R | powershell)

b) Execute o comando abaixo

docker run -d -p 6379:6379 --name redis-1 [docker.io/redis:4.0.8-alpine](http://docker.io/redis:4.0.8-alpine) redis-server --appendonly yes

Você deve ver um resultado parecido com este:

# 2 Configurando o Totvs RM

---

a) Edite o arquivo RM.Host.Service.exe.config e insira as chaves abaixo. Informe o **IP** e **PORT** com os valores da máquina onde foram instalados.

<add key="KVSCacheConfig" value=" **IP:PORT**” />

b) Reinicie o RM.Host.Service. Realize esta configuração em todos os Servidores de App e Servidores de Job.

# Download dos arquivos

---

Download arquivo DOCX

Realize o download do documento

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superior

false

Cache Centralizado - **Get Started**

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false 250
