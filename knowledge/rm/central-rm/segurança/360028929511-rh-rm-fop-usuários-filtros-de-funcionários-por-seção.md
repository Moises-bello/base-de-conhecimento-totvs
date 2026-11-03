---
article_id: 360028929511
category: Segurança
content_hash: 49bef76654f5e466fcabee80c6de1193355774513dd43c871cf7cd58fa7986b6
fetched_at: '2026-06-28T22:46:46.828314+00:00'
product: rm
section_id: 1500000834641
source: central-rm
title: 'RH - RM - FOP - Usuários: Filtros de funcionários por seção'
type: support-article
updated_at: '2025-03-13T11:15:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028929511-RH-RM-FOP-Usu%C3%A1rios-Filtros-de-funcion%C3%A1rios-por-se%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:40 min  
  
Dúvida**Como parametrizar o sistema para que um usuário visualize apenas os **funcionários** de uma ou mais seções específicas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para restringir o acesso do usuário à visualização de todos os funcionários e limitá-lo a apenas uma ou algumas seções específicas, é necessário realizar a criação de um filtro por usuário, conforme os seguintes passos:  
  
1. Acesse **Serviços Globais | Usuários**;2. Crie ou edite o usuário desejado e acesse **Anexos | Filtros por Usuário**;  
3. Informe a coligada desejada e a tabela PFUNC;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029779451/mceclip1.png)  
  
4. No campo Filtro clique em **Novo** para cadastrar ou nos três pontos [...] para selecionar um existente;  
5. Ao incluir, selecione Código da Seção, operador igual (=) e informe o valor das seções que o usuário terá acesso no cadastro de funcionário;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029789532/mceclip0.png)  
6. Salve as informações;  
7. Após realizar a criação do filtro no usuário, ao acessar o cadastro de funcionário, o usuário visualizará apenas as informações da seção do filtro **mesmo que crie um filtro na tela de visão dos funcionários para ver todos os registros**.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029780871/mceclip3.png)
