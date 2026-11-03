---
content_hash: 5559e24ee5789ccf905ad8e6a5b5529d8ca83bca5cf4108cbbb09795f02f17bf
fetched_at: '2026-06-29T00:10:26.844722+00:00'
page_id: '514751005'
product: rm
source: tdn-rm
title: Instalador do TReports por linha de comando
type: documentation
url: https://tdn.totvs.com/display/LRM/Instalador+do+TReports+por+linha+de+comando
version: 6
---

# Objetivo

Os parâmetros de instalação do TReports têm como objetivo otimizar o processo de instalação do produto, que tornará a instalação mais rápida e fácil, diminuindo a interação do instalador com o usuário.

# Como utilizar os parâmetros

Para maiores detalhes de como instalar utilizando parâmetros na linha de comando consulte a página de .

# Instalação

### Opções de exibição:

/VERYSILENT

* Modo silencioso, sem interação do usuário

### Parâmetros:

TReports

**Os parâmetros são case-insensitive**

| TOTVS Update | | | |
| --- | --- | --- | --- |
| **Parâmetro** | **Opção** | **Padrão** | **Explicação** |
| /DIR | Caminho do diretório | C:\TOTVS | Caminho onde será efetuada a instalação |
| /treports | (0 ou 1) | 1 | Define se será definido um SGBD para o Treports |
| /rac | (0 ou 1) | 1 | Define se o RAC será instalado |
| /TR\_SGBD | (Oracle ou SqlServer) | SqlServer | Tipo de SGBD para o Treports |
| /TR\_DBServer | obrigatório |  | Endereço do servidor do SGBD do Treports |
| /TR\_DBName | obrigatório |  | Nome do banco de dados  do SGBD do Treports |
| /TR\_DBUser | obrigatório |  | Usuário do SGBD do Treports |
| /TR\_DBPassword | obrigatório |  | Senha do SGBD do Treports |
| /licenseServerIP | obrigatório |  | Endereço do servidor do License Server |
| /licenseServerPort | obrigatório |  | Porta do servidor do License Server |
| /RAC\_SGBD | (Oracle ou SqlServer) | Oracle | Tipo de SGBD para o RAC |
| /RAC\_DBServer | obrigatório |  | Endereço do servidor do SGBD do RAC |
| /RAC\_DBName | obrigatório |  | Nome do banco de dados  do SGBD do RAC |
| /RAC\_DBUser | obrigatório |  | Uuário do SGBD do RAC |
| /RAC\_DBPassword | obrigatório |  | Senha do SGBD do RAC |
| /TR\_PORT | [1 - 65535 ] | 80 | Porta do IIS |
| /TR\_Tenant | texto | treports | Tenant do IIS |
| /TR\_DNS | opcional |  | DNS do IIS |

**Exemplo EXE:** C\treports.exe **/DIR="CAMINHO\_DIRETORIO" /treports=1 /rac=1 /TR\_SGBD="TPOD\_SERVIDOR" /TR\_DBServer="NOME\_DO\_SERVIDOR" /TR\_DBName="NOME\_DA\_BASE" /TR\_DBUser="USUARIO" /TR\_DBPassword="SENHA" /licenseServerIP="IP\_DO\_LICENSE\_SERVER" /licenseServerPort="PORTA" /RAC\_SGBD="TIPO\_SERVIDOR" /RAC\_DBServer="NOME\_DO\_SERVIDOR" /RAC\_DBName="NOME\_DA\_BASE" /RAC\_DBUser="USUARIO" /RAC\_DBPassword="SENHA" /tr\_port="PORTA\_DO\_IIS" /tr\_tenant="TENANT" /tr\_dns="[http://](http://tenant)DNS\_DO\_TENANT" /RAC\_IP="IP\_DO\_SERVIDOR\_RAC" /RAC\_PORT="PORTA\_DO\_SERVIDOR"** /VERYSILENT
