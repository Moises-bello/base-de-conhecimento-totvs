---
content_hash: f4ca4d2ea88c5187e3227e249d1e1f9ea737bc35fff97fee1d2dc859c33f276b
fetched_at: '2026-06-29T00:10:04.554355+00:00'
page_id: '452719216'
product: rm
source: tdn-rm
title: Requisição de Substituição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719216
version: 3
---

**Requisição de Substituição**

---

Este tipo de requisição tem por objetivo possibilitar o preenchimento de vagas de funcionários desligados, transferidos ou realocados para outro cargo ou função.  
Este tipo de requisição somente poderá ser criada automaticamente após a aprovação das respectivas requisições pai, que poderão ser as requisições de desligamento, alteração de dados funcionais, transferência ou transferência com alteração de dados funcionais, ou seja, não é permitido ao usuário criar/abrir uma requisição de substituição e também não é permitida a vinculação manual de uma requisição pai a uma requisição de substituição.

**Passos para gerenciar uma Requisição de Substituição**

**1º Passo:** Acessar o módulo: Planejamento e Captação | Requisições | Substituição.

**2º Passo:** Aprovar/Reprovar a Requisição.

**3º Passo:** Vincular funcionário e/ou candidato a esta Requisição, após a aprovação da mesma, considerando as opções:

* **Criar um Processo de Seleção vinculado a esta Requisição** (link documento Roteiro de Seleção de Pessoal – já existente no help)
* **Incluir um funcionário no processo de movimentação de pessoal, pelo processo "Incluir em processo de movimentação de pessoal"**

**Para isso, deverá:**

Acessar Configurações | Parametrizador | Requisições e marcar os parâmetros "Requisição obrigatória para alterar cargo e/ou salário" ou "Requisição obrigatória para transferir funcionário" ou "Requisição obrigatória para transferir e alterar dados".

Acessar o cadastro de Funcionários, selecionar um funcionário que desejar incluir no processo de movimentação de pessoal e executar o processo: "Incluir em processo de movimentação de pessoal".

Será exibida uma tela onde deverá ser informada a Requisição de Substituição a ser considerada na alteração dos dados do funcionário.

Se a alteração dos dados consistir em:

**Função e/ou salário:** será criada a Requisição filha de Alteração de Dados Funcionais;

**Seção:** será criada a Requisição filha de Transferência;

**Função e/ou salário e seção:** será criada a Requisição filha de Transferência com Alteração de Dados Funcionais.

Para que a Requisição de Substituição, que possui alguma das Requisições filhas citadas acima seja concluída, primeiramente deverá efetivar(concluir) as Requisições filhas.

**Importante:**

Caso exista licença do Totvs Folha de Pagamento, a efetivação da Requisição deverá ser realizada por este aplicativo, acessando o menu Administração de Pessoal | Aprovação de Alterações Cadastrais | Efetivar Alteração de Dados Funcionais ou Efetivar Transferência ou ainda Efetivar Transferência com Alteração de Dados Funcionais. Caso contrário, a efetivação da Requisição deverá ser realizada através do Totvs Gestão de Pessoas, acessando o menu Planejamento e Captação | Requisições | Aumento de Quadro.

Ao excluir uma Requisição Filha, que foi gerada pela vinculação de um funcionário a uma Requisição de Aumento de Quadro, este funcionário será removido automaticamente da lista de pessoas selecionadas da Requisição Pai.

* **Incluir um candidato em processo de admissão, através do processo "Incluir no processo de admissão"**

Acessar Configurações | Parametrizador | Requisições e marcar o parâmetro "Requisição obrigatória para admissão".  
Acessar o cadastro de Pessoas ou Candidatos, selecionar um candidato que desejar incluir no processo de admissão e executar o processo "Incluir no processo de admissão".   
Será exibida uma tela onde deverá ser informada a Requisição de Substituição a ser considerada na admissão do candidato.  
Para que a Requisição de Substituição seja concluída é necessário que o candidato seja admitido.

* **Andamento do Processo de Captação**

A aba Andamento do Processo de Captação tem como objetivo possibilitar que gestores e usuários responsáveis por movimentar requisições do modulo Planejamento e Captação visualizem o progresso da seleção a qual a requisição esta vinculada, a partir da própria requisição.  
Nesta aba é possível verificar informações como:

1. Data inicio do Perfil da Vaga;
2. Data previa para termino;
3. Etapa atual no processo de seleção;
4. Numero de candidatos selecionados na etapa atual;
5. Lista dos candidatos podendo visualizar seu Currículo.

**Importante:** Caso exista licença do Totvs Folha de Pagamento, a contratação do candidato deverá ser realizada por este aplicativo, sendo que o parâmetro "Somente inclui candidatos em processo de admissão no RM Vitae" deverá estar marcado em Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros II.

Ao remover um candidato de uma Requisição de Aumento de Quadro, este terá seu status alterado de "candidato em processo de admissão" para "candidato". As pessoas selecionadas na Requisição de Substituição podem ser removidas pelo Processo Remover Pessoas da Seleção.

Vale ressaltar que este processo só poderá ser executado para candidatos que ainda não foram admitidos e funcionários que ainda não tiveram seus dados alterados.

**Campos Complementares na Requisição de Substituição**

* Esta funcionalidade permite a inclusão de **Campos Complementares** nas **Requisição de Substituição**
* Os Campos Complementares criados para a Requisição de Substituição possuem **abrangência global**. Eles serão exibidos em **todas as coligadas** do sistema, independentemente da coligada em que foram criados ou da tabela dinâmica vinculada.
* Para visualizar e gerenciar a existência desses campos, siga o caminho no menu: **Planejamento e Captação | Requisições | Campos Complementares | Substituição**

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Identificação Parecer de Substituição Pessoas Selecionadas  
Rateio de Centros de Custos

|  |  |
| --- | --- |
|  | Como Fazer |

---

Cancelar Requisição Suspender Requisição Revogar Suspensão Inserir no Fluxo Passar para atendente anterior Remover Pessoas da Seleção  
Incluir Parecer em lote  
Alterar Fluxo da Requisição  
Alterar Aprovador Atual da Requisição  
Alterar Dados da Requisição
