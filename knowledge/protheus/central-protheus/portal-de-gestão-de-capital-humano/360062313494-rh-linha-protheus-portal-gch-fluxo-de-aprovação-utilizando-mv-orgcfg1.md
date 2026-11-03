---
article_id: 360062313494
category: Portal de Gestão de Capital Humano
content_hash: 10c5366a1d988d9ea99a9830b6e7eebf0d5fea304d0829419cffcac29f6d1f24
fetched_at: '2026-06-28T22:42:58.994225+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Fluxo de aprovação utilizando MV_ORGCFG=1
type: support-article
updated_at: '2023-11-14T15:05:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062313494-RH-Linha-Protheus-PORTAL-GCH-Fluxo-de-aprova%C3%A7%C3%A3o-utilizando-MV-ORGCFG-1
---

**Dúvida**Como definir o fluxo de aprovação, no portal com o parâmetro **MV\_ORGCFG=1**  
  
**Ambiente**TOTVS RH (Linha Protheus) -  Portal Gestão Capital Humano - Todas as versões  
  
**Solução**Importante ter definido o cadastro de movimento de postos e ocupações. Caso tenha dúvidas em como realizar este procedimento consulte os artigos abaixo.  
[MP - ORG - Para que server a rotina Movimentos de Departamentos (ORGM010) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062311454)  
[MP - ORG - Para que server a rotina Movimentação de Postos (ORGA030) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003717761)  
  
Após essa definição é necessário montar a visão e estrutura.  
Para as Vagas geradas com controle de posto precisa ter o cadastro de **Visão** do tipo **comunicação**. Para maiores informações consulte:  
[MP - ORG - Para que serve a rotina de Visão (ORGA060) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003110702-MP-ORG-Para-que-serve-a-rotina-de-Vis%C3%A3o-ORGA060-e-como-incluir-)  
  
Realizado o cadastro da visão e carregado os departamentos relacionados a esta visão. Para realizar seu cadastro acesse Módulo 70 (**SIGAORG**) em:  
**1.** Atualizações > Estrutura > Visão.  
Preencha os dados conforme orientações de help de campo.  
Após o preenchimento, confira os dados e confirme.  
 **2.** Em Ações Relacionadas, selecione a opção Estrutura, posicionando previamente sobre a visão desejada. **3.** No *browse* de Visões, em **Ações Relacionadas,** estão disponíveis as opções:  
• Pesquisar  
• Carregar  
 **4.** Acione-as conforme necessidade, de acordo com as instruções do Help e *slave* o registro.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004806601)  
  
**5.** Defina a estrutura da visão. Nesta opção é possível estabelecer a ordem da estrutura, de acordo com os dados cadastrados na visão, definindo hierarquia para os departamentos/postos.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004086001)  
  
**6.** Posicione na tela e clique com o botão direito do mouse, posicione em **Incluir** e selecione a **sub-opção** desejada, sendo elas:  
  
**• Novo(s)** itens na Lista  
Ao selecionar esta opção o sistema abre o cadastro de visões, possibilitando a seleção do item desejado ou a inclusão de um novo item

• **Item da Lista**  
Esta opção apresenta uma janela listando os itens cadastrados em visões, sendo possível selecioná-los e adicioná-los a estrutura.

• **Todos os Itens da Lista**  
Esta opção adiciona a estrutura todos os itens do cadastro de visões.  
  
Selecione os item que deseja adicionar á estrutura, estabelecendo a hierarquia dos departamentos ou postos.  
  
 ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004020862)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004087841)  
  
**7.** Após configurar a estrutura confirme para finalizar.

**Dica**: Dando duplo clique no item da visão é possível visualizar qual matricula/ participante e está alocada em cada nível.  
  
Nível Superior![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004021342)

Nível inferior  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004664182)  
  
**8.**Após criação da visão deve ser vinculado o seu código nos menus conforme abaixo:  
  
Para Configuração de Menus do portal é necessário acesso ao **Módulo 18 - Terminal de consulta do Funcionário** e seguir nas opções **Atualizações > Configurações > Menus   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19056140960023)**Após abrir a raiz dos menus posicione no menu desejado e depois no botão **editar**no rodapé da tela.![](https://centraldeatendimento.totvs.com/hc/article_attachments/19056248027159)  
  
Uma premissa **extremamente importante** para utilização da Ferramenta de Busca Colaborador é que o menu de Solicitações > Pré-Abono esteja informado a sua rotina W\_PWSA160.APW e a visão possa estar informada no campo Visão de Aprovações, caso contrário o sistema não conseguirá encontrar os níveis de acordo com a estrutura hierarquia montada.  
  
Obs. Exemplo de funcionamento será apresentado no índice 02 - Exemplos de Utilização.![](https://centraldeatendimento.totvs.com/hc/article_attachments/19056295471767)  
  
Neste exemplo usarei a solicitação de Justificativa Pré-Abono, para desenhar o fluxo de aprovação no portal. Entendendo o conceito do sistema poderá ser aplicada para qualquer solicitação.  
  
Quando a matricula apontada como nível inferior acessar o portal e realizar qualquer solicitação, será direcionada ao superior para aprovação das solicitações, conforme exemplo.  
![phMvMweB29.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103281534)  
  
**Saiba Mais**  
[Artigo sobre Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)  
[Documentação oficial válida para portal GCH e MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=802014186)
