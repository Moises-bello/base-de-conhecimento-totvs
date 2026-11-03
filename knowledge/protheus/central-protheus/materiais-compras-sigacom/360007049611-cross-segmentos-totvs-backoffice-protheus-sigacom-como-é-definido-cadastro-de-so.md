---
article_id: 360007049611
category: Materiais - Compras (SIGACOM)
content_hash: 75a8b86dd623fa5bd57d93449545daee6b4adf287955832ef877d20b003e312a
fetched_at: '2026-06-28T22:41:07.625587+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido cadastro
  de Solicitantes ( MATA084 ) no Módulo de Compras ?
type: support-article
updated_at: '2026-06-19T17:17:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007049611-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-definido-cadastro-de-Solicitantes-MATA084-no-M%C3%B3dulo-de-Compras
---

**Dúvida**

Como é definido cadastro de Solicitantes ( MATA084 ) no Módulo de Compras ?

**Ambiente**

Microsiga Protheus a partir da versão 11  
  
  
**Solução**

No Cadastro de Solicitantes são definidos os direitos de solicitações de produtos ou grupos de produtos, para cada usuário ou para um grupo de usuários.  
Além disso, é possível determinar qual grupo de compras irá analisar a solicitação feita pelo usuário/grupo de usuários e dar continuidade no processo de Cotação/Pedido de Compras.

Vídeo Youtube com a Configuração do Cadastro de Solicitantes

How To| MP-SIGACOM Cadastro de Solicitantes #TOTVS Backoffice (linha Protheus) <https://www.youtube.com/watch?v=J7lsoKAEqtI>]

---

Processo Bloqueio simples de Solicitação de compras funciona da seguinte forma:

**Parâmetros: MV\_RESTSOL**=**S** e **MV\_APROVSC**=**T**. E também o **MV\_APRSCEC=F**

Vídeo Youtube com a Configuração de ***Bloqueio de Solicitação de Compras.***

How To| MP-SIGACOM Bloqueio de Solicitação de Compras #TOTVS; <https://www.youtube.com/watch?v=tKkrIX35f30>

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido o bloqueio simples da Solicitação de Compras ( MATA110 ) no Módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19804481955351-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-definido-o-bloqueio-simples-da-Solicita%C3%A7%C3%A3o-de-Compras-MATA110-no-M%C3%B3dulo-de-Compras)

Caso queira que TODAS as solicitações de compras incluídas sejam bloqueadas, deve-se apenas configurar os parâmetros (**MV\_RESTSOL**=**S,** **MV\_APROVSC**=**T e MV\_APRSCEC=F**), Produto com **B1\_SOLICIT(Restrição)=Não**, e **não cadastrar os Solicitantes.**  
Nesta situação TODAS as solicitações de compras entrarão bloqueadas.

Ao cadastrar um solicitante (no cadastro de solicitantes) com o grupo de materiais **008**:

* Se o solicitante incluir uma **SC** de produto do grupo de materiais **008**, a **SC** será incluída liberada;
* Se incluir uma **SC** de um produto diferente do grupo **008**, a **SC** é incluída bloqueada.
* Se incluir \* no Grupo de Produto do Solicitante, a SC será incluída liberada para todos os grupos de produtos.

**Obs:**

Para que as Solicitações caiam bloqueadas **sem o uso de Cadastro de Solicitantes** conforme descrito acima o parâmetro ***MV\_APROVSC*** deve estar habilitado (***T***) e o parâmetro ***MV\_APRSCEC*** desabilitado (***F***), o ***MV\_RESTSOL** = **S, MV\_CHKSOLI  = F*** e o campo ***Restrição (B1\_SOLICIT)*** do Cadastro de Produto = **Não**.

---

***Obs1:***

## **Parâmetros envolvidos no processo da rotina de Cadastro de Solicitante:**

Parâmetros: MV\_RESTSOL , MV\_APROVSC e MV\_CHKSOLI

Exemplo da rotina:

Para incluir um cadastro acesse Atualizações > Administração de Compras > Solicitante **(MATA084):**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18439548581271)

No cabeçalho o campo AI\_USER  sistema valida informações de cadastros de usuários para vincular.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40378751241495)

Para isso deve existir cadastro do Solicitante no Configurador >Usuário > Senhas > Usuários:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40378760027287)

Voltando à Tela da Rotina:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40449351407383)

Mais informações de cadastro através do link:

[PCOM09005 - Solicitantes (MATA084)](http://tdn.totvs.com/pages/releaseview.action?pageId=274630904)

***Obs2:***

Caso Digite "**\*"** nas entidades contábeis dos campos ***DBK\_CC, DBK\_CONTA, DBK\_ITEMCT, DBK\_CLVL*** em versões anteriores à versão 12.1.27 e seja gravado um valor nos campos ao invés do "**\*"** digitado será necessário realizar a migração de versão para versão 12.1.27 ou ajustar a validação desses campos conforme as informações da documentação a abaixo:

[5967493 DMANMAT02-19255 DT Asterisco no campo DBK\_CC](https://tdn.totvs.com/display/public/PROT/5967493+DMANMAT02-19255+DT+Asterisco+no+campo+DBK_CC)

No grid

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414211913111)

**Obs3:**

Para que haja restrição de inclusão de SC com bloqueio por centro de custo é necessário ativar os parâmetros:

MV\_RESTSOL - Controle de restrição de solicitante = S  
MV\_CHKSOLI - Indica controle de solicitantes= T  
MV\_RESTSCC - Indica entidade contábil no controle de solicitantes na SC = T   
MV\_RESTCOM - Bloqueia acesso a SC = S

Ao realizar esse processo , quando o usuário for incluir uma SC com centro de custo que não esteja no cadastro de Solicitante será apresentado o HELP

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409648915095)

**Importante:** O cadastro de solicitantes não faz o bloqueio de inclusão de solicitação de compras para outros usuários apenas restringe se o um usuário poderá alterar ou deletar uma SC já criada por outro usuário.

Para restringir a inclusão de Solicitação de Compras para determinado usuário deve ser feito via privilégios no Configurador:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40378760027671)

Crie uma regra para MATA110:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40378760028567)

Amarre a regra no usuário:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40378751243287)

​  
Desta forma, o usuário não conseguirá usar mais este botão:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40378760028951)

**Obs4:**

**Configuração de Gera Cotação x Solicitante x Grupo de Compras**

Para garantir que apenas usuários pertencentes ao Grupo de Compras vinculado ao cadastro de Solicitante possam realizar cotações, é necessário configurar a seguinte restrição:

1. Habilite o parâmetro **MV\_RESTCOM = S**
2. Incluir o comprador na Rotina de cadastro de compradores (**COMA087)**
3. Vincular o Comprador na Rotina de Grupo de Compras**(MATA086)**
4. Vincular o Grupo de compras no Cadastro do Solicitante**(MATA084)**

Dessa forma só poderá fazer cotações os usuários que tiverem dentro do Grupo de compras.

***Obs5:***

Para que **somente usuários cadastrados como Solicitante** possam Realizar a inclusão de Solicitação de Compras para determinado Produto, só será possível para produtos com "Restrição". Dessa forma, o parâmetro ***MV\_RESTSOL*** deve estar habilitado com seu conteúdo **S**  e no Cadastro de Produto o campo Restrição ***Restrição (B1\_SOLICIT)*** =**Sim.**

- Assim, se se tentar incluir uma Solicitação de Compras com um produto com o campo ***Restrição (B1\_SOLICIT)*** =**Sim** por um usuário que não seja Solicitante será apresentado o Help abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32906944172311)

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Restrição de Solicitantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11491127349911)

[PCOM09005 - Solicitantes (MATA084)](http://tdn.totvs.com/pages/releaseview.action?pageId=274630904)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido o bloqueio simples da Solicitação de Compras ( MATA110 ) no Módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19804481955351-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-definido-o-bloqueio-simples-da-Solicita%C3%A7%C3%A3o-de-Compras-MATA110-no-M%C3%B3dulo-de-Compras)

[PCOM06003 - Como funciona o bloqueio de solicitação de compras?](https://tdn.totvs.com.br/pages/releaseview.action?pageId=233754768)

[PCOM06006 - Cadastro de Solicitante e Solicitação de Compra](https://tdn.totvs.com.br/pages/releaseview.action?pageId=286735615)

[5967493 DMANMAT02-19255 DT Asterisco no campo DBK\_CC](https://tdn.totvs.com/display/public/PROT/5967493+DMANMAT02-19255+DT+Asterisco+no+campo+DBK_CC)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
