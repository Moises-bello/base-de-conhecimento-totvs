---
content_hash: c2e27005c7d5613c4f2ce19e54ddbc9f2aa1ba97919ced0cf7cfcf583821b0ab
fetched_at: '2026-06-28T21:35:17.662184+00:00'
page_id: '116359178'
product: fluig
source: tdn-fluig
title: Central de componentes
type: documentation
url: https://tdn.totvs.com/display/fluig/Central+de+componentes
version: 53
---

# Índice

true.\*ndicenone

## Objetivo

A Central de Componentes permite gerenciar todos os componentes existentes na plataforma. É possível adicionar componentes adquiridos na [Fluig Store](http://www.fluigstore.com/) e, também, baixar componentes para personalizá-los e importá-los novamente. A opção de *download* é exibida apenas para componentes que permitem desenvolvimentos sobre a plataforma.

## Fazer *download* de um componente

Para personalizar um componente, primeiramente é necessário fazer o *download* do mesmo pela Central de Componentes.

## Customização de um componente

Após o download do widget, o desenvolvedor deve realizar os seguintes passos **antes** de iniciar a alteração do widget:

1. Descompacte o .zip;
2. Importe o projeto Maven através do pom.xml no Eclipse ou sua IDE de preferência;
3. No arquivo application.info altere os seguintes parâmetros:  
   1. **application.code**=NOME\_DA\_SUA\_WIDGET
   2. **locale.file.base.name**=NOME\_DA\_SUA\_WIDGET
   3. Remova o parâmetro **application.extendible**=true
   4. Adicione o parâmetro **application.origincode**=NOME\_DA\_WIDGET\_ORIGINAL. Exemplo: **socialtimeline**.
4. Altere o nome dos arquivos de internacionalização do diretório **src/main/resources**, substuindo o nome do widget atual pelo nome de seu widget:  
   1. **\*.properties** para **NOME\_DA\_WIDGET.properties**
   2. **\*\_en\_US.properties** para **NOME\_DA\_WIDGET\_en\_US.properties**
   3. **\*\_es.properties** para **NOME\_DA\_WIDGET\_es.properties**
   4. **\*\_pt\_BR.properties** para **NOME\_DA\_WIDGET\_pt\_BR.properties**
5. Altere o contexto do projeto Web no arquivo **jboss-web.xml** localizado no diretório **src/main/webapp/WEB-INF**:
   1. <context-root>**/NOME\_DA\_WIDGET**</context-root>

Pronto. O widget está pronto para ser customizado e compilado para poder ser feito o upload!

Atenção

O compartilhamento de registros entre diferentes ambientes e empresas através do Eclipse é um **comportamento esperado na plataforma**. Quando um usuário autenticado na Empresa A exporta uma criação para o ambiente, esse registro também ficará visível e disponível na Empresa B, conforme as regras de visibilidade globais configuradas.

## Adicionar um componente no no TOTVS Fluig Plataforma

Para adicionar um componente no Fluig Plataforma, deve-se fazer login como administrador e seguir os passos abaixo.

0.5falseexemplostrue1Passo 1  

* Acesse o**Painel de controle** → agrupador **Aplicativos** → **Central de componentes**.

Em atualizações anteriores à **1.6.5 (Liquid)**, a Central de componentes é acessada pela aba **WCM** no **Painel de controle**.

2Passo 2  

* Acione **Escolher arquivo** e selecione o arquivo do componente para publicação na plataforma Fluig.

* Acione **Enviar** para fazer a publicação.

3Passo 3

* Após o envio, o componente será exibido na lista de componentes. É possível usar o campo Buscar, localizado no canto direito da página, para encontrá-lo.

## Ativar/Desativar um componente

Por padrão, ao incluir um novo componente na plataforma, este componente virá desativado. Para ativá-lo, deve-se seguir os passos abaixo.

0.5falseexemplos25Ativar  

* Pesquise pelo componente que deseja-se ativar através do campo Busca localizado no canto direito da página.

* Selecione o componente na lista de componentes.

* Acione **Ativar**. Será exibida uma mensagem confirmando a ativação e o status do componente será alterado para Ativo.

6Desativar

* Pesquise pelo componente que deseja-se desativar através do campo Busca localizado no canto direito da página.

* Selecione o componente na lista de componentes.

* Acione **Desativar**. Será exibida uma mensagem confirmando a desativação e o status do componente será alterado para Inativo.

Atenção!

Orientamos que o componente (.war ou .ear) não seja removido manualmente da pasta **apps/**. Essa remoção trará impactos consideráveis pois o comando de *undeploy* é acionado executando as seguintes ações para cada item abaixo:

* *Widget* (**.war**):
  + Remove todas as *widgets* de todas as páginas;
* *Layout* (**.war**):
  + Remove todas as páginas**\*** que utilizam esse *layout*;
* Tema (**.war**):
  + Remove todas as páginas**\*** que utilizam esse tema;
* *Component* (**.ear**):
  + Remove todas as páginas desse componente.

Removendo manualmente, **o processo de recuperação é irreversível**, dado que todos os registros desse componente também serão removidos do banco de dados pois não serão mais utilizados.

**\*** As páginas internas não são removidas, como por exemplo: **cpaneladmin**

Recomendação

Recomendamos que o processo correto seja feito desativando estes componentes através da Central de componentes que é encontrada no menu **Painel de Controle** > agrupador **Aplicativos** > **Central de componentes**.

## *Redeploy* de componentes (Atualização de componentes)

Quando um componente é modificado, se ele possui o arquivo "pages.xml", é necessário clicar em **Ativar** novamente para criar as novas páginas.

A Central de componentes agirá da seguinte maneira:

* Para as páginas já existentes.  
  + Se a página possui rascunho, ele será liberado como uma versão nova e a página que está no componente será a próxima versão. Ex.:
    - página criada pela publicação de componente - **v1**;
    - usuário editou a página - criou um rascunho e não liberou;
    - novo componente é *deployado* e a página em questão faz parte desse componente: rascunho criado pelo usuário é liberado, criando a **v2**. Com a publicação do componente, a **v3** da página é criada de acordo com o componente. Desta forma, o usuário não perde alterações realizadas - se ele desejar pode restaurar a **v2** como nova versão da página - **v4**.
  + Para páginas sem rascunhos será criada apenas uma nova versão e liberada. Ex.:
    - página criada pela publicação de componente - **v1**;
    - novo componente é *deployado* e a página em questão faz parte desse componente: com a publicação do componente, a **v2** da página é criada de acordo com o componente. Desta forma, o usuário não perde alterações realizadas - se ele desejar pode restaurar a **v1** como nova versão da página - **v3**.
* Para as páginas novas.
  + Será feita a criação e publicação delas.

Caso a nova versão do componente não tenha mais algumas páginas será necessário desativar e reativar o componente. Exemplo:

* componente publicado com 5 páginas;
* ativar o componente (criação das páginas);
* alteração do arquivo "pages.xml", removendo páginas;
* enviar novamente o componente com 2 páginas;
* desativar (exclui as páginas existentes);
* ativar novamente.

Se o componente não for desativado, as páginas ainda existirão.
