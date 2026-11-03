---
content_hash: cbd8772ee459b771c8978313e21f39724fd561821182a6521ea1fa29318cacfe
fetched_at: '2026-06-28T21:35:28.958040+00:00'
page_id: '73078179'
product: fluig
source: tdn-fluig
title: Guia de instalação Fluig Studio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73078179
version: 75
---

true.\*ndicenone

# Instalação da IDE

---

Para utilização do plugin de desenvolvimento do Fluig é necessário possuir uma IDE baseada em Eclipse. As IDEs homologadas para trabalhar com o Fluig Studio estão listadas abaixo:

| IDEs Homologadas | Página de *download* | Requisitos |
| --- | --- | --- |
| Eclipse Luna | <https://www.eclipse.org/downloads/packages/release/luna/sr2/eclipse-ide-java-developers> Atenção! O Eclipse Luna não é compatível com a atualização Voyager 2.0 do Fluig. | Ter instalado o JDK 8 da Oracle: <https://www.oracle.com/br/java/technologies/javase/javase8-archive-downloads.html> |
| Eclipse 2019-R9 | <https://www.eclipse.org/downloads/packages/release/2019-09/r/eclipse-ide-enterprise-java-developers> | Ter instalado o JDK 8 da Oracle: <https://www.oracle.com/br/java/technologies/javase/javase8-archive-downloads.html> Atenção! O recurso de Autocompletar, na edição de eventos não funcionará por um problema no JSDT (*JavaScript Development Tools*) da IDE. |

Notas:

* O *plugin* de desenvolvimento do Fluig não é compatível com o sistema operacional macOS.

* Desenvolvedores que utilizam o plugin do Eclipse precisam atualizar para uma versão que execute com **Java 11**.

# Como ativar o OpenJDK

---

Para evitar inconformidades de licenças e estar de acordo com o uso proposto para mitigar riscos de auditoria, é imprescindível utilizar o OpenJDK para os desenvolvimentos.

Veja a seguir como ativar o OpenJDK já instalado em sua máquina.

**01.** Abra o Eclipse.

**02.** No menu superior, clique em **Window** → **Preferences**.

**03.** Na janela que será aberta, localize o menu à esquerda, expanda a opção **Java** e clique em **Installed JREs**.

**04.** Caso o Java antigo da Oracle ainda esteja listado à direita, selecione-o e clique em **Remove**.

**05.** Clique em **Add...**.

**06.** Selecione a opção **Standard VM** e clique em **Next**.

**07.** No campo **JRE home**, clique em **Directory...**.

**08.** Navegue até a pasta onde o OpenJDK foi instalado. Normalmente, o caminho é:

**09.** Selecione a pasta e clique em **Selecionar Pasta**.

**10.** O Eclipse carregará automaticamente as informações da JRE. Clique em **Finish**.

**11.** Na lista principal de JREs, marque a caixa de seleção ao lado da nova instalação do **OpenLogic OpenJDK** para defini-la como padrão.

**12.** Clique em **Apply and Close**.

Pronto! Seu ambiente estará configurado com o OpenJDK 8, sem dependência de licenças.

# Instalação do Fluig Studio

---

**Pré requisitos**

* Para a instalar e atualizar o Fluig Studio será necessário acesso à internet na estação em que a IDE está instalada.

Com sua IDE instalada e devidamente configurada restam apenas quatro passos simples que são os mesmos em ambas as IDEs.

InstalaçãoslidePasso 1  

* Selecione no menu “Help” a opção “Install New Software”  ou “Ajuda” e a opção “Instalar novo Software” se sua IDE estiver traduzida.

Passo 2  

* Adicione um novo “update site” selecionando o botão "Add":

Passo 3  

* Cadastre o endereço **http://update.fluig.com**, referente a última versão do plugin do Fluig disponível, confirmando os dados conforme figura abaixo:

Importante!

Para o TDS 11.2 e o Eclipse em versões anteriores à Mars, é recomendável adicionar também o repositório  [**https://archive.eclipse.org/graphiti/updates/0.11.2/**](https://archive.eclipse.org/graphiti/updates/0.11.2/), referente a versão compatível do Graphiti© com o Fluig Studio.

Nota:

Se deseja informar a atualização do plugin de uma versão específica, basta informar "*/<versãoFluig>*" após a URL padrão, onde <versãoFluig> corresponde ao número da versão desejada.

**Exemplo:** Possuo o Fluig 1.2.8 e desejo atualizar o plugin Fluig para a mesma versão do servidor, como já existe uma versão mais atual disponível na URL padrão, basta informar: **http://update.fluig.com/128** .

Passo 4  

* Selecione a opção que você acabou de cadastrar no **Passo 3** e confirme a operação.

Importante!

Para o correto funcionamento da instalação do Fluig Studio é necessário selecionar o *checkbox* “Contact all update sites during install to find required software”.

Nota:

Na ocorrência de erros referentes à autenticação no proxy, durante essa etapa, você pode tentar desabilitar o proxy, o firewall e até mesmo o antivírus na máquina onde estiver instalando o plugin, e em seguida prosseguir com a instalação. Sugere-se também fazer um teste de instalação em uma máquina fora da rede para comparar.

Passo 5

* Após o download e reinício da IDE a mesma estará pronta para trabalhar com o Fluig Studio.

**Dica:** Para atualização basta selecionar o update cadastrado com o Fluig Studio conforme ilustrado no passo número 4.

Importante!

Não é recomendado o uso do plugin "Team Foundation Server plug-in for Eclipse" (TFS) no mesmo TDS do plugin Fluig.

O plugin Fluig utiliza algumas bibliotecas de terceiros para comunicação com os *webservices* do servidor Fluig. Entre elas, o plugin Apache Xerces (<http://xerces.apache.org/>), que é instalado automaticamente e pode ser visualizado em *Sobre > Detalhes da Instalação > Plugins*. A versão atual disponível nos repositórios do Eclipse Luna é a versão 2.9.0.

Identificamos que o TFS também faz uso do Xerces, porém, na versão 2.8.0. Normalmente isso geraria um erro ou um alerta, na hora da instalação, mas o TFS não o instala diretamente, apenas carrega-o internamente a partir da pasta *plugins/com.microsoft.tfs.core\_14.0.2.201512281637/libs/xerces-2.8.0*.

Por se tratarem de duas versões diferentes, quando carregado primeiramente o Xerces do TFS, ao tentar utilizar algumas funções do plugin Fluig, o TDS identifica versões diferentes do mesmo arquivo e dispara um erro.

A pasta pode ser removida manualmente para que os dois possam trabalhar juntos, mas o TFS pode não funcionar corretamente.

## Vídeo How to

---

Se preferir veja a seguir o vídeo que ilustra o processo de instalação do Fluig Studio

854480
