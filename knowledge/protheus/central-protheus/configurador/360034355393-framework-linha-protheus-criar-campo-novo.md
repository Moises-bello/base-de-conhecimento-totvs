---
article_id: 360034355393
category: Configurador
content_hash: 4d5cba57643642b554b33e60247fa30ae0d34e1f6bcef7f093b538d5caf2d447
fetched_at: '2026-06-28T22:42:19.029589+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Criar campo novo
type: support-article
updated_at: '2026-04-02T23:55:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034355393-Framework-Linha-Protheus-Criar-campo-novo
---

**Dúvida**Como proceder para criar novos campos?  
   
 **Ambiente**Protheus - Configurador - Versão 12  
  
**Solução**Segue abaixo procedimento para criar um novo campo no Portheus:  
01. Acesse Configurador > Base de Dados > Dicionário > **Bases de Dados**  
  
02. Clique em **Dicionário de Dados**, selecione a tabela onde este campo será inserido, e clique em **Editar**  
![NC_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043568014)  
  
03. Expanda a tabela, clique em **Campos** e clique em **Incluir**  
  
![NC_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044417153)  
  
04. Em **Campo**, insira o nome que o campo terá. Ele deve iniciar com o prefixo da tabela. Por exemplo, na tabela SA1, o prefixo é A1\_, então o campo ficaria com a nomenclatura A1\_CAMPO  
  
![NC_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044417173)  
  
05. Preencha os outros campos obrigatórios da aba ***Campo***, como Tipo, Tamanho, Contexto e Propriedade  
  
06. Na aba ***Informações***, o campo obrigatório é o **Título**, que é o texto que vai aparecer na tela da rotina  
  
07. Na aba ***Uso***, defina qual será o uso do campo. Se ele for **Obrigatório**, marque essa caixinha. A opção **Usado** indica se o campo será usado na tabela, se irá aparecer na rotina. A opção **Browse** indica se o campo será exibido no browse da rotina, onde são listados os registros  
  
08. Com a configuração básica feita, clique em **Salvar**  
09. Na tela da listagem de campos, clique em **Confirmar   
  
![NC_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044417193)**10. Na tela da listagem de tabelas, clique em **Atualizar base de dados**  
  
![NC_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043568034)

|  |
| --- |
| **Aviso**:  O procedimento de "Atualizar base de dados" tem por finalidade confirmar a inclusão do campo na tabela no banco de dados. Este procedimento deve ser feito em modo exclusivo, ou seja, não pode haver nenhum usuário com alguma rotina aberta que utilize a tabela envolvida. |

11. Na tela **Atualização do Dicionário de Dados**, clique em **Avançar**  
  
![NC_06.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043568054)  
  
12. Na próxima tela, clique em **Avançar** novamente  
  
13. Aguarde o processamento. Ao final, será exibida uma tela como essa, indicando **Atualização finalizada com sucesso**. Clique em **Finalizar**.  
  
![NC_07.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044417213)
