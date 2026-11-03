---
content_hash: db64de817722e9541bb76aaed7382d131010ee1bd3844949dc0d15d53d5a4f1f
fetched_at: '2026-06-29T00:10:59.034859+00:00'
page_id: '610528299'
product: rm
source: tdn-rm
title: ACELERADOR DE IMPLANTAÇÃO - FOLHA DE PAGAMENTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=610528299
version: 15
---

**01 -** **ATUALIZADOR**

A base deve estar atualizada. No módulo de Serviços Globais | Administração | Cópia de Coligada | Cadastro de  Entidades deverá existir as entidades da Folha de Pagamento a partir do código 86 - Cargos.

**02 - COLIGADA**

Criar a coligada

**03 - Acessar o módulo Gestão contábil**

**Para a inclusão de Filiais e máscaras na coligada destino é necessário estar no módulo Gestão Contábil e seguir a seguinte ordem:**

1. Acessar módulo Gestão Contábil
2. Alterar o contexto para a coligada de destino
3. Inserir as Filiais e máscaras necessárias

**Motivo:** Se acessar o módulo Folha de Pagamento no contexto da coligada destino serão exigidos valores obrigatórios no parametrizador.

**04 - FILIAL**

Esse item poderá ser obrigatório ou não, depende de como será feita a cópia entre coligadas.

**Atenção:** Esse procedimento deve ser executado caso o usuário faça cópia de tabela que o código da Filial seja obrigatório, como por exemplo cópia de Departamento.  Ou para o caso de existir a informação da Filial nos registros das tabelas como centro de custo, agrupamento de contas contábeis e agrupamento de contas gerenciais que a informação da Filial não é obrigatória mas a coligada utiliza essas informações.

**Exemplo:** Criar Filiais na coligada de destino com os mesmos códigos das Filiais existentes na origem.

O sistema valida o código da Filial, então será feito da seguinte forma:

Criação da Filial em cada coligada:

|  |  |  |
| --- | --- | --- |
| **COLIGADA ORIGEM** |  |  |
|  | **CÓDIGO DA FILIAL** | **NOME DA FILIAL** |
|  | 1 | MATRIZ |
|  | 2 | BELO HORIZONTE |
|  | 3 | PORTO ALEGRE |

|  |  |  |
| --- | --- | --- |
| **COLIGADA DESTINO** |  |  |
|  | **CÓDIGO DA FILIAL** | **NOME DA FILIAL** |
|  | 1 | BELÉM |
|  | 2 | SALVADOR |
|  | 3 | PALMAS |

Ao copiar o Departamento entre coligadas e no cadastro do Departamento 01 estiver o código da Filial 1 – Matriz, será copiado e ao finalizar o Departamento 01 da coligada de destino terá Filial 1 – Belém.

Assim será feito para qualquer cadastro que utilize a informação de Filial. Caso o usuário queira alterar a Filial deve acessar o cadastro na coligada de destino, como no exemplo o Departamento, e alterar para a Filial desejada.

**05 –** **MÁSCARAS OBRIGATÓRIAS**

Existem máscaras que devem cadastradas no módulo de Gestão contábil antes da cópia entre coligadas.

**Atenção:** **Para a inclusão das máscaras abaixo siga na seguinte ordem:**

1. Acessar módulo Gestão Contábil
2. Alterar o contexto para a coligada de destino
3. Alterar máscaras, inclusive a máscara de Departamento nos Parâmetros Globais - **Confira se todas as máscaras relacionadas abaixo foram inseridas para somente depois voltar para a coligada origem, estando ainda no módulo Gestão Contábil.**
4. Alterar o contexto para a coligada origem
5. Acessar o módulo Serviços Globais

**Motivo:** Se acessar o módulo Folha de Pagamento no contexto da coligada destino serão exigidos valores obrigatórios no parametrizador.

* **MÁSCARA DO** **CENTRO DE CUSTO**

Acessar o módulo Gestão Contábil na coligada de destino – Informar máscara do Centro de Custo em Ambiente | Parâmetros | TOTVS Gestão Contábil | Lançamentos – Centro de Custo

* **MÁSCARA DO** **PLANO DE CONTAS CONTÁBIL**

Acessar o módulo Gestão Contábil na coligada de destino – Informar a máscara do Plano de Contas Contábil em Ambiente | Parâmetros | TOTVS Gestão Contábil | Lançamentos -  Plano de Contas - Plano de Contas Contábil

* **MÁSCARA DO** **PLANO DE CONTAS GERENCIAL**

Acessar o módulo Gestão Contábil na coligada de destino – Informar a máscara do Plano de Contas Gerencial em Ambiente | Parâmetros | TOTVS Gestão Contábil | Lançamentos -  Plano de Contas - Plano de Contas Gerencial

* **MÁSCARA DO** **DEPARTAMENTO**

Informar máscara Departamento da coligada de destino nos parâmetros Globais em Ambiente | Parâmetros | Parâmetros Globais - Gerais

**Observação:** Informe essa máscara enquanto estiver no módulo de Gestão Contábil da coligada de destino.

**ATENÇÃO:** Para a cópia do Departamento deve ser verificado o item 2 deste documento sobre a informação do código da filial.

**06 - TEMPLATE**

Acessar menu Gestão | TOTVS Compartilhamento e pesquisar por FOP - Acelerador de Implantação - Folha de Pagamento e baixar o arquivo.

Acessar o módulo de Serviços Globais | Administração | Cópia de Coligada | Cadastro de template e estará disponível.

Mais informações sobre as taeblas disponibilizadas:

**Observação:** Para copiar entre coligadas o contexto deve estar com a coligada origem.

Para fazer a cópia da coligada, selecione o Template e execute o processo “Cópia entre coligadas”.

**Atenção:** Existe um Template padrão que poderá ser importado e para editar o Template padrão é necessário criar uma cópia para customizá-la.

Veja maiores detalhes em<https://tdn.totvs.com/pages/releaseview.action?pageId=592067102>

No processo pode ser selecionado o tipo de gravação de dados que será realizado:

**Gravar dados por conjunto de cópia (transação) parametrizada no template** - Neste caso somente salva a cópia após o conjunto de cópia (transação) estiver finalizado. Se houver algum registro inconsistente na coligada origem nenhum registro será salvo, inclusive das outras tabelas relacionadas no conjunto de cópia (transação).

**Gravar dados registro por registro** - Neste caso se houver algum registro com inconsistência na coligada origem somente o registro inconsistente não será salvo. Porém pode degradar a performance da cópia e é recomendável marcar a opção de "Substitui registros no destino se eles já existirem" em conjunto com a opção de controle de transação registro a registro, pois caso haja necessidade de rodar a copia novamente ou reprocessar pode ocorrer erro de registro já existente na coligada de destino.

**OBSERVAÇÕES:**

**01 - Grupo de eventos** – Caso aconteça de não copiar algum grupo de evento com a seguinte mensagem:

*Processando Grupo de Eventos 01... Erro:Este grupo de evento não está com o parâmetro marcado 'Lançar Eventos do Grupo'*

Verifique se no grupo de eventos em que o parâmetro 'Lançar Eventos do Grupo' está desmarcado existe evento cadastrado na pasta “Eventos do Grupo” e o parâmetro foi somente desmarcado sem excluir esse evento. Exclua o evento e desmarque o parâmetro 'Lançar Eventos do Grupo' novamente que o grupo de evento será copiado.

**02 - Permissão de acesso** – O usuário que for executar o processo deve ter perfil de acesso que tenha permissão para cópia entre coligadas de cada módulo (tabela).
