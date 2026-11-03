---
article_id: 360001052008
category: Configurador
content_hash: 681869cf17e1b144b442a86519fec49cc8b8161950a2f0522628ebb5c864178c
fetched_at: '2026-06-28T22:42:18.907405+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus   - Definir campo como obrigatório
type: support-article
updated_at: '2025-10-29T17:14:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001052008-Framework-Linha-Protheus-Definir-campo-como-obrigat%C3%B3rio
---

**Dúvida**Como tornar um campo obrigatório?  
  
**Ambiente**Protheus - Configurador - A partir da versão 11.8  
  
**Solução**Para tornar um campo obrigatório no sistema, realize os seguintes passos:  
  
Primeiramente identifique o nome do campo. Para isso, clique sobre o **campo** e pressione a tecla **F1**.  
  
![Campo_Obrigat_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001693347)  
  
Após verificar o nome do campo, siga o procedimento abaixo:  
1. Acesse Configurador > Base de Dados > Dicionário **> Bases de Dados**;  
2. Clique em Dicionário de Dados, selecione a tabela do campo, e clique em **Editar**;  
  
![Campo_Obrigat_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001694047)  
  
3. Expanda a tabela, clique em **Campos** e localize o campo que vai alterar;  
4. Clique sobre o campo e clique em **Editar;  
  
![Campo_Obrigat_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001666228)**5. Na aba **Uso**, marque a caixinha **Obrigatório** e clique em **Salvar;  
  
![Campo_Obrigat_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001666308)**6. Na tela da listagem de campos, clique em **Confirmar (seleção);**7. Na tela da listagem de tabelas, clique em **Atualizar base de dados**;  
  
![Campo_Obrigat_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001694167)  
  
  
**Importante**Este procedimento de **Atualizar base de dados** tem por finalidade confirmar a inclusão do campo na tabela no banco de dados. Este procedimento deve ser feito em modo **exclusivo**, ou seja, não pode haver nenhum usuário com alguma rotina aberta que utilize a tabela envolvida.

8. Na tela **Atualização do Dicionário de Dados**, clique em **Avançar;  
  
![Campo_Obrigat_06.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001694227)**

9. Aguarde o processamento. Ao final, será exibida uma tela como essa, indicando **Atualização finalizada com sucesso**. Clique em **Finalizar**.  
  
![Campo_Obrigat_07.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001666328)
