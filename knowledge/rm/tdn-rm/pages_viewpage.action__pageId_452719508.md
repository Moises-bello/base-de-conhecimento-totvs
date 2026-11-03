---
content_hash: d312c3326111d9e4f595d2dce4b0114ac18733636e57cecf3ddebb8844e431bc
fetched_at: '2026-06-29T00:10:08.091643+00:00'
page_id: '452719508'
product: rm
source: tdn-rm
title: Transferência com alteração de dados funcionais progressivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719508
version: 5
---

**Transferência com alteração de dados funcionais progressivo**

Neste anexo o usuário encontra as progressões cadastradas para a requisição de "Transferência com alteração de dados funcionais" selecionada.

As progressões podem alterar função, nível, faixa e salário do funcionário, então poderemos ter uma requisição alterando um funcionário para diferentes tipos de função e salários.

**Observação:**

A alteração dos campos de nível, faixa e salário obedecerão o funcionamento dos parâmetros "Considerar os salários das tabelas salariais" e "Permitir alteração manual do salário", verificando se utiliza ou não as Tabelas Salariais.

As informações mais importantes de uma progressão são:

* **Data mínima de efetivação:** Data mínima para efetivação da progressão.
* **Proposta de alteração:** Dados futuros do funcionário após a aprovação da progressão.
* **Motivo de mudança de salário:** Esse campo é importante por que o sistema permite criar parametrizações para motivos específicos, e a parametrização poderá aplicar alguma validação na inclusão ou edição.

Operações que estão disponíveis nesta tela:

* **Inclusão :**Existem duas formas de inclusão de progressão, a primeira ocorre quando o usuário tenta cadastrar uma requisição e o sistema sugere progressões, a segunda é quando o usuário clica no botão incluir e cadastra manualmente uma progressão.
* **Edição:**O usuário poderá editar as progressões manuais e as sugeridas pelo sistema.

**Importante**: Não aconselhamos a alteração das datas das progressões de forma que seja afetada a ordem cronológica da criação, o ideal é inserir progressões com datas posteriores as já cadastradas no sistema.

* **Exclusão:**A exclusão de uma progressão só poderá ser realizada via processo "Remover transferência com alteração de dados funcionais progressiva".

**OBS**.: Quando remove todas as progressões, a requisição assume o valor da primeira progressão cadastrada.

**IMPORTANTE**:

Regra para Inclusão, Alteração e Exclusão.

O sistema poderá bloquear a inclusão, edição ou exclusão de uma progressão se alguma regra da parametrização for violada  ou se o status da progressão estiver diferente de "pendente".

A transferência entre filiais não permite a inclusão de progressões, ou seja, o sistema não sugere progressão e não permite que insira a mesma manualmente.

Exibição do menu em anexo

O sistema realiza duas consultas para saber se o anexo poderá ser exibido na abertura da visão, são elas: Se existe parametrização ou progressão registrada no sistema, caso alguma dessas afirmações retorne verdadeiro o anexo é exibido.

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

Passo a passo - Aumento Progressivo
