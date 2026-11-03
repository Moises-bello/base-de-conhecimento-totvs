---
article_id: 19198544881175
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 80d920646c5227585bac4f7e2407509fa26322113915b7bf48f721300d2d492a
fetched_at: '2026-06-28T22:41:48.355209+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - Exclusão de
  bem Vinculado a CIAP
type: support-article
updated_at: '2023-11-20T16:50:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19198544881175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Exclus%C3%A3o-de-bem-Vinculado-a-CIAP
---

**Dúvida**

Na exclusão de um Bem apropriado de CIAP, o CIAP é excluído junto ao bem.  
  
**Ambiente**PROTHEUS – Ativo Fixo – A partir da versão 12.1.2210  
  
  
**Solução**  
Ao realizar a exclusão do ativo vinculado a um código de CIAP é informado que o bem esta associado ao CIAP, perguntando se deseja prosseguir com a exclusão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19198575972887)

Ao selecionar 'Sim' o Ativo é excluído, e o CIAP tem se status alterado de, "Ativo apropriado", para "Ativo Sem Ocorrências", conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19198551196439)

Outra opção seria baixar o Ativo, pois conforme informa a documentação:

#### [Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 - ESTORNO DE CREDITO DE CIAP NA BAIXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018577172-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-ESTORNO-DE-CREDITO-DE-CIAP-NA-BAIXA)

Ao realizar a baixa do ativo ocorre automaticamente a baixa do CIAP, que é verificado na rotina de manutenção de CIAP (MATA905) e estorno CIAP (MATA906) no módulo Fiscal.  
Porém não é gerado estorno de crédito do CIAP que já foi apropriado ao baixar o bem.

Link com informação referente ao credito de ICMS sobre ativo permanente

[CIAP - Crédito de ICMS sobre o Ativo Permanente](https://tdn.totvs.com/pages/releaseview.action?pageId=708871751)

Saiba Mais:

[Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - CIAP campos bloqueados - N1\_CODCIAP e N1\_ICMSAPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011054291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-CIAP-campos-bloqueados-N1-CODCIAP-e-N1-ICMSAPR-)

[Cross Segmento - Backoffice Linha Protheus - SIGAATF - Ativo cadastrado com CIAP por engano.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000368067-MP-SIGAATF-Ativo-cadastrado-com-CIAP-por-engano-)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - CIAP - Crédito ICMS sobre ativo permanente/Relatório CIAP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028514051-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-CIAP-Cr%C3%A9dito-ICMS-sobre-ativo-permanente-Relat%C3%B3rio-CIAP)

[Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 CONCEITO TRANSFERÊNCIA DE BENS COM CIAP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021375172-MP-SIGAATF-ATFA060-CONCEITO-TRANSFER%C3%8ANCIA-DE-BENS-COM-CIAP)
