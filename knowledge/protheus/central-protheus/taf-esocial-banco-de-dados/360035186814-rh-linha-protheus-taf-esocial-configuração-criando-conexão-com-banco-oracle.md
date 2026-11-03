---
article_id: 360035186814
category: TAF - eSocial - Banco de dados
content_hash: d584e08e81a769968fc1b28fd5ef100f99f418d395bb11eaae2f5dc97963e6bd
fetched_at: '2026-06-28T22:45:11.573767+00:00'
product: protheus
section_id: 1500001536801
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial -  CONFIGURAÇÃO - Criando conexão com banco
  Oracle
type: support-article
updated_at: '2024-09-25T12:03:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035186814-RH-Linha-Protheus-TAF-eSocial-CONFIGURA%C3%87%C3%83O-Criando-conex%C3%A3o-com-banco-Oracle
---

**Dúvida**Como configurar o banco o TAF para conexão com o banco Oracle?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

1. **Configuração de Variáveis de Ambiente no Windows:**

   * Abra as propriedades do sistema no Windows.
2. **Acesso às Variáveis de Ambiente:**

   * Na janela de propriedades do sistema, clique na aba "Avançado" e então no botão "Variáveis de Ambiente".  
     ![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045741414)
3. **Adição de Nova Variável:**

   * Na seção "Variáveis de sistema", clique no botão "Novo" para adicionar uma nova variável.  
     ![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360046598813)
4. **Configuração da Variável TNS\_ADMIN:**

   * Digite "TNS\_ADMIN" no campo "Nome da variável".
   * No campo "Valor da variável", insira o caminho completo para a pasta do Oracle 64 bits.
   * Clique em "OK" para confirmar a criação da variável.  
       
     ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072904673)
5. **Validação da Configuração:**

   * As variáveis necessárias para a conexão estão agora configuradas no sistema.
   * Você pode validar a conexão utilizando o DBMonitor.

**Observação:** Não é necessário configurar o ODBC para bancos Oracle.

6. **Edição do Arquivo dbaccess.ini:**

   * Abra o arquivo "dbaccess.ini".
   * Navegue até a seção [ORACLE].
7. **Configuração do Parâmetro ClientLibrary:**

   * Dentro da seção [ORACLE], localize o parâmetro "ClientLibrary".
   * Defina o valor desse parâmetro como o caminho completo para a biblioteca OCI.DLL do Oracle.  
       
     **Por exemplo:**

     ```
     [ORACLE]
     ClientLibrary=<Caminho_completo_para_oci.dll>   
     (Ex.:D:\oracle\oracle\client_1\oci.dll)
     ```
8. **Teste da Conexão:**

   * Após realizar as configurações acima, realize um teste de conexão com o banco de dados Oracle:
     + Acesse a opção "TAF - CONFIGURAÇÃO" no menu.
     + Siga as instruções para criar e testar conexões com o DBAccess.

Ao seguir esses passos, você configurará com sucesso o TAF para estabelecer uma conexão com o banco de dados Oracle no ambiente especificado. Certifique-se de seguir as etapas com atenção para garantir uma configuração correta e bem-sucedida.
