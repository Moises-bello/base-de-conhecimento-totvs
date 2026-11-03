---
content_hash: de5ea64d6d841b5858e70d40cee9602438954f14e95764e81cde670be1235a42
fetched_at: '2026-06-29T00:08:40.848610+00:00'
page_id: '286511036'
product: rm
source: tdn-rm
title: Smart Client RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Smart+Client+RM
version: 8
---

O Smart Client RM nada mais é que o mesmo RM.exe utilizado nos ambientes locais e três camadas, e utiliza protocolo TCP ou HTTP para se comunicar com o servidor de aplicação, o Host.

Versões anteriores à 12 fazem necessária a utilização do TS para utilizar o RM, por três motivos:

1. Algumas telas ainda estão em Delphi.
2. A comunicação entre o RM.exe e o Host é muito pesada e exige muito em relação ao consumo de banda.
3. A atualização da parte client é manual, ou seja, a cada atualização de patch ou release, as estações de trabalho precisam ser atualizadas manualmente.

A versão 12 trouxe novas implementações que eliminam a necessidade do uso de TS, são elas:

1. \*Mais telas foram migradas para tecnologia .NET, a mesma do RM.exe.
2. \*\*A comunicação entre o RM.exe e o Host sofreu bastante evolução, como a redução considerável do tamanho dos pacotes, compactação eficaz dos dados trafegados e otimização das chamadas ao servidor de aplicação.
3. Criação do mecanismo de download do client RM sem a necessidade de instalador.
4. Criação do mecanismo de update automático do servidor de aplicação e do client (RM.exe).
5. Melhorias no cockpit para trabalhar em ambientes distribuídos e remotos.

Informações para Windows 7 (Obsoleto)Observação

Para a execução de TLS 1.1 e 1.2 no Windows 7 é necessário adicionar os registros abaixo, visto que são os protocolos de comunicação ativos atualmente e que por padrão não são ativos na versão Windows7:

Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]  
"DisabledByDefault"=dword:00000000

**Arquivo disponível para download:** [Arquivo.reg](https://tdn.totvs.com/download/attachments/215482828/arquivo.reg?version=1&modificationDate=1590091618463&api=v2)

**\* Não é possível utilizar o Smart Client RM para funcionalidades ainda em Delphi.**

**\*\* Para uma boa experiência de uso, é recomendado que a latência máxima de rede entre a estação de trabalho e o servidor seja de no máximo 60 milissegundos e a largura de banda média por usuário seja de no mínimo 256 Kbps.**

Segue uma simples ilustração do resultado dessa evolução:

* Nas versões anteriores a 12 havia a necessidade da camada de TS, conforme ilustração abaixo:

* Na versão 12 a camada de TS não se faz necessária, desde que a rede atenda aos requisitos mínimos.  
  Desta forma o RM.exe se comunica diretamente com o Host sem a necessidade de um protocolo RDP:

Acesse o link abaixo e veja a documentação sobre o TOTVS Update, fundamental para utilização do Smart Client RM:

[TOTVS Update](http://tdn.totvs.com.br/display/LRM/Configurando+o+Smart+Client+RM+e+TOTVS+Update)
