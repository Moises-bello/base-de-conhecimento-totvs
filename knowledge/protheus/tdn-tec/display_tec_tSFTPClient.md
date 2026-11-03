---
content_hash: bafb36d273584d248c5cd84d4b9a1c21b343554418bd819e791a673e575d90ae
fetched_at: '2026-07-02T19:24:28.544434+00:00'
page_id: '799251913'
product: protheus
source: tdn-tec
title: tSFTPClient
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient
version: 5
---

O SFTP, ou Secure File Transfer Protocol, é um protocolo seguro para transferência de arquivos diversos, confidenciais ou não, entre computadores, servidores e dispositivos de armazenamento em nuvem, que faz uso do protocolo SSH (Secure Shell) para criptografar todos os dados transferidos. Isso torna o SFTP uma opção muito mais segura do que outros protocolos de transferência de arquivos como FTP ou HTTP.

É possível utilizar a Classe tSFTPClient, disponível na linguagem TLPP, para implementar funcionalidades equivalentes a Classe tFTPClient, disponível na linguagem em ADVPL, de forma mais segura e eficiente.

## Certificados de Login

Para gerar certificados de Login, é importante atentar-se a estes procedimentos:

## Configuração

No arquivo de configurção INI do Application Server (appserver.ini), segue um exemplo de como configurar algumas chaves utilizadas especificamente pela Classe TSFTPClient:

```
[SFTP]
privatekey   = D:\Keys\SFTPDEV_PREFERED\withpass\id_rsa
publickey    = D:\Keys\SFTPDEV_PREFERED\withpass\id_rsa.pub
certpassword = m1nh4S3nH4fl3!SXHL3SSD
ShellExec    = 1
```

As descrições de cada chaves da sessão SFTP:

* PRIVATEKEY é utilizada para configurar o caminho do arquivo referente a chave privada localizado no servidor.
* PUBLICKEY é utilizada para configurar o caminho do arquivo referente a chave pública localizado no servidor.
* CERTPASSWORD é a senha da chave pública. Se não existir, basta omiti-la.
* SHELLEXEC Permite habilitar o recurso de envio de comandos diretamente para o prompt de comandos do servidor SFTP remoto. Valores aceitos: 0-Inativo (Padrão) / 1-Ativo.

## Autenticação

O SFTP suporta dois métodos de autenticação:

Autenticação via senha: A autenticação via senha é o método mais comum de autenticação SFTP. Requer que o usuário forneça um nome de usuário e uma senha para acessar o servidor SFTP.

Autenticação via chave pública: A autenticação via chave pública é uma maneira mais segura de autenticar em um servidor SFTP que requer a criação de uma chave pública e uma chave privada. A chave pública é enviada ao servidor SFTP e a chave privada é mantida pelo usuário.

A autenticação via chave pública é mais segura do que a autenticação via senha pois não requer o envio de senha para o servidor SFTP, tornando mais difícil para um invasor roubar a senha.

## Vantagens do SFTP

Segurança: Usa criptografia para proteger todos os dados transferidos.

Confiabilidade: Protocolo confiável que fornece transferências seguras e consistentes de arquivos.

Flexibilidade: Pode ser usado para transferir arquivos entre diferentes sistemas operacionais e dispositivos.

## Desvantagens do SFTP

Velocidade: Pode ser um pouco mais lento do que outros protocolos de transferência de arquivos como o FTP.

Complexidade: Pode ser um pouco mais complexo de configurar e usar do que outros protocolos de transferência de arquivos. Requer o uso do servidor OpenSSH para prover o acesso SFTP através da camada SSH.

## Métodos da Classe SFTP

## Disponibilidade

Esta classe está disponível a partir da versão 20.3.2.1 do Application Server
