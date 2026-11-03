---
article_id: 15907132123799
category: Manutenção de Ativos (SIGAMNT)
content_hash: 114fbc4ec3c796e0feb1a0215a72eaeea87174bb8f13fa28b96305ecfe2d9e52
fetched_at: '2026-06-28T22:42:33.087034+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Criação do novo filtro para Ordens de Serviço
  no Retorno Modelo 2 - MNTA435
type: support-article
updated_at: '2023-12-11T20:18:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15907132123799-Manufatura-Linha-Protheus-MNT-Cria%C3%A7%C3%A3o-do-novo-filtro-para-Ordens-de-Servi%C3%A7o-no-Retorno-Modelo-2-MNTA435
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15907172551319) Tempo aproximado para leitura: **00:02:05 min** **Dúvida**Como utiliza-se a opção de filtro no *browse* de busca das **Ordens de Serviço - O.S** na **rotina Retorno Modelo 2 - MNTA435**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**  
Ao acessar a rotina, a tela inicial apresentada será a seguinte:

![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15907186873111)

Para realizar a busca de todas as ordens de Serviço em aberto, basta utilizar o botão de **Lupa**, destacado na imagem acima. Após a busca, podem ser realizados diversos filtros pela opção **Filtrar**, no canto direito da tela:

![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15907163939095)

Os filtros criados podem ser salvos, assim, toda vez que a rotina for acessada e for realizada a primeira busca, ela já será realizada com os filtros que forem salvos, similar ao comportamento dos outros filtros de outras rotinas do **Protheus**. Para utilizar um filtro de forma fixa, basta utilizar a opção **Salvar**, conforme indicado abaixo:

![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15907177917463)

**Importante**Caso não haja nenhuma **OS** para o filtro criado, a busca irá informar que não existem registros para o filtro selecionado. Nesse caso, pode-se remover todos os filtros ou criar um novo, e então realizar nova busca.  
Neste processo de implementação do filtro no **MNTA435**, também foram realizadas as alterações abaixo:

* Remoção do [P.E. MNTA4006](https://tdn.totvs.com/pages/viewpage.action?pageId=636957776), pois não será mais utilizado;
* Adicionado novo [P.E. MNTA435Q](https://tdn.totvs.com/pages/viewpage.action?pageId=715833364) em substituição ao [P.E. MNTA435H](https://tdn.totvs.com/pages/viewpage.action?pageId=515287318), que não será mais utilizado;
* Remoção do [P.E. MNTA435H](https://tdn.totvs.com/pages/viewpage.action?pageId=515287318), pois não será mais utilizado, sendo substituído pelo [P.E. MNTA435Q](https://tdn.totvs.com/pages/viewpage.action?pageId=715833364).
* Adicionada nova opção na rotina: **Pesquisar Todas as Ordens de Serviço**, que tem como objetivo apresentar todas as **OS** liberadas disponíveis;
* Alterado comportamento no [P.E. MNTA4355](https://tdn.totvs.com/pages/viewpage.action?pageId=528470605);

**Saiba mais**Para acesso completo a documentação acesse: [DNG-18873 DT Criação de novo filtro para as Ordens de Serviço no Retorno Modelo 2](https://tdn.totvs.com/pages/releaseview.action?pageId=723294361)
