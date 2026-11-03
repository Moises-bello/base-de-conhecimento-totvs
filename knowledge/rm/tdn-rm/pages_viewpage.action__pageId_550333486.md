---
content_hash: 02930ade998552c00a9ddec7dbb6aa4fd8b8ccba8fa2160347cc2de98de2a2f9
fetched_at: '2026-06-29T00:10:43.765445+00:00'
page_id: '550333486'
product: rm
source: tdn-rm
title: DT Liberação de frequência diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550333486
version: 31
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Educacional |
| Linha de Produto: | Linha RM |
| Segmento: | Educacional |
| Módulo: | Frequência diária - Portal, Educa Mobile e Sistema |
| Função: | Digitação de frequência diária |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [PORTALMOBILE01-10355](https://jiraproducao.totvs.com.br/browse/PORTALMOBILE01-10355) |

## **02. SITUAÇÃO/REQUISITO**

Permitir um controle de liberação de frequência diária para o professor e/ou operador do sistema, pois tal liberação era permitido apenas pelo coordenador definido na turma/disciplina com a marcação do parâmetro "Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina" contido em "Parâmetros | Educacional | Secretaria | Notas/Faltas".

## **03. SOLUÇÃO**

Foi criado um tratamento nos sistemas (Portal, Mobile e Sistema), de maneira que o usuário possa liberar ou não a frequência diária para visualização dos alunos. Lembrando que esse comportamento será permitido apenas se NÃO estiver marcado a liberação pelo coordenador, conforme mostra a figura abaixo:

**Sistema - Digitação de Frequência Diária**

Nessa tela, foi incluído uma legenda para as colunas dos dias que ainda não foram liberados e um novo parâmetro chamado "Liberar frequência após salvar (Ainda não liberado)", que permite ao usuário liberar (marcado) ou não (desmarcado) a frequência, conforme mostra a imagem abaixo:

Para mais informações, acesse a documentação de [Digitação de frequência diária no sistema](https://tdn.totvs.com/x/pPxbGQ).

false

**A partir da versão 12.1.29.231.**

Caso o usuário não informe nenhuma ação na tela, ao clicar no botão: "Salvar", será apresentado a mensagem:

"Deseja liberar a frequência para todos os alunos listados para o período informado?  
Ao marcar "Não", será liberado apenas para a data que teve alteração".

**OBSERVAÇÃO:** É  necessário que seja informado o número de aulas dadas no período no campo: "Número de aulas dadas".

Neste momento, o usuário tem duas opções.

**=>** **Ao marcar "Não":**

   - Será liberado apenas a data que teve alteração (de frequência).

Exemplo: Teve alteração apenas para a data: 23/03, será liberado a frequência apenas para essa data.

   - Se não tiver nenhuma ação na tela, não irá liberar a frequência para o(s) aluno(s).

**=>** **Ao marcar "Sim":**

 - Será liberado a frequência para o(s) aluno(s) para o período informado.

Exemplo: No filtro de: data inicial e Data final, foi informado o período de: 01/03/2021 à 31/03/2021, no caso será liberado a frequência para o período em questão.

**Portal - Frequência**

Para que o usuário possa ter uma experiência única, as alterações do Sistema e Portal foram bem parecidas e tendo divergências apenas de plataforma (Windows e Web), conforme podemos observar na imagem abaixo:

Para mais informações, acesse a documentação de [Frequência diária no portal](https://tdn.totvs.com/x/DaUlE).

**Mobile - Frequência diária**

Nessa tela, como o digitação de frequência é por data e não por período, não teve a necessidade de inserir uma legenda. Mas o campo para liberar ou não a frequência também foi disponibilizado nessa funcionalidade, conforme podemos observar na imagem abaixo:

Para mais informações, acesse a documentação de [chamada do professor no mobile](https://tdn.totvs.com/x/fvCbFg).

Informação

Após salvar a frequência em uma das funcionalidades mostradas acima com o parâmetro marcado "Liberar frequência após salvar", também será marcado o campo de controle "FrequenciaDispWeb" do plano de aula (Campo FREQUENCIADISPWEB da tabela de nome SPLANOAULA terá o valor igual a 1, indicando que a frequência foi liberada).
