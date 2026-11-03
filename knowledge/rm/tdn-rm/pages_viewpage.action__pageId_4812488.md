---
content_hash: 927844c96fa47d9975972ad5ea0802e739d36ad5240f885e6a2e683a529c41f1
fetched_at: '2026-06-29T00:10:18.527393+00:00'
page_id: '4812488'
product: rm
source: tdn-rm
title: Aprovação de Batidas - RSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812488
version: 6
---

BLOCK

Aprovação de Batidas - RSS

FAQ: **Aprovação de Batidas - RSS**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.0 |

Avaliação

Esse documento tem como objetivo auxiliar na criação de um RSS que demonstra as batidas pendentes da aprovação do gestor.

O RSS Aprovação de batidas poupa tempo, pois a cada atualização realizada no RM Portal referente a batidas, o assinante do Canal RSS receberá uma notificação, bastando apenas clicar no link encaminhado para acessar a página e proceder com a aprovação.

Causa

**Saiba como configurar um RSS e obter uma poderosa ferramenta de gestão**

Para inicializar um RSS, antes de tudo, deve-se possuir uma ou várias consultas SQL na base. A SQL deve contemplar informações relevantes para o retorno correto do *Feed*. Deve conter campos na cláusula SELECT e WHERE que servem como parâmetros, “campos chave” na criação do Canal RSS. Ou seja, quando a SQL apresentar alteração na quantidade (número de linhas) ou no conteúdo o RSS será disparado.

É importante lembrar que essas consultas SQL devem conter informações relevantes a quem quiser assinar o canal.

Pelo fato de uma SQL poder ser “filtrada” através de parâmetros, use bastante os parâmetros para trabalhar com os *Feeds*, principalmente aqueles que envolvam Coligada, Usuário e Datas, que são valores padrão (será explicado no item Parâmetros) do RSS. Dessa forma é possível ter uma informação mais enxuta para cada usuário.

Solução

1) Antes de configurar o RSS, é preciso definir nos parâmetros globais, os quais podem ser acessados através do menu “Ambiente” de qualquer aplicativo da solução, a URL de acesso ao RM Portal:

[![clip_image002](http://lh6.ggpht.com/_G7KXZLoZDsY/TMbVcNNPfHI/AAAAAAAACR8/JuupGMtD3bM/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVbdj0e1I/AAAAAAAACR4/cCuD2mBG1hY/s1600-h/clip_image002%5B6%5D.jpg)

[![clip_image004](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVdA0hNpI/AAAAAAAACSE/JAL7PDvxnB4/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVcaEjpEI/AAAAAAAACSA/QHG7EiapTmY/s1600-h/clip_image004%5B8%5D.jpg)

2) Para criar uma consulta SQL, acesse o menu "Gestão" de qualquer aplicativo da solução:

*[![clip_image006](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVeSLUiSI/AAAAAAAACSM/twf9-K9pBhE/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVd9UecSI/AAAAAAAACSI/v-iRo0fGq64/s1600-h/clip_image006%5B6%5D.jpg)*

3) Crie a consulta abaixo:

**Para Base SQL**

> **Código : RSS.PTO.002 Título : Batidas a serem aprovadas**
>
> **SELECT** ABATFUN.CHAPA, ABATFUN.DATA,PPESSOA.NOME,
>
> ( **SELECT** PP.NOME
>
> **FROM** PSUBSTCHEFE, PFUNC, PPESSOA PP
>
> **WHERE** PSUBSTCHEFE.CHAPASUBST = PFUNC.CHAPA
>
> **AND** PFUNC.CODPESSOA = PP.CODIGO
>
> **AND** PP.CODUSUARIO = :CODUSUARIO
>
> **AND** **SUBSTRING**(PFUNC.CODSECAO, 1, **LEN**(PSUBSTCHEFE.CODSECAO)) = PSUBSTCHEFE.CODSECAO
>
> ) CHEFE
>
> **FROM** ABATFUN **INNER** **JOIN** PFUNC **ON** (ABATFUN.CHAPA = PFUNC.CHAPA)
>
> **INNER** **JOIN** PPESSOA
>
> **INNER** **JOIN** GUSUARIO **ON** PPESSOA.CODUSUARIO = GUSUARIO.CODUSUARIO
>
> **ON** (PPESSOA.CODIGO = PFUNC.CODPESSOA)
>
> **INNER** **JOIN** APARAM **ON** (APARAM.CODCOLIGADA = ABATFUN.CODCOLIGADA)
>
> **WHERE** ABATFUN.STATUS <> 'C' **AND** ABATFUN.STATUS <> 'D' **AND**
>
> ABATFUN.DATA>= APARAM.INICIOPERMES **AND** ABATFUN.DATA <= APARAM.FIMPERMES
>
> **AND EXISTS** ( **SELECT** PSUBSTCHEFE.CODSECAO
>
> **FROM** PSUBSTCHEFE, PFUNC, PPESSOA PP
>
> **WHERE** PSUBSTCHEFE.CHAPASUBST = PFUNC.CHAPA
>
> **AND** PFUNC.CODPESSOA = PP.CODIGO
>
> **AND** PP.CODUSUARIO = :CODUSUARIO
>
> **AND** **SUBSTRING** (PFUNC.CODSECAO, 1, **LEN**(PSUBSTCHEFE.CODSECAO)) = PSUBSTCHEFE.CODSECAO)

**Para Base Oracle :**

> **SELECT** ABATFUN.CHAPA, ABATFUN.DATA,PPESSOA.NOME,
>
> ( **SELECT** PP.NOME
>
> **FROM** PSUBSTCHEFE, PFUNC, PPESSOA PP
>
> **WHERE** PSUBSTCHEFE.CHAPASUBST = PFUNC.CHAPA
>
> **AND** PFUNC.CODPESSOA = PP.CODIGO
>
> **AND** PP.CODUSUARIO = :CODUSUARIO
>
> **AND** **SUBSTR**(PFUNC.CODSECAO, 1, **LENGTH**(PSUBSTCHEFE.CODSECAO)) = PSUBSTCHEFE.CODSECAO
>
> ) CHEFE
>
> **FROM** ABATFUN **INNER** **JOIN** PFUNC **ON** (ABATFUN.CHAPA = PFUNC.CHAPA)
>
> **INNER** **JOIN** PPESSOA
>
> **INNER** **JOIN** GUSUARIO **ON** PPESSOA.CODUSUARIO = GUSUARIO.CODUSUARIO
>
> **ON** (PPESSOA.CODIGO = PFUNC.CODPESSOA)
>
> **INNER** **JOIN** APARAM **ON** (APARAM.CODCOLIGADA = ABATFUN.CODCOLIGADA)
>
> **WHERE** ABATFUN.STATUS <> 'C' **AND** ABATFUN.STATUS <> 'D' **AND**
>
> ABATFUN.DATA>= APARAM.INICIOPERMES **AND** ABATFUN.DATA <= APARAM.FIMPERMES
>
> **AND EXISTS** ( **SELECT** PSUBSTCHEFE.CODSECAO
>
> **FROM** PSUBSTCHEFE, PFUNC, PPESSOA PP
>
> **WHERE** PSUBSTCHEFE.CHAPASUBST = PFUNC.CHAPA
>
> **AND** PFUNC.CODPESSOA = PP.CODIGO
>
> **AND** PP.CODUSUARIO = :CODUSUARIO
>
> **AND** **SUBSTR** (PFUNC.CODSECAO, 1, **LENGTH**(PSUBSTCHEFE.CODSECAO)) = PSUBSTCHEFE.CODSECAO)

Ainda no menu “Gestão”, clique em “Canais RSS”:

[![clip_image008](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVfIBUihI/AAAAAAAACSU/5Fuxedg2Auw/clip_image008_thumb%5B1%5D.jpg?imgmax=800 "clip_image008")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVe11B-AI/AAAAAAAACSQ/y0vvWUeavts/s1600-h/clip_image008%5B4%5D.jpg)

4) Na janela de Canal RSS clique no ícone [![clip_image010](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVgMF1xFI/AAAAAAAACSc/9jJDLt_Zm_A/clip_image010_thumb%5B1%5D.jpg?imgmax=800 "clip_image010")](http://lh5.ggpht.com/_G7KXZLoZDsY/TMbVfmQcDzI/AAAAAAAACSY/0auo6bLfsHo/s1600-h/clip_image010%5B4%5D.jpg) (Incluir). Feito isso, será aberta a tela de inclusão do canal. Conheça seus campos e como preenchê-los conforme RSS proposto por este documento:

***Aba “Identificação”:***

[![clip_image012](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVhaVDsTI/AAAAAAAACSk/v5173fScMj8/clip_image012_thumb%5B1%5D.jpg?imgmax=800 "clip_image012")](http://lh5.ggpht.com/_G7KXZLoZDsY/TMbVg6OH0DI/AAAAAAAACSg/AP-Ly6e_09k/s1600-h/clip_image012%5B6%5D.jpg)

**Disponível para todas as Coligadas:** marcando esta caixa de seleção o canal será exibido como opção de RSS para todas as coligadas presentes nos produtos RM.

**Titulo:** Preenchimento obrigatório. É exibido no início do canal, coloque um nome de fácil identificação do canal.

**Descrição:** Preenchimento obrigatório. É exibido logo após o título do canal. Coloque uma breve descrição sobre o canal RSS.

**Imagem:** Campo opcional. Ao escolher uma imagem essa será exibida em forma de link para o campo URL.

**URL:** Campo opcional. Ao inserir um endereço de um site, o mesmo será o link da imagem, caso seja inserida.

***Aba “Permissões”:***

[![clip_image014](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbViI5gy1I/AAAAAAAACSs/MoGH_JQnrGw/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh5.ggpht.com/_G7KXZLoZDsY/TMbVh41ftBI/AAAAAAAACSo/CqLBJvuTPvQ/s1600-h/clip_image014%5B4%5D.jpg)

A permissão a um canal RSS é dada a um ou mais perfis, os quais devem ser criados com antecedência no produto. Este perfil deve ser associado ao Canal, para isso, basta selecionar o perfil na tela de visualização de perfis e clicar em OK.

***Aba “Fontes”:***

[![clip_image016](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVjJ50DfI/AAAAAAAACS0/OozvT3QFHYQ/clip_image016_thumb%5B1%5D.jpg?imgmax=800 "clip_image016")](http://lh5.ggpht.com/_G7KXZLoZDsY/TMbVi42jbAI/AAAAAAAACSw/0aZjYrn47W8/s1600-h/clip_image016%5B4%5D.jpg)

**Consulta SQL do Alerta:** Campo obrigatório. Essa consulta é a parte principal do Canal, ela comanda o disparo do RSS. Com base na variação do seu conteúdo, na variação de linhas ou diferenças de valores, a SQL retorna os números de *Feeds* a serem enviados para o usuário. Ou seja, funciona como uma *trigger* no banco de dados, quando um evento é detectado no banco este dispara uma ação programada pelo usuário.

**Identificador Único:** Um conjunto de campos da Consulta SQL do Alerta que diferencia um *Feed* de outro, como a “chave primária” da Fonte RSS. Isso torna cada *Feed* único. Ficará disponível após a salvar a Fonte. Por exemplo, considere a consulta SQL abaixo:

SELECT PFunc.Nome, PFunc.Salario FROM PFunc

Se no campo “Identificador Único” selecionarmos “PFunc.Nome” e “PFunc.Salario”, sempre que um dos campos sofrer um INSERT ou um UPDATE, será disparado o RSS. Se selecionarmos somente o campo “PFunc.Salario”, quando este campo sofrer um INSERT ou um UPDATE é que será disparado o RSS.

**Título:** Campo obrigatório. Descreva uma identificação sobre o *Feed* e/ou informações que retornam da SQL de leitura. (*Consulte o item Passagem de Parâmetro)*

**Descrição:** Campo obrigatório. Deverá inserir informações sobre o *Feed* e/ou informações que retornam da SQL de leitura. *(Consulte o item Passagem de Parâmetro)*

**SQL/URL do Tipo de Leitura:** Deve-se escolher entre uma SQL ou uma URL para a leitura do *Feed*. A fonte de leitura deve ter conteúdo referente ou detalhamento das informações da SQL do alerta.

**Para demonstrar as batidas a serem aprovadas, use a URL que direciona para a página de aprovação. Exemplo****:**

*http://localhost/Corpore1100/Main.aspx?ActionID=PtoABatFunActionWeb&SelectedMenuIDKey=AprovarBatidas*

**Passagem de Parâmetros:** Em alguns pontos do configurador, encontramos o botão “Parâmetros”. Este indica que aquele determinado recurso pode ser usado com passagem de parâmetros.

[![clip_image018](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVkFZ08_I/AAAAAAAACS8/x7mw2rdkq2E/clip_image018_thumb%5B1%5D.jpg?imgmax=800 "clip_image018")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVj4JFk5I/AAAAAAAACS4/qBkMOTDK8kw/s1600-h/clip_image018%5B4%5D.jpg)

Um parâmetro também pode ser identificado através de chaves “{}”, dentro destas chaves, devemos colocar números sequenciais. O conjunto de chaves e números sequenciais identifica um parâmetro. Conforme exemplo da tela abaixo:

[![clip_image020](http://lh6.ggpht.com/_G7KXZLoZDsY/TMbVlGtzkvI/AAAAAAAACTE/LFzOGZcxPXI/clip_image020_thumb%5B1%5D.jpg?imgmax=800 "clip_image020")](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVktSP4yI/AAAAAAAACTA/gxEtg6Thzsw/s1600-h/clip_image020%5B4%5D.jpg)

**Valores Defaults dos Parâmetros:** O RM Portal permite escolher alguns valores defaults na passagem de parâmetros, esses valores são:

Ø **Valor Fixo** – Permite que seja passado um valor fixo em todas as vezes que for solicitada a Leitura do RSS. Válido somente para consultas SQL.

Ø **Usuário RSS** – Usuário que está logado ou irá logar no RM Portal.

Ø **Última Coligada do Usuário RSS** – Última coligada que o usuário do RSS acessou.

Ø **Data da leitura** – A data da última leitura de algum RSS feita pelo usuário.

5) Para publicar o canal, vá à edição deste, copie a URL a ser enviada aos assinantes que tenham interesse, em seguida acesse “Processos / Publicar Canals RSS”.

[![clip_image022](http://lh6.ggpht.com/_G7KXZLoZDsY/TMbVl6kM_UI/AAAAAAAACTM/chUqwnoqMKI/clip_image022_thumb%5B1%5D.jpg?imgmax=800 "clip_image022")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVlpf2xTI/AAAAAAAACTI/QZpkMVC5k5U/s1600-h/clip_image022%5B4%5D.jpg)

[![clip_image024](http://lh6.ggpht.com/_G7KXZLoZDsY/TMbVnI33yxI/AAAAAAAACTU/7WIUpAst980/clip_image024_thumb%5B1%5D.jpg?imgmax=800 "clip_image024")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVmdhvKSI/AAAAAAAACTQ/QH09I0NLrUA/s1600-h/clip_image024%5B4%5D.jpg)

6) Através da tela de publicação do Canal RSS são configurados: assunto e texto do e-mail, o qual será usado para convidar os usuários associados ao perfil cadastrado no Canal RSS para participar do mesmo.

[![clip_image026](http://lh5.ggpht.com/_G7KXZLoZDsY/TMbVn_i72WI/AAAAAAAACTc/MBYcLnUTa4U/clip_image026_thumb%5B1%5D.jpg?imgmax=800 "clip_image026")](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVnRkAm7I/AAAAAAAACTY/ELVLAa92oKc/s1600-h/clip_image026%5B4%5D.jpg)  
Para facilitar o uso dessa rotina foram incluídos 2 marcadores:

**1.** **[TITULOCANAL]** – deve ser substituído pelo título do Canal, que está na tela de cadastro do Canal RSS.

**2.** **[URLCANAL]** – Será substituído pela URL para assinar o Canal.

Após alterar o assunto e o corpo do e-mail, se necessário, clique em “Executar” para envio do convite.

7) Assinando um **Canal RSS** a partir de um **Leitor de RSS**:

8.1) O leitor de RSS pode ser acionado através do menu “Gestão” de qualquer aplicativo RM.

[![clip_image028](http://lh6.ggpht.com/_G7KXZLoZDsY/TMbVpFe_-SI/AAAAAAAACTk/D-hR7_SPbIo/clip_image028_thumb%5B1%5D.jpg?imgmax=800 "clip_image028")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVoRwL1-I/AAAAAAAACTg/euzTj9SWhw8/s1600-h/clip_image028%5B4%5D.jpg)

8.2) No Leitor RSS, clique em “Canais / Adicionar Canal”

[![clip_image030](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVps7-M_I/AAAAAAAACTs/lGjo5ddxPOc/clip_image030_thumb%5B1%5D.jpg?imgmax=800 "clip_image030")](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVpQnwvNI/AAAAAAAACTo/1JHtJwJpuxA/s1600-h/clip_image030%5B4%5D.jpg)

8.3) Copie a URL enviada por e-mail e insira no seu leitor de RSS, após preenchimento dos demais campos do leitor, clique em OK.

[![clip_image032](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVqtEL26I/AAAAAAAACT0/6CfzmdHAEg4/clip_image032_thumb%5B1%5D.jpg?imgmax=800 "clip_image032")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVqCrAU9I/AAAAAAAACTw/GBdv54vhGHI/s1600-h/clip_image032%5B4%5D.jpg)

[![clip_image034](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVrer3z_I/AAAAAAAACT8/CE6dz9GA1tM/clip_image034_thumb%5B1%5D.jpg?imgmax=800 "clip_image034")](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVq1YSs0I/AAAAAAAACT4/HVwexoD8cHo/s1600-h/clip_image034%5B4%5D.jpg)

8) Assinando um **Canal RSS no Firefox**:

9.1) Copie a URL enviada por e-mail, cole na barra de endereço do navegador e clique na tecla “Enter” do seu teclado**.** Será exibida uma tela para inserir o usuário e senha do RM Portal para acessar o Canal RSS. Após a inserção clique em OK.

[![clip_image036](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVsmo-qEI/AAAAAAAACUE/KshO-CrucxM/clip_image036_thumb%5B1%5D.jpg?imgmax=800 "clip_image036")](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVr0YqLzI/AAAAAAAACUA/MdfoECt4lNc/s1600-h/clip_image036%5B4%5D.jpg)

9) Assinando um **Canal RSS no Microsoft Outlook 2007**:

10.1) No Outlook, clique com o botão direito do mouse sobre “RSS Feeds”.

10.2) Selecione “Adicionar Novo RSS Feed...”

[![clip_image038](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVtlB6M1I/AAAAAAAACUM/FCH5Is2zyhg/clip_image038_thumb%5B1%5D.jpg?imgmax=800 "clip_image038")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVtDLsfwI/AAAAAAAACUI/nITYjIfF0hA/s1600-h/clip_image038%5B4%5D.jpg)

10.3) Na tela exibida inclua a URL do RSS, enviada por e-mail. Clique em “Adicionar”.

[![clip_image040](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVuSo4BNI/AAAAAAAACUU/Sw9Dk3b_5bI/clip_image040_thumb%5B1%5D.jpg?imgmax=800 "clip_image040")](http://lh5.ggpht.com/_G7KXZLoZDsY/TMbVt67j-SI/AAAAAAAACUQ/2TVw80POPaA/s1600-h/clip_image040%5B4%5D.jpg)

[![clip_image042](http://lh6.ggpht.com/_G7KXZLoZDsY/TMbVvXbGHMI/AAAAAAAACUc/p8XAMrLNZd8/clip_image042_thumb%5B2%5D.jpg?imgmax=800 "clip_image042")](http://lh3.ggpht.com/_G7KXZLoZDsY/TMbVu1P958I/AAAAAAAACUY/vtEelPPRXBs/s1600-h/clip_image042%5B5%5D.jpg)

10.4) Para assinar o RSS no Outlook 2007 deve-se inserir o usuário e senha do RM Portal, caso seja solicitado.

[![clip_image044](http://lh5.ggpht.com/_G7KXZLoZDsY/TMbVwStlb0I/AAAAAAAACUk/wbzimnemnj8/clip_image044_thumb%5B4%5D.jpg?imgmax=800 "clip_image044")](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbVv4R-YYI/AAAAAAAACUg/vsXuuNqa22s/s1600-h/clip_image044%5B7%5D.jpg)

Observações

|  |  |
| --- | --- |
|  | **Informações Adicionais**  No momento do registro do Canal RSS no leitor de RSS(Outlook, Firefox, etc.), deve-se informar qual usuário dos sistemas da linha RM está autorizado a registrar o canal.  Ao incluir/alterar/excluir uma **Fonte** é necessário salvar o **Canal** novamente para efetuar as alterações.  O uso do “NOLOCK” nas consultas SQL melhora o desempenho e seu uso é incentivado principalmente nas consultas de tabelas muito grandes. Este recurso é exclusivo para bases SQL Server.  Veja como usar o "NOLOCK" em uma consulta:  SELECT \* FROM NOME\_TABELA (NOLOCK); |
|  | **1.** **Problemas para Autenticar usuário quando Adicionamos um novo RSS**      [image](http://lh6.ggpht.com/_G7KXZLoZDsY/TMbVw6lEw8I/AAAAAAAACUo/zCjXgKbRAWY/s1600-h/image%5B6%5D.png)    **Primeiramente** devemos verificar o arquivo WEB.Config  Procure pelo nome “**ServiceAlias**” , nesta clausula deve estar apontado **value="XXXXX" />**  onde XXXX é o nome do Alias configurado no **Alias. dat** para acesso a base que se deseja.  **Segundo**  Acesse o Menu INICIAR do Windows , acesse “Ferramentas Administrativas \ Gerenciador do Serviços de Informações da Internet (IIS)”  Acesse “Sites\Default Web Site” clique e “Autenticação”    As autenticações devem ficar da seguinte maneira  Obs: Em alguns servidores pode haver menos ou mais serviços    **Terceiro**  Verifique o Site “CorporeRM” . Clique em autenticação    As autenticações do site devem ficar da seguinte maneira  Obs: Em alguns servidores pode haver menos ou mais serviços    Em seguida resete o seu IIS (pelo menu ou pelo comando iisreset.exe)  No caso do sistema Operacional ser o Windows XP, deve-se desmarcar a opção Autenticação do Windows Integrada.  **[clip_image011](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbV1n6_FnI/AAAAAAAACVQ/UEhtNuWfEmQ/s1600-h/clip_image011%5B4%5D.jpg)**      [clip_image013](http://lh4.ggpht.com/_G7KXZLoZDsY/TMbV2nLLVWI/AAAAAAAACVY/45VMbeB2nXc/s1600-h/clip_image013%5B4%5D.jpg) |
|  | **Quarto**    Caso após essas verificações o problema ainda continuar, verificar o arquivo **MADAM.DLL** dentro da pasta \CorporeRM\RM.NET e \CorporeRM\Corpore.NET\Bin e conferir se a versão dessa DLL está a mesma da BibliotecaRM. |
