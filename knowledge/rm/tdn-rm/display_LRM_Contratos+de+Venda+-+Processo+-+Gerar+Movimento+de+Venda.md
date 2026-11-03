---
content_hash: ea32477decfcb1e36f75a0bb85970eaff9d59bb40d6fbfc459299bc0c7cf4581
fetched_at: '2026-06-29T00:09:47.923318+00:00'
page_id: '435105102'
product: rm
source: tdn-rm
title: Contratos de Venda - Processo - Gerar Movimento de Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Processo+-+Gerar+Movimento+de+Venda
version: 6
---

O processo Gerar Movimento de Venda tem o objetivo de integrar a venda ao TOTVS Gestão de Estoque, Compras e Faturamento. Através do processo, será criado um movimento para que o outro sistema possa manipular seu faturamento ou outras ações permitidas por ele.   
Ao executar o processo, primeiramente é necessário ter cadastrado um Parâmetro de Movimento, localizado nos cadastros básicos do TOTVS Incorporação. Depois de informar o parâmetro, o restante dos campos será preenchido a partir dos valores informados no mesmo e se o seu checkbox Obrigatório não foi selecionado, o sistema não permitirá alterações do restante dos campos que foram preenchidos a partir do parâmetro.   
Para que o processo seja executado, é necessário informar um produto ou serviço, que será vinculado como Item do Movimento.

**Permissões Necessárias:**Para acesso a funcionalidade é necessário que o usuário esteja vinculado a um Perfil de Usuários, com as permissões, a seguir, habilitadas:

* 02.01.01- Contratos de Venda
* 02.01.01.01 - Contratos: Incluir
* 02.01.01.03 - Contratos: Editar
* 02.01.01.08 - Contratos: Gerar Lançamentos
* 02.01.01.11 - Contratos: Gerar Plano de financiamento
* 02.01.01.16 - Contratos: Compradores
* 02.01.01.18 - Contratos: Gerar Contratos
* 02.01.01.26 - Contratos: Vendedores
* 02.01.01.35 - Contratos: Condições de Financiamento- Incluir
* 02.01.01.36 - Contratos: Condições de Financiamento- Editar
* 02.01.01.43 - Contratos: Movimento de Venda

**Localização**: Conectado ao Parâmetro para Geração de Movimento: A conexão é feita através do campo Parâmetro Default do Movimento

**Ações Permitidas:**

* Incluir Produto/Serviço
* Pesquisar Produto/Serviço
* Visualizar Produto/Serviço
* Editar Produto/Serviço
* Excluir Produto/Serviço

**Campos da tela:**

* **Parâmetro Default do Movimento**: Carrega os outros campos do formulário conforme o parâmetro default informado.

Se o parâmetro selecionado estiver com o checkBox Obrigatório selecionado, O sistema não permitirá que os campos, preenchidos automaticamente por ele no processo, sejam alterados;  
Alterações efetuadas no Parâmetro de Geração de Movimentos, através da tela da execução do processo Gerar Movimento de Venda, que afetem o bloqueio ou não dos campos preenchidos automaticamente por ele serão refletidas apenas se o processo for cancelado e executado novamente.

* **Lookup**: Filtra apenas Parâmetros com o Tipo de Geração "Movimento de Venda";
* **Código do Movimento**: Informa qual o movimento gerado no final da execução do processo. Permite apenas movimentos com o código 1.1.xx;
* **Data de Emissão**: Data em que o movimento será emitido. Campo do tipo data, no formato: 'DDMMAAAA'. Permite valores entre 01011753 a 31129998. Não influencia o campo Data de Entrega;
* **Filial**: Filial qual o movimento que será criado pertencerá;
* **Data de Entrega**: Informa qual a data de Entrega do item no movimento. Campo do tipo data, no formato: 'DDMMAAAA'. Permite valores entre 01011753 a 31129998. Não influencia o campo Data de Emissão;
* **Centro de Custo**: Define qual o Centro de Custo do movimento. Será permitido inserir o rateio em cada um dos itens do movimento, caso exista;
* **Histórico**: Responsável por criar o histórico do movimento. Permite a utilização dos mnemônicos existentes no Parâmetro para Geração de Movimentos.
