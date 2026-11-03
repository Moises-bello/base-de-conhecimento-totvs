---
article_id: 360042045853
category: TAF - eSocial - DBAccess
content_hash: ed96b00e26efeb0c27334d1a6447193fef53d59c97dda0dce6cffbd08c405485
fetched_at: '2026-06-28T22:45:12.433517+00:00'
product: protheus
section_id: 1500001536981
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - DBACCESS - Alterar serviço TAF-DBAccess
  de 32bits para 64bits
type: support-article
updated_at: '2024-05-27T14:18:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042045853-RH-Linha-Protheus-TAF-eSocial-DBACCESS-Alterar-servi%C3%A7o-TAF-DBAccess-de-32bits-para-64bits
---

**Dúvida**

Como alterar a arquitetura do TAF-DBAccess de 32 para 64 bits?

**Ambiente:**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Solução**

1. Faça o download do DBAccess64 através do seguinte link:   
   <https://suporte.totvs.com/portal/p/10098/download#detail/1112219>
2. Acesse os serviços do Windows e procure pelo serviço TAFDBAccess:  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065629433)
3. Siga os passos abaixo:  
   - Clique com o botão direito do mouse sobre o serviço e acesse as "Propriedades":  
   - Verifique se o serviço está configurado como 64 bits:  
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064642574)
4. Caso esteja configurado como 32 bits, exclua o serviço seguindo o próximo passo.  
     
   (Para excluir o serviço, abra o Prompt de Comando como Administrador e execute o seguinte comando abaixo):  

   ```
   sc delete NOME_SERVIÇO_DBACCESS32
   ```
5. Se o serviço do DBAccess estiver configurado como 64 bits, prossiga com a atualização seguindo o artigo abaixo: [TAF - ATUALIZAÇÃO - Como atualizar o DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034522854)  
     

   **\*\*ATENÇÃO:\*\*** Se o seu DBAccess já estiver configurado como 64 bits, vá para o próximo passo e execute o atualizador.
6. Siga os passos abaixo para configurar o DBAccess na arquitetura de 64 bits:  
   - Acesse o diretório de instalação do TAF e localize o diretório TAFDBAccess32 e/ou TAFDBAccess.  
   - Procure pelo arquivo `dbaccess.ini`, copie-o e cole-o na pasta TAFDBAccess64.  
   - Abra o arquivo `dbaccess.ini` para edição e adicione o seguinte comando no final:  

   ```
   [SERVICE]  
   NAME=Taf-DbAccess64  
   DISPLAYNAME=Taf-DbAccess64
   ```
7. No mesmo diretório do DBAccess, localize o executável `dbaccess.exe` e crie um atalho para o mesmo:  
     
   - Clique com o botão direito do mouse no atalho recém-criado e acesse as "Propriedades".  
   - Na guia "Atalho", verifique o campo "Destino" e deixe-o como no exemplo a seguir: `"C:\TOTVS\TAF\TafDbAccess64\dbaccess.exe -install"`.   
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055523714)  
   - Execute-o para criar o serviço nos serviços do Windows.
8. Acesse novamente os Serviços do Windows e verifique se o serviço TAF-DBAccess64 foi criado:  
     
   - Clique com o botão direito do mouse no serviço e verifique se a inicialização está configurada como "Automático":  
   ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064653354)  
     
   - Na aba "Recuperação", deixe a opção "Não executar nenhuma ação" nas falhas.  
   ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065640573)  
     
   - Clique em "Aplicar" e "OK" para salvar as configurações.
9. Realize os testes de conexão conforme a documentação abaixo:  
   [TAF - CONFIGURAÇÃO - Criando e testando conexões com o DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574)
