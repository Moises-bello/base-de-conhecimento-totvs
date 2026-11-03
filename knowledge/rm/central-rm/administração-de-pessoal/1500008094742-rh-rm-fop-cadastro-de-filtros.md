---
article_id: 1500008094742
category: Administração de Pessoal
content_hash: 008bcb6b0f958b48181f93fb66b0ae1f7dc67b95ee720057a277ed3d59f87303
fetched_at: '2026-06-28T22:47:02.177638+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Cadastro de filtros
type: support-article
updated_at: '2025-03-12T10:01:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008094742-RH-RM-FOP-Cadastro-de-filtros
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:04:40 min****Dúvida**Como realizar cadastro de filtros no sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**Os filtros são utilizados para melhorar a visualização dos registros em uma visão ou mesmo trazer aqueles que lhe fazem necessidade.  
  
**Cadastro de filtros**Para criar um filtro nas visões do sistema, clique no botão Filtrar | Novo Filtro:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865464438935/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865486423959/mceclip1.png)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865489069719/mceclip2.png)  
  
**Opções do item Selecionado:** São os campos da visão que estão disponíveis para filtrar.  
  
**Operador:** São os tipos de condições que o usuário consegue adicionar para filtrar os dados da visão.  
  
**Expressão:** É onde se encontram as condições cadastradas no filtro selecionado.  
  
1. **Filtros utilizando LIKE:**- Action de Movimento  
**Expressão**: Fornecedor LIKE [CODCFO]  
  
![](https://tdn.totvs.com/download/attachments/61932706/1.jpg?version=1&modificationDate=1370345813000&api=v2&effects=drop-shadow)  
  
- Action de Movimento  
**Expressão**: Fornecedor LIKE [FORNECEDOR]  
  
 ![](https://tdn.totvs.com/download/attachments/61932706/2.jpg?version=1&modificationDate=1370345813000&api=v2&effects=drop-shadow)  
  
- Action de Movimento  
**Expressão**: Fornecedor LIKE [] %  
  
![](https://tdn.totvs.com/download/attachments/61932706/3.jpg?version=1&modificationDate=1370345813000&api=v2&effects=drop-shadow)  
  
2. **Filtro usando IS NOT NULL (Todos - Retorna todos os registros da visão):**- Action de Funcionários  
**Expressão**: Chapa IS NOT NULL  
  
**![](https://tdn.totvs.com/download/attachments/61932706/image2013-6-5%2011%3A19%3A34.png?version=1&modificationDate=1370442140000&api=v2&effects=drop-shadow)**3. **Filtro usando operador = (igual)**- Action de Funcionários  
**Expressão**: Situação = A  
  
**![](https://tdn.totvs.com/download/attachments/61932706/image2013-6-5%2011%3A22%3A23.png?version=1&modificationDate=1370442308000&api=v2&effects=drop-shadow)**4. **Filtro usando uma consulta SQL (IN SQL):**- Action de Funcionários  
**Expressão**: Chapa IN (SelecaoCodSit)  
  
   ![](https://tdn.totvs.com/download/attachments/61932706/image2013-6-5%2011%3A39%3A10.png?version=1&modificationDate=1370443315000&api=v2&effects=drop-shadow)  
  
Sobre este operador, **saiba mais** [Filtro com IN SQL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015189732-RM-Frame-Filtro-com-IN-SQL).  
  
5. **Filtro variáveis de contexto ( $Hoje):**- Action de Gerenciamento de Jobs  
**Expressão**: Criado EM = $Hoje  
  
![](https://tdn.totvs.com/download/attachments/61932706/image2013-6-5%2011%3A41%3A44.png?version=1&modificationDate=1370443470000&api=v2&effects=drop-shadow)  
  
**Informações sobre Filtros**Para que um determinado filtro seja sempre aplicado no momento da abertura de uma visão (tela), basta que seja marcada a opção **Sempre usar este filtro ao abrir a visão**:  
  
**![](https://tdn.totvs.com/download/attachments/61932706/image2018-2-5_15-27-32.png?version=1&modificationDate=1517855255000&api=v2&effects=drop-shadow)****Copia de filtros entre coligadas**Para copiar um filtro entre coligadas é necessário Selecionar o Filtro e Clicar em Copiar Filtro:  
  
![](https://tdn.totvs.com/download/attachments/61932706/image2018-2-5_15-44-4.png?version=1&modificationDate=1517856246000&api=v2&effects=drop-shadow)  
  
Após clicar em **não** basta selecionar as coligadas que o filtro será replicado:  
  
![](https://tdn.totvs.com/download/attachments/61932706/image2018-2-5_15-44-33.png?version=1&modificationDate=1517856276000&api=v2&effects=drop-shadow)

**Filtro Global**Para adicionar um filtro como Global, é necessário selecionar o Filtro, clicar com o botão direito do mouse e selecionar a opção filtro global:  
  
![](https://tdn.totvs.com/download/attachments/61932706/image2018-2-5_15-34-19.png?version=1&modificationDate=1517855661000&api=v2&effects=drop-shadow)

**Permissão para Filtro Global**Para ter acesso ao Filtro Global, é necessário que o usuário tenha permissão no item **Filtros Globais** no perfil do módulo em que ele deseja utilizar os filtros Globais. Por exemplo, para ter acesso aos Filtros Globais no módulo RM Gestão de Estoque, Compras e Faturamento, o usuário deve estar associado à um perfil do RM Nucleus que tenha permissão no item **Filtros Globais** no **Acesso a Menus**:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865508100119/mceclip3.png)  
  
**Enviar para barra de Ferramentas**A Opção de Enviar para a barra de ferramentas, disponibiliza o filtro na barra de ferramentas, seja ele por Usuário ou Global, respeitando o escopo do filtro.

![](https://tdn.totvs.com/download/attachments/61932706/image2019-9-2_11-18-4.png?version=1&modificationDate=1567433884897&api=v2&effects=drop-shadow)

![](https://tdn.totvs.com/download/attachments/61932706/image2019-9-2_11-18-46.png?version=1&modificationDate=1567433927203&api=v2&effects=drop-shadow)  
  
**Importante**- Filtros criados com Valor sendo um colchete aberto e fechado "[]" fazem com que, ao escolher o filtro na visão, o usuário precise preencher o que está buscando. Por exemplo, se crio o filtro para buscar uma chapa de funcionário, seleciono o filtro e digito a chapa que desejo naquele momento: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012647901/mceclip0.png)**  
- Filtros Globais só podem ser adicionados na barra de ferramentas por usuários que possuírem permissão em filtros globais conforme item 2.3 desta documentação;

- Os Filtros Globais irão aparecer na barra de ferramentas para todos os usuários caso o mesmo seja habilitado.  
  
**Saiba mais**Para mais informações sobre os operadores, expressões e suas respectivas definições, acesse nosso TDN [Utilização de Filtros](https://tdn.totvs.com/pages/releaseview.action?pageId=403746935).
