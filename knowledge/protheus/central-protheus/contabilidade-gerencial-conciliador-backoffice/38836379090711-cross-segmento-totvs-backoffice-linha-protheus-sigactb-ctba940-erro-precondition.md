---
article_id: 38836379090711
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: 6aba5ad39505bf273103cfb3ab172a12bd2cc8b2262edc38d72455c4de099dde
fetched_at: '2026-06-28T22:40:30.997328+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB -  CTBA940 - Erro
  "Precondition Required"
type: support-article
updated_at: '2026-03-06T14:52:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38836379090711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Erro-Precondition-Required
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38836392178199) Tempo aproximado para leitura: **02 min**  
  
**Dúvida**  
Ao tentar acessar a rotina Conciliador backoffice (CTBA940), o sistema não carrega a tela do conciliador e apresenta a mensagem de erro "*Precondition Required*".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38836498616343)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - a partir da versão 12.1.33  
  
  
**Solução**  
A mensagem mencionada pode ocorrer em ambientes que estejam utilizando versões desatualizadas dos binários do Protheus. Para a correção, é necessário verificar se o ambiente está atualizado, o que inclui os binários (WebApp + WebAgent), a LIB e o Pacote acumulado de expedição contínua do BackOffice.

**Passos**

1. Acesse a pasta "protheus\_data" do seu ambiente e renomeie a pasta "http-root" (podendo alterá-la para http-root-bkp, por exemplo).

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38836392183959)
2. Em seguida, reinicie os serviços do Protheus (dbaccess e appserver) e valide o acesso novamente.
3. Se mesmo após o processo de renomear a pasta e reiniciar os serviços a mensagem prosseguir, realize a atualização do binário que estiver desatualizado.

   * [Pacote acumulado do backoffice](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1182881).
   * [Pacotes LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)
   * [Pacotes DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll).
   * [Binário AppServer](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/).
   * [Binário SmartClient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/).

**Saiba Mais**

[Erro HTTP ao acessar novas rotinas PO-UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535166755095-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Erro-HTTP-ao-acessar-novas-rotinas-PO-UI).  
[CTBA940 - Conciliador BackOffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-BackOffice)
