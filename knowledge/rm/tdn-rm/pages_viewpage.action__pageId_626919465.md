---
content_hash: a421882422b1b3bfa34f538bd20218e9c84f82ee5e181be4b04608744871ee5a
fetched_at: '2026-06-29T00:11:04.373930+00:00'
page_id: '626919465'
product: rm
source: tdn-rm
title: Rascunho_Projeto de Inovação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626919465
version: 1
---

O projeto de Inovação,  tem como objetivo gerenciar os processos (solicitação, aprovação e registro) referente aos dados de atividades de inovações tecnológicas, onde resulta no registro de patente através do *Workflow* do Totvs Fluig.

O Projeto de inovação poderá ser classificado em seis tipos de invento:

* Desenho Industrial
* Cultivar/Biológico
* Obra Literária
* Patente
* Programa de Computador
* Marca

Para o Módulo de Projeto de inovação, será necessário efetuar alguns cadastros no qual os mesmos são utilizados durante o processo de Solicitação, sendo: 

* Fonte de Fomento: Cadastro de Empresa no Totvs Gestão Educacional, será necessário associar a categoria: Agência de Fomento.

```
  Este cadastro é utilizado no cadastro inicial \[Registrar Processo\] da solicitação do Inventor.
```

Cadastro: Totvs Gestão Educacional | Atividades Acadêmicas | Acadêmico | Empresas

* Instituição: O cadastro da Instituição também é cadastrado no Totvs Educacional, onde é necessário cadastrar a categoria como: Universidade

```
   Este cadastro é utilizado no cadastro inicial \[Registrar Processo\] da solicitação do Inventor.
```

Cadastro: Totvs Gestão Educacional | Atividades Acadêmicas | Acadêmico | Empresas

* Motivo de Arquivamento: Este cadastro será utilizado na etapa: Avaliar Documentação (Gestor) no momento em que o Gestor do processo deseja arquivar a solicitação criada pelo inventor, ou caso a Solicitação seja Reprovada.

Cadastro: Totvs Gestão Educacional | Atividades Acadêmicas | Acadêmico | Pesquisa/Extensão | Motivo de Arquivamento

Classificação do Tipo de Programa: Esta classificação é utilizada na etapa \[Registrar processo\] quando o tipo de invento for:

* Desenho Industrial
* Cultivar/Biológico
* Obra Literária
* Patente

Cadastro: Totvs Serviços Globais | Cadastros | Tabelas Dinâmicas | Cód: PESQEXT020 – Classificação do Tipo de Programas  
Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.

* Código = gestor\_processo| Descrição = Gestor de Processo
* Código = inovação | Descrição = Inovação
* Código = contrato | Descrição = Contrato
* Código = contrato\_inovação | Descrição = Contrato Inovação

Em seguida, associar os usuários aos respectivos papéis cadastrados.  
  
**Descrição do Processo:**  
Logar com o usuário associado ao papel de: "Inventor" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Projeto de Inovação | Projeto de Inovação".

Ao selecionar essa opção, será aberto um formulário com o código do usuário logado e a data corrente. Nele deverão ser informados os dados do invento que podem ser classificamos como:

* Desenho Industrial;
* Cultivar Biológico;
* Obra Literária;
* Patente;
* Software;
* Programa de Computador.

E os dados dos inventores da tecnologia, no qual podem ser classificamos como:

* Aluno;
* Professor;
* Externo;
* Adicionar uma nova pessoa.

Após registrar o processo o fluxo avançará para a atividade "Avaliar Invento", onde um usuário vinculado ao papel "Inovação" terá duas opções:

* Avançar para a atividade "Invento Aprovado".
* Avançar para a atividade "Invento Reprovado", onde o invento será reprovado e o fluxo finalizado.

Na etapa "Invento Aprovado" será verificado o valor do campo "Inventor independente", existente no formulário de cadastro. Se ele estiver desmarcado o fluxo avançará para a atividade "Assinar Declaração de Inventores e/ou Contrato", porém, se o campo estiver marcado o fluxo será encaminhado para a atividade "Elaborar Contrato", onde um usuário vinculado ao papel "Contrato" irá elaborar o contrato para inventores independentes. Esse processo pode ocorrer quantas vezes forem necessárias, até que o contrato esteja de acordo com o solicitado.

Após a criação do contrato ele será anexado ao processo e o fluxo avançará para a atividade "Avaliar Contrato", onde um usuário vinculado ao papel "Inovação" irá verificar se o contrato está condizente para assinatura do inventor. Esse processo pode ocorrer quantas vezes forem necessárias, até que o contrato esteja de acordo com o solicitado. Passando por essa avaliação o fluxo será encaminhado para a atividade "Assinar Declaração de Inventores e/ou Contrato", que será assumida pelo inventor que iniciou o processo. Se ele for um inventor independente o contrato e a declaração de inventores deverão ser assinados, porém se o inventor não for independente será necessário assinar apenas a declaração de inventores. Assim que a declaração de inventores for assinada o fluxo avançará para a atividade "Avaliar Documentação (Inovação)", onde o usuário vinculado ao papel "Inovação" irá avaliar a documentação e definirá se ela está pertinente.

Ele terá três opções:

* Avançar para a atividade "Avaliar Documentação (Gestor)".
* Avançar para a atividade "Solicitar Pedido de Reconsideração", caso a documentação seja reprovada.
* Avançar para a atividade "Solicitar Documentação para Depósito".

Na etapa "Avaliar Documentação (Gestor)" um usuário vinculado ao papel "Gestor de processo" irá avaliar toda a documentação e definirá se ela está pertinente. Caso ela seja aprovada, o fluxo será encaminhado para a atividade "Solicitar Documentação Para Depósito", caso contrário o fluxo avançará para a atividade "Solicitar Pedido de Reconsideração". Na etapa "Solicitar Pedido de Reconsideração" o inventor que iniciou o processo irá avaliar as considerações pela reprovação da documentação e realizará os ajustes necessários para solicitar nova avaliação. Após avaliar a documentação na etapa "Avaliar Pedido de Reconsideração", o usuário vinculado ao papel "Gestor de processo" terá três opções:

* Retornar para a atividade "Solicitar Pedido de Reconsideração".
* Avançar para a atividade "Processo Arquivado", onde o processo será arquivado e o fluxo finalizado.
* Avançar para a atividade "Solicitar Documentação para Depósito".

Na etapa "Solicitar Documentação para Depósito" o usuário, vinculado ao papel "Inovação", indicará ao solicitante a documentação necessária para realizar o depósito. Assim que documentação for indicada, o fluxo será encaminhado para a atividade "Providenciar Documentação Para Depósito". Nessa etapa o inventor que iniciou o processo deverá providenciar toda documentação para realizar o depósito do invento. Esse processo pode ocorrer quantas vezes forem necessárias, até que a documentação esteja de acordo com o solicitado.   
Após providenciar a documentação o fluxo avançará para a atividade "Analisar Documentação", onde o usuário vinculado ao papel "Inovação" deverá verificar a documentação entregue. Assim que a análise chegar ao fim, o usuário terá duas opções:

* Retornar para a atividade "Providenciar documentação para depósito".
* Avançar para a atividade "Reunião Para Elaboração do Relatório".

Na etapa "Reunião Para Elaboração do Relatório" o inventor que iniciou o processo deverá convocar uma reunião com os interessados. Após a elaboração do relatório o fluxo deverá seguir para a atividade "Registrar/Manter INPI". Nessa etapa o usuário vinculado ao papel "Inovação" deverá preencher os dados referentes aos protocolos do INPI. Assim que esses protocolos forem preenchidos, o usuário terá duas opções:

* Avançar para a atividade "Agendar Vencimentos".
* Finalizar o fluxo.

Na etapa "Agendar Vencimentos" o usuário vinculado ao papel "Inovação" poderá finalizar o processo ou criar dados de alerta (Atividades Ad-Hoc), assim serão geradas novas tarefas para o responsável ficar ciente dos compromissos futuros para as patentes. Assim que todos os responsáveis concluírem suas tarefas o fluxo poderá ser finalizado.  
  
Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
   
  
   
 

 Informações Complementares

---

[Como Cadastrar uma Atividade Ad-hoc](http://tdn.totvs.com/pages/releaseview.action?pageId=142813148)

Veja Também

---

[Documento Técnico - Projeto de Inovação 'Solicitação'](http://tdn.totvs.com/display/LRM/DT_PROJETO_INOVACAO)
