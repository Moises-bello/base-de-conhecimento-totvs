---
article_id: 360035979154
category: Materiais - Compras (SIGACOM)
content_hash: ed1ac918b8e3006c55616a4c77992fb006faad485a3fdb4843819c6d9fc119f3
fetched_at: '2026-06-28T22:41:18.694776+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Fornecedor não habilitado
  no Quality é impedido de participar do processo de cotação
type: support-article
updated_at: '2022-05-18T20:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035979154-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Fornecedor-n%C3%A3o-habilitado-no-Quality-%C3%A9-impedido-de-participar-do-processo-de-cota%C3%A7%C3%A3o
---

**Dúvida**

Fornecedor não habilitado no Quality é impedido de participar do processo de cotação

**Ambiente**  
Protheus – Compras – A partir da versão 12  
  
**Solução**

O sistema realiza a validação no caso da cotação conforme exemplo abaixo:

- Identifica qual tabela o parâmetro ***MV\_ARQPROD***está consultando a informação;

- Valida se no cadastro do produto o campo **B1\_TIPOCQ** **-** Tipo de C.Q**.** na aba **CQ** consta como **Sigaquality**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047030834/mceclip4.png)

- Verifica se existe cadastro de **Especificação de Produto** *(QIEA010)*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047892473/mceclip0.png)

- Valida cadastro dentro do módulo Gestão de Qualidade o **Produto x Fornecedor** *(MATA061)* o campo **Situação (A5\_SITU) =***N/HABILITADO*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047894093/mceclip2.png)

- Nessa situação na rotina Atualização > Cotações > **Atualização de Cotação** (*MATA150*) se o parâmetro ***MV\_QBLQFOR*** estiver como **S**  *(indica que o fornecedor deve ser validado pela rotina)* o sistema apresentará o alerta conforme abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047913913/mceclip5.png)

***A150BLQFO** - O Produto: " ### " no Item: " ### ", desta cotacao, foi bloqueado pela Qualidade para este Fornecedor*

- Mais detalhes sobre configuração do SIGAQIE verifique artigo a seguir: [MP - QUA - Cadastros necessários para gerar uma entrada no SIGAQIE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020570212-MP-QUA-Cadastros-necess%C3%A1rios-para-gerar-uma-entrada-no-SIGAQIE)

- Principais funções validadas:

* COMXFUN
* MATA150
* QIEXFUN
