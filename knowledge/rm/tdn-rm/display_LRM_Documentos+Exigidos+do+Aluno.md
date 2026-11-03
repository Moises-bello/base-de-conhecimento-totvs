---
content_hash: 34bacb2a09b3b40dbc1d8cb418c847513146eb322f4519e80547bf2b3356df8b
fetched_at: '2026-06-29T00:09:33.363446+00:00'
page_id: '425458994'
product: rm
source: tdn-rm
title: Documentos Exigidos do Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/Documentos+Exigidos+do+Aluno
version: 32
---

# Descrição

Esta funcionalidade permite que os usuários da secretaria definam os documentos **obrigatórios para o ingresso de alunos na instituição**, de acordo com o período letivo e a matriz curricular aplicada.

Para cada parametrização por curso, dentro de um período letivo, é possível especificar quais documentos serão exigidos e se serão obrigatórios ou não.

Tela depreciada

Esta tela com o seguinte conjunto de informações está disponível somente até a versão **12.1.2502.**

## Tipo de documento

**Ingresso**: Os documentos do tipo Ingresso são, por padrão, verificados apenas na primeira matrícula do aluno no sistema.

Caso o usuário deseje que esses documentos sejam exigidos em todas as matrículas realizadas no período letivo, o sistema disponibiliza o parâmetro **“Exigir documentos não entregues pelo aluno, do tipo ingresso, mesmo que não seja a primeira matrícula”**, localizado em: *Configurações > Parâmetros > Matrícula > Movimento 2*.  
Quando ativado, esse parâmetro torna obrigatória a apresentação dos documentos em todas as matrículas.

**Por Período Letivo**: Os documentos definidos por período letivo são verificados sempre que o aluno realiza uma matrícula ou rematrícula.

## Exigido por sexo

É possível definir se um documento será exigido para o sexo **Masculino**, **Feminino** ou **Todos**. Por padrão, a opção selecionada é **Todos**.

Para alunos cadastrados com o sexo **Masculino**, serão solicitados apenas os documentos marcados como **Masculino** ou **Todos**. Documentos definidos como **Feminino** não serão exibidos. Esse comportamento também se aplica à matrícula realizada pelo portal.

Caso o sexo do aluno **não esteja definido** no cadastro, o sistema exigirá **somente os documentos marcados com a opção Todos**.

# Parametrização de Envio de documentos.

O sistema permite bloquear a matrícula na ausência de documentos exigidos. Para configurar esse bloqueio, acesse **Configurações > Parâmetros > Matrícula > Movimento 1/4** e ative o parâmetro **"Bloquear matrícula na falta de documentos exigidos"**. Com esse parâmetro habilitado, o sistema impedirá a matrícula do aluno até que todos os documentos obrigatórios sejam apresentados.

O processo de alteração da situação de matrícula também pode ser impactado pela ausência de documentos obrigatórios. Nas configurações de situação de matrícula por período letivo, ao marcar o parâmetro **"Bloquear alteração para este status por falta de doc. obrigatórios"**, o sistema realizará a verificação no momento da alteração e impedirá a mudança de status caso haja pendência de documentos obrigatórios.

É possível conceder permissão para que um usuário consiga efetivar a matrícula mesmo sem a apresentação dos documentos exigidos. Para isso, acesse **Serviços Globais > Perfil do Usuário > Anexo Parâmetros Educacionais** e configure a exceção conforme necessário.

Para mais informações sobre a configuração de parâmetros do sistema acesse:  .

# Validar documento pela inteligência artificial

Este recurso está disponível a partir da versão **12.1.2506**.

No cadastro de documentos obrigatórios no aluno, ao marcar o campo **"Validar documento pela inteligência artificial"**, a seguinte mensagem será exibida.

Os documentos com este campo marcado serão validados automaticamente por inteligência artificial no momento do envio, tanto durante a etapa de **envio de documentos na matrícula online** (quando disponível), quanto na aba **Documentos** do cadastro acadêmico no **portal do aluno**.

Após a validação pela IA, os documentos receberão o status **"Validado"** ou **"Recusado"**, conforme o resultado da análise.

**Obs**. Para os documentos com status **Recusado**, mediante parametrização, será enviado automaticamente um e-mail, por meio da [Central de Notificações](https://tdn.totvs.com/pages/viewpage.action?pageId=425458864)e do [eduCONNET](https://tdn.totvs.com/display/LRM/03.5+-+Cadastro+de+Mensagens), para o Aluno/Responsáveis informando quais documentos foram recusados e o motivo da recusa. Funcionalidade disponível a partir da versão 12.1.2506.128.
