---
article_id: 360041573894
category: TAF - eSocial - Atualização
content_hash: 2118180abefe450811b8d902e23c211b8450343e8bb8d79aeac8d64c0669c392
fetched_at: '2026-06-28T22:45:13.332346+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Atualização - UPDDISTR: Falha TOPCONN
  No conection: -2 ou -35'
type: support-article
updated_at: '2024-09-27T16:47:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041573894-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-UPDDISTR-Falha-TOPCONN-No-conection-2-ou-35
---

**Ocorrência**

**Verifique no console do atualizador se é apresentado:**

Warning - TOPCONN - No connection: **-2 - NO\_CONNECTION**  
**OU:**

Warning - TOPCONN - No connection: **-35 - NO\_DB\_CONNECTION**

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Causa**

Esse erro ocorre devido à arquitetura de 32 bits do DBAccess, exigindo uma conversão manual para 64 bits.

**Solução**

1. Acesse a pasta de instalação do TAF e exclua os arquivos com as extensões \*.TSK, \*.LOG e \*.OLD.

**Solução para Banco de Dados SQL Server:**

2. Configure o Administrador de Fonte de Dados ODBC em 64 bits:

   a. Execute *%WinDir%\System32\odbcad32.exe* para acessar a ferramenta Administrador de Fonte de Dados ODBC de 64 bits.

   b. Observação: O Administrador de Fonte de Dados ODBC na pasta SysWow64 é de 32 bits. Não configure esse Fonte de Dados ODBC!  
     
   (Para mais informações clique no link abaixo:  
   [Como criar uma fonte de dados para uso com Microsoft SQL Server](https://tdn.totvs.com.br/display/tec/DBAccess+-+Como+criar+uma+fonte+de+dados+para+uso+com+Microsoft+SQL+Server))
3. Verifique o driver a ser configurado e homologado pela TOTVS para conectar corretamente com o banco de dados SQL Server:   
   [Automação Fiscal - CONFIGURAÇÃO - Criando conexões via ODBC em 64 bits](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034281974)

**Solução para Banco de Dados Oracle:**

4. Certifique-se de que o Oracle Client na arquitetura de 64 bits esteja instalado em seu servidor. Se não estiver configurado, acesse o site da Oracle e baixe a versão correspondente.
5. Configure o ORACLE para o sistema TAF:   
   [Automação Fiscal- CONFIGURAÇÃO - Criando conexão com banco Oracle](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035186814)
6. Configure o arquivo OCI.DLL no arquivo dbaccess.ini, na seção [ORACLE], verificando o caminho da DLL do Oracle Client de 64 bits.   
     
   **Exemplo:**

   [ORACLE] ClientLibrary= D:\oracle\oracle\client\_1\oci.dll

(Para saber mais sobre as conexões com o oracle clique no link abaixo:  
[Como configurar o DBAccess para utilizar o Oracle com OCI](https://tdn.totvs.com.br/display/tec/DBAccess+-+Como+configurar+o+DBAccess+para+utilizar+o+Oracle+com+OCI))

**Conversão e Atualização do DBAccess para 64 Bits:**

7. Se o serviço de DbAccess de 64 bits não existir, crie-o:

   * [Automação Fiscal - DBACCESS - Alterar serviço TAF-DBAccess de 32bits para 64bits](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042045853)
8. Se o serviço de 64 bits já existir, atualize o DBAccess para a versão mais recente:

   * [Automação Fiscal - ATUALIZAÇÃO - Como atualizar o DBAccess para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034522854)
9. Teste a conexão com o banco de dados conforme detalhado no artigo:

   * [Automação Fiscal - CONFIGURAÇÃO - Criando e/ou testando conexões com o DBAccess para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574)

Essas etapas devem resolver o problema de conexão indisponível no Console do Atualizador. Certifique-se de seguir cada etapa com cuidado para garantir o sucesso da solução.
