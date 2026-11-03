---
article_id: 38158139735319
category: Financeiro - Conciliação de Vendas
content_hash: 857f7f8fcae823ef23a93974c59a8dc616cdc9798f243a4b2893b6e91558cb4f
fetched_at: '2026-06-28T22:37:26.283099+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Conciliador de pagamento e vendas
type: support-article
updated_at: '2026-02-04T16:51:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38158139735319-Cross-Segmentos-Backoffice-Protheus-Conciliador-de-pagamento-e-vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38158130737431) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
O Protheus possui alguma rotina de conciliação de pagamentos e vendas?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**  
Este processo tem como objetivo realizar a conciliação dos registros de vendas e/ou pagamentos efetuados por meio de operadoras/administradoras de cartões (débito e/ou crédito), bem como de pagamentos digitais e PIX — sendo estas duas últimas modalidades disponíveis exclusivamente para conciliação de pagamentos, desde que os respectivos títulos tenham sido gerados no módulo Financeiro do Protheus.

Os arquivos encaminhados pelas administradoras de cartões são importados e validados por meio da rotina de importação, assegurando a integridade das informações para posterior conciliação.

Após a importação, é possível realizar a conciliação dos movimentos conforme regras automáticas previamente configuradas, bem como efetuar ajustes manuais, quando necessário.

**Documentação detalhando o processo:**

[Conciliador Pagamentos e Vendas](https://tdn.totvs.com/display/public/PROT/Conciliador+Pagamentos+e+Vendas+-+Financeiro+%28Contas+a+Receber%29+-+P12)

O processo de conciliação é dividido em duas etapas principais:

**Conciliação de vendas:** consiste no reconhecimento do registro de venda no sistema em relação à confirmação de venda enviada no arquivo da administradora.

[FINA914 - Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=655440482)

**Conciliação de pagamentos:** consiste na identificação do registro de pagamento no sistema em relação à confirmação de pagamento enviada no arquivo da administradora. Após o reconhecimento e a confirmação da conciliação, o título correspondente é baixado automaticamente no sistema.

Adicionalmente, o sistema disponibiliza relatórios para conferência das críticas geradas durante a importação, bem como para o acompanhamento das conciliações realizadas.

[FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877)

**Saiba mais**

[Cross Segmento Backoffice Linha Protheus - SIGAFIN - FINA910 - Qual a diferença entre Sitef Antigo FINA910 e Sitef Novo FINA918](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007187161-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA910-Qual-a-diferen%C3%A7a-entre-Sitef-Antigo-FINA910-e-Sitef-Novo-FINA918)
