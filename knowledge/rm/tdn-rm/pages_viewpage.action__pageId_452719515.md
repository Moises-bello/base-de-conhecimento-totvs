---
content_hash: 9428abb74d4eff43be355dcd81055376596b653672c76ac7759dec9d8e86c74e
fetched_at: '2026-06-29T00:10:08.445558+00:00'
page_id: '452719515'
product: rm
source: tdn-rm
title: Assistente para Fornecimento Automático de EPI/EPC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719515
version: 10
---

## **Assistente para Fornecimento Automático de EPI**

A partir deste assistente, poderá ser associado um EPI ou vários EPI´s para uma ou mais pessoas ou EPC ou vários EPC´s para um ou mais Locais de Trabalho.

O fornecimento é feito automaticamente, após escolhidas as pessoas, os destinos e os EPI/EPC´s.

Após a finalização do processo de fornecimento automático, os dados poderão ser conferidos no cadastro do funcionário: Cadastros | Funcionários | Anexos | Segurança e Medicina | EPI's e também pelo relatório específico gerado ao final do processo.

O relatório a ser utilizado no Assistente para fornecimento de EPI/EPC deve conter como parâmetros os campos CODCOLIGADA, IDDESCARTE, IDDEVOLUCAO, IDEMPRESTIMO da tabela VEMPRESTIMOEPI para que o mesmo seja gerado corretamente ao final do processo.

### **Executando o Assistente de Fornecimento:**

* Deverá ser definido o tipo de ação:
  + Fornecimento
  + Devolução
  + Descarte
* A quem se destina:
  + Apenas Funcionários de Acordo com a Exposição a Riscos
  + Qualquer pessoa
  + Apenas Funcionários
  + Local de Trabalho

#### **Fornecendo um EPI/EPC:**

Após escolher a ação do tipo: "Fornecimento", o usuário deverá definir a quem se destina o EPI.

Caso o mesmo escolha:

* "Qualquer pessoa", o sistema exibirá na segunda tela do assistente, de acordo com o filtro criado pelo usuário qualquer pessoa cadastrada no sistema.
* "Apenas Funcionários", o sistema exibirá na segunda tela do assistente, de acordo com o filtro criado pelo usuário apenas pessoas que estejam cadastradas no sistema como FUNCIONÁRIOS.
* "Local de Trabalho", o sistema exibirá na segunda tela do assistente, de acordo com o filtro criado pelo usuário os locais de trabalho cadastrados.

Na terceira tela do assistente, no lado esquerdo, quando o sistema não estiver trabalhando integrado ou estiver integrado com algum sistema externo, independente do destinatário escolhido para recebimento do EPI/EPC, serão exibidas opções de filtro para seleção dos EPI/EPC's a serem fornecidos:

"Código do Risco" e "Código do Grupo de EPI".

O usuário deverá escolher de qual lote o EPI/EPC será retirado.

*IMPORTANTE: O processo em Lote tem o benefício da inclusão coletiva em uma única ação, desta forma ao escolher o lote a ser adionado você deverá realizar a seleção de todos os registros que serão fornecidos de uma vez e depois clique no botão <OK>.*

Quando integrado com o Totvs Gestão de Estoque, Compras e Faturamento, independente do destinatário escolhido para recebimento do EPI, será exibida como opção de filtro "Local de Estoque" para seleção dos EPI/EPC's a serem fornecidos. O usuário deverá escolher de qual local de estoque o EPI será retirado.

Ainda nesta tela, quando integrado com o Totvs Gestão de Estoque, Compras e Faturamento, o usuário tem a opção de escolher que apenas EPI's com quantidade maior que zero sejam exibidos, para tal, o parâmetro: "Buscar apenas EPI/EPC's com quantidade maior que zero" deverá ser marcado.

Já do lado direito, ainda na mesma tela, serão informados detalhes do fornecimento do EPI/EPC. O usuário deverá definir a data de empréstimo a ser considerada:

* Livre: Pode-se informar qualquer data e a mesma será válida para todos os funcionários selecionados.
* Admissão: Será considerada a data de admissão do funcionário.
* Última mudança de seção: Será considerada a última data de mudança de seção de cada funcionário. A admissão de um funcionário é considerada como mudança de seção, portanto, se o funcionário nunca mudou de seção será considerada a data de admissão.

Quando integrado com o Totvs Gestão de Estoque, Compras e Faturamento, o usuário deverá informar à qual Centro de Custo este EPI/EPC pertence.

Nesta tela será possível o usuário informar se o EPI/EPC que está sendo emprestado ao funcionário é "Eficaz" ou não.

Caso o destino for "Apenas Funcionários de Acordo com a Exposição a Riscos" é feita uma validação para verificar se os funcionários selecionados possuem um Reconhecimento/Avaliação de Risco que possui esse EPI/EPC vinculada a ela.

Na quarta tela do assistente será exibido um resumo do(s) empréstimo(s) que será(ão) realizado(s).

O sistema demonstrará informações do EPI/EPC nos seguintes campos: "Situação", "Cód. EPI", "Id. Lote", "Nome", "Item do EPI", "Detalhe", "Data do Empréstimo" e "Ação".

Nesta tela, será possível "setar" o tipo de ação a ser executada no momento do empréstimo: "Fornecer", "Devolver/Descartar e fornecer um novo" e "Não fornecer".

Na quinta tela do assistente o usuário deverá clicar no botão: "Executar" para que o sistema conclua o processo de fornecimento do EPI/EPC.

É possível também nesta tela setar a execução do processo novamente, marcando a opção: "Executar este processo novamente ao término da execução".

Ao final do processo o sistema irá gerar "Id. de Empréstimo" dos EPI's e habilitará a opção para geração de um relatório de conferência.

**Observação:**

Para que a geração do relatório seja possível, o relatório criado para este fim deve ser do tipo: "Segurança e Saúde Ocupacional".

O relatório a ser utilizado no Assistente para fornecimento de EPI deve conter como parâmetros os campos CODCOLIGADA, IDDESCARTE, IDDEVOLUCAO, IDEMPRESTIMO da tabela VEMPRESTIMOEPI para que o mesmo seja gerado corretamente ao final do processo.

#### **Devolvendo um EPI/EPC:**

**Para essa ação o usuário deverá marcar a opção devolução na tela do assistente.**

Encontra-se disponível também a flag "Aceito Sugestão na Ação". 

* Com a flag marcada será sugerido ao usuário a ação de devolução para todos os EPIs/EPCs fornecidos para a pessoa, funcionário ou local de trabalho. (Mesmo com a sugestão o usuário poderá realizar o ajuste das ações na tela do assistente).
* Com a flag desmarcada não serão sugeridas ações de devoluções para os EPIS/EPCs, desta forma o usuário poderá escolher a ação para cada item na tela do assistente.

Após escolher a ação do tipo: "Devolução", o usuário deverá definir que tipo de destinatário está devolvendo o EPI/EPC.

Na segunda tela do assistente o usuário deverá selecionar a pessoa que está devolvendo o EPI, e na tela seguinte, informar o motivo pelo qual este EPI está sendo devolvido.

Quando integrado com o Totvs Gestão de Estoque, Compras e Faturamento, o sistema exige que seja informado o "Centro de Custo" e o "Local de Estoque" do EPI/EPC.

Na quarta tela do assistente serão exibidos os EPI's a serem devolvidos pela pessoa, funcionário ou local de trabalho selecionada na etapa anterior, e o usuário tem a opção de:

* Devolver: O usuário devolverá este EPI/EPC e após higienização este poderá ser utilizado por outra pessoa.
* Não Devolver: O item não será devolvido.

Na quinta tela do assistente o usuário deverá clicar no botão: "Executar" para que o sistema conclua o processo de devolução do EPI/EPC.

#### **Descartando um EPI/EPC:**

**Para essa ação o usuário deverá marcar a opção 'descarte' na tela do assistente.**

Encontra-se disponível também a flag "Aceito Sugestão na Ação". 

* Com a flag marcada será sugerido ao usuário a ação de descartar todos os EPIs/EPCs fornecidos para a pessoa, funcionário ou local de trabalho. (Mesmo marcando a flag "Aceito Sugestão na Ação" o usuário poderá realizar o ajuste das ações na etapa 4 do assistente de fornecimento).
* Com a flag desmarcada não serão sugeridas ações de descarte para os EPIS/EPCs, desta forma o usuário poderá escolher a ação para cada item na etapa 4 do assistente.

Após escolher a ação do tipo: "Descartar", o usuário deverá definir que tipo de destinatário está descartando o EPI/EPC.

Na segunda tela do assistente o usuário deverá selecionar a pessoa que está descartando o EPI.

Na terceira tela do assistente, quando integrado com o Totvs Gestão de Estoque, Compras e Faturamento, o sistema exige que seja informado o "Centro de Custo" e o "Local de Estoque" do EPI/EPC.

Na quarta tela serão exibidos os EPI's a serem descartados pela pessoa, funcionário ou local de estoque selecionada na etapa anterior, e o usuário tem a opção de:

* Descartar: O usuário descartará o EPI/EPC fornecido.
* Não Descartar: O usuário não descatará o EPI/EPC fornecido para o funcionário, pessoa ou local de estoque

Na quinta tela do assistente o usuário deverá clicar no botão: "Executar" para que o sistema conclua o processo de descarte do EPI/EPC.

**Observação**: Foi criada a coluna PERCENTUALUTILIZADO na tabela VEPI, que será preenchida após o processo de devolução do EPI, representando o % utilizado do EPI pelo funcionário.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Parametrização Integração Totvs Gestão de Estoque, Compras e Faturamento
