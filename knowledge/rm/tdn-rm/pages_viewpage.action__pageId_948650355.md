---
content_hash: 5f8f20430817014da40cbabc8456b0621030649152f1cd8978761fa993377eb9
fetched_at: '2026-06-29T00:12:09.682023+00:00'
page_id: '948650355'
product: rm
source: tdn-rm
title: 04 - Aprovação e Reprovação de mensagens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=948650355
version: 13
---

# Sumário

---

Sumário

# Aprovação

---

A Gestão de Mensagens tem como objetivo permitir que os usuários e os responsáveis por aprovações acompanhem e visualizem as mensagens processadas. Além disso, essa funcionalidade oferece recursos adicionais, como visualização dos detalhes da mensagem, edição, aprovação, reprovação, uso como modelo, exclusão, entre outros.

A **Central de Comunicação** disponibiliza o recurso de **envio de mensagens mediante aprovação**, permitindo que o processo de comunicação institucional seja mais seguro, padronizado e aderente às diretrizes da organização.

Isso significa que um usuário pode **criar e submeter uma mensagem**, porém essa mensagem **somente será enviada após a aprovação de um responsável**, previamente definido na  **[Regra de Comunicação](https://tdn.totvs.com/pages/viewpage.action?pageId=898441783)** associada ao tipo de mensagem e usuário (autor da mensagem).

**Quando o recurso de aprovação é aplicado?**

* Sempre que a **[Regra de Comunicação](https://tdn.totvs.com/pages/viewpage.action?pageId=898441783)** vinculada ao usuário (autor) estiver configurado para requerer aprovação
* O sistema identifica automaticamente, no momento do envio, se aquela mensagem exige ou não aprovação.

**Fluxo do processo de aprovação:**

1. O **autor da mensagem** cria e submete a mensagem.
2. A mensagem fica com o status **“Pendente de aprovação”**.
3. Os **usuários aprovadores**, configurados na regra de comunicação, recebem a notificação de que há uma mensagem aguardando análise.
4. O aprovador acessa a [gestão de mensagens](https://tdn.totvs.com/pages/viewpage.action?pageId=944706219) e utiliza a opção **“Aprovar ou visualizar”** para revisar os detalhes da mensagem.

   Demonstração

   Uma boa prática para usuários aprovadores é utilizar os filtros para localizar rapidamente mensagens que estão pendentes de aprovação, seja de um autor específico ou de todas as mensagens pendentes.

   Além disso, é possível realizar diversas combinações dos filtros para refinar ainda mais a busca.
5. Na tela de visualização da mensagem na etapa final, o aprovador pode:

✅ **Aprovar:** a mensagem segue para envio (imediato ou conforme agendamento configurado).

❌ **Reprovar:** a mensagem não será enviada e passará ao status **“Reprovado”**, sendo obrigatório informar uma **justificativa de reprovação**.

💡 **Exemplo prático:**

Imagine que um colaborador da secretaria acadêmica precise comunicar aos alunos sobre a renovação de matrícula. Ele elabora uma mensagem e, ao enviar, o sistema verifica que este tipo de comunicação exige aprovação do coordenador do curso.

* A mensagem então fica com status **“Pendente de aprovação”**.
* O coordenador acessa o Portal Gestão Educacional entra na  [gestão de mensagens](https://tdn.totvs.com/pages/viewpage.action?pageId=944706219), localiza a mensagem e aciona a opção **“Aprovar ou Visualizar”** , revisa o texto, verifica se os filtros estão corretos (como público-alvo, filiais, cursos) e então aprova a mensagem.
* Caso o coordenador identifique que há um erro, como uma data incorreta ou informação equivocada, ele pode reprovar a mensagem e inserir uma justificativa, por exemplo:

> **“Mensagem reprovada devido a erro na data de início da renovação. Favor corrigir e reenviar.”**

* Todo o fluxo de aprovação respeita as **Regras de Comunicação**, que definem quem são os aprovadores, os tipos de mensagens que exigem aprovação e as condições específicas.
* Se a mensagem não exige aprovação, ela seguirá diretamente para o envio ou para o agendamento, conforme indicado pelo autor.

# Reprovação

---

Durante o processo de análise e aprovação de mensagens, é permitido ao usuário reprovar qualquer mensagem que esteja com o status **“Pendente de Aprovação”**. Ao ser reprovada, a mensagem **não será enviada** e passará a ter o status **“Reprovado”**.

Ao selecionar a opção **“Aprovar ou Visualizar”**, será exibida a mensagem para que o aprovador possa realizar a devida conferência. Na etapa final desse fluxo, estará disponível a ação **“Reprovar”**.

Ao clicar em **“Reprovar”**, será apresentada uma tela (conforme a imagem abaixo), onde o usuário deverá obrigatoriamente informar uma **justificativa para a reprovação** e, em seguida, confirmar a ação clicando no botão **“Reprovar”**.

Informações Importantes:

* Mensagens reprovadas **não poderão ser reenviadas para aprovação**.
* Caso deseje reaproveitar o conteúdo, o usuário pode utilizar a funcionalidade **“Usar como modelo”**, realizar os ajustes necessários e então enviar uma nova mensagem para aprovação.
Consulta da Justificativa de Reprovação

A justificativa informada no momento da reprovação ficará registrada. Para consultá-la, acesse a tela de **Gestão de Mensagens** e utilize a ação **“Justificativa da Reprovação”** disponível no menu de opções da mensagem.

Ao acessar a opção "Justificativa da Reprovação" será apresentada a tela conforme a imagem abaixo.

# Notificação de Envio

Sempre que ocorrer uma ação de **solicitação de aprovação**, **aprovação**, **reprovação** ou **conclusão de processamento** na Central de Comunicação, será gerada uma **notificação interna** com o objetivo de **enviar um e-mail ao usuário do sistema**.Para saber mais sobre a notificação de envio [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=965444172).
