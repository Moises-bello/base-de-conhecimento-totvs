---
article_id: 360063387433
category: MDFe - Manifesto de Carga
content_hash: e559fc10dff746b4728b8f8b2c17f59a19fe6530262ffdc94b5bc745d36422af
fetched_at: '2026-06-28T22:40:08.307295+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Manifesto
  de Carga Nota técnica 2021.001
type: support-article
updated_at: '2025-06-17T17:35:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063387433-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Manifesto-de-Carga-Nota-t%C3%A9cnica-2021-001
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2021.001 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

![2021.001_mdfe.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003129602)

Esta Nota Técnica promove ajustes no leiaute do MDF-e do **modal rodoviário adequando o grupo de informações do vale pedágio em acordo com a definição da Agência Nacional de Transportes Terrestres (ANTT).**   
  
Define a **inclusão da chave do PIX como forma alternativa de recebimento do frete no modal rodoviário** e no evento de pagamento do frete.   
  
Também promove uma nota explicativa sobre a **regra de validação da duplicidade de chaves de acesso visando padronizar o entendimento em todos os DF-e.**   
  
E por fim, **o novo padrão de placas do Mercosul não traz mais no registro do licenciamento a informação da UF** de emplacamento do veículo, tornando facultativo o preenchimento desse campo.

* Para acessar a documentação da **solicitação acesse o link:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=612257032>

* **Protheus** realizar atualização do link abaixo, aplicar a **Patch e compilar o MDFESEFAZ:**

12.1.2310:<https://r.totvs.io/p/1017818>

12.1.2410:<https://r.totvs.io/p/1017819>

Rdmake com MDFESEFAZ:  [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1152113)

* **TSS**realizar atualização do link abaixo:

RPO do TSS:    [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)

Atualizar também os**Schemas** (<https://suporte.totvs.com/portal/p/10098/download#detail/761857>) compatível para ambos release.

* **Importante:**

#### As alterações, **nesta Nota técnica** liberadas pelo desenvolvimento:

* **Saiba mais:**

Conforme divulgado pela consultoria da TOTVS, **na qual menciona sobre o pedágio, no link abaixo:**

[Clique Aqui](https://www.totvs.com/blog/fiscal-clientes/mdf-e-adequacao-do-vale-pedagio/)

Para implementar as TAGS háuma ISSUE que foi liberada pelo desenvolvimento.

* Para acessar a documentação da **solicitação acesse o link:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=625151417>

* **Conforme a** Nota técnica 2020.001:

![2021.001_cronograma.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003131202)
