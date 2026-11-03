---
content_hash: 5d85a1263b0ebd77fdce2c018dd6e9210afe8ee5168b30574c7cfc7427874d21
fetched_at: '2026-06-29T00:10:47.021334+00:00'
page_id: '556875782'
product: rm
source: tdn-rm
title: 07.2 Assinatura de Contrato Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/07.2+Assinatura+de+Contrato+Financeiro
version: 49
---

Essa documentação pode ser utilizada para **Ensino Superior e Básico**

## **Assinatura de contrato financeiro**

O responsável ou aluno, ao finalizarem a matrícula, após ler e aceitar o contrato financeiro, será realizado a matrícula como de costume, porém será salvo os dados da assinatura desse aceite que ficará disponível na tabela  SASSINATURACONTRATO, onde se encontrado dados como data e hora da assinatura, contexto da matrícula, o arquivo/Texto que foi lido, dentre outros dados importantes.

Para que o ocorra o funcionamento adequado do sistema na hora que o usuário for realizar a assinatura do contrato, é necessário que o contrato esteja cadastrado com o tipo "Plano" e que haja somente um contrato válido com esse tipo, para a matriz aplicada a qual o aluno está realizando a matrícula online.

Se for necessário para a instituição fazer o cadastro de outros contratos para atender outras demandas é importante que o tipo seja diferente de "Plano".

Assinatura de contrato financeiro através da confirmação "Li e aceito"

Quando o tipo de assinatura configurado não for assinatura com uso de **Token/Chave de segurança** ou **TOTVS Assinatura Eletrônica(TAE)**, será utilizado o tipo **"Li e aceito"** para assinatura do contrato financeiro no processo de matrícula on-line.

Para esse tipo de assinatura, somente o usuário Responsável financeiro do Aluno e/ou o usuário Responsável financeiro do contrato do aluno é que poderão realizar a matrícula. Esta validação é feita na etapa de seleção do Curso/Série ou Habilitação do aluno na matrícula on-line.

Para mais detalhes dessa validação, favor verificar:  ou  .

Assinatura de contrato financeiro com token/chave de segurança

Foi disponibilizado um nível de segurança a mais na matrícula: agora a instituição tem a possibilidade de ativar a opção de assinatura do contrato financeiro com token.

Com esse parâmetro marcado, será exibido para o usuário que está realizando a matrícula, uma opção de assinatura do contrato informando um token que chegará no e-mail do **Responsável financeiro** do aluno. Juntamente com o token também será enviada uma cópia do contrato financeiro que será assinado.

Esse token/chave de segurança é salvo criptografado na base de dados para maior segurança e ele é válido até que seja utilizado para a assinatura do contrato para o qual ele foi gerado.

Ao chegar na etapa de contrato, o aluno/responsável deve ler o contrato financeiro, clicar no botão "Li e aceito os termos do contrato" e em seguida, só será possível finalizar a matrícula, após clicar em "assinar", assim, será enviado um e-mail para o **Responsável financeiro** do aluno e a pessoa que está lendo o contrato terá que informar o número do token recebido. Com o token correto, será possível finalizar a matrícula.

Será salvo na tabela referente a assinatura, a data hora do envio do e-mail e para qual endereço de e-mail foi enviado.

Para realizar a parametrização, marque a opção "Utilizar assinatura com token/chave de segurança"

É possível encaminhar automaticamente para o aluno um e-mail contento o contrato com o manifesto.

Para realizar a parametrização acesse: Parâmetros | RM portal | RM Portal - Matricula | Portal - Assinatura contrato

Note que para que o parâmetro **Enviar e-mail do contrato com o manifesto na finalização da matricula** esteja habilitado, o parâmetro **Utilizar assinatura com token/chave de segurança (somente novo Portal do Aluno)** precisa está marcado.

Com as tags [NOME USARIO], [NOME ALUNO] e  [RA]  é permitido personalizar o texto a ser enviado junto ao contrato anexado.

Vale lembrar que o contrato é enviado no **formato pdf,** quando utilizar um relatório do reports ou **texto**, quando não utilizar o reports.

No campo acima é possível informar qual o texto que será enviado no e-mail para o **Responsável financeiro** do Aluno tendo a possibilidade de utilizar duas tags:

* **[NOME USUARIO**] - Nome do usuário que está logado no portal, realizando a assinatura do contrato.
* **[TOKEN]** - Token/Chave de segurança gerado para assinatura do contrato financeiro.

OBS: O token é composto por 6 dígitos numéricos.

Versões anteriores

Até as versões **12.1.2402.241, 12.1.2406.179, 12.1.2410.114,**o usuário logado com permissão para realizar a matrícula é quem receberia o token para assinatura do contrato na matrícula.

Para que esse comportamento seja mantido, foi disponibilizado o seguinte parâmetro nas versões superiores às citadas anteriormente:

**ATENÇÃO: a partir da versão 12.1.2502 esta configuração não estará mais disponível e o comportamento atual do sistema é que estará em vigor. Ou seja, somente o responsável financeiro pode realizar a matrícula.**

Para que o contrato seja corretamente exibido no portal durante o processo de matrícula, é necessário que a configuração "Disponível para impressão" esteja habilitada:

Caso esta configuração não esteja habilitada e a configuração "Utilizar assinatura com token/chave de segurança" esteja habilitada, durante o processo de matrícula o portal emitirá mensagem requerendo a assinatura do contrato mas o contrato não será exibido para ser lido e realizado o aceite:

#### Funcionamento **no novo portal do aluno**

Após realizar os passos acima, o usuário pode finalizar a matrícula, salvando na tabela referente a assinatura, os dados dessa assinatura realizada.

Para consultar as assinaturas do contrato basta acessar nos anexos do contrato a opção de visualizar assinaturas.

Importante

Para que o envio do e-mail seja realizado com sucesso, a parametrização de envio de e-mail deve estar configurada corretamente e no cadastro do aluno e/ou do responsável financeiro deve estar cadastrado um e-mail válido.
