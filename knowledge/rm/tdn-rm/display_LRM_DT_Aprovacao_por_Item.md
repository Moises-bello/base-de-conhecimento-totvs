---
content_hash: 80a88cc3695d28619570d96f71b6efb0e7b078f614f63f06cc130f4f41541891
fetched_at: '2026-06-29T00:06:03.530499+00:00'
page_id: '198956051'
product: rm
source: tdn-rm
title: DT_Aprovacao_por_Item
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Aprovacao_por_Item
version: 3
---

## APROVAÇÃO POR ITEM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Aprovação por Item na Cotação | MovAprovarMovProcAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Aprovações por Tipo de Movimento | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | Perfil do Usuário, |
| **Parâmetro(s):** | Aprovação |
| **Requisito (ISSUE):** | PCREQ-6378 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | TPROCESSO –Processo de Aprovação por Item na Cotação  TMOVAPROVA – Guarda os movimentos aprovados no processo de aprovação, |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.7 |

## Descrição

A Aprovação por Item permite definir critérios para restringir/permitir a inserção de itens de movimento na cotação através do processo de aprovação que utiliza uma fórmula com critérios específicos para a aprovação dos itens de movimento para serem apresentados na tela de seleção de produtos que irão compor uma cotação.

## Procedimento para Configuração

O processo de Aprovação de Itens de Movimento na Cotação deve ser utilizado para restringir a inclusão de itens no processo de Cotação. Neste caso, deverão ser feitas parametrizações específicas no Perfil associado aos Usuários que aprovarão os itens de movimentos.

O processo de Aprovação de Itens de Movimento na Cotação, inicia com o cadastro da Aprovação por Tipo de Movimento para cada perfil que se deseja tornar aprovador.

 Neste caso será criado um processo novo para seleção na tela de cadastro (**Aprovação por Item na Cotação**)

**Observação:**A lógica da fórmula a ser utilizada depende da necessidade da restrição/permissão de Aprovação. Esta fórmula deverá obrigatoriamente retornar o valor ‘0’, quando não aprovar, e ‘1’ para aprovar. No caso da aprovação por item o contexto de utilização da fórmula será o de item de movimento.

**CONFIGURAÇÃO DE PARÂMETROS**

Ao associar os Usuários ao Perfil parametrizado os mesmos se tornarão aptos a efetuar a Aprovação (Processo na tela do tipo de movimento informado no cadastro). Para tal o movimento deverá ser parametrizado para utilizar a aprovação (Ambiente / Parâmetros / Gestão de Estoques, Compras e Faturamento).

Nos parâmetros do tipo de movimento que se deseja parametrizar a aprovação é necessário acessar a **Etapa 6 – Movimento – Outros Dados** e configurar a opção **Aprovação**  como **Usa**.

## Procedimento para Utilização

### **Aprovação por Item**

Estando na tela de Movimentos processo de aprovação consiste em selecionar um movimento não aprovado e executar o processo **Aprovação**:

No caso da Aprovação por item na cotação, deve –se selecionar o processo homônimo, e posteriormente selecionar os itens que serão submetidos ao processo de aprovação e clicar um **Executar**:

Na seleção de itens de movimento deve-se selecionar os itens de movimento que se deseja aprovar e clicar em **OK**:

**Observação**:

Caso necessário, é possível agrupar os itens de movimento selecionando e arrastando as colunas do cabeçalho para a parte superior da grade, conforme a imagem acima.

Após a execução do processo apenas os itens que passarem na validação da fórmula cadastrada anteriormente serão aprovados.

## **Desaprovação por item**

Caso queira retornar o movimento que tenha sido Aprovado para o status ‘Não Aprovado’, utilize o processo Desaprovação. Neste caso os itens de movimento que estejam participando de algum processo de cotação não poderão sofrer a desaprovação.

Apenas itens já aprovados podem ser desaprovados.

No caso da Desaprovação por item na cotação, deve –se selecionar o processo Desaprovação na tela de Movimentos:

A partir deste ponto o processo é o mesmo da **Aprovação,** porém o item de movimento só pode ser desaprovado pelo usuário que o aprovou ou por um usuário supervisor!
