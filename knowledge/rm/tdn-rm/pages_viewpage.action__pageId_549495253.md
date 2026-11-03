---
content_hash: bc0f2a4ebd8134f5524791fc520f24b4bc52e25e66a2987379c09ec3ecd55dd0
fetched_at: '2026-06-29T00:10:43.014436+00:00'
page_id: '549495253'
product: rm
source: tdn-rm
title: Documentação - Anexo - Documentos de Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549495253
version: 21
---

# **1) Introdução**

---

Disponível à partir da versão 12.1.29, esta funcionalidade permite ao administrador, anexar ao cadastro de documentação, arquivos de contratos e documentos em geral, no formato .pdf para o usuário final acessar através do Portal do Cliente ou do aplicativo Meu Imóvel.

# **2) Procedimentos para utilização**

---

Para que os arquivos anexos sejam cadastrados é necessário que a permissão do perfil**[05.01.02]** esteja habilitada corretamente como mostra a figura:

Com a permissão habilitada o usuário deve primeiro cadastrar a documentação, [via controle de documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105339)

Após o cadastro com sucesso da documentação, poderemos associar os arquivos através do menu **Anexos / Documentos de Aluguel**:

# **3) Informações gerais**

---

* Ao cadastrar um novo documento, o usuário deverá obrigatoriamente inserir o nome do documento e o arquivo. O arquivo deverá ser do tipo PDF e não há limite de tamanho;
* Além desses dois campos, o usuário pode definir se o documento está ativo (vigente) ou não. Por exemplo, após uma negociação, um aditivo foi feito e sobrepõe todos os termos do primeiro contrato e assim gerando um novo documento. Neste exemplo, caso o administrador deseje manter o histórico ele pode transformar o contrato antigo para inativo, e o novo contrato ele atribui como ativo. Esta informação (ativo / inativo) será apresentada para o usuário final no Portal do Cliente e no aplicativo Meu Imóvel;
* Outro campo passível de alteração é o "Publicar". Este campo informa se o documento estará visível ou não para o usuário no Portal do Cliente e no aplicativo Meu Imóvel;
* Ainda na tela de criação/edição do documento, o usuário conseguirá visualizar e baixar o documento salvo no sistema.

# **4) Informações para Assinatura Digital**

---

### **Introdução**

---

À partir da versão 12.1.31, o processo de assinatura digital atrelado aos documentos de aluguel passa a garantir um controle maior destes documentos, que podem ser assinados digitalmente através do portal TOTVS Sign, garantindo segurança e transparência nos processos de efetivação de contratos.

### **Parametrizações iniciais**

---

O Parametrizador global permite ao usuário inserir as *urls*para autenticação e integração ao portal TOTVS Sign como mostrado abaixo:

* O parâmetro "Atualizar situação das assinaturas dos documentos ao carregar a visão", se marcado realiza a consulta do status dos documentos na plataforma TotvsSign assim que é realizado a abertura da visão dos documentos, caso desmarcado essa atualização do status do documento no RM é realizada na abertura de cada documento.

### Cadastros de documentos para assinatura digital

---

No menu de Contratos de Locação, estará disponível a opção TOTVS Assinatura Eletrônica, como mostra a figura abaixo:

### Aba Identificação

---

Utilizando esta funcionalidade na barra de ferramentas dos contratos de  aluguel, poderemos inserir o documento e cadastrar os destinatários e suas validações de processos.

Temos também a opção de visualizar o documento anexado, clicando no link "Visualizar".

O sistema só permitirá anexar um documento do tipo .pdf.

### Aba Destinatários

---

Nesta etapa deveremos selecionar os e-mails dos usuários que deverão receber o documento para assinatura no TOTVS Sign. O RM permite um usuário ser assinante ou validador. O RM não irá permitir a inclusão do documento caso não tenha definido os destinatários. Da mesma forma, não é possível cadastrar um destinatário sem que se defina que o mesmo é validador ou assinante do documento. Na imagem abaixo, temos três e-mails, dois destes são assinantes e um está cadastrado como validador.

Para cadastrar um destinatário, devemos clicar no botão "Novo".

Nesta etapa, podemos inserir um ou vários e-mails separados por ponto e vírgula.

Podemos também fazer uma pesquisa por Cliente/Fornecedor. Somente clientes / fornecedores que possuem e-mail aparecerão nesta listagem. Sendo assim, basta selecionar o cliente /fornecedor e adicioná-lo à lista de destinatários.

Importante

* Ao inserir o e-mail dos assinantes e validadores, imediatamente estes e-mails serão associados ao documento no portal TOTVS Sign.
* Da mesma forma, ao excluir os e-mails nesta visão, os mesmos serão excluídos do Portal TOTVS Sign
* É importante lembrar que estes usuários não precisam possuir uma conta ativa no portal TOTVS Sign, mas deverão usar o mesmo e-mail de cadastro para ter acesso ao documento.

### **Aba Validações**

---

Nesta aba, deveremos selecionar quais processos do aluguel que irão validar o status da assinatura eletrônica, ou seja, impedindo que os mesmos sejam efetivados caso o documento esteja ainda pendente de assinaturas.

Temos as seguintes opções: Efetivação do aditivo, do contrato, do encerramento e do escalonamento.

**Os processos listados acima se estiverem marcados, somente poderão ser efetivados quando todos os assinantes tenham concluído a sua assinatura. Ou seja, o status do documento está marcado como "finalizado".**

Caso o documento ainda esteja com status de "pendente", o sistema irá emitir a seguinte mensagem de erro, indicando o documento que ainda precisa de suas assinaturas:

### Atualizando o status dos documentos

---

Existem duas formas de atualizar o status destes documentos que foram enviados ao TOTVS Sign. O parâmetro ***Atualizar situação das assinaturas dos documentos ao carregar a visão*** disponível em ***Parâmetros / Parâmetros Globais / Integração TOTVS SIGN***irá controlar esse comportamento:

* Caso o parâmetro esteja marcado, assim que for aberta a visão de documentos o TOTVS Gestão de Imóveis irá sincronizar o status destes documentos com o TOTVS Sign, o que pode acarretar certa lentidão;
* Caso o parâmetro esteja desmarcado, o sistema irá apenas sincronizar este status utilizando o processo "Atualizar status de documentos". Vale lembrar que, caso o documento não exista no TOTVS Sign no momento da sincronia, o sistema irá excluir o documento do RM assim que concluir o processo.

Independente do parâmetro, os status dos documentos sempre serão atualizados ao efetivar os contratos.

### **Exclusão de documentos**

---

Para remover os documentos do RM e do TOTVS Assinatura Eletrônica, basta o usuário acessar o processo "Exclusão de documentos".

Este processo irá consultar o documento associado à action em específico e com isso, realizará sua exclusão nos dois sistemas.

**Importante**: Quando o documento é excluído via processo, o sistema irá disparar e-mails para todas as partes envolvidas neste documento, alertando que o mesmo foi excluído. 

### **Visualização de documentos**

---

Para visualizar um documento do TOTVS Assinatura Eletrônica e consultar seu status, basta clicar no link "Visualizar", na aba identificação:

Desta forma o sistema irá mostrar o documento e o seu status atual, se está pendente, finalizado ou rejeitado. Possibilitando salvar o mesmo em .PDF ou realizar uma impressão. Além de outros controles.
