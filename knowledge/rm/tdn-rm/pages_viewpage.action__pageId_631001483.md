---
content_hash: 162b54438fdb4994b4ec9211cd059f404f1938a6c0370c601971d59625ee8cf9
fetched_at: '2026-06-29T00:11:05.422815+00:00'
page_id: '631001483'
product: rm
source: tdn-rm
title: Configuração exclusiva para produtos que ainda possuem dependências em Delphi.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=631001483
version: 25
---

Para utilização dos aplicativos Delphi da Linha RM com Oracle 19c é necessário cumprimento dos pré-requisitos listados abaixo, caso não utilize o Delphi a instalação do Client Oracle deverá ser a respectiva versão instalada de acordo com a portabilidade.

**1º  ITEM**- Permitir login com versão do Oracle 10g

No servidor de banco de dados, ir até o arquivo sqlnet.ora do listener e inserir os seguintes parâmetros:

Exemplo do caminho padrão : C:/ORA19C/APP/network/admin

**SQLNET.ALLOWED\_LOGON\_VERSION\_SERVER=10**

**SQLNET.ALLOWED\_LOGON\_VERSION\_CLIENT=10**

***Obs**. Este arquivo fica no home do Oracle, uma dica para localizar qual arquivo está sendo usado é executar o comando* **TNSPING nome\_do\_servico\_oracle,** *por exemplo TNSPING EXEMPLO12133DEV*

**2º ITEM** - Verificar se usuário RM tem compatibilidade de senha com o 10G

Esta informação pode ser verificada com o *select* abaixo:

**SELECT USERNAME,PASSWORD\_VERSIONS FROM DBA\_USERS WHERE USERNAME='RM';**

Caso tenha a compatibilidade com o 10G acima mencionada, os aplicativos Delphi  podem ser usados no oracle 19C.

Caso não tenha, segue o roteiro a ser adotado:

**Passo 1**- Desabilitar sensibilidade de senha, para isso execute o seguinte comando abaixo:

alter system set sec\_case\_sensitive\_logon = false scope=both;

**Passo 2** - Reiniciar o listener com os comandos: *"lsnrctl stop"* e *"lsnrctl start"* (se necessário, entrar no banco de dados e executar o comando *"alter system register"* para que o Oracle configure as entradas no listener através da verificação de status "lsnrctl status ").

**Passo 3**- Pronto agora podemos alterar a senha do user 'rm'. Exemplo de alteração de senha por exemplo:

*alter user RM identified by **rm**;*

**Passo 4** *- Desbloquear o usuário rm para ter acesso ;*

*alter user rm identified by rm account unlock;*

**Passo 5**- Verificar novamente se o usuário tem compatibilidade com o 10G:       RM **10G** 11G 12C:

**SELECT USERNAME,PASSWORD\_VERSIONS FROM DBA\_USERS WHERE USERNAME='RM';**

**SHOW PARAMETER SEC\_CASE\_SENSITIVE\_LOGON**

**Obs.** Após os passos acima, o usuário passará a ter a compatibilidade com o 10G;

**3º ITEM** - Utilização do Oracle Client 11g (**Versão máxima**)

Os aplicativos Delphi demandam o uso do Oracle Client na versão 11.2.0.4, mesmo em uso do Oracle Server 19c.

**Informações complementares:**

**Caminho para baixar o Oracle Client 11.2.04:**

Oracle 11g 32Bits: <https://suporte.totvs.com/portal/p/10098/download?e=1022083>

Oracle 11g 64Bits: <https://suporte.totvs.com/portal/p/10098/download?e=1022084>

**Descobrindo a versão do client Oracle na máquina**

Basta seguir os seguintes passos:

1) Abra o prompt de comando do windows;

2) Digite sqlplus

A informação em destaque é a versão do Oracle Client da máquina.
