---
content_hash: 445fa795a7eb8209ca55b51c295dcb2cceba7ed86aec22f9350debdb58ebbaae
fetched_at: '2026-06-29T00:06:27.007994+00:00'
page_id: '229147486'
product: rm
source: tdn-rm
title: DT_Gestao_de_Metas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Gestao_de_Metas
version: 1
---

# Gestão de Metas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | pdi | metas | |
| **Versões/Release:** | *12.1.4* |

## Descrição

A Gestão de Metas tem como objetivo definir o caminho (metas) a ser cumprido pelos funcionários para se chegar a um objetivo. Utilizando o Totvs Portal, gestores podem acompanhar as metas de todos os seus participantes. Pontos de impacto da Gestão de Metas:

1) PDI: Utiliza a estrutura de metas e seu acompanhamento para criar as ações e lançamentos de completude.

2) Requisitos de Acesso: Realiza a concessão de requisitos de acesso, ao realizar o cumprimento das metas

## Procedimento para Utilização

**Cadastro da meta**

Acessar Acompanhamento / Gestão de Metas para criar um novo registro.

Nome: campo descritivo para nomear a Gestão de Metas;

Status: campo que conterá o status da Gestão de Metas. Este não é editável e pode conter somente os seguintes valores: Aberta, Em planejamento, Suspensa/Replanejamento, Cancelada e Finalizada;

\*\*\*Somente metas com o Status Aberta são visualizadas no Totvs Portal.

Descrição: campo descritivo para maiores explicações sobre a meta;

Data início/Data fim: campo que controla a data de início/fim da meta. Se a data fim for menor que a data de acesso do avaliador no Totvs Portal, a meta não é visualizada;

Grupo da meta: campo que define em qual grupo as metas serão vinculadas;

**Cadastro da meta tipo agrupadora**

Tipo: Campo que define qual será o tipo da meta:  
- Agrupadora

Composição de metas: aba para definição da composição das metas. A composição pode conter “Meta valor” e “Meta agrupadora”. Incluir metas com o status planejamento ou suspenso/replanejamento.   
Cada meta vinculada terá um percentual de participação na “meta pai”. O percentual deverá ser um valor numérico entre 0 e 100.  
Se o valor do somatório dos percentuais for maior que 100, será emitido um alerta para o usuário revisar os percentuais definidos.  
Somente poderá ser alterada a composição de metas com o status “Em planejamento” ou “Suspenso / Replanejamento”, e somente metas neste mesmo status poderão ser incluídas na composição de metas.

Atribuições:

- Avaliador: um funcionário ou um externo. Apenas uma opção deve ser preenchida;  
 - Avaliados: uma seção, uma equipe, um funcionário ou um externo. Apenas uma opção deve ser preenchida;

Somente poderá ser alterada a atribuição de metas com o status “Em planejamento” ou “Suspenso / Replanejamento”.

**1.2 – Cadastro da meta tipo valor**

Tipo: campo que define qual será o tipo da meta:   
- Valor

Configuração  
Tipo de valor

- Valor de referência   
- Faixa de valores: aba para definição das faixas de valores a serem utilizadas na apuração das metas. Será através do enquadramento de faixas que será possível verificar o cumprimento de uma meta.   
O cadastro de faixas permitirá que o usuário crie faixas que cubram todos os valores possíveis, utilizando para isso os operadores <, <=, >, >= e =.   
A faixa que estiver com o campo “Meta Cumprida quando estiver nesta faixa” marcado, define a faixa onde a meta estará cumprida.

Valor de referência   
- Valor referência: valor base para cumprimento da meta.   
- Cumprimento da meta  
         Acima do valor de referência.  
         Abaixo do valor de referência.

Forma de avaliação  
- Somatório dos lançamentos   
- Último lançamento

Opções   
Avaliado visualiza meta: campo que define que quando o avaliado acessar o Totvs Portal, suas metas serão visualizadas.

Exige aceite dos avaliados: campo que define que o avaliador pode solicitar o aceite da meta ao avaliado através do Totvs Portal. Ao solicitar o aceite, o avaliado recebe email com a informação de pendência de aceite. Este campo somente será habilitado se o campo “Avaliado visualiza meta” estiver marcado.

Avaliado pode lançar resultado: campo que define que quando o avaliado acessar o Totvs Portal é permitido realizar lançamento de resultados nas metas. Este campo somente será habilitado se o campo “Avaliado visualiza meta” estiver marcado.

Lançamento exige aprovação do avaliador: campo que define que quando o avaliado incluir um lançamento através do Totvs Portal, o lançamento ficará pendente até a aprovação do avaliador. Este campo somente será habilitado se o campo “Avaliado pode lançar resultado” estiver marcado.

Envio automático de e-mail após lançamento: campo que define que quando o lançamento da meta for realizado no Totvs Portal, um email será enviado ao avaliador.

Atribuições

- Avaliador: um funcionário ou um externo. Apenas uma opção deve ser preenchida;

- Avaliados: uma seção, uma equipe, um funcionário ou um externo. Apenas uma opção deve ser preenchida;

Somente poderá ser alterada a atribuição de metas com o status “Em planejamento” ou “Suspenso / Replanejamento”.

**Atenção**

- Uma meta só poderá ser excluída ou ter sua atribuição e sua composição alteradas se estiver com o status “Planejamento”.  
- Uma meta agrupadora que for “meta pai” numa composição de metas, não poderá ser alterada para “meta valor”.  
- O resultado de uma meta se refere diretamente a ela e não à atribuição. Portanto a apuração do resultado não será feita por membros, mas sim em relação à meta.

**Em caso de dúvidas consulte o help do aplicativo ou entre em contato pelo Help Desk**.

**2 – Lançamento de resultados de metas**

Acessar Acompanhamento / Gestão de Metas e selecionar uma meta do tipo Valor.

Aba Lançamentos: aba que permite que o usuário registre os resultados de uma determinada meta;

O campo “Data alteração” por padrão insere a data atual e esta nunca pode ser maior que ela.   
Pode ser preenchido o campo “Valor” ou “Comentário”, ou se desejar os dois campos simultaneamente.  
 Somente metas com o status “Aberta” permitem a inclusão, exclusão e edição de lançamentos de resultados.

Processo: Lançamento de resultados de metas

Este processo tem por objetivo facilitar o lançamento em lote de resultados de metas. Somente metas do tipo “Valor” e com o status “Aberta” poderão ter valores de resultados lançados.   
Se uma meta agrupadora for selecionada para a execução do processo, o usuário deve selecionar as metas filhas que estarão disponíveis para o lançamento de resultados na etapa seguinte.   
Para efetuar o lançamento de resultados deve seguir os seguintes passos:

1 – Selecionar as metas disponíveis;   
2 – Selecionar uma ou mais atribuições para fazer o lançamento de resultados;   
3 – Informar os dados do lançamento (Valor e/ou Comentário e Data de alteração);   
4 – Sistema exibe resultados lançados no processo, sendo possível “Excluir Lançamento” e alterar o lançamento antes de finalizar o processo;   
5 – Resumo dos lançamentos e conclusão do processo.

Observação:   
- A data terá como valor padrão a data atual e é de informação obrigatória.   
- Os campos Valor e Comentário não são obrigatórios, mas ao menos um dos dois sempre deverá ser informado.

3 – Planejamento de metas

Este processo tem por objetivo auxiliar o usuário a fazer o planejamento de metas. Através deste processo será possível criar metas e atribuições, além de permitir a réplica dessas metas, quando forem do tipo “Valor”. Só não será permitido a edição da composição das metas agrupadoras.  
Para efetuar o planejamento de metas deve seguir os seguintes passos:

1 – Informar os dados iniciais da meta;   
2 – Se a meta for do tipo Agrupadora:   
      2.1 - Escolher a forma de atribuição de metas;   
      2.2 – Definir os avaliados da meta;   
      2.3 – Definir o avaliador da meta. Verificar as atribuições definidas até o momento, escolhendo prosseguir ou acrescentar novas atribuições;   
      2.4 – Resumo da solicitação e conclusão do processo;   
3 – Se a meta for do tipo Valor:   
      3.1 – Informar a complementação das informações da meta;   
      3.2 – Se o tipo de valor para cumprimento da meta for Valor de Referência:   
      3.2.1 - Escolher a forma de atribuição de metas;   
      3.2.2 – Escolher a periodicidade (mensal, bimestral, trimestral, quadrimestral e semestral);   
      3.2.3 – Escolher se a meta é individual ou coletiva;   
      3.2.4 – Possibilidade de definir se as metas criadas no processo serão adicionadas à composição de uma meta agrupadora existente.   
      3.2.5 - Definir os avaliados da meta;   
      3.2.6 - Definir o avaliador da meta. Verificar as atribuições definidas até o momento, escolhendo prosseguir ou acrescentar novas atribuições;   
      3.2.7 - Resumo da solicitação e conclusão do processo;   
  3.3 – Se o tipo de valor para cumprimento da meta for Faixa de Valores:   
     3.3.1 – Definir as faixas de valores;   
     3.3.2 - Escolher a forma de atribuição de metas;   
     3.3.3 – Escolher a periodicidade (mensal, bimestral, trimestral, quadrimestral e semestral);  
     3.3.4 – Escolher se a meta é individual ou coletiva;   
     3.3.5 – Possibilidade de definir se as metas criadas no processo serão adicionadas à composição de uma meta agrupadora existente.   
     3.3.6 - Definir os avaliados da meta;  
     3.3.7 - Definir o avaliador da meta. Verificar as atribuições definidas até o momento, escolhendo prosseguir ou acrescentar novas atribuições;   
     3.3.8 - Resumo da solicitação e conclusão do processo;   
4 – Finalizar o planejamento de metas.

**4 – Vincular/Desvincular Requisitos de Acesso e Metas**

Este processo tem como objetivo vincular os Requisitos de Acesso às Metas.   
Para efetuar o vínculo deve seguir os seguintes passos:

1 – Selecionar uma meta do tipo Agrupadora para executar o processo;  
 2 – Realizar o filtro de requisitos de acesso;   
3 – Selecionar os requisitos de acesso desejados na árvore da esquerda. É possível selecionar vários registros simultaneamente pressionando a tecla “SHIFT” e “CTRL”;  
 4 – Incluir os requisitos de acesso nas metas, arrastando e soltando os mesmos sobre as metas da árvore da direita. É possível deletar um registro, selecionando-o e pressionando a tecla “DELETE”.   
5 – Conclusão do processo.

Os requisitos de acesso vinculados podem ser visualizados através do Anexo “Requisitos de Acesso vinculados”

**5 – Trocar status de metas**

Abrir/Reabrir metas: processo responsável em alterar o status da meta para “Aberta” quando selecionar uma meta com o status “Em planejamento”, “Suspensa” e/ou “Finalizada”.

Validações:

- Se o processo for disparado com apenas uma meta agrupadora selecionada, deverá ser exibida uma listagem com as metas filhas existentes, onde o usuário poderá escolher mais metas que deseja que sejam alteradas neste momento.   
- Se o processo for disparado com mais de um item selecionado, as metas selecionadas deverão ser submetidas ao processo.   
- Para metas agrupadoras, será verificada se as metas que estejam definidas em sua composição totalizem 100%. Caso o total não seja 100% será incluído um alerta que não impede a troca de status.   
- Verificar se há mais de um responsável definido para uma meta. Nesse caso será incluído um alerta que impede a troca de status.   
- Verificar se, para metas do tipo Valor, que utilizam faixas de valores, verificar se há pelo menos uma faixa que define a meta como “Cumprida”. Caso não exista será incluído um alerta que não impede a troca de status.

Suspender/Replanejar metas: processo responsável em alterar o status da meta para “Suspensa” quando selecionar uma meta com o status “Aberta”.

Validações:  
- Se o processo for disparado com apenas uma meta agrupadora selecionada, deverá ser exibida uma listagem com as metas filhas existentes, onde o usuário poderá escolher mais metas que deseja que sejam alteradas neste momento.  
 - Se o processo for disparado com mais de um item selecionado, as metas selecionadas deverão ser submetidas ao processo.

Cancelar metas: processo responsável em alterar o status da meta para “Cancelada” quando selecionar uma meta com o status “Suspensa”

Validações:   
- Se o processo for disparado com apenas uma meta agrupadora selecionada, deverá ser exibida uma listagem com as metas filhas existentes, onde o usuário poderá escolher mais metas que deseja que sejam alteradas neste momento.  
- Se o processo for disparado com mais de um item selecionado, as metas selecionadas deverão ser submetidas ao processo.

Finalizar metas: processo responsável em alterar o status da meta para “Finalizada” quando selecionar uma meta com o status “Aberta”.

Validações:   
- Se o processo for disparado com apenas uma meta agrupadora selecionada, deverá ser exibida uma listagem com as metas filhas existentes, onde o usuário poderá escolher mais metas que deseja que sejam alteradas neste momento.   
- Se o processo for disparado com mais de um item selecionado, as metas selecionadas deverão ser submetidas ao processo.   
- Para metas agrupadoras, será verificada se as metas que estejam definidas em sua composição totalizem 100%. Caso o total não seja 100% será incluído um alerta que não impede a troca de status.  
 - Verificar se há mais de um responsável definido para uma meta. Nesse caso será incluído um alerta que impede a troca de status.   
- Verificar se, para metas do tipo Valor, que utilizam faixas de valores, verificar se há pelo menos uma faixa que define a meta como “Cumprida”. Caso não exista será incluído um alerta que não impede a troca de status.

# Informações Adicionais

Gerenciamento da Gestão de Metas através do Totvs Portal

Visão geral:

Filtros – Metas em que sou Avaliado   
              Metas em que sou Avaliador   
              Exibir somente controles de metas vigentes   
Botão Aplicar – ação para aplicar os filtros definidos acima;   
Meta – contém a descrição da meta;   
Período – período de início e fim da meta;   
Data do último lançamento – data que o último lançamento foi realizado;   
Valor de referência – valor de referência para cumprimento da meta;   
Situação – exibe os lançamentos já realizados na meta. Ao clicar sobre o campo é apresentado o histórico dos lançamentos já efetuados, bem como a situação dos lançamentos (Pendente, Aprovado e Reprovado). O campo será destacado na cor “verde” se a meta estiver cumprida e na cor “vermelha” se a meta não estiver cumprida.  
 Status – indica o status da meta que pode ser: Aberta, Em planejamento, Suspensa/Replanejamento, Cancelada e Finalizada;

Operações:

De acordo com o papel do usuário em relação à meta, avaliado ou avaliador, estarão disponíveis algumas opções de interação com as metas, sendo:   
- Avaliados:   
Aceitar metas: Caso a meta esteja configurada para exigir aceite dos avaliados, esta opção estará disponível para que o avaliado aceite a meta que estiver atribuída a ele;   
Solicitar aprovação lançamento: Caso a meta esteja configurada para permitir que o avaliado solicite aprovação do lançamento, ele poderá acionar essa ação, que enviara um e-mail para o avaliador. Este e-mail informará sobre o lançamento de resultado pendente de aprovação;

- Avaliador: Solicitar lançamento de acompanhamento: Ao ser acionada pelo avaliador, esta ação envia um e-mail ao avaliado solicitando que ele inclua um lançamento de resultado;  
 Pendências de aceite: Caso a meta esteja configurada para exigir aceite por parte do avaliado, esta ação possibilitará ao avaliador solicitar o aceite da meta que ainda não tiver sido aceita pelo avaliado; 

 Aprovar ou reprovar lançamentos: Caso a meta esteja configurada para necessitar de aprovação do avaliador e ainda estiver pendente, esta ação estará disponível para que o avaliador faça a aprovação ou reprovação dos lançamentos;   
- Avaliados e Avaliador:   
Lançar acompanhamento: Permite realizar o lançamento de um valor realizado na meta. Para avaliados esta opção estará disponível se a meta estiver configurada para permitir que o avaliado faça o lançamento de resultados;
