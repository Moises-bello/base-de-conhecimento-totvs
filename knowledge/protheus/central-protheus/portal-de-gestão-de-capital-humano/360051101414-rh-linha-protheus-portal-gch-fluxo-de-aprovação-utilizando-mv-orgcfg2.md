---
article_id: 360051101414
category: Portal de Gestão de Capital Humano
content_hash: e856f5b3a3f12b88c287ea5c01d421418acc21251d685b6b8cece80a9cbb5799
fetched_at: '2026-06-28T22:43:00.071442+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Fluxo de aprovação utilizando MV_ORGCFG=2
type: support-article
updated_at: '2021-04-07T12:46:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051101414-RH-Linha-Protheus-PORTAL-GCH-Fluxo-de-aprova%C3%A7%C3%A3o-utilizando-MV-ORGCFG-2
---

**Dúvida**Como definir o fluxo de aprovação, no portal com o parâmetro MV\_ORGCFG=2?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Portal Gestão Capital Humano - Todas as versões  
  
**Solução**Neste exemplo usarei a solicitação de Desligamento, para desenhar o fluxo de aprovação no portal. Entendendo o conceito do sistema poderá ser aplicada para qualquer solicitação.  
  
Importante ressaltar que quando o conteúdo do parâmetro **MV\_ORGCFG =2**, deve ser apontado a **Filial** e **Matricula Responsável** no cadastro do **Departamento**, qualquer informação indevida em seu cadastro poderá comprometer a chave de busca, utilizada no fluxo de aprovação.  
  
Quando a empresa utiliza o conteúdo do parâmetro **MV\_ORGCFG= 2** , deverá ter conhecimento que  além do cadastro do **Departamento** no  módulo 07 (SIGAGPE), deve obrigatoriamente ter o cadastro da **Visão** no módulo 70 (SIGAORG), nesta visão deve ser incluídos  cada departamento utilizado nas aprovações, montando sua estrutura.  
  
Acesso o ambiente Configurador **(SIGACFG)**, no seguinte caminho: Atualizações > Cadastro > Parâmetros.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080741193/mceclip0.png)  
  
Localize e edite o parâmetro **MV\_ORGCFG = 2**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079661474/mceclip1.png)  
  
Feito isto é necessário realizar os cadastros de departamento, para isto acesse o Módulo 07 (SIGAGPE), no seguinte caminho: Atualizações > Cadastro > Departamento.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079661614/mceclip2.png)  
  
Este cadastro deve ser desenhado conforme a necessidade e regra da empresa, neste exemplo estarei cadastrando **5 departamentos**, para demonstrar **5 níveis de aprovação**. A empresa pode optar por trabalhar com mais ou menos níveis de aprovação.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080741613/mceclip3.png)  
  
Iremos utilizar em nossas simulações estes 5 departamentos. Apartir de agora  devemos começar a desenha sua estrutura de aprovação.  
  
**1° Nível de aprovação**: Para o departamento de código**"**000000003" - Descrição - "Primeiro nível de aprovação", estou apontando a Empresa , Filial e Matricula responsável.  
No meu caso ficou **Departamento  000000003** , Empresa R5, Filial Matriz - **Matricula Resp. 000010**.  
Ou seja qualquer funcionário que estiver alocado ao departamento e fizer uma solicitação, será direcionado a matricula responsável deste departamento.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079662214/mceclip4.png)  
  
Após salvar seu registro observe que alimentou o campo chave de busca.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080745293/mceclip5.png)  
  
**2° Nível de Aprovação**: Para o departamento de código "000000004" - Descrição - "Segundo nível de aprovação", estou apontando a Empresa , Filial e Matricula responsável.   
No meu caso ficou: **Departamento  000000004**, Empresa R5, Filial Matriz - **Matricula Resp. 000011.**Ou seja qualquer funcionário que estiver alocado ao departamento e fizer uma solicitação, será direcionado a matricula responsável deste departamento. Após salvar veja que alimenta o campo chave de busca.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080746233/mceclip7.png)  
  
**3° Nível de Aprovação**: Para o departamento de código "000000005" - Descrição - "Terceiro nível de aprovação", estou apontando a Empresa , Filial e Matricula responsável.   
No meu caso ficou:**Departamento  000000005**,  Empresa R5, Filial Matriz - **Matricula Resp. 000012.**Ou seja qualquer funcionário que estiver alocado ao departamento e fizer uma solicitação, será direcionado a matricula responsável deste departamento. Após salvar veja que alimenta o campo chave de busca.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079668634/mceclip8.png)  
  
**4° Nível de Aprovação**: Para o departamento de código "000000006" - Descrição - "Quarto nível de aprovação", estou apontando a Empresa , Filial e Matricula responsável.   
No meu caso ficou: **Departamento  000000006**,  Empresa R5, Filial Matriz - **Matricula Resp. 000013.**Ou seja qualquer funcionário que estiver alocado ao departamento e fizer uma solicitação, será direcionado a matricula responsável deste departamento. Após salvar veja que alimenta o campo chave de busca.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080746533/mceclip9.png)  
  
**5° Nível de Aprovação**: Para o departamento de código "000000007"- Descrição - "Terceiro nível de aprovação", estou apontando a Empresa , Filial e Matricula responsável.   
No meu caso ficou: **Departamento  000000007**,  Empresa R5, Filial Matriz - **Matricula  Resp 000014.**Ou seja qualquer funcionário que estiver alocado ao departamento e fizer uma solicitação, será direcionado a matricula responsável deste departamento. Após salvar veja que alimenta o campo chave de busca.  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079669394/mceclip10.png)  
  
Para dar continuidade ao processo, devemos cadastrar a visão e apontar estes departamentos, para isto acesso Módulo 70 (SIGAORG), no seguinte caminho: Atualizações > Estruturas > Visões > Incluir.  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079670554/mceclip11.png)  
  
Deverá adicionar uma descrição e incluir todos os departamentos relacionados em sua aprovação.  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079670674/mceclip12.png)  
  
Após inclusão é necessário **Montar a Estrutura da Visão**, posicione no cadastro da sua visão clique em Outras Ações > Estrutura.  
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080748213/mceclip13.png)  
  
Com o botão direito do Mouse clique sobre a descrição, Incluir > Item da lista, até montar sua estrutura.  
  
![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079676634/mceclip20.png)  
  
Desta forma foram incluídos os departamentos relacionados ao processo. Salve e anote o código da Visão.  
  
![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080755893/mceclip19.png)  
  
Devemos apontar o código desta visão no cadastro do **menu do portal** para a opção de solicitação desejada. Acesse o módulo 18 **(SIGATFC)**, no seguinte caminho: Atualizações > Configurações > Menu > Portal RH > Outras Ações > Menu > Posicione na opção desejada e clique em Editar.  
  
No meu exemplo estou usando a opção Desligamento, porém a empresa pode aplicar esta orientação para qualquer outra solicitação.  
  
Observe os campos em destaque, devo apontar qual visão esta relacionada e os níveis de aprovação.  
Importante sempre que os níveis de aprovação estiver com **"0 " "ZERO "** o sistema irá passar por todos os níveis de aprovação desenhado no meu exemplo 5 níveis. Porém caso a empresa decida que deve ter um nível menor de aprovação basta fixar esta informação no campo Níveis de Aprovação.  
  
![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080749053/mceclip16.png)  
  
A parte de configuração está realizada, lembre de avaliar a alocação de cada funcionário nos departamentos corretos, para não serem direcionado errados as solicitações. O sistema sempre terá como referencia o Cadastro do Funcionário , departamento de Alocação, e qualquer solicitação será direcionado a Matricula responsável do departamento de Alocação do Funcionário.

Acessando o portal para validar as aprovações.  
A Matricula 000010 , realiza uma solicitação de Desligamento  a um membro de sua equipe.

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079691054/mceclip21.png)  
  
Gerou corretamente para o Segundo nível aprovar.  
  
A matricula 000011 loga no portal para aprovar a solicitação de desligamento ao atender, direciona corretamente ao terceiro nível de aprovar.  
  
![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079691354/mceclip22.png)  
  
A matricula  000012 loga no portal , acessa a rotina de acompanhamento e aprova a solicitação de desligamento. Direcionando a aprovação para o quarto nível de aprovação.

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080770173/mceclip23.png)

![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080770273/mceclip24.png)  
  
A matricula 000014 loga no portal e aprova a solicitação de desligamento, direcionando assim para o Quinto e ultimo nível de aprovação.

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079691814/mceclip25.png)  
  
![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080770893/mceclip26.png)  
  
Por fim a matricula 000014 loga no portal e prova a solicitação de desligamento no portal e direciona ao Rh aprovar através da rotina TCFA040.

![mceclip27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080771433/mceclip27.png)  
  
![mceclip28.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079692954/mceclip28.png)

![mceclip29.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080771973/mceclip29.png)  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079699474/mceclip0.png)  
  
**Saiba Mais  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)**
