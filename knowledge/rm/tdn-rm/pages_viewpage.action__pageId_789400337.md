---
content_hash: beb3a2acdd39ab109cfb03e77f4dd9a4b3319f4b19fcb59e8b6005ba81943d0c
fetched_at: '2026-06-29T00:11:39.749101+00:00'
page_id: '789400337'
product: rm
source: tdn-rm
title: Criar gerencial/gerenciada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789400337
version: 32
---

Permite configurar turmas gerenciais e gerenciadas que serão utilizadas na futura geração de turmas/disciplinas.

Para realizar a criação de gerencial e gerenciada, é necessário selecionar dois ou mais registros da tabela de resultados:

No exemplo acima, a instituição pode optar por adicionar gerencial/gerenciada selecionando as cinco turmas e criando uma turma gerencial e quatro gerenciadas, conforme abaixo:

É necessário selecionar qual será a turma GERENCIAL, ou seja, qual turma irá gerenciar as outras turmas.

Ao realizar a criação de uma turma gerencial e suas gerenciadas algumas validações são verificadas:

* As datas de inicio e fim das turmas e o tipo de turma, baseado no modelo de turmas, não podem ser diferentes.
* Os Horários e os professores (inclue as associações de horários) da turma disciplina não podem ser diferentes da turma gerencial.
* As turmas/disciplinas envolvidas não podem ter número de aulas semanais divergentes.

Ao encontrar essas divergências o sistema exibe as informações, apenas das regras que estão sendo quebradas.

Ao marcar a opção **Utilizar configurações da turma gerencial selecionada**, o sistema exclui as informações das turma gerenciadas, atualizando essas informações com as informações da Turma gerencial. Caso existam horários e professores nas turmas gerenciadas, estes serão excluídos.

É possível identificar, na tabela de resultados, através dos ícones e do tooltip, a turma GERENCIAL(que gerencia as demanda das demais turmas) e as turmas GERENCIADAS(que são gerenciadas pela turma gerencial).

Clicando na seta para baixo, ao lado do ícone de status, é possível verificar a rastreabilidade, ou seja, é possível ver na turma GERENCIAL, quais são suas turmas gerenciadas e, nas turmas GERENCIADAS, é possível ver quem é sua turma gerencial.

Caso uma turma esteja com o ícone de GERENCIADA, não será possível realizar outra operação de adicionar gerencial/gerenciada com a mesma.

É permitido incluir novas turmas GERENCIADAS dentro de uma GERENCIAL, para isso, selecione na tabela de resultados, a turma identificada como GERENCIAL, em seguida selecione uma ou mais turmas que não possuam identificação de GERENCIAL ou GERENCIADA. Nesse caso, será identificado a turma GERENCIAL e as demais serão automaticamente incluídas como GERENCIADAS.

Ao realizar a criação de uma turma gerencial e suas gerenciadas algumas validações são verificadas:

**Observação!** Turmas GERENCIAL e GERENCIADA não podem ser desalocadas.

**Validações de regras com agrupadora/agrupada:**

* A turma AGRUPADA não pode ser GERENCIAL ou GERENCIADA.
* A turma AGRUPADORA pode ser GERENCIADA, mas não GERENCIAL.
* Uma turma GERENCIAL não pode ser uma AGRUPADA, AGRUPADORA ou GERENCIADA.
* Uma turma GERENCIADA não pode ser uma GERENCIAL ou AGRUPADA

**Turma que contém [subturma](https://tdn.totvs.com/display/LRM/Adicionar+Subturmas)** **associada.**

Caso o parâmetro Utilizar turma/disciplina e subtuma com horários independentes(Parametros| Secretaria|Geral 2/7), estiver desmarcado, o sistema permite realizar a associação de gerencial e gerenciada, mesmo que a estrutura (Código da Subturma e Quantidade) da subturmas estejam diferentes.

Ao marcar o parâmetro **Utilizar turma/disciplina e subtuma com horários independente** e realizar a associação, o sistema exibe uma mensagem informando que as subturmas deve conter o mesmo código e a mesma quantidade de subturma.

Os dados da turma gerenciada são apagados e os dados da gerencial são replicados para a gerenciada.

Não é permitido criar ou remover subturmas para turmas gerenciadas.

Ao criar ou recriar subturmas na turma gerencial, a alteração reflete automaticamente nas turmas gerenciadas, caso o vínculo entre elas já exista.

Caso uma turma/disciplina com subturmas for convertida em gerenciada, sua estrutura de subturmas será removida e passará a refletir a da turma gerencial.

Para subturmas em que o horário ou o professor diferem, ao realizar a associação, o sistema exibe uma mensagem de validação.

**Turma que contém [alocação de professor sem horário](https://tdn.totvs.com/pages/viewpage.action?pageId=731215136#:~:text=Realizando%20aloca%C3%A7%C3%A3o%20de%20Professores%20sem%20hor%C3%A1rio)** **associada.**

Ao selecionar turmas para serem gerenciadas, será realizada uma validação com base na estrutura de alocação de professores e horários. A validação seguirá os seguintes cenários:

1. **Turmas com professores alocados, mas sem horários definidos:**
   * Se uma turma selecionada para ser gerenciada possui um ou mais professores alocados, porém sem horários definidos, a turma gerencial (aquela que irá gerenciar as demais) deverá ter os mesmos professores alocados sem horários.
2. **Turmas com professores alocados e horários definidos:**
   * Caso as turmas selecionadas para serem gerenciadas possuam professores alocados com horários definidos, a turma gerencial também deverá seguir essa mesma estrutura. Ou seja, deverá ter os mesmos professores alocados com os respectivos horários.

Se a turma gerencial não possuir a mesma estrutura de alocação (professores e horários) que as turmas selecionadas para serem gerenciadas, a validação falhará e uma mensagem de erro será retornada.

Abaixo um exemplo:  
  
Turmas ainda sem associação gerencial/gerenciada:   
  
  
  
Professores alocados nas turmas :   
  
  
  
  
Ao tentar criar à associação gerencial gerenciada esperado que:   
  
  
  
Vale ressaltar que assim como as outras validações, o usuário poderá escolher que os dados da gerencial sejam considerados como absolutos, e o sistema irá fazer as modificações nas turmas selecionadas para serem gerenciadas.
