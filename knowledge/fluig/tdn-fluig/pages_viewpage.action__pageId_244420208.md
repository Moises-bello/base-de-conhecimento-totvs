---
content_hash: 82967067209fc6d84faaf1413373a79d5fd4320e24b67f5c56a095dba1d22ed1
fetched_at: '2026-06-28T21:35:23.155468+00:00'
page_id: '244420208'
product: fluig
source: tdn-fluig
title: ARQ - Por que ao iniciar o serviço do fluig ocorre o erro 'Local hostname not
  found, check the file “hosts”'?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244420208
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.5.10 ou superior

# Ocorrência

Ao inicializar o serviço do fluig, o sistema não sobe e o log registra a mensagem abaixo. O que devo fazer para o serviço do fluig subir?

xmlEclipseMensagem em log

# Causa

O *hostname* (nome da máquina) do servidor não foi adicionado ao arquivo *hosts*. A falta desta configuração pode causar uma série de problemas na utilização da plataforma, por isso a inicialização é interrompida.

# Solução

Adicionar o *hostname* no arquivo *hosts* do sistema operacional apontando para o IP da própria máquina (*loopback*). No exemplo abaixo, o IP local é "127.0.1.1" e o *hostname* é "servidor-fluig":

Exemplo de arquivo hosts no Windowstrue

# Observação

* No Windows, este arquivo fica armazenado no diretório C:\Windows\System32\drivers\etc\hosts.

* No Linux, o caminho padrão é /etc/hosts. Para descobrir o *hostname* de um servidor Linux, utilize o comando: **cat /etc/hostname**.
