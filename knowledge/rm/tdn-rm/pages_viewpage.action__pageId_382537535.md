---
content_hash: 0763f22cb241b34ec065711c40800d737bf1ec7f4cfb3acd5669aba13bd2284d
fetched_at: '2026-06-29T00:09:03.680303+00:00'
page_id: '382537535'
product: rm
source: tdn-rm
title: DT_Lançamento de Abono Global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382537535
version: 3
---

# LANÇAMENTO DE ABONO GLOBAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Automação de Ponto |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Lançamento Global de Abonos | Lançamento Global de Abonos | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | PONTO01-4018 |
| **Tabelas Utilizadas:** | AABONOFUNCIONARIO |
| **Versões** | 12.1.21 |

## Descrição

Com a nova gestão de abonos, o processo de Lançamento Global de Abonos foi evoluído. Atente-se para as mudanças neste processo:

**Grupo de Funcionários:**

**1 - Quebra de Seção**: Informe o código de quebra da seção a qual pertencem os funcionários que terão os abonos lançados.

**2 - Seleção de Funcionários:**Clique no botão "Seleção de Funcionários" para acessar a janela que irá exibir as opções de seleção por situação, tipo, código de recebimento ou Chapa.

**Perfil de Parâmetros:**

**3 - Perfil de Parâmetros:** Este campo permite guardar a configuração dos parâmetros habilitados do lançamento global de abonos. Ao acessar novamente este módulo, basta selecionar o perfil criado para o sistema trazer os parâmetros salvos.

**Observação:** Ao marcar o parâmetro para Usar a Nova Gestão de Abonos, será necessário recriar todos os perfis já salvos, devido a incompatibilidade entre os parâmetros da tela antiga com os parâmetros da nova tela.

**Gravar parâmetros em um novo perfil:**Podemos salvar os parâmetros do lançamento global de abonos. Para gravar um novo perfil do lançamento será necessário:

* Definir na tela os parâmetros que considerar necessário para o lançamento;
* Digitar um nome para o novo perfil;
* Salvar o perfil no ícone Incluir Perfil.

**Salvar perfil ao concluir:**Este parâmetro é utilizado para incluir um novo perfil de parâmetros após a execução do processo.

**Incluir perfil:** Este ícone deve ser utilizado para incluir um novo perfil.

**Excluir perfil:**Este ícone deve ser utilizado para excluir um perfil já cadastrado.

**Opções de Cadastro:**

**4 - Inserir:** Selecione esta opção para Incluir o abono para o(s) funcionário(s).

**5 - Substituir:** Selecione esta opção para realizar a substituição de informações para um abono já lançado.

**Observação:**

* + Ao realizar o processo de substituição de abono por intervalo será possível substituir somente o Código do abono, sendo necessário informar exatamente o intervalo utilizado na inclusão do abono;
  + Ao realizar o processo de substituição de abono por intervalo serão excluídos todos os abonos cadastrados no dia para a inclusão de abono com os novos parâmetros informados;
  + Na substituição de abono por número de horas será possível substituir o código do abono e o número de horas, sendo necessário respeitar a data do abono já lançado;
  + Na substituição de abono por número de horas, caso já tenha um abono por intervalo cadastrado para o mesmo dia, será feita a exclusão apenas do abono de número de horas para o lançamento de abono com os novos parâmetros informados.

**6 - Excluir:** Selecione esta opção para Excluir um abono já lançado.

**Observação:**

* Na exclusão de abonos por intervalo é necessário informar o intervalo de datas.O abono será excluído conforme o código definido.
* Já na exclusão por número de horas será validado apenas a data do lançamento na hora da exclusão. Caso tenha mais de um abono por número de horas cadastrado para o dia, ao informar a data para exclusão, serão excluído todos os abonos;
* Ao selecionar a opção de Excluir será desativado o campo Justificativa, pois a informação contida neste campo não será validada no processo de exclusão.

**7 - Código do Abono:** Informe neste campo o código do abono que será utilizado no lançamento.

Opção de Solicitação:

**8 - Abono por Intervalo:** Selecione esta opção para realizar o lançamento de abonos por intervalo. Para este lançamento será habilitado os campos "De" e "Ate", sendo necessário informar Data/Hora início e Data/Hora fim do intervalo a ser abonado.

**9 - Abono por Número de Horas:** Selecione esta opção para realizar o lançamento de abonos por número de horas. Neste lançamento será habilitado os campos "De", "Até" e "Número de Horas", sendo necessário informar a Data início, Data fim e Número de horas para o lançamento do abono.

Intervalo de Lançamento:

**10 - De ... Até:** Ao selecionar a Opção de Solicitação de Abono por Intervalo será necessário preencher neste campo a Data/Hora início e Data/Hora fim do lançamento. Selecionado a opção de Abono por Número de Horas, deverá informar nestes campos apenas a Data início e Data fim do lançamento.

**Observação:** Algumas validações destes campos:

* A hora fim informada não pode ser menor que a hora início;
* A data fim não pode ser menor que a data início;
* Não será permitido a inclusão de abonos com data anterior ao período Atual e Ativo;
* Poderá realizar o lançamento de abono para data posterior ao período Atual e Ativo;
* Todos os campos do Intervalo de Lançamento são obrigatórios, não sendo executado o processo caso não tenho o preenchimento de algum deles;
* Ao realizar o lançamento de abono por intervalo para mais de um dia, será cadastrado apenas um abono com o intervalo desejado.

**11 - Número de Horas:** Informe neste campo a quantidade de horas que será abonada.

**12 - Justificativa:** Informe neste campo a justificativa para o lançamento do abono. Este campo não é de preenchimento obrigatório.

**13 - Abonar até o fim da Jornada:** Selecionando este parâmetro, será considerado no cálculo do lançamento, o abono até o final da jornada do funcionário.

**Observação:** Ao marcar este parâmetro, caso seja feito o lançamento de abono com intervalo ou número de horas inferior às ocorrências de falta/atraso, será considerado no cálculo toda a jornada para ser abonada. Entretanto, no cadastro do abono não será alterado o intervalo ou número de horas informado no lançamento.

**14 - Executar:** Utilize essa opção para executar o processo de lançamento de abono global.

**15 - Cancelar:** Utilize essa opção para cancelar o processo de lançamento de abono global.
