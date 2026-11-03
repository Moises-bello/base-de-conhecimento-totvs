---
article_id: 360017975892
category: Financeiro - Configurador
content_hash: 81e597a22d6711aca000ded5b1aabd1e5c8aea9bd080dc48fe52f82d96524f19
fetched_at: '2026-06-28T22:37:57.627139+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CFG - Dicionário desatualizado
  como criar um campo
type: support-article
updated_at: '2022-08-18T02:13:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017975892-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CFG-Dicion%C3%A1rio-desatualizado-como-criar-um-campo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Dicionário desatualizado como criar um campo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Orientação a atualização do dicionário completo conforme portal e a execução do UPDDISTR. Porém, caso entenda como inviável, segue abaixo procedimento para criar um novo campo no ***Protheus**:*  
1. Acesse **Configurador > Base de Dados > Dicionário > Bases de Dados**  
2. Clique em **Dicionário de Dados**, selecione a tabela onde este campo será inserido, e clique em **Editar**  
![NC_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013444792/NC_01.png)

3. Expanda a tabela, clique em **Campos**e selecione a opção **Incluir**  
   ![NC_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013444832/NC_02.png)
4. No **Campo**, preencha com nome do campo, por padrão deve ser iniciado com o prefixo da tabela.   
   Por exemplo: Na tabela **SA1**, o prefixo é  **A1\_**, o campo será preenchido com **A1\_CAMPO**  
   ![NC_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013444892/NC_03.png)
5. Preencha os outros campos obrigatórios da aba ***Campo***, como **Tipo, Tamanho, Contexto** e **Propriedade.**
6. Na aba ***Informações*,**o campo obrigatório é o **Título**, como será mostrado na tela da **rotina.**
7. Na aba ***Uso*,**defina se o campo se é **Obrigatório** ou não, opção **Usado**(indica se o campo será usado na **tabela**aparecer na rotina), opção ***Browse*** (indica se o campo será exibido no **browse** da rotina).
8. Concluída a configuração, clique em **Salvar**
9. Na tela da **listagem de campos**, clique em **Confirmar**   
   ![NC_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013464431/NC_04.png)  
   10.Na tela da listagem de tabelas, clique em **Atualizar base de dados**  
   ![NC_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013464531/NC_05.png)

**Importante:**  
Este procedimento de **Atualizar base de dados** tem por finalidade confirmar a inclusão do campo na tabela no banco de dados. Este procedimento deve ser feito em modo exclusivo, ou seja, não pode haver nenhum usuário com alguma rotina aberta que utilize a tabela envolvida.  
  
11. Na tela **Atualização do Dicionário de Dados**, clique em **Avançar**  
![NC_06.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013445072/NC_06.png)

12. Na próxima tela, clique em **Avançar**novamente.
13. Aguarde o processamento. Ao final, será exibida a mensagem **Atualização finalizada com sucesso.**Clique em **Finalizar.  
    ![NC_07.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013464611/NC_07.png)**

**Saiba mais:**  
[Atualizador de dicionário e base de dados - UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468)
