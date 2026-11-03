---
content_hash: 2166a9ec09d9fdd659dc4daab2c99557de0ef40e4a3c7baa70c0c18d44c77316
fetched_at: '2026-06-29T00:09:33.163011+00:00'
page_id: '425458929'
product: rm
source: tdn-rm
title: Processo Seletivo / Venda Online de Cursos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458929
version: 37
---

Aviso

A partir da release 12.1.34 (previsto para 14/01/2022), não será possível a utilização do Portal do Processo Seletivo no ambiente [C](http://corpore.net/)orpore.net (Antigo). As manutenções e suportes à este portal serão disponibilizados até a release 12.1.33 e, tão somente, abril de 2022. Após esta data, serão disponibilizados, apenas, para o [novo Portal do Processo Seletivo](https://tdn.totvs.com/pages/releaseview.action?pageId=284883621), no ambiente da FrameHTML (Novo).

# Descrição

É por meio desse cadastro que será possível criar, configurar e alterar um processo seletivo ao longo da sua execução. A criação e configuração de um processo seletivo são relativamente complexas, exigindo que o usuário forneça uma grande quantidade de dados. Para informações de como cadastrar um processo seletivo  .

# Para disponibilizar um Processo Seletivo on-line

É necessário configurar o Portal do Processo seletivo. As configurações do Portal são parametrizadas em Parâmetros do Sistema | Processo seletivo |  . É também possível configurar um portal para receber inscrições de "menores de 18 anos" ou de pessoas que não são portadoras de algum documento. Para isso é necessário alterar os parâmetros da Área pública e disponibilizar "Utilizar senha no portal" e se este parâmetro for desmarcado será exigida a data de nascimento do usuário. Na forma de identificação utilizar "CPF" ou "RG" para aqueles que são portadores de documento e "Código de Usuário" e "Email" para quem não tem documento.

Lembrando que:

* Email, CPF, RG serão disponibilizados somente se na Guia Portal " Pessoas" forem parametrizados como visível e obrigatório**.**
* É necessário ter a Forma de Inscrição do tipo online com datas de inscrição definidas de acordo com o Calendário do processo seletivo.
  + As datas do processo seletivo devem estar válidas, ou seja, caso o período de inscrição, seleção ou resultados estejam expirados ou em branco, o processo seletivo não será exibido no portal de inscrições.
* Estar com Locais do processo seletivo já cadastrados e com tipos de profissionais definidos em cada local para receber alocações de profissionais e candidatos.
* Ofertar e configurar a(s) etapa(s) das as áreas, se houver, para ocorrer a seleção.

#### Informações financeiras

Para geração de taxa de inscrição e suas formas de pagamento, acesse: 

ImportanteCaso o processo seletivo utilize taxa de inscrição, utilize a geração de lançamentos com registro online de boletos e o convênio utilizado possua alguma fórmula para associação de layout de registro online, deve criado o usuário "RMProcessoSeletivo" no cadastro de Globais com permissão na coligada na qual será registrada a inscrição do candidato,. Para mais informações acesse o link:  .Inscrição

A partir da versão 12.1.2205 foi disponibilizado no cadastro da área de interesse ofertada a possibilidade de definir um período de inscrição.

Caso o período não seja preenchido será mantida a regra que considera o período de inscrição do processo seletivo.

Para saber mais sobre período de inscrição clique em: [Regras para habilitar a inscrição](https://tdn.totvs.com/pages/viewpage.action?pageId=678587180)

Nesta fase é possível executar os seguintes processos:

 

[Venda Online de Cursos (RM.exe)](https://tdn.totvs.com/x/-MGrKw)

 

 

**Tipos de Processos Seletivos**

É possível ter vários tipos de Processo Seletivo dependendo da configuração feita pelas guias de informações e anexos. Os possíveis tipos são:

* Processo seletivo terceirizado.
* Processo seletivo local.
* Processo seletivo com atividades agendadas.
* Processo seletivo controlado por vagas.
* Processo seletivo com utilizando cotas federais.

**Se Processo Seletivo terceirizado**

O Processo seletivo terceirizado é identificado pelo preenchimento do campo Instituição na aba Identificação do cadastro do Processo seletivo. Após indicar que este processo seletivo é terceirizado, as áreas ofertadas deste tipo de processo seletivo serão as Áreas de interesse Cliente, cadastradas em Tabelas auxiliares. As áreas de interesse cliente são áreas a ofertada nos processos seletivos deste tipo, mas que não fazem parte dos cursos ofertados regularmente pela Instituição de ensino local. Essa situação acontece somente para processos seletivos realizados para terceiros, pois a instituição que está gerenciando o processo seletivo, oferece áreas que não compõem a grade de cursos da mesma.

**Se Processo Seletivo local**

O processo seletivo local é caracterizado pelo não preenchimento do campo Instituição na guia identificação do cadastro do processo seletivo. Ou seja, não é terceirizado. Sendo assim, suas áreas ofertadas serão cadastradas na própria Instição, pelo módulo TOTVS Educacional, cadastro de Cursos.

**Se Processo Seletivo com atividades agendadas**

Para montar um processo seletivo com atividades agendadas, é necessário cadastrar os Tipos de atividades agendadas (no menu Tabelas Auxiliares| Tipo de atividade agendada), depois ir ao anexo Atividades agendadas (do Processo seletivo) e disponibilizar cada atividade na ordem que a Instituição julgue ser correta para ser executada pelos candidatos que se inscreverem nestes agendamentos. Para cada atividade é disponibilizado um ou mais recursos em determinado período de tempo (data) através do processo "Alocar recursos e horários para atividade".   
No momento em que um candidato se inscreve em um processo seletivo com atividades agendadas, a guia Agendamentos será disponibilizada (somente neste caso) no cadastro de inscrições do candidato para que ele escolha entre as datas e horários, a opção que melhor o atenda para executar aquela atividade do processo seletivo.

**Restrições de um Processo Seletivo com atividades agendadas**

Quando um candidato for se inscrever em um processo seletivo que utiliza controle de vagas, e o mesmo se encontrar como excedente, o sistema não irá disponibilizar os campos de atividades para preenchimento. No Portal, o serviço Inscrições/Resultado mostrará as informações da inscrição do candidato que está inscrito como excedente e qual é a posição.

**Se Processo Seletivo com controle de vagas**

Deverá parametrizar o processo seletivo para Utilizar controle de vagas. Este recurso poderá ser utilizado quando houver a necessidade de realizar um processo seletivo com controle de vagas. Quando esta opção for utilizada, o usuário deverá escolher também o tipo do controle de vagas.  Quando uma área ofertada for escolhida por um candidato na inscrição e o processo seletivo utilizar controle de vagas e se as vagas desta área estiverem esgotadas, o sistema poderá tomar duas opções de acordo com a configuração feita.  
Se a configuração for "Não permitir novas inscrições", a inscrição será interrompida e o usuário será notificado que as inscrições estão encerradas por falta de vagas.  
Se a configuração for "Permitir novas inscrições, mas os candidatos ficarão como excedentes", o usuário será notificado que não há mais vagas para a área ofertada e caso o candidato deseje continuar a inscrição e ser excedente, o sistema irá informar ao candidato o seu número como excedente. Estas informações serão gravadas em um painel na inscrição do candidato rm.exe, identificando o candidato como excedente e sua posição.   
No portal estará disponível na área privada do candidato no serviço Inscrições/Resultados.

Informações

Caso o processo seletivo possua valor de inscrição e esteja definido para "Utilizar controle de vagas" com a opção de "Permitir novas inscrições, mas os candidatos ficarão como excedentes", os candidato que se inscreverem como excedente não terão o lançamento da taxa de inscrição gerado.

O lançamento da taxa de inscrição só será gerado quando o candidato se tornar inscrito, para um candidato excedente se tornar inscrito é necessário que ocorra a liberação de vagas e a liberação de vagas na área ofertada só ocorrerá quando uma inscrição existente nesta área ofertada for cancelada (), excluída () ou o número de vagas da área ofertada () for incrementado.

Importante

À partir das versões 12.1.2402.294, 12.1.2406.264 , 12.1.2410.215 e 12.12502.132 foram implementadas algumas melhorias no processo de concorrência de vagas, buscando manter a integridade do limite de vagas, porém estas melhorias só serão aplicadas após a execução do atualizado da base de dados.

Importante: estas melhorias se aplicam a bases de dados SQL Server, o Oracle não disponibiliza atualmente os mesmos níveis de integridade de concorrência como SQL Server;

**Se Processo Seletivo utilizando cotas federais**

Deverá configurar o processo seletivo para trabalhar com cotas federais através do anexo  

# Preparar o Processo Seletivo para execução das provas

Após o período de inscrição e antes do período de seleção deverão ser executados os seguintes processos:

 

 

 

 

 

 

 

 

 

# Preparar o Processo Seletivo para Classificação dos candidatos

Após o período de  seleção e antes do período de Divulgação de resultados deverão ser executados os seguintes processos:

 

 

 

 

 

 

# Apuração de resultados do Processo Seletivo

 

 

 

 

 

 

 

# **Finalizar um Processo Seletivo**

No Portal em Inscrições | Resultados, área privada do candidato será possível visualizar informações referentes sua 1ª opção, como Opção de idioma, nº de inscrição, Pontuação, Classificação, nº de vagas da área, Situação Atual (se classificado ou desclassificado), Etapa Realizada - e caso tenha mais de uma etapa este campo será preenchido com a etapa que ocorreu a última classificação.   
Se o processo for controlado por vagas e se o candidato for excedente, será exibida nesta a página sua posição como excedente.  
Em Resultados Gerais divulgado na área publica do Portal, se o processo seletivo possuir área ofertada com mais de uma etapa, a consulta será filtrada por etapas e caso tenha ocorrido chamadas haverá edital da 1ª, 2ª... Chamada. O usuário pode optar para que a montagem da lista seja por ordem de classificação ou alfabética.

A lista de Classificação geral será exibida apenas se:

**1 -**O parâmetro "Mostrar Classificação Geral" estiver marcado

**2 -**Existirem dados de classificação geral para o processo seletivo na tabela SPSCLASSIFICACAOGERAL.

Ao acessar o link "Clique aqui para ver a Classificação geral" é apresentada ao usuário a lista com a classificação geral do processo seletivo. Nesta lista contêm as colunas: Nº de Inscrição, Candidato, Classificação geral e Pontuação geral.  O usuário pode optar para que a montagem da lista seja por ordem de classificação ou alfabética.  
   
Durante o período de divulgação de resultados poderá ocorrer os seguintes processos:

 

# Após a Divulgação

[Excluir lançamentos de inscrições anônimas não importadas](https://tdn.totvs.com/x/Uj2AGg) 

# Ensino Básico

No momento da  o candidato poderá informar quais itinerários que deseja se inscrever. Ao finalizar a inscrição este candidato será matriculado no TOTVS Educacional conforme parametrização na área de interesse ofertada. A partir das versões: **12.1.27.332, 12.1.28.239, 12.1.29.182, 12.1.31.100 e 12.1.32** o candidato além de ser matriculado no período letivo, também será matriculado em todos os itinerários que o mesmo se inscreveu, mas **não** será matriculado em nenhuma disciplina dos itinerários inscrito. O mesmo comportamento acontece quando se executa a matrícula do candidato de dentro do RM.exe no cadastro da inscrição do candidato por meio do botão **Matricular**.

# Máximo de inscrições por candidato

Importante

No cadastro do **Processo Seletivo**, aba **Informações Complementares**, o campo **"Máx. inscrições por candidato"** define o teto operacional de inscrições permitidas para um mesmo usuário no processo em questão.

* **Configuração de Limite:** Se definido como **1**, o candidato fica restrito a uma única inscrição; se configurado com valor **superior a 1**, o sistema permite que o candidato realize inscrições até atingir o número exato estipulado.

**Obs:  Na aba Parâmetros, seção Visibilidade/Obrigatoriedade dos campos, caso o CPF esteja marcado como obrigatório, o sistema aplicará uma trava de segurança que impede múltiplas inscrições para o mesmo CPF, independentemente do valor definido no limite de inscrições. Conforme a [documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=285638952#:~:text=A%20partir%20da%20vers%C3%A3o%2012.1.2506,par%C3%A2metros%20de%20visibilidade%20do%20formul%C3%A1rio.)**

Veja também

---

 

 Informações Complementares

---
