---
content_hash: d3296c1eefd813bd5505017bc5dea5e25d3b89708a9eb4f7360e2ce4d60a74d8
fetched_at: '2026-06-28T21:35:30.819710+00:00'
page_id: '860252124'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Scripts do processo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=860252124
version: 43
---

Nota:

Esta documentação refere-se ao Editor de processo atual da plataforma.

75%

5.\*ndice

25%

trueIdioma

# Falando de *scripts* do processo...

---

Os *scripts* podem ser associados aos eventos do processo para personalizar o que deve acontecer quando determinado evento ocorrer. Eles são chamados ao longo da execução do processo, em momentos predeterminados pelos eventos, tais como a criação de uma solicitação ou a chegada de uma solicitação em uma determinada etapa do processo.

Ao utilizar *scripts* nos processos, é possível manipular valores do formulário relacionado a eles, fazer a comunicação com serviços externos, enviar *e-mails* para pessoas externas, manipular anexos da solicitação e fazer publicação no recurso , consultar *datasets*, adicionar validações na movimentação da solicitação, integrar com outras solicitações ou outros pontos da plataforma, gerar *logs* etc.

Neste recurso também são exibidos os *scripts* de atividades de serviço, ou seja, que foram criados a partir da configuração de uma atividade de serviço que existe no diagrama do processo.

Para diferenciar os *scripts*, eles possuem um identificador logo abaixo do seu nome:

* **Edição por desenvolvimento**: identifica que o *script* foi criado a partir de desenvolvimento, ou seja, pelo Fluig Studio, na própria aba ***Scripts*** do processo ou em outras ferramentas externas à plataforma. Esse *script* pode ser editado e excluído diretamente na aba ***Scripts***.

* **Edição pela interface**: identifica que o *script* foi criado pela interface, ou seja, a partir das configurações de uma atividade de serviço existente no diagrama do processo. Esse *script* inicialmente não pode ser excluído. Apenas é possível excluí-lo depois de habilitar a sua edição na aba ***Scripts*** e, nesse caso, não será mais possível editá-lo a partir da interface, nas configurações da atividade de serviço, e o seu identificador é alterado para **Edição por desenvolvimento**.

Dica!

Obtenha mais detalhes e informações mais técnicas sobre o desenvolvimento de *scripts* para eventos em:

50%

* ;

* ;

* Personalizando o *e-mail* padrão (*onNotify*);
50%

* *E-mails* personalizados (*notifier.notify*);

* ;

* [Exemplos avançados de processos](https://git.fluig.com/projects/SAMPLES/repos/exemplos-avancados-de-processos/browse).
#ebecf0

trueExemplo de uso  
Em um processo de **Pagamento de fornecedores**, existe a necessidade de enviar uma notificação por *e-mail* para uma pessoa da empresa fornecedora quando o pagamento for realizado e a solicitação for finalizada. Por ser de outra empresa, essa pessoa não é uma participante do processo e nem possui cadastro na plataforma, não sendo possível notificá-la a partir das configurações de notificação disponíveis no componente .

Neste caso, é possível adicionar um *script* para o evento ***afterProcessFinish***. Assim, quando a solicitação for finalizada, a pessoa da empresa fornecedora ficará ciente de que o seu pagamento já foi feito, pois ela também receberá o *e-mail* de notificação.

jsafterProcessFinish Templates de e-mail"
var templateEmail = "CODIGO\_TEMPLATE\_EMAIL";
var parametros = new java.util.HashMap();
//Parâmetro que será utilizado como assunto do e-mail
parametros.put("subject", "Seu pagamento foi realizado");
//Parâmetro do template que receberá o nome do responsável contido no
//campo "responsavelFornecedor" do formulário
parametros.put("NOME\_RESPONSAVEL", hAPI.getCardValue("responsavelFornecedor"));
//Parâmetro do template que receberá o valor pago e que está contido no
//campo "valorPago" do formulário
parametros.put("VALOR\_PAGAMENTO", hAPI.getCardValue("valorPago"));
//Instancia lista de destinatários
var destinatarios = new java.util.ArrayList();
//Adiciona o e-mail externo do responsável pelo fornecedor da solicitação
//que está contido no campos "emailFornecedor" do formulário
destinatarios.add(hAPI.getCardValue("emailFornecedor"));
//Realiza o envio do e-mail
notifier.notify(remetente, templateEmail, parametros, destinatarios, "text/html");
} catch(e) {
log.error("Erro ao enviar e-mail ao fornecedor: " + e);
}
}]]>

## Ver *scripts* do processo

---

**100%true5%**

**01.** Com o processo em modo de [edição](https://tdn.totvs.com/pages/viewpage.action?pageId=233763153#Plataforma%E2%9D%99Configurarprocessos-Editarprocesso), clique na aba  ***Script***– localizada no meio da barra superior.

**02.** Na lateral esquerda, veja todos os *scripts* relacionados ao processo.

#f2f2f2#f2f2f2

Os *scripts* são identificados como:

* **Edição por desenvolvimento**: indica que o *script* foi criado a partir de desenvolvimento, ou seja, pelo Fluig Studio, na própria aba ***Scripts*** do processo ou em outras ferramentas externas à plataforma;

* **Edição pela interface**: indica que o *script* foi criado pela interface, ou seja, a partir das configurações de uma atividade de serviço existente no diagrama do processo.

**03.** Clique em cada *script* para ver o seu conteúdo.

#f2f2f2#f2f2f2

Para ocultar a lista de *scripts*, clique em **Fechar** . Para ver a lista novamente, basta clicar em **Abrir**.

## Adicionar *script* no processo

---

**100%true5%**

**01.** Com o processo em modo de [edição](https://tdn.totvs.com/pages/viewpage.action?pageId=233763153#Plataforma%E2%9D%99Configurarprocessos-Editarprocesso), clique na aba  ***Script***– localizada no meio da barra superior.

**02.** Na lateral esquerda, clique em **Adicionar *script***– localizado na parte superior.

**03.** Selecione o evento do processo para o qual deseja adicionar um *script*.

**04.** Clique em **Adicionar**.

**05.** Na área de codificação, insira o código do *script* que deve ser executado quando o evento selecionado ocorrer no processo.

**06.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar o *script* criado.

**07.** Na mensagem exibida, clique em **Ok, entendi**.

## Editar *script* do processo

---

**100%true5%**

**01.** Com o processo em modo de [edição](https://tdn.totvs.com/pages/viewpage.action?pageId=233763153#Plataforma%E2%9D%99Configurarprocessos-Editarprocesso), clique na aba  ***Script***– localizada no meio da barra superior.

**02.** Na lateral esquerda, localize e clique sobre o *script* que deseja editar.

**03.** Se o *script* for de uma atividade de serviço existente no diagrama do processo, na mensagem de confirmação exibida, clique em **Editar** e, em seguida, em **Habilitar edição**.

#f2f2f2#f2f2f2

Ao habilitar a edição do *script* de uma atividade de serviço a partir da aba ***Scripts***, ele não pode mais ser editado pela interface nas configurações da atividade. Seu identificador mudará de **Edição pela interface** para **Edição por desenvolvimento** e as opções de edição e exclusão existentes nas configurações da atividade de serviço são substituídas pela opção **Acessar *script* de integração**, que direcionará para aba ***Scripts*** do processo onde o *script* pode ser editado.

**04.** Na área de codificação, edite o código do *script* que deve ser executado.

**05.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as alterações feitas no *script*.

**06.** Na mensagem exibida, clique em **Ok, entendi**.

## Excluir *script* do processo

---

**100%true5%**

**01.** Com o processo em modo de [edição](https://tdn.totvs.com/pages/viewpage.action?pageId=233763153#Plataforma%E2%9D%99Configurarprocessos-Editarprocesso), clique na aba  ***Script***– localizada no meio da barra superior.

**02.** Na lateral esquerda, localize o que deseja excluir.

**03.** Clique em **Excluir**.

#f2f2f2#f2f2f2

Essa opção não é exibida para *scripts* que são de atividades de serviço. Para excluí-los, é necessário acessar as configurações da atividade de serviço ou habilitar a edição do *script* e depois excluí-lo.

**04.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar o processo considerando a exclusão do *script*.

**05.** Na mensagem exibida, clique em **Ok, entendi**.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
