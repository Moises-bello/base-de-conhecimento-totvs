---
article_id: 25667061248151
category: TAF - eSocial - Instalação
content_hash: bcde28bebe23bc31a4dc492dc1c868aeeb5039b4b44fa9cbe3f840a323e255a2
fetched_at: '2026-06-28T22:45:10.990453+00:00'
product: protheus
section_id: 1500001536881
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Como desinstalar o DBACCESS para reinstalação?
type: support-article
updated_at: '2025-07-10T20:26:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25667061248151-RH-Linha-Protheus-TAF-eSocial-Como-desinstalar-o-DBACCESS-para-reinstala%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25667088820631) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como desinstalar o serviço do DBACCESS para reinstalação?  
  
**Ambiente**RH - Linha Protheus - TAF - eSocial - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

**OBS.:**Os procedimentos à seguir são para clientes que utilizam o TAF Segregado, se for ambiente Protheus, recomendamos que abra um ticket com setor de Protheus Framework ou Tecnologia para validar o cenário.

1. Pare o serviço do DBACCESS caso esteja em execução;
2. Pare os demais serviços que dependam deste DBACCESS, como TAF-WS, TAF-APPSERVER e TSS;
3. Realize um backup da pasta do DBACCESS;
4. Verifique como é o nome do serviço do DBACCESS e copie o nome:  
     
   Exemplo:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25669902485911)
5. Acesse o Prompt de comando (CMD) como administrador;
6. Digite o seguinte comando:  
     
   SC DELETE "NOME DO SERVIÇO DO DBACCESS"  
     
   Exemplo:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25669902493847)  
     
   1. Aperte ENTER e veja se foi concluído com êxito:  
      ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25669902501527)
7. Abra o arquivo DBACCESS.INI e realize as alterações conforme abaixo:  
     
   1. Na seção [GENERAL] adicione o parâmetro port=:  
      **[General]**  
      **port=1234\*****Obs.:** *Insira uma porta de acordo com as politicas de segurança da informação da empresa   
      \* A porta adicionada acima não é recomendação de uso*
   2. Adicione a seção abaixo para nomear o serviço do DBACCESS:  
      **[SERVICE]**  
      **NAME=TOTVS-DBACCESS**  
      **DISPLAYNAME=TOTVS-DBACCESS**
   3. Salve o arquivo e feche-o na sequência;
8. Apague os arquivos de LOG no DBACCESS (DBCONSOLE.LOG e DBACCESS.LOG)
9. Clique com o botão direito no arquivo DBACCESS.EXE e crie um atalho do mesmo:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25669933531031)
10. Com o atalho criado, clique com o botão direito e vai em propriedades:  
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25669933537047)
11. Na aba Atalho no campo Destino, no final do caminho após o .exe adicione o parametro -install:  
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25669933541911)
12. Execute o atalho com as configurações como Administrador
13. Verifique se o serviço foi criado corretamente e clique com o botão direito para selecionar o tipo de inicialização automática e inicie-o em seguida:  
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25670203269527)  
      
    Obs.: Se houver problemas para iniciar o serviço enviem os arquivos (DBACCESS.INI, DBCONSOLE.LOG e DBACCESS.LOG).
14. Com o serviço criado e iniciado, recrie a conexão com o seu banco de dados de acordo com o material abaixo:  
    [RH - Linha Protheus - TAF - eSocial - CONFIGURAÇÃO - Criando e/ou testando conexões com o DBAccess para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574)
