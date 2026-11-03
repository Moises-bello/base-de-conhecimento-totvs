---
content_hash: 88419717c7025f69aeefb75fa2dc193ac5be7b0e69d16d670d40ff9459298709
fetched_at: '2026-06-29T00:06:00.488824+00:00'
page_id: '196809118'
product: rm
source: tdn-rm
title: DT_Recuperação_de_dados_no_dia_D_do_Censo_do_ensino_básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=196809118
version: 17
---

# Recuperação de dados no dia "D" do Censo do ensino básico

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *TOTVS Gestão Educacional* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **EDU** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Arquivamento e recuperação dos dados do Educacenso.* | *[Recuperação de dados no dia "D" do Censo do ensino básico](http://tdn.totvs.com/pages/viewpage.action?pageId=194512773)* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | ``` “Matrícula e Avaliação” |“Matrículas” (Matrícula no período letivo) ``` | “Matrícula e Avaliação” | “Matrículas” (Matrícula no período letivo) | | ``` “Matrícula e Avaliação” | “Matrículas” (acessar o processo “Alterar situação de matrícula”) ``` | “Matrícula e Avaliação” | “Matrículas” (acessar o processo “Alterar situação de matrícula”) | | “Atividades acadêmicas” | “Assistentes” | “Arquivamento e recuperação dos dados do Educacenso” | “Atividades acadêmicas” | “Assistentes” | “Arquivamento e recuperação dos dados do Educacenso”. | |
| **Cadastros Iniciais:** | *Cadastro de matricula no período letivo*  *Preparação do arquivo para o Educacenso* |
| **Parâmetro(s):** | *Parâmetros do Educacional -> Configurações”-> “Parâmetros” -> “Secretaria” -> “Geral 5/5”*  *Parâmetros de Perfil para o Educacional -> Sistemas Globais” ->” Segurança” ->” Perfis” -> "Parâmetros educacionais"* |
| **Requisito (ISSUE):** | [PCREQ-5424](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-5424 "PCREQ-5424") |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *SMATRICPL* |
| **Versões/Release:** | *12.1.7* |

## Descrição

```
Permitir ao usuário obter uma “fotografia” dos seus dados e arquiva-los, em distintas linhas do tempo para futuro envio ao Educacenso.
```

## 

## Procedimento para Utilização

A funcionalidade de geração dos dados Educacenso sofreu uma reformulação, permitindo ao cliente obter uma “fotografia” dos seus dados em momentos distintos na linha do tempo. Evitando assim, que a volatilidade dos dados ao longo do tempo, mascare a real situação da época requerida. Sendo assim, devemos seguir alguns passos:

**1º Passo)** Foi criado o campo “data de encerramento de matrícula para efeitos do Educacenso” na matrícula do período letivo, que juntamente com o campo “data de matrícula” irão definir uma lógica de filtro por meio da data de corte informada pelo MEC.  A data de corte deverá estar compreendida entre a “data de matrícula” e a “data de encerramento de matrícula para efeitos do Educacenso”, sendo que esta última poderá ser nula. Segue a cláusula que será acrescida às consultas do banco de dados, possibilitando buscar os alunos e suas respetivas turmas, esta lógica se aplica da seguinte forma:

(:DATACORTE >= SMATRICPL.DTMATRICULA AND :DATACORTE <= SMATRICPL. DTMATRICULAENCERRA) OR (:DATACORTE >= SMATRICPL.DTMATRICULA  AND SMATRICPL. DTMATRICULAENCERRA  IS NULL)

**2º Passo)** Ambos os campos,  “data de matrícula” e “data de encerramento para efeitos do  Educacenso” poderão ser alterados por meio de permissão, configurada em “Sistemas Globais” | ” Segurança” | ” Perfis” (sistema: Educacional), para tanto deve-se editar o perfil e através do botão direito do mouse escolher o menu: “Outras informações” ->” Parâmetros educacionais”.

* Permitir alterar a data de matricula no período letivo;
* Permitir alterar a data de encerramento da matricula para efeitos do Educacenso no período letivo.

**3º Passo)** Na tela de parametrização do TOTVS Educacional é de suma importância a definição das consultas que serão usadas na extração dos dados para o Educacenso  (Consultas SQL: MEC.2016.00.00, MEC.2016.00.10, MEC.2016.20.00, MEC.2016.30.00, MEC.2016.40.00, MEC.2016.50.00, MEC.2016.51.00, MEC.2016.60.00, MEC.2016.70.00, MEC.2016.80.00). As consultas necessárias devem ser importadas da seguinte forma:

* No ato da importação, sugere-se importar para todas as coligadas.
* Atentar para a aba parâmetros, e clicar em “Fixo”, para que o código da consulta SQL fique exatamente com o mesmo nome da consulta importada.
* Após importação de todas consultas citadas acima, verificar se as mesmas estão devidamente parametrizadas em “Configurações” | “Parâmetros” | “Secretaria” - “Geral 5/5”.

**4º Passo)**Executar o processo de preparação do arquivo acessando a funcionalidade: “Atividades acadêmicas” | “Assistentes” | “Preparação do arquivo para o Educacenso”.

**5º Passo)**Acessar a funcionalidade “Atividades acadêmicas” | “Assistentes” | “Arquivamento e recuperação dos dados do Educacenso”.

**6º Passo)** Esta funcionalidade será responsável por “tirar as fotografias” dos dados do censo, gerando uma versão base. Neste processo deverá ser informada a “data de corte” definida pelo MEC e então clicar no botão “Gerar arquivo base”, responsável por gerar um arquivo XML “base” que será exibido no canto esquerdo da tela no formato de árvore (treeview). O usuário poderá gerar a versão “base” a partir dos dados da base de dados, ou de uma outra versão “base” já gerada.

**7º Passo)** Para alterar os dados de uma versão “base” basta seleciona-la e clicar no botão “Ler arquivo”, que carregará os dados e os exibirá no lado direito no formato de árvore.

**8º Passo)**Os campos “data de matrícula” e “data de encerramento da matrícula para efeitos do Educacenso” na matrícula do período letivo podem sofrer alteração mediante permissão. Desta forma podem ocorrer casos em que o usuário altere os cadastros, possibilitando que um determinado aluno passe a ter mais de uma turma nos dados referente ao registro 80. Tendo em vista este tipo de situação existe a funcionalidade “Considerar último registro de matrícula” (um botão na tela),  que permitirá somente a permanência da última matricula feita pelo sistema. Esta verificação será feita a partir do campo físico RECCREATEDON da tabela SMATRICPL.

**9º Passo)** O botão “Remover item” exclui uma ou várias linhas marcadas, nos casos em que a linha possui filhos estes também serão excluídos.

       Exemplos:

* Exclusão do registro 30, ocasiona  a exclusão dos itens dos registros 40, 50 e 51.
* Exclusão do registro 60, ocasiona a exclusão dos itens dos registros 70 e 80.

**10º Passo)** Após fazer os devidos ajustes nos dados destas tabelas, o usuário deverá salvar esta manutenção, clicando no botão “Salvar nova versão XML”. Esta ação gera um novo arquivo XML que será listado na visão em árvore, preservando sempre a versão anterior intacta.

**11º Passo)** O usuário poderá gerar várias versões de manutenção, no entanto, deverá definir qual será a versão oficial, para que o Gerador de Saídas a utilize no momento de gerar o arquivo TXT definitivo. Para definir a versão oficial basta selecionar a versão desejada e clicar no botão “XML oficial”.

**12º Passo)** Será permitido excluir todos os arquivos de Manutenção gerados, com exceção do arquivo Base, bastando selecionar a versão desejada e clicar no botão “Excluir arquivo”.

**13º Passo)** Definido o arquivo XML oficial, o usuário poderá gerar o arquivo .txt que será enviado para o MEC. Para a geração do arquivo o usuário deverá acessar o módulo “Integração” e a funcionalidade disponível no menu: “Gerador de Saídas” | “Layouts”. Nos casos em que o Layout “Educacenso” ainda não tenha sido importado, o usuário deverá fazê-lo por meio do menu anexo à própria visão de Layouts: “Processos” | “Importar Layout”.

**14º Passo)** Após importação do layout, deve-se executar a geração por meio do menu anexo à própria visão de Layouts: “Processos” | “Geração de Saídas”.

**15º Passo)** Este processo irá requerer três parâmetros, sendo eles: Código coligada, código filial e ano base.

O conteúdo destes campos será por exemplo:  1 para código coligada, 1 para código filial e 2015 para ano base. O arquivo final será gerado em uma pasta de nome “saídas” criada no mesmo diretório da aplicação, no seguinte formato de nome :

EducaCenso-AAAAMMDDhhmmss, onde, AAAA (ano), MM (mês), DD(dia), hh(hora), mm(minutos), ss(segundos).

Exemplo: EducaCenso-20150720115856
