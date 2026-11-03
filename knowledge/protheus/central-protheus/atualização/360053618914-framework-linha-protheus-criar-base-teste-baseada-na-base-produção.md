---
article_id: 360053618914
category: Atualização
content_hash: ded48fa3be7e9685ff117575feed55613ecf67dc9a6589b59d1d876c8d674981
fetched_at: '2026-06-28T22:42:21.233484+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Criar base Teste baseada na base Produção
type: support-article
updated_at: '2024-03-26T12:59:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053618914-Framework-Linha-Protheus-Criar-base-Teste-baseada-na-base-Produ%C3%A7%C3%A3o
---

**Dúvida**Como criar uma base de teste baseada em uma cópia da base de produção?  
  
**Ambiente**Protheus - AppServer - Versão 12  
  
**Solução**Procedimento para criar base de teste baseada em cópia da base de produção.  
  
Para testes, validações de novas atualizações, simulações de erros e correções, é importante ter uma base teste, que pode ser uma cópia da base de produção. Segue abaixo procedimento de como criá-la:  
1. Pare todos os serviços do Protheus (Servidor de Aplicação, Servidor de Licenças, DBAccess)  
2. Faça uma cópia da pasta raiz do Protheus (Ex.: C:\TOTVS 12\)  
3. Na pasta cópia, abra o arquivo **appserver.ini**4. Para melhor identificação, altere o nome do**[Ambiente]**5. Na seção **[Service]**, altere as linhas **Name=** e **DisplayName=**  
6. Se a base teste está no mesmo servidor da base produção, altere a porta na seção **[TCP]**  
7. Na seção do ambiente, faça a adequação dos caminhos das pastas para o nome da pasta renomeada que você criou  
8. Se tiver seção **[HTTP]**, altere sua porta  
9. Utilize um banco de dados separado da Produção. Crie o banco no seu SGBD (ou faça uma cópia do banco de dados principal), configure a ODBC, e então aponte as configurações dessa base na seção **[DBAccess]** ou linhas **DB** do ambiente  
  
Após efetuar a configuração, inicie o Protheus da base Teste em modo **console** (crie um atalho para o executável e insira o comando -console após o caminho do executável nas Propriedades do atalho) ou crie um **serviço** para o executável (comando appserver.exe -install pelo Prompt de Comando, na pasta do appserver.exe).  
  
Para configurar o acesso pelo **SmartClient** a essa base, você pode criar uma cópia da pasta Smartclient apenas para essa base, ou utilizar a mesma da Produção, alterando a seção **[TCP]** do arquivo **smartclient.ini**. Seguem as configurações:  
**Se for utilizar uma cópia da pasta Smartclient:**  
1. Após fazer a cópia, abra o arquivo **smartclient.ini**  
2. Na seção **[TCP]**, altere a porta para a que foi definida no arquivo **appserver.ini** (se a base foi colocada em outro servidor físico, altere também a linha **Server**, inserindo o endereço IP do servidor)  
3. Na seção **[Config]**, na linha **EnvServer**, apague o conteúdo e insira o nome do ambiente que você definiu no arquivo appserver.ini  
4. Ao acessar pelo atalho deste **Smartclient**, será conectado na base Teste  
  
**Se for utilizar o mesmo Smartclient da produção:**  
1. Abra o arquivo **smartclient.ini** da produção  
2. Copie a seção **[TCP]**, e cole logo abaixo  
3. Altere o nome dessa segunda seção **TCP**, para **[TCP-Teste]**, por exemplo  
4. Nessa seção, altere a porta para a que foi definida no arquivo **appserver.ini** (se a base foi colocada em outro servidor físico, altere também a linha **Server**, inserindo o endereço IP do servidor)  
5. Na seção **[Config]**, na linha **EnvServer**, após o nome do ambiente de produção, insira uma virgula e o nome do ambiente que você definiu no arquivo **appserver.ini**  
6. Ao abrir o **Smartclient**, em **Comunicação no cliente**, alterne entre o **TCP** de Produção e o **TCP-Teste**. E em **Ambiente no servidor**, alterne entre o nome do **Ambiente de Produção** e o **Ambiente Teste**

Segue abaixo um exemplo de configuração do arquivo smartclient.ini, e a tela de conexão com as opções:  
![im1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091764313)  
  
![im2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089607454) ![im3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089607614)  
  
![im4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089608294)
