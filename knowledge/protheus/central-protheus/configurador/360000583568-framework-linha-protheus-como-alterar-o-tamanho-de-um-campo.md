---
article_id: 360000583568
category: Configurador
content_hash: 7b2638e2fc9b99df48994b15c97f3e02b57d73ab492d5ec1649ec98a273d0ab5
fetched_at: '2026-06-28T22:42:18.938023+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Como alterar o tamanho de um campo
type: support-article
updated_at: '2024-05-08T11:36:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000583568-Framework-Linha-Protheus-Como-alterar-o-tamanho-de-um-campo
---

**Dúvida**  
Como alterar o tamanho de um campo?  
  
**Ambiente**  
Protheus – Configurador - A partir da versão 11.8  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
Para alterar o tamanho de algum campo da rotina, primeiramente identifique o nome do campo. Para isso, clique sobre o campo e pressione **F1**.

![](http://tdn.totvs.com/download/attachments/271400228/TC_01.png?version=1&modificationDate=1486041951000&api=v2)

Após verificar o nome do campo, siga o procedimento abaixo:  
1. Acesse Configurador > Base de Dados > Dicionário > **Bases de Dados**;  
2. Clique em Dicionário de Dados, selecione a tabela do campo, e clique em **Editar**;

![](http://tdn.totvs.com/download/attachments/271400228/TC_02.png?version=1&modificationDate=1486041951000&api=v2)

3. Expanda a tabela, clique em **Campos** e localize o campo que vai alterar;  
4. Clique sobre o campo e clique em **Editar**;

**![](http://tdn.totvs.com/download/attachments/271400228/TC_03.png?version=1&modificationDate=1486041951000&api=v2)**

5. Em **Tamanho**, digite o novo tamanho do campo e clique em **Salvar**;

**![](http://tdn.totvs.com/download/attachments/271400228/TC_04.png?version=1&modificationDate=1486041951000&api=v2)**

6. Na tela da listagem de campos, clique em **Confirmar** (seleção)  
7. Na tela da listagem de tabelas, clique em **Atualizar base de dados**;

**![](http://tdn.totvs.com/download/attachments/271400228/TC_05.png?version=1&modificationDate=1486041951000&api=v2)**

**Importante**Este procedimento de **Atualizar base de dados** tem por finalidade confirmar a inclusão do campo na tabela no banco de dados. Este procedimento deve ser feito em modo **exclusivo**, ou seja, não pode haver nenhum usuário com alguma rotina aberta que utilize a tabela envolvida.  
  
8. Na tela **Atualização do Dicionário de Dados**, clique em **Avançar**;

**![](http://tdn.totvs.com/download/attachments/271400228/TC_06.png?version=1&modificationDate=1486041951000&api=v2)**

9. Na próxima tela, clique em **Avançar** novamente;  
10. Aguarde o processamento. Ao final, será exibida uma tela como essa, indicando **Atualização finalizada com sucesso**. Clique em **Finalizar**.

![](http://tdn.totvs.com/download/attachments/271400228/TC_07.png?version=1&modificationDate=1486041951000&api=v2)
