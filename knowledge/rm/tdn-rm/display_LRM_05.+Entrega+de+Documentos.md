---
content_hash: 7bca5d9e3b8c58d34fd02e5da51b6f1ec89a0d8da741be5b8c2fabdb6e34cfd4
fetched_at: '2026-06-29T00:11:05.371682+00:00'
page_id: '630385862'
product: rm
source: tdn-rm
title: 05. Entrega de Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/05.+Entrega+de+Documentos
version: 27
---

## Entrega de Documentos

Essa funcionalidade permite o envio eletrônico de documentos, obrigatórios ou opcionais, durante o processo de matrícula, abrangendo tanto alunos do Ensino Básico quanto do Ensino Superior. Essa abordagem contribui para a modernização do processo acadêmico, promovendo agilidade, organização e centralização das informações documentais.

Para que a etapa de entrega de documentos seja exibida durante o processo de matrícula online, é necessário habilitar o parâmetro **Exibir etapa de documentos na matrícula**.

Para isso, acesse: **Parâmetros > RM Portal - Matrícula > Portal - Matrícula / Geral 4/6**.

Ao marcar o parâmetro **Exibir etapa de documentos na matrícula**, os parâmetros **Alertar alunos** e **Bloquear alunos** ficaram desabilitados, e a mensagem sobre documentos pendentes, não será mais exibida durante o processo de matricula.

Documentos do tipo Ingresso, mesmo que configurados como obrigatórios, serão exibidos na etapa de entrega de documentos **apenas na primeira matrícula do aluno**. Para que esses documentos também sejam apresentados em processos de **rematrícula**, é necessário habilitar o parâmetro **"Considerar documentos do tipo ingresso mesmo que não seja a primeira matrícula"**.

Para ativar essa configuração, acesse: **Parâmetros > Matrícula > Movimento > Considerar documentos do tipo ingresso mesmo que não seja a primeira matrícula**.

Os documentos visíveis no portal serão somente os documentos com **status diferente** de **validado**.Exceto se estiver configurado para validação por inteligência artificial que é descrita no próximo tópico abaixo.

## **Validação de documento pela Inteligência Artificial**

* Recurso está disponível a partir da versão **12.1.2506**.

Para que o documento seja validado automaticamente por inteligência artificial durante a etapa de envio de documentos na matrícula online, é necessário, além de habilitar a opção de **validação por IA** no cadastro do documento exigido, ativar também o parâmetro correspondente no sistema. Essa configuração pode ser feita acessando: **Parâmetros > RM Portal Matrícula > Portal - Matrícula / Geral 4/6**.

Caso esse parâmetro não esteja marcado, o documento enviado durante o processo de matrícula online ficará com o status **"Entregue em validação"**, aguardando validação manual em momento posterior.

Se o documento estiver marcado para validação por inteligência artificial e o parâmetro **"Validar documentos pela Inteligência Artificial na matrícula"** estiver habilitado (consulte em ), o documento enviado durante a matrícula online será automaticamente analisado pela IA e receberá um dos seguintes status, conforme o resultado da validação: **"Validado"** ou **"Recusado"**.

Por outro lado, se o documento estiver marcado para validação por IA nos *Documentos Exigidos* da parametrização por curso, mas o parâmetro de validação por IA na matrícula **não estiver habilitado**, o documento enviado durante a matrícula online permanecerá com o status **"Entregue em validação"**, aguardando validação manual em momento posterior.

Caso o documento seja de envio obrigatório e, durante o processo de validação automática pela inteligência artificial, seja classificado como inválido (recebendo o status **"Recusado"**), o sistema impedirá o prosseguimento da matrícula. Nessa situação, será necessário que o aluno envie um novo documento que, ao ser analisado pela IA, receba o status **"Validado"** para que o processo de matrícula possa continuar normalmente.

Vale ressaltar que para que o documento seja recusado de forma correta é necessário cadastrar e configurar o  tanto para validação do **tipo**e do **conteúdo**.

Caso o parâmetro **"Validar documentos pela Inteligência Artificial"** em Parâmetros | RM Portal Matrícula | Portal - Matrícula / Geral 4/6 esteja marcado, os documentos visíveis no portal serão os documentos com qualquer um dos status possíveis: Não entregue, Entregue em validação, Recusado e Validado.

Caso este parâmetro esteja desabilitado, os documentos visíveis no portal serão somente os documentos com **status diferente** de **validado**.

### Importante

Ao enviar o arquivo, caso a validação por Inteligência Artificial esteja habilitada, e a seguinte mensagem abaixo for exibida no portal do aluno, será necessário seguir obrigatoriamente os dois passos a seguir.

* Cadastrar e configurar o  seja para validação do **tipo**e do **conteúdo**.

## Informações Complementares

Para maiores informações, Acesse: .
