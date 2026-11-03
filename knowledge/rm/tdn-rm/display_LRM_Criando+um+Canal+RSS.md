---
content_hash: 513c42861c08bfd76356e871acaa7683ef96f69330d18eda7a0fcbf241380916
fetched_at: '2026-06-29T00:10:57.225583+00:00'
page_id: '59900109'
product: rm
source: tdn-rm
title: Criando um Canal RSS
type: documentation
url: https://tdn.totvs.com/display/LRM/Criando+um+Canal+RSS
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.40 |
| **Processo** | **:** | Canal RSS |
| **Subprocesso** | **:** | Criar e gerenciar um canal RSS |
| **Data da publicação** | **:** | 22/05/2013 |

**Objetivo: Este guia ajudará na criação de um novo canal RSS dentro da Nova MDI dos sistemas CorporeRM da TOTVS.**

**1.** **Criando o Canal RSS**

Para criar o canal RSS, é utilizado a visão de Canal RSS, acessada pelo Menu Gestão:

Após acessar essa visão, serão listados os RSS cadastrados na base de dados que o filtro da visão selecionou.

Clicando no botão Incluir (CTRL + INS), será aberto a visão para inclusão de um novo registro.

Nessa aba, deve ser preenchido o campo **Título,** sendo Obrigatório o preenchimento desse**.**

Após o preenchimento, deverão ser incluídas as Permissões dos usuários, na aba seguinte.

Esse ponto é de extrema importância, visto que os usuários associados a esses perfis terão acesso a assinar o Canal RSS.

Por fim será criada a Fonte RSS que é responsável pelo retorno dos *feeds* RSS.

Essa Fonte RSS consiste em uma Consulta SQL, que ao sofrer alteração de dados ou de registros, ao longo da utilização do sistema, retorna um *feed* RSS.

Na inclusão da Fonte RSS, é necessário a criação de uma consulta SQL que contenha o resultado que será analisado pelo RSS.

Uma vez que essa consulta SQL sofrer alteração, o alerta será disparado.

Vamos criar uma consulta, que simplesmente retorna o campo CHAPA e SALARIO do funcionário.

Com isso iremos monitorar todas as alterações que serão feitas no salário do Funcionário.

**2.** **Criando a Consulta SQL do Alerta**

Clicando nas reticências, será aberto a janela de pesquisa das Consultas SQL. Como não criamos ainda a consulta SQL, clicaremos no botão Incluir (CTRL+INS).

Lembre-se de marcar a opção “Disponível para o RM Portal” para que essa consulta possa ser utilizada pelo RSS.

Após a inclusão da Consulta SQL, preencha os demais campos da Fonte RSS, lembrando que obrigatoriamente os campos **Cons. SQL de Alerta**, **Título e Cons. SQL de Leitura**.

Na inclusão dos campos Título e Descrição, é possível a utilização de parâmetros, que podem ser buscados da consulta SQL.

A inclusão de parâmetros se faz pelo uso de chaves “{}“, como no exemplo a seguir:

Se algum parâmetro for definido, o mesmo deverá ser configurado clicando no botão Parâmetros ao lado do respectivo campo.

Uma vez informado os parâmetros e as informações desejadas nos campos da Fonte RSS, clicar no botão Salvar.

Após Salvar, será habilitado o botão de Selecionar, do campo Identificador Único. Esse campo é responsável por definir qual a informação que o RSS checará quando houver modificação na Consulta SQL.

Selecionaremos nesse nosso exemplo, os dois campos CHAPA, SALARIO.

**OBS:** No final do processo, se os *Feeds* não estiverem retornando, deve-se alterar os campos selecionados para o Identificador Único

Após fazer isso, salvar novamente a Fonte e também o Canal RSS. Logo o mesmo já poderá ser assinado.

Clicando em Meus Canais, serão listados todos os canais que o usuário Logado tem permissão.

A coluna Assinado, mostra os canais que já foram assinados e os que ainda podem ser assinados.

Ao clicar duas vezes na imagem da coluna Assinado, o usuário poderá assinar o canal.

Nesse processo, podem ser marcadas a opções:

**-** **Enviar email**: Dispara um EMAIL com o *Feed* RSS para o usuário em questão.

**-** **Sincronizar canal automaticamente:** Sempre que houver atualização, o *feed* será recebido sem a intervenção do usuário.

**- Adicionar aos Favoritos:** Adicionar o Canal RSS ao Menu dos “Meus Canais”.

Após assinado o Canal RSS, será disponibilizado o Leitor RSS para acompanhamento dos *Feeds*.

Lembrando que os Canais RSS são passíveis de inclusão no Outlook ou no Navegar da Internet.

Devido a consulta SQL ter sido criada sem um parâmetro WHERE adequado, esse *Feed* irá retornar na sua primeira verificação, todos os funcionários do sistema. Depois disso, somente os funcionários que tiverem o salário alterado ou novos funcionários serão retornados no*Feed.*

**Informações Adicionais**

**1.** **Problemas para Autenticar usuário quando Adicionamos um novo RSS**

**Primeiramente** devemos verificar o arquivo WEB.Config

Procure pelo nome “**ServiceAlias**” , nesta clausula deve estar apontado**value="XXXXX" />**

onde XXXX é o nome do Alias configurado no **Alias. dat** para acesso a base que se deseja.

**Segundo**

Acesse o Menu INICIAR do Windows , acesse “Ferramentas Administrativas \ Gerenciador do Serviços de Informações da Internet (IIS)”

Acesse “Sites\Default Web Site” clique e “Autenticação”

As autenticações devem ficar da seguinte maneira

Obs: Em alguns servidores pode haver menos ou mais serviços

**Terceiro**

Verifique o Site “CorporeRM” . clique em autenticação

As autenticações do site devem ficar da seguinte maneira

Obs: Em alguns servidores pode haver menos ou mais serviços

Em seguida resete o seu IIS (pelo menu ou pelo comando iisreset.exe)

No caso do sistema Operacional ser o Windows XP, deve-se desmarcar o opção Autenticação do Windows Integrada.

Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.CanaisRSS.aspx).

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
