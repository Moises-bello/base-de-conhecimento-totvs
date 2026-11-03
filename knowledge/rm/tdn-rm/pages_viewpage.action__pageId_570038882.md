---
content_hash: 34d17d585c7c6b1eb2acb03950a26ddb335c4850502b93ec2d97f6dfa21bc103
fetched_at: '2026-06-29T00:10:52.041236+00:00'
page_id: '570038882'
product: rm
source: tdn-rm
title: TOTVS Assinatura Eletrônica - Anexo Global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570038882
version: 25
---

**Introdução**

---

Quando o usuário necessita incluir documentos digitais do TOTVS Assinatura Eletrônica em determinado módulo, ele poderá utilizar este ícone e realizar a sua associação diretamente ao TOTVS Assinatura Eletrônica.

Desta forma, o RM está preparado, de forma global e customizada a receber a integração das assinaturas digitais através deste anexo.

Para consultar a documentação do TOTVS Assinatura Eletrônica, basta ir diretamente na visão e clicar no ícone TOTVS Assinatura Eletrônica como mostra a imagem abaixo:

Os arquivos incluídos são associados ao DataServer e a Chave do registro no qual foi aberto o Anexo.

Importante: Caso o usuário não possua parametrização global preenchida com os endpoints do portal TOTVS Assinatura Eletrônica, será apresentado um banner informativo quando clicar no ícone.

### Primeiro acesso através do RM

---

Quando o usuário ainda não possui cadastro no TOTVS Assinatura Eletrônica, o RM irá validar este usuário quando o mesmo tentar inserir o documento. Caso este usuário já exista o TOTVS Assinatura Eletrônica irá prosseguir com as etapas abaixo, para inclusão dos documentos, destinatários e validadores.

Quando o usuário não existe, ou seja o e-mail cadastrado do usuário logado no RM não existe no TOTVS Assinatura Eletrônica, o RM irá cadastrá-lo automaticamente na tela de inclusão de documentos como mostrado abaixo:

Neste momento o RM valida o usuário logado no RM. Caso o e-mail não seja encontrado no ambiente TOTVS Assinatura Eletrônica, será proposta a sua criação na etapa seguinte:

Será necessário inserir o **Nome Completo**, o **CPF/CNPJ**, o **E-mail**, e a **Senha** do usuário, além de aceitar a **Política de Privacidade** e o **Termo de Uso**, para que o cadastro no TOTVS Assinatura Eletrônica ocorra com sucesso.

Terminando esta etapa o usuário já pode inserir seus documentos no portal TOTVS Assinatura Eletrônica.

### Aba Identificação

---

Ao cadastrar um envelope novo utilizando o anexo na barra de ferramentas, poderemos cadastrar os documentos, os destinatários e o seu papel.

Em um envelope, o sistema permite que sejam anexados um ou mais documentos em formato *pdf* e/ou anexar um relatório.

Na aba **identificação**, temos as seguintes informações:

* **Identificador:** Este campo é preenchido automaticamente pelo sistema;
* **Status do Envelope:** Através deste campo poderemos consultar a situação deste envelope no TOTVS Assinatura Eletrônica.

Os seguintes status poderão ser visualizados:

* + **Pendente**: Quando o documento ainda não foi assinado por nenhum dos destinatários cadastrados;
  + **Rejeitado**: Quando o documento foi rejeitado no TOTVS Assinatura Eletrônica por algum motivo, informado pelo destinatário;
  + **Finalizado**: Quando o documento já foi assinado por todos os destinatários.
* **Nome do Envelope:** É o nome que será exibido no portal do TAE, quando os usuários logarem no mesmo;
* **Solicitar Assinatura Manuscrita:** Ao marcar esta opção, ao assinar um documento, todas as páginas do mesmo serão rubricadas e será utilizada a [Assinatura Manuscrita (Rubrica)](https://tdn.totvs.com/pages/viewpage.action?pageId=776123935) do destinatário.

### **Aba Documentos**

---

Nesta aba pode-se incluir os arquivos, em formato pdf e/ou os relatórios que serão envelopados e enviados para os destinatários do envelope.

Pode-se incluir arquivos que atendam o tamanho máximo exibido na informação Arquivo (limite máximo de ##Mb), de forma que é possível de se enviar mais de um arquivo para validação mesclando com um ou mais relatórios do TCGI.

Após selecionar o arquivo e ou o relatório, acione o botão "+" para incluir cada um deles.

Também é possível utilizar o botão para excluir os arquivos, caso necessário.

Novidade!

A partir do Release 12.1.2310 é possível de se incluir os Relatórios do TCGI nos envelopes que serão enviados para a assinatura no TAE.

### Aba Destinatários

---

Nesta aba deveremos selecionar os e-mails dos usuários que deverão receber o documento para assinatura no TOTVS Assinatura Eletrônica.

O destinatário pode desempenhar apenas um dos papéis abaixo:

* **Assinante:** É a pessoa que tem interesse no documento, ou seja, a pessoa a qual o documento se destina e que irá assinar o documento; ou
* **Validador:** É a pessoa que irá validar o documento como testemunha no TOTVS Assinatura Eletrônica.

Caso o destinatário responsável pelo e-mail informado não esteja cadastrado no TOTVS Assinatura Eletrônica, o mesmo receberá um e-mail com convite para se cadastrar na plataforma (no cadastro é importante que seja informado o mesmo e-mail indicado no processo).

O sistema não irá permitir a inclusão do documento caso não se tenha definido o destinatário.

Da mesma forma, não é possível cadastrar um destinatário sem que se defina que o mesmo é assinante ou validador do documento.

Para cadastrar um destinatário, devemos clicar no botão "Novo".

Nesta etapa, podemos inserir um ou vários e-mails separados por ponto e vírgula.

Podemos também fazer uma pesquisa por Cliente/Fornecedor. Somente clientes / fornecedores que possuem e-mail aparecerão nesta listagem. Sendo assim, basta selecionar o cliente/fornecedor e adicioná-lo à lista de destinatários.

O e-mail do cliente/fornecedor que será utilizado no TAE é o que estará registrado no campo E-Mail da aba Principal do contato:

Importante

* Ao inserir o e-mail dos assinantes e validadores, imediatamente estes e-mails serão associados ao documento no portal TOTVS Assinatura Eletrônica.
* Da mesma forma, ao excluir os e-mails nesta visão, os mesmos serão excluídos do Portal TOTVS Assinatura Eletrônica
* É importante lembrar que estes usuários não precisam possuir uma conta ativa no portal TOTVS Assinatura Eletrônica, mas deverão usar o mesmo e-mail de cadastro para ter acesso ao documento.
* Ao inserir um documento pelo anexo, o TAE irá buscar automaticamente os locatários ativos do contrato de locação e os compradores da venda, facilitando os fluxos de aprovação. Eles serão definidos como assinantes automaticamente. Para que a inclusão automática funcione, o comprador ou o locatário devem possuir o campo e-mail preenchido.

### Atualizando o status dos documentos

---

Existem duas formas de atualizar o status destes documentos que foram enviados ao TOTVS Assinatura Eletrônica.

O parâmetro ***Atualizar situação das assinaturas dos documentos ao carregar a visão*** disponível em ***Parâmetros / Parâmetros Globais / Integração TOTVS Assinatura Eletrônica***irá controlar esse comportamento:

* Caso o parâmetro esteja marcado, assim que for aberta a visão de documentos o TOTVS Gestão de Imóveis irá sincronizar o status destes documentos com o TOTVS Assinatura Eletrônica, o que pode acarretar certa lentidão;
* Caso o parâmetro esteja desmarcado, o sistema irá apenas sincronizar este status utilizando o processo "Atualizar status de documentos". Vale lembrar que, caso o documento não exista no TOTVS Assinatura Eletrônica no momento da sincronia, o sistema irá excluir o documento do RM assim que concluir o processo.

Independente do parâmetro, os status dos documentos sempre serão atualizados ao efetivar os contratos.

### **Exclusão de documentos**

---

Para remover os documentos do RM e do TOTVS Assinatura Eletrônica, basta o usuário acessar o processo "Exclusão de documentos".

Este processo irá consultar o documento associado à action em específico e com isso, realizará sua exclusão nos dois sistemas.

**Importante**: Quando o documento é excluído via processo, o sistema irá disparar e-mails para todas as partes envolvidas neste documento, alertando que o mesmo foi excluído. 

### **Visualização de documentos**

---

Para visualizar um documento do TOTVS Assinatura Eletrônica e consultar seu status, basta clicar no link "Visualizar Arquivo", na aba identificação:

Desta forma o sistema irá mostrar o documento e o seu status atual, se está pendente, finalizado ou rejeitado. Possibilitando salvar o mesmo em .PDF ou realizar uma impressão. Além de outros controles.
