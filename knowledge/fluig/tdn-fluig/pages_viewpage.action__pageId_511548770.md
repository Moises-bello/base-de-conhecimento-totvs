---
content_hash: 27b0dea2c4fb0ba45e9a5c7987efd451cc924f4691bad2033cc737380e8d6f6e
fetched_at: '2026-06-28T21:35:27.267088+00:00'
page_id: '511548770'
product: fluig
source: tdn-fluig
title: Bloquear ação download de documento para Android
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=511548770
version: 7
---

# Índice

4true.\*ndicenone

# Bloquear download de documentos

---

Os procedimentos abaixo demonstram como bloquear no My Fluig o *download* de documentos que tenham essa opção desabilitada pelo publicador/administrador.

## Configurando permissão de download de documentos no My Fluig

---

É possível configurar permissão de *download* para visualização de documentos no aplicativo Android. Para realizar esta alteração siga os passos abaixo:

false11Passo 1

* Efetue a autenticação no TOTVS Fluig Plataforma pela web utilizando o usuário **wcmadmin** e acesse **Painel de Controle  → WCM → Empresas**.
2Passo 2

* Selecione a empresa que deseja alterar e então clique na opção **Editar**.
3Passo 3

* A tela de edição de empresa será apresentada. Clique no botão **Cadastrar dados adicionais****.**
4Passo 4

* A tela de dados adicionais da empresa será apresentada. No campo **Chave,** informe o valor **enableDocumentSecurityOnMobile**e no campo **Valor**informe:

***true*:**  Para que a configuração de permissão de *download* do documento definida pelo publicador seja considerada na visualização pelo My Fluig.

***false*:** Para habilitar a visualização do documento através do dispositivo móvel aos usuários que possuam permissão de Leitura (ou superior), independente da configuração definida pelo publicador.

5Passo 5

* Clique no botão **Salvar** para salvar os dados adicionais. O item **enableDocumentSecurityOnMobile**será adicionado na listagem de dados adicionais da empresa.

## Configurando permissão de download do documento

---

Além de configurar a chave **enableDocumentSecurityOnMobile**na empresa, é necessário também configurar a permissão no documento, da seguinte forma:

false11Passo 1

* Acesse a pasta onde o documento está salvo e no final da linha do documento, clique no botão **Mais opções** e selecione **Propriedades**.
2Passo 2

* Selecione a aba **Informações Gerais** e localize o campo **Permite download e impressão?**
3Passo 3

* Para que o documento possa ser baixado e visualizado no *mobile*, basta manter o campo assinalado.
4Passo 4

* Para impedir o *download* do documento, **desmarque esta opção**. **Conforme a imagem abaixo**:

Hey!

Para garantir a segurança do arquivo físico, certifique-se em marcar a opção **Utiliza visualizador interno?**.

## Comportamento da configuração para o usuário no aplicativo

---

Acompanhe o funcionamento da configuração de bloqueio da ação de download e como ela será apresentada para o usuário nos passos abaixo:

false11Passo 1

* Caso o usuário tenha permissão para fazer o *download* do documento, será possível baixar e visualizar o documento tocando na opção **Salvar documento**.

2Passo 2

* Caso o usuário não tenha permissão para fazer o *download* do documento, ou seja, quando na Fluig Plataforma o parâmetro **enableDocumentSecurityOnMobile** foi definido como *true*, o documento não será visualizado ou baixado e na tela será apresentada a seguinte mensagem:

## Permissões de download e impressão na aba Segurança

---

Nas propriedades de documentos e pastas, há uma opção chamada **Download e impressão** na aba **Segurança**, que permite especificar quais usuários/grupos terão o download do documento liberado.

Caso o Fluig esteja na Atualização 1.5.12 ou anterior, quando a chave **enableDocumentSecurityOnMobile** for configurada no ambiente, independentemente do valor atribuído a ela (*true* ou *false*), as permissões de download e impressão definidas na aba Segurança não serão levadas em consideração pelo My Fluig.

A partir da Atualização 1.5.13, as configurações da aba Segurança serão aplicadas no My Fluig, desde que a chave **enableDocumentSecurityOnMobile** tenha sido habilitada.

Atenção

Uma vez definido o parâmetro **enableDocumentSecurityOnMobile**, esta configuração será aplicada para os novos usuários que adicionarem sua conta no aplicativo do Fluig para Android.

Para usuários que já possuem a conta configurada em um dispositivo móvel Android, na próxima vez em que o aplicativo for aberto, esta configuração será atualizada. Caso o dispositivo estiver usando rede 3G, essa verificação é feita apenas uma vez por dia.
