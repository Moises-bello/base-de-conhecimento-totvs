---
content_hash: 0dc2c8ea99f9a0d9109888a830c75b6fbf2bb9b1c1be20de5f3b49fa75e4938a
fetched_at: '2026-06-29T00:08:57.801001+00:00'
page_id: '356810967'
product: rm
source: tdn-rm
title: Sincronismo MS Project
type: documentation
url: https://tdn.totvs.com/display/LRM/Sincronismo+MS+Project
version: 3
---

---

Para realizar o sincronismo, primeiramente é necessário que seja realizada a configuração dos parâmetros de importação em Parâmetros Gerais na aba Configuracao MS Project. Para isso acesse: "Projeto | Construção & Projetos | Gerais | Configuração MS Project".

Também deve ser feita a configuração dos Parâmetros do Projeto na Integração com MS Project, e para isso, acesse: "Projeto | Construção & Projetos | Projetos (F6) | Integração | MS Project".

Após estas configurações terem sido realizadas, será possível executar o sincronismo em: "Planejamento | Integração com o MS Project | Sincronismo com o MS Project".

Serão apresentados os campos para configuração das preferências do usuário para realizar a sincronização, que são:

**Criar novo arquivo:** Esse campo deve ser marcado se for necessário criar um novo arquivo.

**Informe a localização do arquivo MS Project:** Este campo será utilizado para informar o local em que o arquivo novo será salvo caso o campo citado anteriormente esteja marcado, ou para selecionar o local em que se encontra o projeto que será sincronizado.

**Cenário:** Selecione o cenário a ser utilizado.

**Planilha:** Selecione a planilha a ser utilizada, Atividades ou Serviços.

**Prioritário (em caso de conflito priorizar):**Defina qual a preferência de sincronização, ou seja, determine se em caso de conflito prevalecerão os dados do TOTVS Obras e Projetos ou os do MS Project.

**Sincronizar Plano Fixado:** O plano fixado irá realizar o sincronismo entre os seguintes campos TOP/ MS Project:

Atenção: O plano Fixado é meramente ilustrativo, ele é atualizado através do sincronismo com o Project, atualizando os campos  Date1 para o Data Início Fixado, Date2 para o Data Fim Fixado e Duração1 para o Duração Fixada.

**Sincronizar Plano Programado:**O plano programado irá realizar o sincronismo entre os seguintes campos TOP/ MS Project:

Caso o campo "Sincronizar Plano Fixado" esteja marcado, o campo "Sincronizar Plano Programado" será automaticamente desabilitado e vice-versa.

**Sincronizar Plano Base:** O plano base irá realizar o sincronismo entre os seguintes campos TOP/ MS Project:

**Observação:** Ao sincronizar o Plano Base e o mesmo não possuir Data Inicio Base e Data Fim Base, o mesmo não será preenchido com a Data Início do Projeto.

**Sincronizar Plano Real**: O plano real irá realizar o sincronismo entre os seguintes campos TOP/ MS Project:

**Sincronizar Percentual Concluído:** O Percentual Concluído irá sincronizar os seguintes campos TOP/ MS Project:

**Sincronizar Ligações:** As ligações serão sincronizadas nos seguintes campos TOP/ MS Project:

**Sincronizar Recursos:** Os recursos serão sincronizados nos seguintes campos TOP/ MS Project:

Abaixo os campos sincronizados no MS-Project X TOP:

|  |  |  |  |
| --- | --- | --- | --- |
| **Plano** | **PERT** | **Project** | **Base de Dados** |
| Plano Programado | Data Início Programado | Início/ Start | DATAINICIOCALC |
| Data Fim Programado | Término/ Finish | DATAFIMCALC |
| Duração Programado | Duração/ Duration | DURACAOCALC |
| Data Início Cedo | Início Antecipado/ Early Start | DATAINICIOCEDO |
| Data Fim Cedo | Término Antecipado/ Early Finish | DATAFIMCEDO |
| Data Início Tarde | Início Atrasado/ Late Start | DATAINICIOTARDE |
| Data Fim Tarde | Término Atrasado/Late Finish | DATAFIMTARDE |
| Plano Base | Data Início Base | Início da Linha de Base/ Baseline Start | DATAINICIOBASE |
| Data Fim Base | Término da Linha de Base/Baseline Finish | DATAFIMBASE |
| Plano Fixado | - | Data1/Date1 | DATAINICIOPLAN |
| - | Data2/ Date2 | DATAFIMPLAN |
| - | Número1/Number1 | DURACAOPLAN |
| Plano Real | Data Início Real | Início Real/ Actual Start | DATAINICIOREAL |
| Data Fim Real | Término Real/Actual Finish | DATAFIMREAL |
| Duração Real | Duração Real/Actual Duration | DURACAOREAL |
| Percentual Concluído | Percentual Concluído | %Concluído | PERCCONCLUIDO |

Para que os dados a serem sincronizados estejam atualizados, recomenda-se fortemente que seja realizado o Cálculo do Projeto antes de se efetuar o Sincronismo.

Após realizar esse processo, tanto o projeto do TOTVS Obras e Projetos (TOP) como o do MS Project estarão sincronizados.

Somente arquivos gerados por este processo podem ser sincronizados, assim, caso o usuário realize a Exportação do arquivo através do antigo processo de "Exportar para o Project", e tente realizar o Sincronismo através do processo "Sincronismo com MS Project " o sistema não irá permitir e irá emitir uma mensagem informando "O arquivo informado foi gerado pelo processo de "Exportar para o project'. Gere um novo arquivo através deste processo."

**Observações:**

A configuração do MS Project permite trabalhar com no máximo 2 (duas) casas decimais. Esta parametrização pode sofrer impacto no momento do cálculo total do custo do Projeto, Unidades dos Recursos e Percentuais.

Os Feriados cadastrados no Calendário parametrizado no TOP, é enviado para o Project no momento do Sincronismo para o campo Exceção do Calendário Padrão do Project.
