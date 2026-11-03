---
content_hash: f86acf8dab7f1e7bd1e086237ec6f577cb87eba02e3168f031193d750100fac4
fetched_at: '2026-06-29T00:10:08.641033+00:00'
page_id: '452719551'
product: rm
source: tdn-rm
title: Inscrição de Participantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719551
version: 2
---

**Inscrição de Participantes**

Este processo tem como objetivo facilitar a inscrição de participantes nas Turmas de Treinamento. Passos para executar a inscrição dos participantes:

Acessar Desenvolvimento| Inscrição de Participantes.

1) Definição para exibir ou não as reservas por centro de custo. Quando este campo estiver marcado, o sistema verifica a definição de reserva de vagas no anexo "Reservas de Vagas" da Turma para realizar a inserção dos participantes na turma de treinamento.

**Observação**:

- Considera o centro de custo da seção do funcionário.

2) Definição dos critérios para a seleção de participantes.

2.1 Somente inscrever as pessoas que atendem aos pré-requisitos do curso. Quando este campo estiver marcado, somente os participantes que possuírem os pré-requisitos do curso poderão ser relacionados à turma.

2.2 Somente inscrever as pessoas que têm disponibilidade para participar do treinamento Quando este campo estiver marcado, haverá a validação de conflito de agenda (mesmo período de realização) entre as turmas que o participante já está incluído e a turma que o usuário queira incluir o participante. Serão consideradas data e hora de início e término das turmas para esta verificação. A validação ocorre para cada participante no momento que o usuário arrastá-lo para a turma desejada.

2.3 Não inscrever as pessoas que estejam repetindo o treinamento. Quando este campo estiver marcado, haverá a validação se o participante já realizou este curso em uma outra turma de treinamento.

3) Seleção dos participantes.

Filtro disponível por Seção e Função, sendo possível fazer filtro com diversas outras opções. Dentre elas, filtro por Seleção, Vaga de Seleção, Etapa de Seleção e Candidatos da Etapa.

4) Seleção das turmas. Filtro disponível por Curso e Entidade, sendo possível fazer filtro com diversas outras opções. Somente as turmas com o status "aberta" ou "proposta" serão visualizadas.

As turmas serão listadas com o código, nome e quantidade de vagas disponíveis. Posicionando o mouse sobre o nome da turma será possível ver informações do período de realização do treinamento.

**Ações disponíveis:**

- Depois de aplicado os filtros, arraste os participantes e solte na turma em que deseja incluí-los. Você pode selecionar vários participantes simultaneamente, pressionando a tecla "Shift" ao selecionar.

**OBS**.: Neste momento o sistema valida se a turma possui vaga para alocar o candidato. Caso não existam vagas disponíveis, uma mensagem de alerta será exibida informando que a operação não será completada por insuficiência de vagas disponíveis.

* Vínculo entre turma e participante poderá ser desfeito selecionando o participante na árvore de turma e em seguida pressionando a tecla "Delete".  
  **OBS**.: Somente candidatos incluídos nas turmas durante a atual execução do processo poderão ser removidos. A exclusão também pode ser realizada pelo anexo Participantes no cadastro de Turmas.

- Flag "Consumir reservas de vagas automaticamente". Quando este campo estiver marcado e os centros de custo da seção dos funcionários inseridos seja o centro de custo das reservas existentes, o sistema preenche as reservas de vagas. Este parâmetro ficará habilitado somente quando o parâmetro "Exibir reservas por centro de custo" estiver marcado.

- Flag "Remover da lista ao inscrever em uma turma".  
Quando este campo estiver marcado, ao arrastar o participante para a árvore de turmas, o mesmo não será mais visualizado na árvore de participantes.

- Botão "Inscrever candidatos automaticamente".

Ao clicar nessa opção, todos os participantes filtrados na árvore da esquerda serão alocados automaticamente e sequencialmente nas turmas de treinamento selecionadas na árvore da direita, respeitando o número de vagas de cada turma de treinamento.

Quando as vagas de uma turma se esgotarem o sistema passará a preencher as vagas da próxima turma da lista, até que sejam incluídos todos os candidatos ou até que se esgotem as vagas das turmas listadas, o que ocorrer primeiro.

Caso ocorra o preenchimento de todas as vagas disponíveis, os candidatos remanescentes continuarão sendo exibidos na árvore de candidatos.

5) Executar o processo. Participantes inscritos na turma de treinamento. Para visualizar acesse Desenvolvimento|Turmas, Anexo| Participantes.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Com o objetivo de facilitar a alocação dos candidatos da seleção nas turmas de treinamento, este processo também está disponível no anexo dos Candidatos da Etapa da Seleção.  
O usuário deverá filtrar e selecionar todos os candidatos da etapa que deseja inserir em turmas de treinamento e executar o assistente. Apenas os candidatos selecionados serão considerados no assistente.   
Mesmo já tendo carregado a lista de participantes no assistente, o usuário, caso deseje, poderá fazer novos filtros para a seleção de pessoas.  
 

|  |  |
| --- | --- |
|  | Veja Também |

---

**Filtro por perfil para Turmas**  
O filtro por perfil para turmas deve ser respeitado neste assistente de inscrição de participantes. Somente as turmas que pertençam ao filtro criado devem ser visualizadas.  
   
Observação:  O Filtro por perfil para Turmas é criado no perfil do usuário.
