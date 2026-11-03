---
content_hash: af19949d2f10c65460b8650d45c2a5298d9cb2fb34c300f21ba3a363ee2a0fe0
fetched_at: '2026-06-29T00:10:07.259626+00:00'
page_id: '452719386'
product: rm
source: tdn-rm
title: Registro de Contato Candidato da Etapa
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+de+Contato+Candidato+da+Etapa
version: 3
---

**Registro de Contato Candidato da Etapa**

O objetivo deste cadastro é armazenar os tipos de contato que podem ser realizados com um candidato participante de um processo de seleção (ex.: telefônico, e-mail e etc.). Este cadastro terá os campos Identificador, Descrição, Ativo, sendo que este último campo indica que o tipo de contato pode ser utilizado nos demais processos do sistema.

**Anexo de registro de contatos.** **Painel de Etapas | Anexos | Candidatos da Etapa | Anexos | Registro de Contato.**

Este anexo armazena os registros de contato, ou seja, comunicação com o(s) candidato(s) em uma determinada etapa da seleção

**Atenção**:

\* os registros de contato deverão ser armazenados para cada candidato na etapa em que o mesmo se encontra. Ao ser aprovado para uma próxima etapa, os registros criados anteriormente não deverão ser apresentados.

Para a tela de edição deste novo anexo, foram criados os seguintes campos:

- **Código do Registro Contato:** Código do registro de contato na etapa

- **Código Coligada:** Código da coligada

- **Código da Seleção:** Código da seleção

- **Código da Vaga:** Código da vaga

- **Código da Etapa:** Código da etapa

- **Código da Pessoa:** Código da pessoa (candidato)

- **Tipo de Contato:** Tipo de contato (Itens cadastrados na tabela dinâmica VTIPOCONTATO)

- **Data/Hora do contato:** Data e hora do registro de contato

- **Responsável pelo contato:** usuário que realizou o contato (irá informar qual usuário de acordo com o login do mesmo no sistema, (RECCREATEDBY). Esse campo é somente para leitura e seu valor não pode ser alterado.

- **Contato com sucesso:** lista com opções para descrever a obtenção de sucesso no contato, com valores possíveis Não, Sim e Não aplicável (quanto o sucesso é desconhecido, como um e-mail enviado e que não se sabe se o destinatário recebeu o e-mail. Preenchimento opcional.

- **Observações sobre o contato:** Observações gerais sobre o registro de contato.

**Envio de e-mails para candidatos.** **Painel de Etapas | Anexos | Candidatos da Etapa | Processos | Enviar e-mail para o(s) Candidatos(s).**

O processo de envio de e-mails para candidatos irá registrar um contato realizado por e-mail. Para isso, existe um parâmetro no sistema que define qual o Tipo de Contato que será utilizado nesse processo. Esse parâmetro irá preencher com o registro de contato referente a E-mail, que será cadastrado pelo administrador do sistema. O registro de contato só será gerado neste processo se o parâmetro citado estiver preenchido com um Tipo de Contato Ativo. Caso contrário, o processo de envio de e-mail será executado normalmente mas sem registrar o contato.

O registro de contato irá preencher com as informações do candidato, a data e hora do momento do envio e o tipo definido no parâmetro descrito acima. O campo "Contato com sucesso" será preenchido com a opção "Não aplicável".

Se por qualquer motivo no sistema não conseguir realizar o envio do e-mail, o registro de contato não será gerado.

**Filtro de registro de contatos.**

Este filtro permite filtrar os candidatos da etapa de acordo com o tipo de contato em relação a seus registros de contato.

**Inclusão de campo na visão "Candidatos da Etapa"**

Nesta coluna será exibido o último registro de contato efetuado com o candidato da etapa. A informação presente neste campo será apresentada da seguinte maneira:  
"Contato via" + Tipo de Contato + "em" + "Data/Hora" + "realizado por" + Usuário, por exemplo "Contato via e-mail em 10/11/2014 realizado por Maria Alves".

**Assistente para Registro de Contatos em Lote:****Painel de Etapas | Anexos | Candidatos da Etapa | Processos | Registro de Contato em Lote**.

Este assistente tem por objetivo gerar o registro de contatos com candidatos de uma etapa de seleção em lote, agilizando assim a tarefa de registrar os contatos realizados (Anexo Registro de Contato).  
Para efetuar essa operação o usuário deve acessa a visão "Candidatos da Etapa", em seguida crie um filtro e/ou selecionar os candidatos da etapa que se deseja criar o registro de contato. Em seguida deverá executar o processo "Registro de Contato em Lote".

Os campos que deverão ser preenchidos pelo usuário são: Tipo de contato, Data/hora de Contato e Observações. O campo "Tipo de contato" permite escolher dentre os registros de contatos já cadastrados no sistema, que estejam "Ativos".

O campo "Responsável pelo contato" será automaticamente preenchido com a identificação do usuário que está executando este registro. Uma vez informados os devidos valores para os campos e executado o processo, o sistema irá criar um registro de contato para cada os candidatos selecionados na etapa.  
   
**Consulta de histórico de contatos**  
      No anexo de histórico de contatos do candidato é possível a visualização de todos os tipos de contato registrados com o(s) candidato(s), em todas as etapas referentes a todos processos seletivos que eles tenham participado.
