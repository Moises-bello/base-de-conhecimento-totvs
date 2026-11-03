---
content_hash: 3346296e8d0ada10f5de7991ae35a993ccc8dac365fdd41a4c411450d7a232f3
fetched_at: '2026-06-29T00:08:27.419171+00:00'
page_id: '271411197'
product: rm
source: tdn-rm
title: MEDU-1730 DT Análise Curricular Cálculo dos Componentes Curriculares do Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271411197
version: 120
---

# ANÁLISE CURRICULAR - CÁLCULO DOS COMPONENTES CURRICULARES DO ALUNO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Análise Curricular* | *Análise Curricular* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Histórico Ensino Superior - Portal** | **Histórico Ensino Superior - Portal** | | **Histórico Ensino Superior - EducaMobile** | **Histórico Ensino Superior - EducaMobile** | | **Relatório - EDUREL0018 - Análise Curricular** | **Relatório - EDUREL0018 - Análise Curricular** | | **Relatório - EDUREL0028 - Histórico do Ensino Superior** | **Relatório - EDUREL0028 - Histórico do Ensino Superior** |   *Obs.: Apenas para o nível de ensino superior.* |
| **Cadastros Iniciais:** | *Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito.* |
| **Parâmetro(s):** | *Em Configurações | Parâmetros | Secretaria | Geral 2/7:*   * *Habilitar a utilização de mínimos exigidos das atividades curriculares na matriz curricular*   + *Exibir ou ocultar o parâmetro de nome Considerar mínimos exigidos das atividades curriculares que estará localizado dentro do cadastro da Matriz Curricular.*   *No cadastro da matriz curricular:*   * *Considerar mínimos exigidos das atividades curriculares.*    + *Efetuar a validação dos mínimos exigidos na matriz aplicada do aluno. Ou seja, será validado na Análise Curricular (Histórico no Portal / EducaMobile, Relatório EDUREL0018 e Relatório EDUREL0028) se o aluno cumpriu os mínimos exigidos na matriz. Lembrando que todos os alunos que estiverem nesta matriz curricular sofrerão a validação, tanto para os que já formaram ou para os que estão cursando.* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *SGRADE* |
| **Sistema(s) Operacional(is):** | *Windows 7 ou superior* |

## Descrição

Melhoria no calculo dos mínimos exigidos para que o mesmo seja parametrizado, ou seja, será possível por meio de parametrização considerar ou não os mínimos exigidos das atividades curriculares da matriz do aluno.

Para isso foi feito a seguinte melhoria: Criação um parâmetro com o nome **Habilitar a utilização de mínimos exigidos das atividades curriculares na matriz curricular**. O mesmo ficará localizado nas configurações gerais do Educacional em Configurações | Parâmetros | Secretaria | Geral 2/7 e o mesmo será por contexto. O parâmetro irá nascer desabilitado e sua função é exibir ou ocultar o parâmetro de nome **Considerar mínimos exigidos das atividades curriculares** que estará localizado dentro do cadastro da Matriz Curricular.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.16.

## Procedimento para Utilização

Foi criado um parâmetro **Habilitar a utilização de mínimos exigidos das atividades curriculares na matriz curricular**, o mesmo ficará localizado nas configurações gerais do Educacional em Configurações | Parâmetros | Secretaria | Geral 2/7.

O parâmetro irá nascer desabilitado e sua função é exibir ou ocultar o parâmetro de nome **Considerar mínimos exigidos das atividades curriculares** que estará localizado dentro do cadastro da Matriz Curricular.

Para este parâmetro na matriz será necessário rodar o *script* CN.2017.02\_01.

Este parâmetro tem por finalidade efetuar, quando marcado, a validação dos mínimos exigidos na matriz aplicada do aluno. Ou seja, será validado na Análise Curricular (Histórico no Portal / EducaMobile, Relatório EDUREL0018 e Relatório EDUREL0028) se o aluno cumpriu os mínimos exigidos na matriz. Lembrando que todos os alunos que estiverem nesta matriz curricular sofrerão a validação, tanto para os que já formaram ou para os que estão cursando.

O parâmetro **Considerar mínimos exigidos das atividades curriculares** somente será visto como marcado se o mesmo estiver marcado e nas configurações gerais o parâmetro **Habilitar a utilização de mínimos exigidos das atividades curriculares na matriz curricular**estiver marcado, caso contrário será visto como desmarcado.

Ao marcar o parâmetro **Considerar mínimos exigidos das atividades curriculares**, o sistema mudará a forma de validação dos mínimos exigidos na matriz aplicada do aluno. Ou seja, será validado na Análise Curricular (Histórico no Portal / EducaMobile, Relatório EDUREL0018 e Relatório EDUREL0028) se o aluno cumpriu os mínimos exigidos na matriz.

Importante

Lembrando que todos os alunos que estiverem nesta matriz curricular sofrerão a validação, tanto para os que já formaram ou para os que estão cursando.

Informações

* Quando o parâmetro **Considerar mínimos exigidos das atividades curriculares** for marcado e salvo o cadastro o sistema irá efetuar a validação dos valores mínimos dos componentes com os somatórios dos valores mínimos e máximos dos itens curriculares de todas as matrizes aplicada. Sendo que, o valor mínimo do componente deve estar obrigatoriamente entre o somatório dos valores mínimos e máximos dos itens curriculares. Caso esta regra não seja obedecida ao salvar o cadastro será levantada uma exceção que não deixará salvar e será exibido uma mensagem contendo quais componentes não passaram nesta validação;
* Após marcação do parâmetro **Considerar mínimos exigidos das atividades curriculares** o sistema efetuará a validação da regra do item anterior ao se alterar o valor mínimo de um componente. Caso não seja obedecido o sistema levantará uma exceção bloqueando a alteração e uma mensagem informativa será exibida, além disso efetuará a validação na alteração dos valores mínimos/máximos dos itens curriculares, sendo que os somatórios dos mínimos dos itens devem ser no máximo o valor mínimo do componente e o somatório dos valores máximos dos itens devem ser no mínimo o valor mínimo do componente. Caso não seja obedecido o sistema também levantará uma exceção bloqueando a alteração e uma mensagem informativa será exibida.

Observação Importante

Caso o valor mínimo do componente estiver vazio ou zero as regras acima não serão aplicadas!

* O cálculo das horas das atividades curriculares irá considerar o atingimento do valor mínimo de cada componente, somando-se os valores dos itens curriculares cumpridos.   
  Supondo a seguinte situação abaixo, o valor mínimo do componente Inglês é de 30 horas, mas para que seja completado 30 horas é necessário o aluno efetuar o pelo menos 10 horas do item curricular Inglês Básico e 20 horas do item curricular Inglês Avançado deste componente. Se o aluno fizer 100 horas apenas no item curricular Inglês Básico, será aproveitada apenas 10 horas e 20 horas ficariam pendentes para este componente, pois deverá ser feita pelo menos 20 horas do item curricular Inglês Avançado. Além disso, analisando este cenário, o aluno ainda ficaria pendente 60 horas do componente Desenvolvimento, no total estaria devendo 80 horas.  
  Caso o aluno tenha cumprido 100 horas em cada uma das três atividades, o sistema fará o cálculo aproveitando apenas as horas mínimas, ou seja, o cálculo final das horas concluídas será de 90 horas, conforme imagens abaixo.

Cadastro de componente curriculares da matriz aplicada:

| Componente Inglês | Valor mínimo: 30 |
| --- | --- |
| Item curricular: Inglês Básico | Item curricular: Inglês Avançado |
| Valor mínimo: 10 | Valor mínimo: 20 |
| Valor máximo: 100 | Valor máximo: 100 |

| Componente: Desenvolvimento | Valor mínimo: 60 |
| --- | --- |
| Item curricular: C# | |
| Valor mínimo: 60 | |
| Valor máximo: 100 | |

|  |  |  |
| --- | --- | --- |
| Análise Curricular | Relatório EDUREL0018 - Análise Curricular | Relatório EDUREL0028 - Histórico Escolar Ensino Superior |
|  | | |
| Histórico no Portal | | |
|  | | |
| Histórico no EducaMobile | | |

Importante

Caso o tipo de avaliação da matriz curricular estiver por crédito, os cálculos serão feitos pelo o número de créditos.

divs
