---
article_id: 4403229575063
category: NFe - Nota Fiscal Eletrônica
content_hash: dec79a4503b4fee78ef81e34db0da9761b0cd37a62566a68c71d5cf14ba3f626
fetched_at: '2026-06-28T22:40:07.128860+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 332: CNPJ
  do adquirente ou do encomendante da importação inválido, em nfe de Importação'
type: support-article
updated_at: '2023-01-12T12:02:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403229575063-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-332-CNPJ-do-adquirente-ou-do-encomendante-da-importa%C3%A7%C3%A3o-inv%C3%A1lido-em-nfe-de-Importa%C3%A7%C3%A3o
---

**Dúvida**Com resolver a rejeição 332: CNPJ do adquirente ou do encomendante da importação inválido, em nfe de Importação?

**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -a partir da versão 12.1.17  
Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Consulte, no *Cadastro Centralizado de Contribuintes - CCC,* o CNPJ informado nos dados da DI e caso ele seja inválido, não o informe no complemento de importação.

* Link do CCC: <https://dfe-portal.svrs.rs.gov.br/NFE/CCC>

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11615759535127)

2. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar **MV\_EASY= N** Quando **não usa integração** com o **módulo SIGAEIC**

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101037393/20201201_145829.gif)**

**3.** Acesse a rotina ****Livros Fiscais**-> **Atualizações**->**Movimentos**->**NF manual de Entrada**->**Outras ações**->**Complementos**->**Importação:****

****![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101036933/20201201_145142.gif)****

4. Acessar a TAG de CNPJ do grupo da **<DI>** não é obrigatória no XML da nota. Caso não tenha o CNPJ correto ou não queira informar o CNPJ do adquirente/ encomendante, basta não preenchê-lo no complemento de importação nos **Livros Fiscais** (tabela CD5, campo CD5\_CNPJAE).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403229243671/mceclip1.png)

5. Após o ajuste no complemento de importação, basta retransmitir a NF-e.

* ***Validação da Sefaz:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403229197975/mceclip0.png)
