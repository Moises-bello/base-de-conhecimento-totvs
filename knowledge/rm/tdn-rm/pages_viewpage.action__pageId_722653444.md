---
content_hash: 510bbe823b124ef813b59920637c7f1cad6a13f9f36c352727f5c223f60d615f
fetched_at: '2026-06-29T00:11:27.371967+00:00'
page_id: '722653444'
product: rm
source: tdn-rm
title: Portal - Geral 1/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=722653444
version: 3
---

A Central de Avisos do professor tem como objetivo, possibilitar que o professor seja alertado dos prazos de suas atividades diárias, como:

* Período de digitação de notas;
* Período de digitação de faltas;
* Período de digitação de conteúdo previsto;
* Período de digitação do conteúdo realizado;
* Período de digitação de plano de aula;
* Alerta para digitação de frequência diária.
* Período de digitação de notas de avaliação;

**Disponível a partir da release: 12.1.31.118**

A regra a ser aplicada para á exibição do aviso referente ao evento: ***Período de digitação de notas de avaliação*** será considerado dois campos referente a data:

           - Data limite digitação (Cadastro da Etapa de Notas)

           - Data de devolução (Cadastro da Avaliação)

O Evento será exibido apenas, se a mesma tiver dentro do prazo de digitação, isso é, será exibido apenas o evento com o status: VENCERÁ EM BREVE.

Será exibido o evento com a respectiva data que acontecer primeiro.

**Exemplo:**

=> Data atual: 26/02

A data limite digitação da Etapa 1 é: 26/02

A data de devolução da avaliação 1 é: 27/02

A data de devolução da avaliação 2 é: 24/02

Resultado esperado: Ao acessar a central de avisos, será exibido:

             => A avaliação 1: Irá considerar a data de devolução da Etapa, pois a data informada acontece primeiro que a data informada na Avaliação.

             => A avaliação 2: Não será exibida, pois a condição referente a data (no caso irá pegar a data informada na avaliação) o prazo já expirou.

Considerações:

Se no cadastro da Etapa, a data limite digitação tiver expirada, o aviso referente ao período de digitação da avaliação, não será apresentado, pois não é possível inserir notas se o prazo de digitação da etapa tiver expirada.

Se no cadastro da Etapa, não tiver informado um período (campo em branco), será exibido o aviso referente ao período de digitação da avaliação somente se a data de devolução tiver dentro do período, isso é: se a data de devolução tiver expirada, não será exibido o aviso.

Principal vantagem é manter o trabalho do professor organizado com alertas a partir dos prazos definidos pela instituição.

Para que essa função esteja disponível será necessário realizar algumas parametrizações.

## **01. PARAMETRIZAÇÃO**

Para que essa funcionalidade fique disponível para o professor, conceder a permissão em:

 **Serviços Globais | Seg****urança | Perfis | Educacional | Portal | Educacional (Portal) | Professor | Central de Avisos**

Em seguida parametrizar a quantidade de dias para os avisos, para que que seja possível mostrar ao professor os prazos que estão próximos ao vencimento, para cada aviso existe um parâmetro para informar quantos dias o aviso começa a ser mostrado no portal.

Atenção

##### Devido a performance, é realizado um cache de 60 minutos das informações carregadas referente a central de avisos. Desta forma, ao fazer uma alteração em algum dado que afete as informações, como exemplo: alterar a data da avaliação, data início e fim da etapa, data início e fim do limite de digitação da etapa, assim como a alteração dos parâmetros, será necessário que o professor faça login novamente no portal para que os dados sejam atualizados ou atualize a página novamente após o tempo de expiração de cache, que é de 60 minutos.

## **02. VISUALIZAÇÃO DO PROCESSO**

false

Para que as disciplinas sejam exibidas no portal:

* A data limite de digitação ser maior ou igual a data atual;
* A turma/disciplina deverá estar ativa;
* O período letivo não poderá estar encerrado;
* O período letivo deverá estar com o parâmetro: "Exibir no portal do professor" habilitado;
* No cadastro da etapa, o parâmetro: "Exibe no portal e na central do aluno" deverá estar habilitado;
* A turma/disciplina não pode ser uma Turma GERENCIADA;
* A frequência diária não poderá estar liberada ao alunos (FREQUENCIADISPWEB).

Após a parametrização, ao logar no portal na página de apresentação, será exibido a opção: Central de Avisos.

O professor contará com o filtro de: Turma/disciplina e Evento, onde por default, será exibido todos os eventos (previamente parametrizado pelo usuário

O filtro de turmas/disciplinas são todas as disciplinas no qual o professor está devidamente parametrizado.

O filtro de Eventos, são os eventos que o usuário do sistema efetuou a parametrização para que o mesmo seja exibido.

     

**Por exemplo:**  
No cadastro da Etapa de Notas, o período de digitação está compreendido entre os dias 01/11/2020 à 30/11/2020 e na parametrização informamos o prazo de 5 dias antes da data final.
