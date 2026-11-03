---
content_hash: f461cfd3f8e9a038d9cd6c9815ad405331c01188df7f13e1e42d0be4d4706a03
fetched_at: '2026-06-29T00:11:21.588212+00:00'
page_id: '697699589'
product: rm
source: tdn-rm
title: Gestão de Fiadores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697699589
version: 31
---

---

A tela de Gestão de  está disponível através do menu Financeiro/Contábil → Contrato → Fiadores → Gestão de Fiadores.

ATENÇÃO

Disponível apenas para o nível de ensino **superior**

Com intuito de facilitar os processos de gestão dos fiadores, esta funcionalidade possibilita ativar/desativar e validar fiadores, podendo alterar seu status. A funcionalidade permite a execução de filtros avançados, e por período letivo para obter os fiadores. A tela principal apresenta também CARDS para facilitar a visualização da quantidade de fiadores por Status.

Visão GeralIMPORTANTE

Para o funcionamento da gestão de fiadores é preciso que o período letivo da matrícula esteja parametrizado. Vide .

No filtro de Período Letivo (Matriz Curricular) são listados apenas os períodos que ainda **não** foram **encerrados**. **E este filtro é aplicado no período letivo da matriz curricular vinculada ao Fiador.**

A tela exibe por padrão a lista dos fiadores pelo período letivo da matriz curricular configurado no contexto atual do usuário. Os fiadores que não possuem matriz curricular vinculada sempre são exibidos, pois não tem vinculo com período letivo.

As linhas exibidas podem ser expandidas possibilitando a visualização da matriz curricular vinculada ao fiador quando houver, os documentos do fiador e da justificativa de reprovação do fiador. A justificativa de reprovação será exibida somente para os fiadores com status reprovado.

Ao clicar no botão de filtro avançado, o usuário pode analisar os fiadores de forma mais específica com a possibilidade de filtrar por, Coligada, Filial, Nível de ensino, Período letivo, Curso, Habilitação, Matriz, Turno e também por Aluno.

Na execução do filtro avançado o usuário é direcionado para a listagem dos fiadores correspondente ao filtro informado.

Na tela do resultado da pesquisa avançada temos o filtro por Status que possibilita especificar ainda mais os fiadores para gestão.

Permissões de acesso

A visualização da Gestão de Fiador é permitida através da permissão de acesso de menu para a tela de Gestão de Fiador e na permissão da Gestão Educacional

As modificações do fiador através da tela de Gestão de Fiadores, o usuário deve possuir a permissão já existente de edição de fiador.

Edição de Fiador

Na tela de gestão é possível ativar/desativar o fiador e também fazer a alteração de status. Para Cada status possui uma cor específica seguindo os padrões de semáforo, o que aumenta a qualidade da interação do usuário.

A alteração do Status do fiador, basta clicar sobre o Status atual do fiador e selecionar a opção desejada.

A **confirmação** da alteração é solicitada, e após confirmar se o usuário possuir **as permissões** necessárias o status do fiador é alterado.

Na reprovação do fiador terá a **solicitação do motivo** da reprovação. Desta forma, o usuário poderá informar o motivo que o fiador do aluno foi reprovado.

A ativação/desativação do fiador basta clicar sobre o **Toggle** na coluna **Ativo/Inativo.** E terá a solicitação de confirmação da alteração do status do fiador.

Busca Avançada

Na tela principal da gestão de fiadores é possível executar a função de **busca avançada**.

O acesso da busca avançada é através do botão presente ao lado da busca por período letivo.

Na tela de busca avançada existem algumas regras e condições de uso.

1 - A busca avançada permite que o usuário efetue a busca de fiadores de outros contextos que além do contexto logado. Para alterar o contexto é preciso que o sistema esteja parametrizado. A parametrização é acessível através do seguinte menu "Configurações Globais | Segurança | Perfis => Sistema Educacional | Anexos => Parâmetros Educacionais" na aba de Financeiro opção "Restringir acesso a opção “Habilitar multi contexto (aplicar filtro por coligada, filial e nível de ensino)” na visão de gestão de fiadores", quando a opção estiver marcada, não será possível a seleção de contextos diferentes do atual no filtro avançado.

2 - É possível executar a busca avançada desde que o contexto esteja informado, ou seja, os campos de busca Coligada, Filial e Nível de ensino sempre devem estar preenchidos para prosseguir com a busca.

3 - Conforme os campos vão sendo preenchidos o próximo campo fica disponível para preenchimento.

4 - O campo Aluno efetua a pesquisa dos alunos de acordo com os filtros preenchidos previamente, e é possível pesquisar o aluno digitando os três primeiros dígitos do RA ou do nome do aluno.

Ex. filtros por aluno:

Retorna a listagem de alunos para o contexto informado

Retorna listagem de alunos matriculados no curso de ENGENHARIA AGRONÔMICA

Resultado da Busca Avançada

A tela de resultado da busca avançada é similar à tela inicial de gestão do fiador, permite a edição dos fiadores e permite filtrar por Status do fiador.

Ambas as telas de listagem de fiador possuem o recurso de paginação automática (infinite scroll), conforme a barra da listagem for descendo o sistema efetua uma nova pesquisa adicionando os próximos fiadores na sequencia.
