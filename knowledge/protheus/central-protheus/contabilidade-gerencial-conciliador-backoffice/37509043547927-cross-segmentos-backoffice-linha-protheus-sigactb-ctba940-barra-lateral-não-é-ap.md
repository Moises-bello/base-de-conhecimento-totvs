---
article_id: 37509043547927
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: cedf92f43fed14f8c7679d0c028008e09afb2cc3d360959c533d849f0030d169
fetched_at: '2026-06-28T22:40:31.013553+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGACTB- CTBA940 - Barra Lateral
  não é apresentada.
type: support-article
updated_at: '2026-02-19T20:26:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37509043547927-Cross-Segmentos-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Barra-Lateral-n%C3%A3o-%C3%A9-apresentada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37509084857239) Tempo aproximado para leitura: 00**:10 min**  
  
**Dúvida**  
Esse incidente ocorre, pois pode haver uma falha na configuração da pasta HTTP-ROOT ou a falta de atualizações do sistema.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial- A partir da release 12.1.2210  
  
**Solução:**  
Este erro do Menu ou Barra Lateral não ser apresentado ocorre devido à desatualização e **incompatibilidade dos arquivos temporários utilizados na composição do front da rotina.**

Este incidente ocorre normalmente devido à:

1- A**tualizações do ambiente, assim verifique se o sistema está totalmente atualizado conforme portal do cliente:**

[Acumulado CTB:](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

Obs: Com a aplicação deve rodar o UPDDISTR com o SDF contido no pacote.

**Para auxílio:**

[Atualização de Dicionário Diferencial - Frameworksp - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=366649057)

[Webapp](https://suporte.totvs.com/portal/p/10098/download?e=1168455#all/all/all/search/webapp)

[LIB](https://suporte.totvs.com/portal/p/10098/download?e=1168455#000006/368/TFLIB/)

[Appserver](https://suporte.totvs.com/portal/p/10098/download?e=1168455#000006/368/TFAPP/)

[Central de Atualizações](https://tdn.totvs.com/pages/releaseview.action?pageId=532651679)

2- I**ncompatibilidade dos arquivos temporários utilizados na composição do front da rotina**efetuado pela leitura dos dados na pasta **http-root** localizada na **Protheus\_data.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/37509084858391)**

Entre na sua pasta protheus\_data e**renomeie ou exclua** a pasta http-root, podendo deixar como http-hoot-bkp,

 Reinicie todos os serviços do **Protheus**. Após a reinicialização, acesse novamente o **Conciliador Backoffice  (CTBA940).**

**Saiba mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Erro HTTP ao acessar novas rotinas PO-UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535166755095-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Erro-HTTP-ao-acessar-novas-rotinas-PO-UI)

##### [Cross Segmentos - Linha Backoffice Protheus - CTBA940 - Tela em branco do conciliador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36941159586455-Cross-Segmentos-Linha-Backoffice-Protheus-CTBA940-Tela-em-branco-do-conciliador)
