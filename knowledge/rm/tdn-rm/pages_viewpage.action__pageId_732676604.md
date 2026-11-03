---
content_hash: bdd7095494f2deedf95dee47e9869f05ffdcfd42a945c4ebf4a5029f96763efc
fetched_at: '2026-06-29T00:11:28.634848+00:00'
page_id: '732676604'
product: rm
source: tdn-rm
title: Venda Online de Cursos (RM.exe)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=732676604
version: 17
---

# **Descrição**

A Venda Online de Cursos é uma modalidade de processo seletivo que possui um fluxo simplificado, ou seja, o candidato é inscrito e logo pode ser matriculado no TOTVS Educacional sem passar por todo o fluxo que existe no processo seletivo (alocação, classificação e chamada).

### Mensagens de Notificações

Para configurar as mensagens de notificações existem duas possibilidades pelos caminhos:

**Processo Seletivo / Venda online de cursos → Anexos → Mensagens de notificação:** neste local, só serão carregados as mensagens abaixo:

* Enviar e-mail para o candidato com sua senha ao portal.
* Confirmação da matrícula no TOTVS Educacional.
* Enviar e-mail para o candidato com a confirmação da inscrição no portal (apenas quando o parâmetro '**Validar manualmente a entrega dos arquivos de documentos obrigatórios antes de matricular o candidato'** estiver marcado).

 **TOTVS Processo Seletivo → Cadastros → Notificações → Mensagens de notificação:**neste local serão carregadas todas as mensagens mas somente as abaixo serão utilizadas: 

* Enviar e-mail para o candidato com sua senha ao portal.
* Confirmação da matrícula no TOTVS Educacional.
* Enviar e-mail para o candidato com a confirmação da inscrição no portal (apenas quando o parâmetro '**Validar manualmente a entrega dos arquivos de documentos obrigatórios antes de matricular o candidato'** estiver marcado).
* Demais mensagens não serão utilizadas

### Requisitos

A matrícula da Venda Online de Cursos está condicionada a utilização do novo processo seletivo e marcando a opção para Venda Online que fica no cadastro inicial do processo seletivo.

Na aba de "Venda Online de Cursos" é possível definir alguns parâmetros:

* **Validar manualmente a entrega dos arquivos de documentos obrigatórios antes de matricular o candidato:** este parâmetro define que se o candidato possuir documentos obrigatórios, o usuário do sistema deverá validar a entrega destes documentos antes de prosseguir com a matrícula.
* **Copiar arquivos de documentos solicitados do candidato para o aluno ao matricular através da Venda Online de Cursos:** este parâmetro define que se o candidato possuir arquivos vinculados a documentos solicitados, estes serão copiados também para o TOTVS Educacional no momento da matrícula.

Se um processo seletivo utiliza Venda Online de Cursos, será habilitado na área de interesse ofertada uma aba com a definição dos parâmetros da matrícula, estes parâmetros são idênticos aos que existem na matrícula do Processo Seletivo RM feita pelo TOTVS Gestão Educacional, porém na Venda Online estes parâmetros são salvos na área ofertada para que o processo de matrícula seja "automático", ou seja, ao selecionar a opção de matrícula da Venda Online o candidato será matriculado exatamente no mesmo processo do TOTVS Gestão Educacional, porém o processo será executado em segundo plano sem nenhuma interferência do usuário do sistema, estes parâmetros também serão principalmente utilizados quando a matrícula for feita pelo portal do processo seletivo diretamente pelo candidato. 

Caso a **Área de interesse ofertada** não possua um **Código do Campus/Polo**, a inscrição utilizará o código definido na [Parametrização por Curso](https://tdn.totvs.com/pages/viewpage.action?pageId=425458887) da área de interesse ou na [Matriz Aplicada](https://tdn.totvs.com/display/LRM/Matriz+Aplicada) que possua o mesmo **Período Letivo** associado.

Parcelas do contrato - Portal Processo Seletivo

Se o sistema estiver configurado para **Gerar no contrato somente as parcelas do plano de pagamento com vencimento igual ou superior à data de inclusão do plano de pagamento no contrato**, o candidato poderá ser **impedido de prosseguir com a inscrição no portal do processo seletivo**.

* **Onde é a Configuração?** A regra é definida no caminho: **Parâmetros Educacional** → **Tesouraria** → **Geral 2/4**.
* **O Que Causa o Impedimento?** Se o contrato do processo seletivo incluir **parcelas vencidas em meses anteriores ao mês atual**, ele não atenderá ao requisito do sistema.
* **Consequência:** O candidato **não conseguirá avançar** para as próximas etapas do processo de inscrição no Portal. O sistema o impedirá de prosseguir até que o requisito da data de vencimento seja atendido pela instituição.

**Sobre a Flexibilização do Plano de Pagamento [Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=728646916) (disponível a partir da versão 12.1.2302).**

Se o parâmetro "Exige contrato financeiro" estiver habilitado, na situação de matrícula | Status no período letivo o sistema irá gerar o contrato, mesmo que o parâmetro "Cadastrar contrato" do Venda online de cursos | Financeiro estiver desabilitado.

Importante

Quando for utilizado a opção de "Gerar lançamentos" é recomendado que exista um usuário de código “***RMProcessoSeletivo***” cadastrado.

Este usuários e faz necessário para situações em que possa existir 100% de desconto em uma determinada parcela do plano do plano de pagamento definido.

Esse cadastro pode ser realizado através do menu “***Serviços Globais | Segurança | Usuários***”.

Informações

Para que os dados de deficiência do candidato sejam replicados ao Aluno matriculado, deve-se marcar o parâmetro "Sobrescrever as informações de deficiência do aluno", disponível na aba "Venda online de cursos | Acadêmico".

Para processos seletivos do nível de ensino básico, alguns campos não serão exibidos pois não são necessários: "Situação de matrícula no curso" e "Situação de matrícula nas disciplinas".

## Matrícula do candidato (RM.exe)

Ao efetuar uma inscrição do candidato em um processo seletivo de Venda Online de Cursos, será habilitado o botão Matricular (é necessário também marcar o parâmetro "**Validar manualmente a entrega dos arquivos de documentos obrigatórios antes de matricular o candidato"**)**.** Ao clicar neste botão o sistema irá validar se o candidato possui algum documento obrigatório pendente (se for definido no processo seletivo e na área ofertada).

Se o candidato não possuir nenhuma pendência de documento ou o processo seletivo não tiver validação de obrigatoriedade de documentos, o sistema irá montar todo o ambiente da matrícula e irá efetuar o processo em segundo plano, caso o candidato tenha pendências de documentos, estas devem ser validadas para a matrícula ser feita.

Informações

Caso o candidato tenha feito a inscrição pelo portal e o processo seletivo de venda online de cursos utilize documentos obrigatório, o mesmo não conseguirá confirmar sua matrícula no portal pois irá constar a pendência de documentos, a inscrição ficará pendente e neste caso o operador do sistema irá fazer a validação dos documentos e este operador que deverá realizar a matrícula através do botão matricular na inscrição do candidato no RM.exe. Nesta situação após a aprovação dos documentos não é liberado nenhuma opção de matricular no portal, somente pelo RM.exe.

Assim que o processo é concluído o candidato já possui uma matrícula no TOTVS Gestão Educacional e sua situação na opção da área de interesse escolhida será de compareceu à chamada, exatamente o status definido quando o processo de matrícula é feito através do TOTVS Gestão Educacional.

Integração de campos complementares

Através do parâmetro "***[Copiar campos complementares do candidato para o registro de aluno e de responsável financeiro](https://tdn.totvs.com/x/-ORqIQ)***" é possível copiar as informações de um campo complementar do candidato para o cadastro de aluno.

Importante

Não é possível realizar matricula em Intinerários Formativos através de processos seletivos do tipo Vendas OnLine.

**Processos**:

* Copiar processo seletivo:

O processo foi atualizado com a inclusão dos novos campos destinados à utilização do recurso de ofertas online. Com isso, foram inclusos os parâmetros do cadastro do processo seletivo e os parâmetros no cadastro das áreas ofertadas.

Endereço: Cadastros | Processo Seletivo / Venda Online de Cursos | Processos: Copiar processo seletivo

## Área ofertada

Na visão de área ofertada é possível executar um processo para a cópia do parâmetros de matrícula de uma área ofertada para outras selecionadas durante o processo.

O processo permite a seleção de uma ou mais áreas ofertadas, do mesmo processo seletivo, para que recebam os mesmos valores configuradas em uma área de origem.

Após a execução do processo, todas as áreas ofertadas selecionadas terão a mesma configuração da área ofertada de origem, recebendo os valores dos parâmetros contidos na aba "Venda Online de Cursos".

**OBS**: os dados de "período letivo", "campus" e "plano de pagamento" serão copiados somente se as áreas ofertadas com suas respectivas matrizes aplicadas de destino tiverem os dados de  "período letivo", "campus" e "plano de pagamento" em suas parametrizações no TOTVS Educacional iguais a da área ofertada de origem.

Parâmetros das abas

* + Acadêmico
  + Financeiro
  + Perfil do Usuário

***Caminho do processo:***

* Cadastros | Área de interesse ofertada | Processos: Copiar parâmetros de matrícula
* Cadastros | Processo Seletivo / Venda Online de Cursos | Anexos: Área de interesse ofertada | Processos: Copiar parâmetros de matrícula

## Controle de Vagas

Quando o processo seletivo utilizar controle de vagas  que permite candidatos excedentes (para mais informação [clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=425458929)), um candidato excedente só se alterado para inscrito se uma inscrição for cancelada ou excluída, ou se for executado o processo de desmatricular alunos do processo seletivo RM através do TOTVS Educacional.

Ao executar este processo marcando o parâmetro na tela para atualizar a lista de excedentes, o sistema irá alterar candidatos excedentes para inscritos de acordo com o número de vagas liberadas, ou seja, de acordo com a quantidade de alunos que tiveram a matrícula desfeita neste processo. Marcando também o parâmetro para matricular candidatos após a alteração dos excedentes, o sistema além de tornar os candidatos excedentes como inscritos, já faz também a matrícula no período letivo conforme definido nos parâmetros da Venda Online da área ofertada.

**Obs**: estes parâmetros só serão exibidos na tela se o processo seletivo utilizar controle de vagas e for da modalidade de Venda Online de Cursos.

## Desmatricular alunos matriculados via Processo Seletivo RM

Ao desmatricular alunos que foram matriculados via processo seletivo é possível filtrar apenas alunos com pendência financeira, como o não pagamento do boleto da matrícula.

## Matrícula na modalidade de venda online de cursos através de uma chamada via WebService (ProcessServer)

Para matricular um candidato através do processo seletivo na modalidade de "Venda online de cursos"  utilizando o webservices, é necessário que primeiro seja feito a inscrição através do DataServer de inscrição, logo em seguida é necessário efetuar a matrícula através do ProcessServer de matrícula de candidatos do processo seletivo. ([Processo Seletivo RM - Matricular](https://tdn.totvs.com/display/LRM/Processo+Seletivo+RM+-+Matricular)), este ProcessServer é utilizado em todas as matrículas originadas do processo seletivo, sendo que para ser utilizado na modalidade de "Venda online de cursos" é necessário alterar uma determinada tag no XML do processo. 

Todas estas as especificações definições podem ser consultadas através do link [Processo Seletivo RM - Matricular](https://tdn.totvs.com/display/LRM/Processo+Seletivo+RM+-+Matricular)
