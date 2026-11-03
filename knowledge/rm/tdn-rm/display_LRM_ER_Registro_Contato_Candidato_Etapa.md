---
content_hash: b032e3d410d1858fabf1459476a0c9b40998d480eed1f88249da0c98bea7f866
fetched_at: '2026-06-29T00:05:59.840955+00:00'
page_id: '192096542'
product: rm
source: tdn-rm
title: ER_Registro_Contato_Candidato_Etapa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Registro_Contato_Candidato_Etapa
version: 17
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU006 | **IRM1** | PCREQ-1960 |
| **Requisito1** | PCREQ-1961 | **Subtarefa1** | PDR\_RHU\_RHU006-167 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## 

## Objetivo

Criação do cadastro de tipos de contato como também o anexo de registro de contatos realizados com os candidatos participantes de uma etapa de seleção.

## 

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Recrutamento e Seleção | Alteração | Planejamento e Captação -> Painel de Etapas -> Anexos -> Candidatos da Etapa | - |
|  |  |  |  |

**Cadastro de Tipos de Contatos**

 

O objetivo deste cadastro é de armazenar os tipos de contato que podem ser realizados com um candidato participante de um processo de seleção (ex.: telefônico, e-mail e etc.). Este cadastro terá os campos Identificador, Descrição, Ativo, sendo que este último campo indica que o tipo de contato pode ser utilizado nos demais processos do sistema.

**Anexo de registro de contatos**

Criar um anexo denominado “Registros de Contato” para a visão de Candidatos da Etapa localizada através do menu**Painel de Etapas > Anexos > Candidatos da Etapa**. Este anexo tem por objetivo armazenar os registros de contato, ou seja, comunicação com o(s) candidato(s) em uma determinada \*etapa da seleção.

*\*Atenção: os registros de contato deverão ser armazenados para cada candidato na etapa em que o mesmo se encontra. Ao ser aprovado para uma próxima etapa, os registros criados anteriormente não deverão ser apresentados.*

Para a tela de edição deste novo anexo, conforme pode ser visto no **Protótipo 01 – Tela de edição: Registro de Contato** serão criados os seguintes campos:

- Código do Registro Contato: Código do registro de contato na etapa  
- \*Código Coligada: Código da coligada  
- \*Código da Seleção: Código da seleção  
- \*Código da Vaga: Código da vaga  
- \*Código da Etapa: Código da etapa  
- \*Código da Pessoa: Código da pessoa (candidato)  
- Tipo de Contato: Tipo de contato (Itens cadastrados na tabela dinâmica VTIPOCONTATO)  
- Data/Hora do contato: Data e hora do registro de contato  
- Responsável pelo contato: usuário que realizou o contato (usuário que registrar o contato no sistema, informar qual usuário de acordo com o log in do mesmo no sistema, RECCREATEDBY). Esse campo será somente para leitura e não terá seu valor alterado em nenhum momento.  
- Contato com sucesso: lista com opções para descrever a obtenção de sucesso no contato, com valores possíveis Não, Sim e Não aplicável (quanto o sucesso é desconhecido, como um e-mail enviado e que não se sabe se o destinatário recebeu o e-mail. Preenchimento opcional.  
- Observações sobre o contato: Observações gerais sobre o registro de contato.

*\*Estes campos somente devem existir internamente, ou seja, não serão exibidos na interface de edição de Registro de Contato.*

**Envio de e-mails para candidatos**

O processo de envio de e-mails para candidatos **(Seleção > Perfil de Vaga >Etapa > Candidatos da Etapa)** deverá ser ajustado para registrar um contato realizado por através de e-mail.Para isso deverá haver um parâmetro no sistema que define qual o Tipo de Contato que será utilizado nesse processo. Esse parâmetro deverá ser preenchido com o registro de contato referente a E-mail, que será cadastrado pelo administrador do sistema. O registro de contato só será gerado neste processo se o parâmetro citado estiver preenchido com um Tipo de Contato Ativo. Caso contrário o processo de envio de e-mail será executado normalmente mas sem registrar o contato.

O registro de contato deverá ser preenchido com as informações do candidato, a data e hora do momento do envio e o tipo definido no parâmetro descrito acima. O campo “Contato com sucesso” será preenchido com a opção “Não aplicável”.

Se por qualquer motivo no sistema não conseguir realizar o envio do e-mail, não deverá ser gerado um registro de contato.

**Filtro de registro de contatos**

Criar a opção de filtro “Tipo de Contato” para a visão de “Candidatos da etapa”. Este filtro será do tipo lookup e permitirá filtrar os candidatos da etapa de acordo com o tipo de contato em relação seus registros de contato.

**Inclusão de campo na visão “Candidatos da Etapa”**

Criar uma coluna informativa na visão “Candidatos da Etapa” com o nome “Último Registro de contato”. Nesta coluna será exibido o último registro de contato efetuado com o candidato da etapa (vide anexo “Registro de Contato”). A informação presente neste campo será apresentada da seguinte maneira:

“Contato via” + Tipo de Contato +” em” + Data/Hora “ + ”realizado por” + Usuário, por exemplo “Contato via e-mail em 10/11/2014 realizado por Maria Alves”.

**Assistente para Registro de Contatos em Lote**

Cria um processo a ser chamado de “Registro de Contatos em Lote”, que será executado através do menu **Painel de Etapas > Anexos > Candidatos da Etapa > Processos > Registro de Contato em Lote**. Este assistente tem por objetivo gerar registro de contatos com candidatos de uma etapa de seleção em lote, agilizando assim a tarefa de registrar os contatos realizados (Anexo Registro de Contato).

Para efetuar essa operação o usuário acessará a visão “Candidatos da Etapa”, em seguida criar um filtro e/ou selecionar os candidatos da etapa que se deseja cria o registro de contato. Em seguida deverá executar o processo “Registro de Contato em Lote”. Ao acessar tal recurso, será apresentada uma tela - Protótipo 02 – Processo: Registro de Contato em Lote - onde haverão três campos que deverão ser preenchidos pelo usuário: Tipo de contato, Data/hora de Contato e Observações. O campos “Tipo de contato” será do tipo look up e permitirá escolher dentre os registros de contatos já cadastrados no sistema, que estejam “Ativos”. O campo “Responsável pelo contato” será automaticamente preenchido de acordo com a identificação da pessoa que está logada no sistema e executando este registro. Uma vez informados os devidos valores para os campos e executado o processo, o sistema irá criar um registro de contato para cada os candidatos selecionados na etapa.

**Consulta de histórico de contatos**

Criar um anexo de histórico de contatos do candidato: deverá ser disponibilizado nessa funcionalidade a visualização de todos os tipos de contato registrados com o(s) candidato(s), em todas as etapas referentes a todos processos seletivos que eles tenham participado.

A visão desses dados deverá ser apresentado conforme a Tabela 1 - Histórico de contato a seguir.

Tabela 1 - Histórico de contato

| Processo Seletivo | Etapa | Tipo de Contato | Data/Hora do Contato | Contato com Sucesso | Responsável |
| --- | --- | --- | --- | --- | --- |
| **Operador** **TAM**  **02/2015** | 2 | E-mail | 11/02/2015 14:30 | N/A | Carlos |
| 3 | E-mail | 11/02/2015 16:30 | N/A | Carlos |
| 6 | E-mail | 12/02/2015 08:00 | N/A | Miguel |

## Protótipos de Tela

**Protótipo 01 - Tela de Edição:  Registro de Contato**

****Protótipo 02 - Processo:  Registro de Contato em Lote****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
