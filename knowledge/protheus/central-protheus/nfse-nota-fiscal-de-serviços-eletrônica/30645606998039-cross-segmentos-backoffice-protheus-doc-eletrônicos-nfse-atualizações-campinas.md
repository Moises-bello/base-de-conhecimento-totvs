---
article_id: 30645606998039
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a3a365f322f556dee24866e0ad3f2d595489b72310fe5fd96961b5cd14ea401d
fetched_at: '2026-06-28T22:39:58.700246+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: ‭Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Atualizações
  Campinas
type: support-article
updated_at: '2025-05-21T12:25:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30645606998039--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Atualiza%C3%A7%C3%B5es-Campinas
---

**Dúvida**  
Quais são as atualizações e procedimentos necessários para contemplar as novas atualizações de Campinas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Solução**A Prefeitura de Campinas alterou o provedor/layout webservice em **ambiente de produção** **em 17/03/2025:  
  
De:** Provedor: DSFNET e Layout 1 **Para:** Provedor: IMA e Layout 2.03Onde se fará necessário as seguintes orientações:  
  
**1. Atualizar RPO do TSS:** [TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS) **2. Demais atualizações no TSS** **[TSS - Atualização do TssNewNfse](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16784834285847-Cross-Segmentos-Backoffice-Protheus-TSS-NFSe-Configura%C3%A7%C3%A3o-do-NewNfse) *[TSS - Atualização de SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)*  
**3. Atualizações no Protheus********Disponível apenas para releases vigentes:  
12.1.2310: [clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)   
12.1.2410: [clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1171486)*****Obs.: Obrigatório que seja realizado um backup antes dos RPO's.***Após atualizações realizadas em ambos os produtos, será necessário que os serviços sejam reiniciados.**Feito isso, deverá acessar a rotina FISA022, reconfigurar o Wizard.cfg por completo, se atentando ao campo de versão, onde deverá agora ser preenchido com 2.03:  
  
![WIZARD_IMA.png](https://tdn.totvs.com/download/attachments/922690857/WIZARD_IMA.png?version=1&modificationDate=1741799956103&api=v2)  
  
Uma vez finalizada a configuração do wizard após todas as atualizações, o parametro **MV\_NEWNFSE** será alterado automaticamente para **S na SPED000 para essa entidade.**  
  
**IMPORTANTE**Em relação as **atualizações do TSS**, caso o ambiente esteja em cloud compartilhado, **as mesmas já foram providenciadas internamente**, não havendo necessidade de nenhuma ação. Somente caso o TSS seja exclusivo cloud, deverão realizar a abertura de um ticket com a solicitação.  
  
Já as **atualizações do Protheus** todos deverão realizar (ambiente cloud ou local).  
  
Fonte da Prefeitura: [clique aqui.](https://campinas.sp.gov.br/sites/sistemas-issqn-nova-versao/nfse-campinas)
