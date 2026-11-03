---
content_hash: 7e00072f2a07cd4915dfa0ba5de717d311b1b76dd501d6b3582d9ed95a0d9520
fetched_at: '2026-06-29T00:09:37.895856+00:00'
page_id: '425459646'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x Backoffice Protheus - Processos  - Geração de Pedidos
  em Suprimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459646
version: 4
---

**Geração de Pedidos em Suprimentos**

---

A inclusão e a exclusão de geração de pedidos em suprimentos ocorre no TOP, sendo os dados sincronizados para o Protheus. Para incluir ou excluir uma geração de pedidos em suprimentos acesse: RM | Projetos | Construção e Projetos | Projetos | Geração de Pedidos  
    
 Para incluir um pedido é necessário:

1. Informar o período a ser pedido, o modo de seleção de tarefas, e o tipo de requisição.  
 2. Informar a(s) tarefa(s).   
 3. Informar o(s) grupo(s) de custo.  
 4. Informar o(s) insumo (s).   
 Após informado os dados para requisição, basta executar o processo e o pedido será gerado no TOP.  
    
 **Observações:**

* A requisição pode ser do tipo:  
    
  + Solicitação de Armazém: gera uma solicitação de armazém no Protheus.
  + Requisição Histórico: permite o registro manual no RM dos movimentos de compra que eventualmente foram criados no Protheus antes da integração ser habilitada, ou seja, serão apenas para consulta (histórico) e para compor corretamente o custo do projeto.

Ao cadastrar um pedido histórico no sistema não há integração com o Protheus, mas os custos são apropriados ao projeto, assim estes pedidos históricos permitem que o valor do projeto seja acertado manualmente.

* + Solicitação de Compra: gera uma solicitação de compra no Protheus.
  + Os parâmetros são setados quando o Assistente de Configuração é executado (como visto no módulo Pré-Requisitos), e não disponíveis para edição nesta integração (é possível editá-los apenas quando o TOP está integrado com BackOffice RM)

Para visualizar os parâmetros acesse: RM | Projetos | Construção e Projetos | Opções | Construção e Projetos | Projetos | Integração | Suprimentos e Faturas | guia Geral e guia Tipos de Mov.  
    
 Após gerar o pedido é necessário enviá-lo ao Protheus. Selecione o pedido e acesse: Processos | Envia pedido para Suprimento/Faturamento gerando apenas 1(um) movimento.  
    
 O ícone do pedido é alterado, e no anexo Movimento é possível visualizar o movimento gerado para o pedido de compra. O anexo Movimento exibe a rastreabilidade do pedido. Através dele é possível verificar se já foi Baixado ou Faturado a quantidade total que foi solicitada. Conforme ocorre a baixa ou emissão de NF, o status do movimento muda (Pendente, Parcialmente Quitado, Quitado). O anexo exibe os dados do pedido na Origem (TOP).   
    
 Quando o processo de geração de pedidos é disparado no TOP, um movimento é enviado para o Protheus (sincronizado via WebService), como uma Solicitação de Armazém (SA) ou Solicitação de Compra (SC), conforme o tipo de requisição. O número gerado para a SA ou SC no Protheus é imediatamente sincronizado para o RM (retorno da chamada ao WebService).  
    
 Para visualizar a SA no Protheus acesse: Protheus | SigaEst | Atualizações | Estoques | Solicitação de Armazém  
    
 **Observações:**

* Conforme parametrizado, quando for dada a baixa no estoque, o Protheus irá executar uma stored procedure no banco RM que irá fazer a apropriação da SA original no RM. O valor enviado para apropriação será: **Valor = (Custo da compra do item / Quantidade do item da NF) \* quantidade do item do projeto**
* Um item da nota fiscal pode ser relacionado com vários itens do projeto.
* A SA gerada pelo TOP só pode ser excluída a partir do mesmo. Não é permitida alteração.
* Para gerar um pedido no TOP é necessário ter cadastrado:  
    
  + Coligada: Incluída como visto no módulo Cadastros (no cadastro Empresa/Filial)
  + Filial: Incluída como visto no módulo Cadastros (no cadastro Empresa/Filial)
  + Sub-Projeto: Um projeto é feito por Obra (sub-projeto), Etapas e Serviços. Acesse: Projetos | Construção e Projetos | Projetos | Selecionar Projeto | Cadastros | Atividades
* **Insumo vinculado a atividade:** Acesse: Projetos | Construção e Projetos | Projetos | Selecionar Projeto | Cadastros | Atividades | Selecionar tarefa | Aba Recursos | Informa Insumo.

Os insumos são cadastrados em: Projetos | Construção e Projetos | Cadastros | Insumos.   
 Ao cadastrar o insumo o mesmo deve ter um produto (sincronizado do Protheus) relacionado, para que a integração da requisição de materiais funcione corretamente. Na edição do insumo, acesse a aba Produtos de Suprimento/faturamento e insira um produto correspondente ao insumo.

* **Cronograma:** Acesse Projetos | Construção e Projetos | Projetos | Selecionar Projeto | Cadastros | Atividades | Selecionar tarefa | Anexo | Cronograma.

Informe a quantidade prevista que deve ser utilizada do material em um determinado período. É necessário fazer isso para cada atividade. Ao informar a quantidade, é necessário salvar o cronograma. Após, clique em calcular projeto (aba Projeto | Calcular Projeto), e depois clique em calcular o cronograma. Para cadastrar um período no cronograma do projeto acesse: Projetos | Construção e Projetos | Opção | Construção e Projetos | Projetos | Cronograma | Períodos

* **Local de Estoque:** É necessário definir local de estoque para cada obra. Acesse: Projetos | Construção e Projetos | Projetos | Selecionar Projeto | Cadastros | Atividades | Selecionar tarefa | Outros (no menu principal)| Subprojeto.
