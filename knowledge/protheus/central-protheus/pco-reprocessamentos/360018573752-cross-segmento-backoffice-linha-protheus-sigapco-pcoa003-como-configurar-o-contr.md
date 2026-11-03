---
article_id: 360018573752
category: PCO - Reprocessamentos
content_hash: 2f5a3b77ada2ab3dbd55cae1f5927d6ac319c4c07797ccdf4ff269391c7e2f0c
fetched_at: '2026-06-28T22:37:06.957619+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: ' Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA003 Como configurar
  o controle de Fases Orçamentárias'
type: support-article
updated_at: '2023-11-21T14:02:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018573752--Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA003-Como-configurar-o-controle-de-Fases-Or%C3%A7ament%C3%A1rias
---

**Dúvida**Como configurar o controle de Fases Orçamentárias?  
  
**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
  
**Solução**

Para que seja possível obter o controle de fases da Planilha de Orçamentária, primeiramente deverá ativar o parâmetro **MV\_PCOEXFS** para "1".

Help do Parâmetro :

![](http://tdn.totvs.com/download/attachments/267800979/image2016-10-19%208%3A56%3A26.png?version=1&modificationDate=1476875170000&api=v2)

![](http://tdn.totvs.com/download/attachments/267800979/image2016-10-19%208%3A56%3A46.png?version=1&modificationDate=1476875171000&api=v2)

Após essa ativação se faz necessário configurar todas as permissões das fases e suas mensagens personalizadas, através da rotina PCOA003 ( Fase Orçamentária )

*Exemplo:*

![](http://tdn.totvs.com/download/attachments/267800979/image2016-10-19%208%3A57%3A14.png?version=1&modificationDate=1476875171000&api=v2)

Seleciono a Fase desejada, em seguida clico "Alterar" verifiquem que o campo Mensagem de Aviso é apresentado com um numeração, nesse caso se fa necessário personalizar o mesmo com uma mensagem desejada :

Exemplo : Planilha em Fase de Planejamento, no caso a mesma esteja em execução, poderá aplicar a mensagem Planilha em Execução altere a fase da planilha para edita-la.

Logo abaixo poderá personalizar cada ação dentro da fase desejada e através do campo Mensagem de Aviso, poderá aplicar o Help de Campo que necessitar.

![](http://tdn.totvs.com/download/attachments/267800979/image2016-10-19%208%3A58%3A0.png?version=1&modificationDate=1476875171000&api=v2)

Após efetuado essa configuração as alterações de Fases Orçamentárias da Planilha Entrarão em Vigor, podendo sofrer manutenções apenas pelo administrador ou conforme a configuração hierárquica desejada.

**Importante**

Caso essa configuração não seja efetuada não é possível obter o controle de lançamentos independente da fase que a planilha orçamentária se encontre.
