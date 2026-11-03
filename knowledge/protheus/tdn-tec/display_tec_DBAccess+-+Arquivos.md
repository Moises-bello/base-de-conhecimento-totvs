---
content_hash: dab65f7f6c62a27c23fd94c7b26bc53b856c6ac4f75e0513b8e857fa33872d0d
fetched_at: '2026-07-02T19:24:21.533135+00:00'
page_id: '268575337'
product: protheus
source: tdn-tec
title: DBAccess - Arquivos
type: documentation
url: https://tdn.totvs.com/display/tec/DBAccess+-+Arquivos
version: 4
---

Arquivos do pacote de instalação

Este documento apresentará a estrutura de pastas, binários e dependências que o true possui.

## Ambientes Windowstrue

Em ambientes com o sistema operacional Windows, dada uma instalação padrão do true, temos o seguinte diagrama:

Detalhes:

Os sufixos dos arquivos podem variar de acordo com a arquitetura do pacote baixado. Exemplo:

* 32 bits = dbaccess
* 64 bits = dbaccess64

| Pasta/Arquivo | Descrição | Tipo |
| --- | --- | --- |
| .\client |  |  |
| .\client\dbapi.dll | Biblioteca *client* do true (deve ser utilizada para o true) | Release |
| .\client\debug |  |  |
| .\client\debug\dbapi.dll | Biblioteca *client* do true (utilizada apenas **para diagnóstico** e sob orientação do time de Tecnologia) | Debug |
| .\debug |  |  |
| .\debug\dbaccess64.exe | Executável do true (utilizado apenas **para diagnóstico** e sob orientação do time de Tecnologia) | Debug |
| .\debug\dbaccess64.pdb | Banco de símbolos de depuração | Debug |
| .\library |  |  |
| .\library\dbaccess64.dll | Executável do true Library (maiores informações ) | Release |
| .\library\debug |  |  |
| .\library\debug\dbaccess64.dll | Executável do true Library (utilizado apenas **para diagnóstico** e sob orientação do time de Tecnologia) | Debug |
| .\library\debug\dbaccess64.pdb | Banco de símbolos de depuração | Debug |
| .\tools |  |  |
| .\tools\dbaccesscfg.exe | Ferramenta para criação e configuração do arquivo de configuração do true via linha de comando (sem interface gráfica) | Release |
| .\dbaccess64.exe | Executável do true | Release |
| .\dbmonitor.exe | Executável do true | Release |
| .\monitor\_ru\_ru.qm | Arquivo de tradução |  |

## Ambientes Linuxtrue

Em ambientes com o sistema operacional Linux, dada uma instalação padrão do true, temos o seguinte diagrama:

Detalhes:

Os sufixos dos arquivos podem variar de acordo com a arquitetura do pacote baixado. Exemplo:

* x86 = dbaccess
* x86-64 = dbaccess64

| Pasta/Arquivo | Descrição | Tipo |
| --- | --- | --- |
| ./client |  |  |
| ./client/dbapi.so | Biblioteca *client* do true (deve ser utilizada para o true) | Release |
| ./client/debug |  |  |
| ./client/debug/dbapi.so | Biblioteca *client* do true (utilizada apenas **para diagnóstico** e sob orientação do time de Tecnologia) | Debug |
| ./library |  |  |
| ./library/dbaccess64.so | Executável do true Library (maiores informações ) | Release |
| ./library/debug |  |  |
| ./library/debug/dbaccess64.so | Executável do true Library (utilizado apenas **para diagnóstico** e sob orientação do time de Tecnologia) | Debug |
| ./multi |  |  |
| ./multi/dbaccess64 | Executável do true | Release |
| ./multi/debug/dbaccess64 | Executável do true (utilizado apenas **para diagnóstico** e sob orientação do time de Tecnologia) | Debug |
| ./tools |  |  |
| ./tools/dbaccesscfg | Ferramenta para criação e configuração do arquivo de configuração do true via linha de comando (sem interface gráfica) | Release |
| ./dbmonitor | Executável do true | Release |
| ./monitor\_ru\_ru.qm | Arquivo de tradução |  |

## Veja também

* [Procedimentos para teste com o build debug - Windows](https://tdn.totvs.com/display/tec/DBAccess+-+Perguntas+frequentes#DBAccess-Perguntasfrequentes-dbfaq3)
* [Procedimentos para teste com o build debug - Linux](https://tdn.totvs.com/display/tec/DBAccess+-+Perguntas+frequentes#DBAccess-Perguntasfrequentes-dbfaq4)
