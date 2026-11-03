---
content_hash: 7f2631f10de9d2b626dd508bc3adc06fae48e205d0e79857cd95e7986245d857
fetched_at: '2026-06-29T00:06:06.107675+00:00'
page_id: '201728420'
product: rm
source: tdn-rm
title: DT_Registro_Contato_Candidato_Etapa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Registro_Contato_Candidato_Etapa
version: 10
---

# CONTATO DO CANDIDATO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Recrutamento e Seleção* | *Registro dos contatos do candidato* | |
| **Versões/Release:** | *12.1.7* |

## Descrição

O objetivo deste cadastro é de armazenar os tipos de contato que podem ser realizados com um candidato participante de um processo de seleção (ex.: telefônico, e-mail e etc.). Este cadastro terá os campos Identificador, Descrição, Ativo, sendo que este último campo indica que o tipo de contato pode ser utilizado nos demais processos do sistema.

**Procedimento para utilização**Fazemos esse processo através do sistema RM, pelo Totvs Gestão de Pessoas. Para realizarmos tais registros devemos ir em **Planejamento e Captação / Painéis e Etapas / Anexos / Candidato da Etapa.**Para a visão de Candidatos da Etapa vamos em**Painel de Etapas / Anexos / Candidatos da Etapa / Selecionar o nome do candidato / Processos / Registro de contato**. Este anexo tem por objetivo armazenar os registros de contato, ou seja, comunicação com o(s) candidato(s) em uma determinada \*etapa da seleção.

*Os registros de contato deverão ser armazenados para cada candidato na etapa em que o mesmo se encontra. Ao ser aprovado para uma próxima etapa, os registros criados anteriormente não deverão ser apresentados.*

Envio de e-mails para os candidatos está em **Seleção / Perfil de Vaga / Etapa / Candidatos da Etapa.**Para registrar um contato realizado por através de e-mail tem o parâmetro **Registro de contato em Lote** no sistema que define qual o Tipo de Contato que será utilizado nesse processo. Esse parâmetro deverá ser preenchido com o registro de contato referente a E-mail, que será cadastrado pelo administrador do sistema. O registro de contato só será gerado neste processo se o parâmetro citado estiver preenchido com um Tipo de Contato Ativo. Caso contrário, o processo de envio de e-mail será executado normalmente mas sem registrar o contato.  
O registro de contato deverá ser preenchido com as informações do candidato, a data e hora do momento do envio e o tipo definido no parâmetro descrito acima. O campo “Contato com sucesso” será preenchido com a opção “Não aplicável”.  
Se por qualquer motivo o sistema não conseguir realizar o envio do e-mail, não deverá ser gerado um registro de contato.  
  
O filtro Tipo de Contanto é do tipo lookup e permite filtrar os candidatos da etapa de acordo com o tipo de contato em relação seus registros de contato.  
Em “Candidatos da Etapa” tem uma coluna com o nome “Último Registro de contato”, nela é exibido o último registro de contato efetuado com o candidato da etapa (vide anexo “Registro de Contato”). A informação presente neste campo será apresentada da seguinte maneira: **Contato via + Tipo de Contato + em + Data/Hora + realizado por + Usuário**, por exemplo, **Contato via e-mail em 10/11/2014 realizado por Maria Alves**.  
Crie um processo a ser chamado de “Registro de Contatos em Lote”, que será executado através do menu **Painel de Etapas / Anexos / Candidatos da Etapa / Processos / Registro de Contato em Lote**. Este assistente tem por objetivo gerar registro de contatos com candidatos de uma etapa de seleção em lote, agilizando assim a tarefa de registrar os contatos realizados (Anexo Registro de Contato).  
Para efetuar essa operação o usuário acessará a visão “Candidatos da Etapa”, em seguida criar um filtro e/ou selecionar os candidatos da etapa que deseja criar o registro de contato. Depois, deverá executar o processo “Registro de Contato em Lote”. Ao acessar tal recurso, será apresentada a tela Registro de Contato em Lote - onde haverão três campos que deverão ser preenchidos pelo usuário: Tipo de contato, Data/hora de Contato e Observações. O campos “Tipo de contato” será do tipo look up e permitirá escolher dentre os registros de contatos já cadastrados no sistema, que estejam “Ativos”. O campo “Responsável pelo contato” será automaticamente preenchido de acordo com a identificação da pessoa que está logada no sistema e executando este registro. Uma vez informados os devidos valores para os campos e executado o processo, o sistema irá criar um registro de contato para cada os candidatos selecionados na etapa.

No anexo de histórico de contatos do candidato está disponibilizado a funcionalidade para visualizar todos os tipos de contato registrados com o(s) candidato(s) em todas as etapas referentes a todos processos seletivos que eles tenham participado.
