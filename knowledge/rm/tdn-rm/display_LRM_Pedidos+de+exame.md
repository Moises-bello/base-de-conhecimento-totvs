---
content_hash: 5100707534beb1533db365d1d83b118a184a75ceaf405639a521721e137daec7
fetched_at: '2026-06-29T00:10:22.709821+00:00'
page_id: '498703248'
product: rm
source: tdn-rm
title: Pedidos de exame
type: documentation
url: https://tdn.totvs.com/display/LRM/Pedidos+de+exame
version: 31
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Regras**
4. **Validações na Solicitação de Exames**
5. **Informação Complementar**

itensVisão Geral

## **01. VISÃO GERAL**

Esta documentação vai te ajudar a entender como pedir exames laboratoriais e de imagem. É um processo bem fácil, e as regras são as mesmas se você acessar a funcionalidade pelo menu "Unidade de Diagnóstico > Pedidos de Exames" ou "Atendimento > Registro de Atendimento> Pedido de Exames".

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

No menu principal, clique em **Unidade de Diagnóstico > Pedidos de Exames**.

Após abrir a tela, você precisará selecionar o paciente para quem o exame será solicitado.

Selecione o paciente/atendimento desejado na lista e clique em Ok.

A tela de **pedido de exame** será exibida. Aqui, você verá todos os pedidos que já foram feitos para o atendimento que você selecionou.

Para criar um novo pedido, clique no botão **Incluir**.

A tela de **inclusão do Pedido de Exame** será aberta.

Alguns campos são preenchidos automaticamente ou dependem de configurações, mas é importante conhecer cada um:

* **Pedido**: É o código do seu pedido de exame, é gerado automaticamente depois que você salvar.

* **Pedido Auxiliar**: Este campo aparece automaticamente se o pedido estiver sendo editado e se o parâmetro "Utiliza número de pedido de exame sequencial por setor" (Ambiente>Parâmetros>Gestão Hospitalar>Unidade Diagnóstico>Parâmetros>outros ½) estiver ativado. O formato é "AAAA-SSSSSS", onde AAAA é o ano e SSSSSS é a sequência do pedido no ano.

* **Unidade de Atendimento**: **Campo obrigatório**. Aqui você seleciona onde o exame será realizado, serão listadas apenas as unidades configuradas para solicitação de exames e que são do tipo Laboratório, Diagnóstico de Imagem ou Central de Exames. Para configurar as unidades, acesse: Ambiente > Parâmetros > Gestão Hospitalar > Parâmetros por Estação de Trabalho > Unidade de Atendimento para Solicitação de Exames.
* **Data/Hora do Pedido**: **Campo obrigatório**.

+ Se o paciente for **interno**, a data e hora atuais do servidor serão preenchidas automaticamente.
+ Se o paciente for **externo**, a data e hora de entrada do paciente serão preenchidas.
+ **Atenção**: Não é permitido inserir uma data anterior à data de entrada do paciente. Para pacientes externos, a data e hora devem estar dentro do período de entrada e saída do paciente.

* **Tipo Solicitante**: **Campo obrigatório**. Por padrão, "Médico" já vem selecionado, mas você pode mudar. Se a unidade executora do exame estiver integrada com a Philips, esse campo será "Médico" e não poderá ser alterado.
* **Nome Prestador Solicitante**: **Campo obrigatório**.

+ Se o "Tipo Solicitante" for **Próprio Cliente**, o nome do paciente será preenchido e não poderá ser alterado.
+ Se o "Tipo Solicitante" for **Médico** e já houver um médico solicitante cadastrado para o atendimento, o nome dele será preenchido.
+ Se o "Tipo Solicitante" for **Outro**, você poderá digitar o nome livremente.

* **Exame no Leito**: Este Campo fica visível quando o paciente for do tipo Interno ou Externo e a unidade do atendimento Realiza Classificação de Risco.
* **Recurso**: **Campo obrigatório** se a unidade executora para o exame usar integração com a Philips.
* **Informações Clínicas**: Campo livre e **não obrigatório**. No entanto, se o convênio do paciente exigir, ele se torna obrigatório e precisa ter no mínimo 20 caracteres. Para habilitá-lo, acesse: **Cadastros > Condições Contratuais > Eletrônico III > Aba Geral III**.
* **Data da última menstruação (DUM - para pacientes do sexo feminino):** Este campo aparecerá para preenchimento, mas **não é obrigatório**. Se for preenchido, a informação será enviada para a tela da central de laudos. Não é permitido informar uma data futura.

Depois de preencher todas as informações, clique em **Salvar**.

Pronto! Seu pedido de exame foi criado.

Depois de preencher os dados do pedido, é hora de adicionar os exames.

Na tela do pedido, vá para a aba **Exames.**

Clique no botão **Incluir** para adicionar um exame.

A tela para inclusão dos exames será aberta.

Ao incluir novos exames, você notará que alguns campos são preenchidos de forma **automática** pelo sistema.

É importante que você conheça cada um desses campos:

* **Exame**: **Campo obrigatório**. Você pode buscar o exame pela descrição, código, sinonímia ou mnemônico. A lista mostrará apenas exames da unidade selecionada.

* **Local**: Define o laboratório onde o exame será feito.

+ Se o exame tiver um laboratório padrão configurado, ele será preenchido automaticamente.
+ Se não houver, o sistema avisará que há laboratórios disponíveis. Você pode selecionar um manualmente.

* **Material Biológico**: **Campo obrigatório** para exames de laboratório. O sistema tenta preencher automaticamente:

+ Se houver apenas um material biológico para o exame, ele será o padrão.
+ Se houver vários materiais e um for padrão, ele será selecionado.
+ Se houver vários e nenhum for padrão, você precisará selecionar um manualmente.

* **Vasilhame e Método**: Campos **não obrigatórios**, preenchidos automaticamente se houver informação no cadastro do exame.
* **Médico Responsável**: **Não obrigatório**, a menos que o parâmetro para "Obrigar responsável pelo exame no atendimento Externo” esteja ativado. Para ativá-lo, acesse o menu: **Ambiente > Parâmetros > Gestão Hospitalar > Registro e Controle > Registro e Controle I**.

+ Se houver um médico executante vinculado à unidade de atendimento, ele será selecionado. Caso contrário, será o médico do atendimento.

* **Material Pendente**: Se esta opção estiver marcada, a data de entrega do exame não será gerada, pois a entrega dependerá do recebimento do material.
* **Data de Entrega**: Calculada automaticamente com base no prazo definido no cadastro do exame.
* **Senha da Guia**: Este campo será **obrigatório** se o parâmetro "Número da Autorização/Senha e procedimentos autorizados sempre obrigatórios" estiver ativado. Para ativá-lo, acesse o menu: **Cadastros > Condições Contratuais > Eletrônico III > Geral II**.

**Informações Adicionais do Paciente**

Na aba **Informações do Paciente**, você pode registrar dados importantes:

* **Peso**: Deve ser maior que 0 e menor que 1000 (kg).
* **Altura**: Deve ser maior que 0 e menor que 3 (m).
* **Volume urinário**: Deve ser maior que 0 e menor que 5000 (ml).
* **Local do corpo de coleta do material biológico:** Campo alfanumérico com no máximo 50 caracteres.

**Importante**: A obrigatoriedade desses campos depende da configuração do exame, você pode acessar e ajustar essa configuração no menu: Cadastros>Unidades de Diagnóstico>Exames e Serviços>Configurações do Exame

* **Instruções**: Aqui você verá as orientações de preparo para os exames, desde que essas informações estejam cadastradas previamente no exame.

Após preencher todos os campos necessários, clique em **Salvar**.

Se quiser adicionar mais exames, clique em **Incluir** novamente na aba "Exames" e repita o processo.

Regras

## **03. REGRAS**

## **Campos Bloqueados: O Que Saber**

Algumas situações farão com que os campos do pedido fiquem bloqueados para edição:

* **Alteração do Exame Após Salvar o Pedido**: Uma vez que um exame foi salvo no pedido, **não é possível alterar o campo "Exame"**. Isso ocorre porque a mudança de um exame afeta várias etapas (débitos, amostras, faturamento, etc.). Se você lançou o exame errado, precisará **cancelá-lo** e fazer um novo pedido com o exame correto.
* **Pedido Cancelado ou Atendimento Faturado**: Se o pedido for cancelado ou o atendimento já tiver sido faturado, **todos os campos serão bloqueados** e não poderão ser alterados.
* **Pedido Integrado**: Se o pedido já foi integrado com outros sistemas, **todos os campos também serão bloqueados** e não poderão ser modificados.

## **Regras Importantes**

Para Atendimento Externo

* Ao inserir um exame para um paciente externo, o sistema sempre verificará a data de entrada do paciente.

**Faturamento**

* **Cobrança de Exames**: Ao salvar um exame, o sistema pode lançar automaticamente o item de débito na conta do paciente. Para isso, a unidade onde o exame será feito e o próprio exame devem estar configurados para faturar.
* **Regra de Cobrança**: A cobrança é baseada na tabela de preços ou de procedimentos do convênio. O sistema também verifica a **compatibilidade de sexo** do procedimento com o sexo do paciente.

+ Por exemplo, se um exame for configurado apenas para o sexo feminino, ele só será cobrado para pacientes femininas. Se houver distinção de cobrança entre sexos, você deve cadastrar um item de débito diferente para o sexo masculino.
+ Se não houver distinção de sexo para a cobrança, o procedimento deve ser configurado como "Todos".

* **Guia/Autorização**: Se o sistema estiver configurado para incluir a guia/autorização junto com o pedido, essa mesma regra de compatibilidade de sexo também será aplicada.
Validações na Solicitação de Exames

## **04. VALIDAÇÕES NA SOLICITAÇÃO DE EXAMES**

Ao adicionar um exame, o sistema realiza diversas validações para garantir que a solicitação esteja correta e de acordo com as regras estabelecidas. Abaixo, detalhamos as possíveis validações e as mensagens que você poderá encontrar:

### Itens de Débito e Preços

* **Exame sem Item de Débito:** Se o exame não tiver um item de débito vinculado, você verá a mensagem: "**Não existe item de débito cadastrado para este exame nas tabelas utilizadas pelo convênio**". Nesse caso, o exame **não será incluído**.

Para cadastrar um item de débito, acesse: **Cadastros > Unidades de Diagnóstico > Exames e Serviços > Anexos > Item de Débito****.**

* **Item de Débito sem Preço:** Caso o exame tenha um item de débito, mas este não possua preço cadastrado na tabela, a mensagem será: "**O exame 'x' não possui preço para o item de débito 'x'.**". O exame **não será incluído**.

Acesse: **Cadastros>Outros Cadastros>Tabelas de Procedimentos e Serviços**

### **Restrições de Horário**

* **Horário Não Permitido:** Se o exame tiver horários permitidos configurados e a solicitação estiver sendo feita fora desses horários, a mensagem exibida será: "**Existe uma restrição de Horários Permitidos para o exame.**"

Para configurar os horários permitidos, acesse o menu: **Cadastros > Unidades de Diagnóstico > Exames e Serviços > Horários Permitidos.**

### **Duplicidade de Exames**

* **Exame Duplicado:** Não é possível solicitar o **mesmo exame**, com o **mesmo material biológico** e a **mesma data/hora de execução** no mesmo pedido. Se a data/hora de execução não for informada, o sistema também não permitirá a solicitação do **mesmo exame** e **mesmo material biológico**.

### **Restrições de Contrato**

As restrições de contrato são regras específicas definidas para cada convênio. Ao tentar adicionar um exame com as seguintes restrições, as mensagens abaixo poderão exibidas:

* **Restrição do tipo Proibida:** Se o exame tiver uma restrição do tipo "proibido", você verá uma mensagem indicando que "**o item não é permitido**". O exame **não será incluído**.

* **Restrição Grátis:** Se o exame tiver restrição do tipo "grátis", será perguntado: "**O exame X possui restrição de contrato, do tipo Grátis. Deseja continuar?**".

+ Se você escolher **"Sim"**, o exame será incluído e aparecerá na aba de **itens grátis**.
+ Se escolher **"Não"**, o exame **não será incluído**.

* **Restrição Particular:** Para exames com restrição do tipo "particular", a mensagem será: "**O item 'x' não possui cobertura pelo convênio. Confirma o seu lançamento na página de gastos particulares?**".

+ Se você escolher **"Sim"**, o exame será incluído e aparecerá na aba de **gastos particulares**.
+ Se escolher **"Não"**, o exame **não será incluído**.

* **Exige Liberação do Convênio:** Se o exame exigir liberação do convênio, a pergunta será: "**O item 'x' exige liberação do convênio! Confirma o seu lançamento?**".

+ Se você escolher **"Sim"**, o item será incluído. A cobrança será baseada na porcentagem coberta pelo convênio ou no valor pago pelo paciente como gasto particular.

Para mais informações detalhadas sobre as restrições de contrato, por favor, consulte a documentação:

<https://tdn.totvs.com/pages/releaseview.action?pageId=625762629#itens--176413381>

### **Restrições com Outros Exames**

* **Restrição por Pedido:** Se houver restrições entre exames e você tentar adicionar um exame que possui restrição com outro já solicitado no mesmo pedido (considerando o intervalo de dias configurado), a mensagem exibida será: "**Existe restrição para o exame selecionado**". Nesse caso, o exame **não será incluído**.

Para configurar as restrições com outros exames, acesse o menu: **Cadastros>Unidades de Diagnóstico>Exames e Serviços>Restrições**

### **Restrições por Faixa Etária**

* **Validação de Faixa Etária:** Se o exame possuir restrições por faixa etária, o sistema verificará a idade e o sexo do paciente de acordo com o que foi cadastrado.

Para configurar a restrição por faixa etária, acesse o menu: **Cadastros>Unidades de Diagnóstico>Exames e Serviços>Anexos>Restrição por faixa etária**

InfComplementarInformação ComplementarInformação Complementar

## **05. INFORMAÇÃO COMPLEMENTAR**

Informação complementar nos permite criar perguntas para serem respondidas dentro do pedido, podendo ser especifico(para exame) ou para o pedido como um todo.

*Obs. Mesmo que seja cadastrado como especifico o preenchimento com as resposta é feito no mesmo lugar, aba de informação complementar no pedido.*

Acessar a funcionalidade pelo menu "Cadastro > Unidade de Diagnóstico > Informações Complementares".

**CADASTRO**

No cadastro informamos:

* Código: Um numérico indicando o identificar único do cadastro.
* Descrição: Descrição da pergunta.
* Tipo: Indica se a pergunta é associada ao pedido (Tabela Padrão) ou ao exame (Especifico)
* Sexo: A qual sexo a pergunta representa
* Ativo: habilita ou desabilita a pergunta de ser exibida no pedido.

No caso da informação ser especifica, devemos ir no cadastro de exames (Menu > Cadastro > Unidade Diagnóstico > Exames e Serviços) e associar a informação ao exame:

Para ter acesso a aba de informações complementares siga para anexos e selecione a opção indicada abaixo:

Nessa tela associamos o cadastro da informação complementar especifica com o exame, caso necessário informe outras informações especificas nesse exame, ou adiciona a informação complementar em outros exame seguindo esse mesmo passo a passo.

**USO**

Após cadastrar o pedido utilize o menu abaixo para adicionar a aba de perguntas e respostas:

Dê um duplo clique na pergunta que deseja responder, informe a resposta e salve:
