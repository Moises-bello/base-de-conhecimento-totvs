---
article_id: 360034395574
category: TAF - eSocial - DBAccess
content_hash: 1d5f2cd30b720a67d24de0784f2c56406600428a15d91b31ffeef89216adb91f
fetched_at: '2026-06-28T22:45:12.424734+00:00'
product: protheus
section_id: 1500001536981
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - CONFIGURAÇÃO - Criando e/ou testando
  conexões com o DBAccess para o TAF
type: support-article
updated_at: '2026-06-26T11:16:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574-RH-Linha-Protheus-TAF-eSocial-CONFIGURA%C3%87%C3%83O-Criando-e-ou-testando-conex%C3%B5es-com-o-DBAccess-para-o-TAF
---

**Dúvida**

Como criar e testar a conexão da aplicação TAF com o Banco de Dados usando o DBAccess?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Todas as versões.

**Solução**

1. Acesse o diretório do TAF-DBAccess, que geralmente está localizado no mesmo diretório de instalação do TAF. Localize o arquivo executável ***dbmonitor.exe*** e execute-o para abrir o aplicativo.   
     
   **Exemplo:** *C:\totvs\TAF\TafDbAccess64:*  
   ![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045437813)
2. Ao executar o aplicativo dbmonitor.exe, digite o nome do servidor ou o endereço IP onde o ODBC está configurado para a conexão com o banco de dados. Em seguida, insira a porta de configuração. Para verificar em qual porta a configuração está, consulte a dica abaixo da imagem:  
   ![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045460553)

   **Dica:** No diretório do TAF-DBAccess, localize o arquivo dbaccess.ini e procure pela seção [GENERAL]. Verifique qual porta o serviço está utilizando:  
   ![13.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045445653)

   **Obs.:** Se o arquivo dbaccess.ini não especificar a porta, as portas padrão usadas pelo DBAccess são 4016, 7890 ou 7999.
3. Após verificar as configurações conforme mencionado acima, clique em "OK". Será exibida a seguinte tela:  
   ![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044589214)
4. Na aba Configurações, verifique qual banco de dados você utiliza para guardar as informações:![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044589374)
5. No exemplo a seguir, utilizaremos o Microsoft SQL:  
   ![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044590154)  
     
   **Atenção:** Se seu objetivo é somente testar a conexão com seu banco de dados, pule para o passo 12.
6. Clique em "Novo" para criar a conexão da aplicação TAF com o Banco de Dados:  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064792114)
7. Insira o nome da conexão do TAF e clique em "OK":  
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065758593)

   ```
   Observação:   
   O nome do ambiente tem que ser exatamente o mesmo nome da sua conexão com o banco de dados!
   ```
8. Com o ambiente TAF criado, insira o nome de usuário e senha do seu banco de dados, conforme o exemplo abaixo, e clique em "Salvar":  
   ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065763773)
9. Repita o mesmo procedimento para o TSS. Clique em "Novo" para criar a conexão do TSS com o Banco de Dados:  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064792114)
10. Insira o nome da conexão do TSS e clique em "OK":  
    ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065770133)

    ```
    Observação:   
    O nome do ambiente tem que ser exatamente o mesmo nome da sua conexão com o banco de dados!
    ```
11. Com o ambiente TSS criado, insira o nome de usuário e senha do seu banco de dados, conforme o exemplo abaixo, e clique em "Salvar":  
    ![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065795413)
12. Para testar a conexão vamos clicar na aba **Assistentes** e ir em **Validação de Conexão:**![8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045443113)
13. Para testar a conexão, clique na aba "Assistentes" e vá para "Validação de Conexão":  
    ![9.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044594394)
14. Selecione o banco de dados a ser testado. No nosso exemplo, estamos utilizando o Microsoft SQL. Clique em Avançar:![10.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045443393)
15. Insira o mesmo nome da conexão que está configurado. Se tiver dúvidas sobre qual nome está marcado, vá para a aba "Configurações" e verifique o nome do ambiente. Valide as conexões tanto do TAF quanto do TSS. Por fim, clique em "Finalizar":  
    ![11.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044594434)
16. Se a conexão for bem-sucedida, a seguinte mensagem será exibida, indicando que o aplicativo TAF está pronto para uso:  
    ![12.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044594414)
