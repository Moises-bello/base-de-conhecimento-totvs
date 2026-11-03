---
article_id: 40662846747671
category: Materiais - Compras (SIGACOM)
content_hash: db0b57d5ce5e12315335de2c1da3cf3ae7f4d4579088af8450de1ab639815d9a
fetched_at: '2026-06-28T22:41:11.697909+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Opção Imprimir
  na rotina do Pedido de Compras.
type: support-article
updated_at: '2026-05-22T13:39:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40662846747671-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Op%C3%A7%C3%A3o-Imprimir-na-rotina-do-Pedido-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40663586275735) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Como saber qual relatório está sendo impresso na opção Imprimir na rotina Pedido de Compras ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigacom - módulo compras - Todas as versões  
  
**Solução**

Para efetuar a impressão do pedido de compras de forma nativa a partir da tela de gerenciamento da rotina, o sistema utiliza o relatório cadastrado para essa finalidade, verificando o parâmetro [**MV\_PCOMPRA**](https://tdn.totvs.com/pages/viewpage.action?pageId=235316809). A ação é executada através do menu de Outras Ações no Browser da rotina pedido de compras.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40662846726423)

Utilizando essa opção o pedido que será impresso é o posicionado no browser. Por padrão é impresso o relatório MATR110, porém há clientes que customizam esse relatório para adequação ao seu processo interno de compras. Logo, se ao verificar que no MV\_PCOMPRA há alguma informação diferente de MATR110, é necessário acionar a sua equipe de TI interna, caso haja algum problema com o relatório, pois trata-se de um relatório customizado, logo o suporte padrão do sistema, não prestará suporte a situação.

**Conforme comunicado oficial da TOTVS** [**Descontinuação dos relatórios MATR´s**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21731391477655-Descontinua%C3%A7%C3%A3o-de-Relat%C3%B3rios-Backoffice-Linha-Protheus)

Os relatórios MATR´s padrão do Protheus, foram descontinuados, sendo necessário utilizar o SmartView para consultas e extração de informações a partir de 31/10/2024.

Os clientes ainda podem continuar utilizando essas rotinas, porém não haverá mais suporte técnico, correções ou atualizações relacionadas a elas. A recomendação é migrar para o SmartView, que oferece maiores possibilidades de personalização.   
  
No **SmartView**, é possível:  
• Duplicar relatórios padrões e editar conforme sua necessidade;           
• Criar novos filtros, adicionar ou remover colunas;           
• Personalizar expressões e regras de negócio;           
• Atender demandas como filtro por datas, campos adicionais, parametrizações específicas e outros ajustes solicitados.  
       
Dessa forma, as necessidades apresentadas por você, talvez podem ser implementadas diretamente via SmartView, apenas utilizando os recursos de edição do próprio gerador de relatórios.  
  
Abaixo estão nossas documentações sobre o smartview caso não tenha configurado em seu ambiente.  
[Smart View no Protheus](https://tdn.totvs.com/display/public/framework/Smart+View+no+Protheus)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o SmartView ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21746957789463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-SmartView)

**Obs:**Dúvidas na configuração do smartview , por gentileza acionar a equipe Protheus Framework.

Segue o link com todos relatórios smartview do módulo de compras [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais são os Relatórios Smartview padrões do Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32301557840023-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-s%C3%A3o-os-Relat%C3%B3rios-Smartview-padr%C3%B5es-do-Compras)

Para utilização do parâmetro **MV\_PCOMPRA** com **Smartview** é necessário preencha no parâmetro **COMSV009**

e que esteja aplicado o últomo Backofficce do portal do cliente,segue link: [Expedição Continua - Backoffice Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160)

***Saiba Mais:***

[25062489 DMANMAT02-54525 DT MATA120 | Pedido de Compra "Outras Ações -> Imprimir" não executa novo relatório do Smart View COMSV009.](https://tdn.totvs.com/pages/releaseview.action?pageId=1015571910)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais são os Relatórios Smartview padrões do Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32301557840023-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-s%C3%A3o-os-Relat%C3%B3rios-Smartview-padr%C3%B5es-do-Compras)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como adicionar campos nos relatórios do Smartview do módulo de compras? Exemplo Relatório Relação de Solicitação compras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37707378170135-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-adicionar-campos-nos-relat%C3%B3rios-do-Smartview-do-m%C3%B3dulo-de-compras-Exemplo-Relat%C3%B3rio-Rela%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%A3o-compras)

[Smart View - Compras](https://tdn.totvs.com/x/x_b0L)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
