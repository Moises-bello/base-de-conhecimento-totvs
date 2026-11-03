---
article_id: 360018757451
category: PCO - Cadastros
content_hash: 6635e16c10fb675299eac6874693cb68ed00f4cc8dc2adb8ec8e5c5d766ebe2a
fetched_at: '2026-06-28T22:37:12.868324+00:00'
product: protheus
section_id: 1500001550802
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA010 - Utilização
  de plano de contas orçamentário sincronizado com o plano de contas contábil.
type: support-article
updated_at: '2023-11-21T12:51:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018757451-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA010-Utiliza%C3%A7%C3%A3o-de-plano-de-contas-or%C3%A7ament%C3%A1rio-sincronizado-com-o-plano-de-contas-cont%C3%A1bil
---

**Dúvida**Utilização de plano de contas orçamentário sincronizado com o plano de contas contábil.  
  
**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
  
**Solução**

O SIGAPCO permite que seja criado um plano de contas com estrutura própria, ou que seja realizado o sincronismo com o plano de contas contábil, simplificando o cadastro do plano de contas orçamentário.

Para que seja possível sincronizar o plano de contas orçamentário com o plano de contas contábil é necessário configurar o parâmetro MV\_PCOSINC, utilizando as seguintes opções:

1 - Será utilizado plano de contas orçamentário com estrutura própria, sem sincronismo com outros planos.

2 - Será utilizado o plano de contas orçamentário sincronizado com a estrutura do plano de contas contábil.

3 - Será utilizado o plano de contas orçamentário sincronizado com o plano de contas por centro de custo.

Habilitando o sincronismo entre os planos de conta a rotina PCOA010 realizará  uma carga inicial na tabela de contas orçamentárias (AK5) com os dados das contas do módulo SIGACTB (CT1). Também será habilitado o botão sincronizar na tela da rotina, que permitirá iniciar o processo manualmente em caso de alterações do plano de contas contábil.

**Importante**

Com o sincronismo das contas orçamentárias habilitado a inclusão de novas contas será desabilitada na rotina PCOA010, sendo necessário realizá-la através do SIGACTB.

**Saiba mais:**

#### [MV\_PCOSINC - Plano de Contas Sincronizado](https://tdn.totvs.com/display/public/mp/MV_PCOSINC+-+Plano+de+Contas+Sincronizado+--+11315)
