---
article_id: 360044295914
category: NFe - Nota Fiscal Eletrônica
content_hash: 826532a80e5d42816b86e625ee5d9b6b18be8f0e0a324478b647725ec54ac629
fetched_at: '2026-06-28T22:40:00.014816+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 539 Rejeição: Duplicidade
  de NF-e com diferença na Chave de Acesso [chNFe: ]'
type: support-article
updated_at: '2024-12-09T18:54:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044295914-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-539-Rejei%C3%A7%C3%A3o-Duplicidade-de-NF-e-com-diferen%C3%A7a-na-Chave-de-Acesso-chNFe
---

**Dúvida**Como corrigir a rejeição 539 Rejeição: Duplicidade de NF-e com diferença na Chave de Acesso?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A rejeição ocorre quando a nota fiscal transmitida já possui uma faixa de numeração autorizada pela SEFAZ, associada a outra chave de acesso. Nesses casos, é fundamental validar primeiramente a chave de acesso retornada pela SEFAZ na rejeição, verificando a data de autorização do documento. Caso a data de autorização seja anterior, será necessário utilizar uma nova numeração que ainda não tenha sido registrada na SEFAZ.

Caso a emissão da nota ocorra no mesmo dia e horário da nota que está sendo transmitida, é importante aplicar as atualizações descritas abaixo no ambiente e, em seguida, monitorar o status do documento novamente.

Link de consulta de chaves de acesso na Sefaz:

<https://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=resumo&tipoConteudo=7PhJ+gAVw2g=>

**Atualização do ambiente TSS**

1 - Substituir o RPO do TSS pelo da documentação abaixo:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)

2 - Atualizar as URLs do TSS:

[TSS - Atualização das URLs do TSS](https://suporte.totvs.com/portal/p/10098/download?e=761864)

**Atualização do ambiente Protheus**

Pacote Acumulado Documentos eletrônicos da Rotina: <https://tdn.totvs.com/pages/releaseview.action?pageId=525010692>

Fonte NFESEFAZ: <https://suporte.totvs.com/portal/p/10098/download?e=1152113>

Após isso, na rotina de transmissão de nota clique em Outras ações -> Transmissão e transmita a numeração da nota novamente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060245134)

Validação da Sefaz:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28393170604823)
