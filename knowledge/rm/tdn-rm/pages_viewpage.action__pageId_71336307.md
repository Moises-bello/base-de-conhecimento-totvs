---
content_hash: 6f99995b9081d65c851103029c1faa20a10271a50fa1ded3bdfac1cb481f5b40
fetched_at: '2026-06-29T00:11:25.595893+00:00'
page_id: '71336307'
product: rm
source: tdn-rm
title: NFS-e - Criação de Projeto na nova MDI - Tags CodigoObra e ART
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=71336307
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NFS-e                        **Versão:***apartir 11.40* |
| **Processo** | **:** | Criação de Projeto na nova MDI - Tags CodigoObra e ART |
| **Subprocesso** | **:** | Criação de Projeto na nova MDI - Tags CodigoObra e ART |
| **Data da publicação** | **:** | 22/07/2013 |

**Introdução:**

A criação de um projeto só é possível através da utilização dos aplicativos Solum e LIBER, no entanto se viu necessário a criação de projetos quando não possuir tais aplicativos. Este passo a passo irá auxiliar na criação de projeto utilizando à nova MDI.

**IMPORTANTE:**É necessário possuir um usuário supervisor no Solum.

**Utilização da NOVA MDI:**

Realize o seguinte procedimento: C: | totvs | CorporeRM | RM.Net | de um duplo clique sobre o aplicativo RM.exe. Feito isso irá aparecer a seguinte tela de login: 

**Login:**

Nesta tela informe o usuário e senha utilizados para “LOGAR” no sistema clique em ACESSAR. Após “LOGAR” realize o seguinte procedimento:

Criar projeto:

Vá em: TOTVS – Linha RM | Projetos | Construção e Projetos.

Feito isso vá em: Selecionar Projeto | Clique em incluir. 

Na tela do novo projeto informe o código da obra no campo CNPJ. Segundo o manual de integração do contribuinte quando informado dados de construção civil torna se obrigatório o CODIGO DA OBRA Juntamente com o código ART. Ao informar os campos clique em salvar.

Após criar o projeto será necessário associa-lo ao movimento para que as informações sejam levadas para o XML. Para isso basta realizar o seguinte procedimento:

No RM Nucleus vá em: Opções | Parâmetros | RMNucleus | localize o movimento utilizado para envio de NFS-e e de um duplo clique sobre o mesmo. Na aba projeto defina como será tratado o Projeto, onde o mesmo poderá ser obrigatório ou opcional, por movimento ou por item. Após definir a utilização avance ate a ultima etapa e salve.

Agora basta somente informar o projeto no movimento, vá em: Projeto  | Dados de Projeto | informe o projeto desejado.

**Regras de validação das TAGs código obra e ART:**

1.0 - Se houver CNPJ do projeto com CEI válido nos Itens e o CNPJ do projeto é igual em todos os itens, adotar o CNPJ e ART do projeto no XML da NFS-e nas tags código obra e ART.

2.0 - Se haver CNPJ do projeto com CEI válido no cabeçalho do movimento, adotar o CNPJ e ART do projeto no XML da NFS-e nas tags código obra e ART.

3.0 - Se haver CNPJ do projeto com CEI válido na filial vinculada ao movimento, adotar o CNPJ da filial e ART do projeto vinculado ao movimento no XML da NFS-e nas tags código obra e ART.

**IMPORTANTE:**

A partir do dia 15/08/2012 a prefeitura do Rio de Janeiro passou a fazer a seguinte validação: 

Para alguns códigos de serviços, relativos a serviços de construção civil, engenharia e congêneres, o Sistema da Nota Carioca, está exigindo, a partir de 15/08/2012, que o contribuinte informe a matrícula CEI da obra a que se refere o serviço.  
   
 Quando a obra, excepcionalmente, não tem obrigação de ter matrícula CEI, o contribuinte deve usar o Código da Obra com os caracteres "CO" na frente.  
   
 Mas há alguns códigos de serviço que fazem o sistema exigir o código da obra e, em certos casos, podem ser prestados sem nenhuma associação a uma obra de construção civil.  
   
 Neste último caso, o contribuinte deverá preencher o campo Código de Obra com as iniciais "COI" (de Código de Obra - Inexistente).

Onde tais validações passaram a ser tratadas com as seguintes regras (somente NFS-e do Rio de Janeiro):

É necessário utilizar as seguintes bibliotecas ou superior:

Biblioteca 11.20.50.132

Biblioteca 11.40.60.118

Biblioteca 11.50.30.116

Regras:

4.0 - Se houver CNPJ do projeto com CEI inválido nos Itens e o CNPJ do projeto igual em todos os itens, adotar "CO" concatenado com o código do projeto juntamente com o ART no XML da NFS-e nas tags código obra e ART.

4.1 - Se houver CNPJ do projeto com CEI inválido no cabeçalho do movimento, adotar "CO" concatenado com o código do projeto juntamente com o ART no XML da NFS-e nas tags código obra e ART.

4.2 - Se o código do projeto é igual a "COI" então este será o código da obra e o ART será o mesmo que está vinculado ao projeto obrigatoriamente.

5.0 - Caso não houver projeto vinculado ao movimento as tags código da obra e ART não serão descritas no xml da NFS-e.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
