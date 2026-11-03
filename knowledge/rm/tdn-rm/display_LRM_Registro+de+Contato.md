---
content_hash: cfa842d8217bfd76dc8409e0a584a316a584e8c8c2c49417ccf863dd5e44320f
fetched_at: '2026-06-29T00:10:00.844651+00:00'
page_id: '452718595'
product: rm
source: tdn-rm
title: Registro de Contato
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+de+Contato
version: 2
---

**Registro de Contato**

O objetivo deste cadastro é armazenar os tipos de contato que podem ser realizados com um candidato participante de um processo de seleção (ex.: telefônico, e-mail e etc.). Este cadastro terá os campos Identificador, Descrição, Ativo, sendo que este último campo indica que o tipo de contato pode ser utilizado nos demais processos do sistema.

**Atenção:**

os registros de contato deverão ser armazenados para cada candidato na etapa em que o mesmo se encontra. Ao ser aprovado para uma próxima etapa, os registros criados anteriormente não deverão ser apresentados.  
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

**Filtro de registro de contatos.**

     Este filtro permite filtrar os candidatos da etapa de acordo com o tipo de contato em relação a seus registros de contato.

**Inclusão de campo na visão "Candidatos da Etapa"**

Nesta coluna será exibido o último registro de contato efetuado com o candidato da etapa. A informação presente neste campo será apresentada da seguinte maneira:

"Contato via" + Tipo de Contato + "em" + "Data/Hora" + "realizado por" + Usuário, por exemplo "Contato via e-mail em 10/11/2014 realizado por Maria Alves".
