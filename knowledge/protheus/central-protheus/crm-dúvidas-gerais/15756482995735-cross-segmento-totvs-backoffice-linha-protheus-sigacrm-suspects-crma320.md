---
article_id: 15756482995735
category: CRM - Dúvidas Gerais
content_hash: 383da2c70d7fc1c2513df2c5648c17188bd2f36f52a021ab87189ae000c6eb03
fetched_at: '2026-06-28T22:40:27.643100+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Suspects -
  CRMA320 '
type: support-article
updated_at: '2023-10-05T13:58:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15756482995735-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACRM-Suspects-CRMA320
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15772677994775) Tempo aproximado para leitura: **00:05:00 min****Dúvida:**

Suspects - CRMA320 - SIGACRM

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Todas as versões.

**Solução:**

Veja nosso vídeo**How To**sobre esse processo: [How To | MP - SIGACRM - Suspects (CRMA320)](https://www.youtube.com/watch?v=-AlKtsmgZFs)

Este cadastro é parte integrante do conceito CRM (Customer Relationship Management) e do relacionamento de contatos. Para o sistema, o status de suspect significa um possível prospect, ou seja, um contato que ainda não foi trabalhado. Este, por sua vez, pode ter sido selecionado, via mailing, por pesquisas na web ou outras ferramentas utilizadas para captação de entidades.

**Para cadastrar um suspect:**

1 - Em Suspects, clique em Incluir. O sistema apresenta a tela de inclusão.  
2 - Preencha os dados conforme orientação do help de campo.  
3 - Confirme.

![sus1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15756452985367)

**ADL (Controle de Conta do Vendedor)**

O parâmetro **[MV\_CRMADL](https://tdn.totvs.com/pages/viewpage.action?pageId=344473418)**tem o objetivo de parametrizar o uso da tabela do ADL (Controle de Conta do Vendedor) nos processos de negócios da administração de vendas no CRM e no Faturamento. Por padrão, o parâmetro deve estar habilitado como **Verdadeiro.**Porém, se os processos de administração forem utilizados somente no módulo CRM, o parâmetro deve ser desabilitado.

**Procedimentos**

1. O parâmetro **MV\_CRMADL**tem o valor**verdadeiro (.T.)**por padrão e permite a manutenção da ADL e de suas funcionalidades.
2. Se o parâmetro for alterado para **falso (.F.)**, o processamento da ADL não ocorrerá e a rotina **Área de Trabalho** do **Faturamento** será bloqueada pois utiliza dados da ADL em seu processo.

**Veja também**

* A consulta aos *Suspects* cadastrados,  a tabela **ACH - Cadastro de Suspects** no tópico [Consulta Cadastro Genéricos.](https://tdn.totvs.com/pages/viewpage.action?pageId=427052528)
* O tópico [Prospects](https://tdn.totvs.com/pages/viewpage.action?pageId=359466772)
* [Estrutura Negócio](https://tdn.totvs.com/pages/viewpage.action?pageId=359468427)

**Saiba mais:**

**[Suspects (CRMA320 - SIGACRM)](https://tdn.totvs.com/pages/releaseview.action?pageId=344472336)**
