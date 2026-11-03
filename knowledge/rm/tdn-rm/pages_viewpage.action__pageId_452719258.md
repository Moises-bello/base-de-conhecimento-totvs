---
content_hash: 6377d09e5ae329254d4aa53af5b872ffca4eda70227f6c136b9518a3cffe6301
fetched_at: '2026-06-29T00:10:04.817366+00:00'
page_id: '452719258'
product: rm
source: tdn-rm
title: Alteração de Dados Funcionais Progressivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719258
version: 5
---

**Alteração de Dados Funcionais Progressivo**

---

Neste anexo o usuário encontra as progressões cadastradas para a requisição de "Alteração de dados funcionais" selecionada.

As progressões podem alterar a função, nível, faixa e salário do funcionário, neste caso poderemos ter uma requisição alterando um funcionário para diferentes tipos de função e salários.

**Observação:**

A alteração dos campos de nível, faixa e salário funcionam de acordo com os parâmetros "Considerar os salários das tabelas salariais" e "Permitir alteração manual do salário", verificando se utiliza ou não as Tabelas Salariais.

As informações mais importantes de uma progressão são:

**Data mínima de efetivação:** Data mínima para efetivação da progressão.

**Proposta de alteração:** Dados futuros do funcionário após a aprovação da progressão.

**Motivo de mudança de salário:** Esse campo é importante por que o sistema permite criar parametrizações para motivos específicos, e a parametrização poderá aplicar alguma regra na inclusão ou edição.

Operações que estão disponíveis nesta tela:

**Inclusão**

Existem duas formas de inclusão de progressão. A primeira ocorre quando o usuário tenta cadastrar uma requisição e o sistema sugere que sejam cadastradas progressões, a segunda é quando o usuário clica no botão incluir e cadastra manualmente uma progressão.

**Dúvida**:  Por que o sistema não bloqueou o inclusão e impediu o usuário de preencher todos os campos?

Por que o sistema precisa saber o motivo da alteração, para saber se existe alguma parametrização para aquele motivo cadastrada no sistema.

**Edição**

O usuário poderá editar as progressões manuais e as sugeridas pelo sistema.

**Importante**:

Não aconselhamos a alteração das datas das progressões de forma que seja afetada a ordem cronológica da criação, o ideal é inserir progressões com datas posteriores as já cadastradas no sistema.

**Exclusão**

A exclusão de uma progressão só poderá ser realizada via processo "Remover alteração de dados funcionais progressiva".

**OBS**.: Quando remove todas as progressões, a requisição assume o valor da primeira progressão cadastrada.

**IMPORTANTE**

Regra para Inclusão, Alteração e Exclusão.

O sistema poderá bloquear a inclusão, edição ou exclusão de uma progressão se alguma regra da parametrização for violada  ou se o status da progressão estiver diferente de "pendente".

**Exibição do menu em anexo**

O sistema realiza duas consultas para saber se o anexo poderá ser exibido na abertura da visão, são elas:

* Se existe parametrização ou progressão registrada no sistema, caso alguma dessas afirmações retorne verdadeiro o anexo é exibido.
* Se estiver tudo correto, feche a visão e abra novamente, por que o anexo só é carregado na abertura da visão.

Caso haja dúvida no cadastro da parametrização consulte o passo a passo no final deste documento.

**Observação:**     A progressão salarial não deve ser aplicada em ***requisições entre coligadas***, pois sua utilização nessa condição pode gerar erros e inconsistências nos dados.

Ressalta-se que, a partir da versão 12.1.2506, o sistema passará a exibir uma mensagem de alerta informando sobre a impossibilidade de realizar a progressão salarial entre coligadas, visando garantir a integridade e a confiabilidade das informações processadas.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Para obter mais informações sobre aumento progressivo clique no link abaixo:

Aumento Progressivo

|  |  |
| --- | --- |
|  | Como Fazer |

---

Passo a Passo - Aumento Progressivo

|  |  |
| --- | --- |
|  | Veja Também |

Transferência com alteração de dados funcionais progressivo
