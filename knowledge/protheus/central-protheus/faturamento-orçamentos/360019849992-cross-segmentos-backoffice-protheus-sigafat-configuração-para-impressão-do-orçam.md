---
article_id: 360019849992
category: Faturamento - Orçamentos
content_hash: adcbe81eca18dfdde4ff2dbdde83a8122661a182a571a20c4a51606495a7b61a
fetched_at: '2026-06-28T22:38:24.957890+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Configuração para impressão
  do Orçamento de Vendas (MATA415)
type: support-article
updated_at: '2026-01-23T18:05:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019849992-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-para-impress%C3%A3o-do-Or%C3%A7amento-de-Vendas-MATA415
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37890756234519)** **Tempo aproximado para leitura:****00:02:00 min**

**Dúvida**

Como configurar a impressão do Orçamento de Vendas (MATA415) através do RDMAKE padrão ORCFAT?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

A rotina de Orçamentos de Venda (MATA415) disponibiliza a impressão do documento através do modelo padrão **ORCFAT**. Caso ao tentar imprimir ocorra o alerta *"RDMAKE informado no parâmetro MV\_ORCIMPR não se encontra no repositório"*, siga os passos abaixo:

1. **Verificação de Parâmetro:** Acesse o **Configurador (SIGACFG)** e garanta que o parâmetro `MV_ORCIMPR` esteja preenchido com o conteúdo `ORCFAT`.
2. **Compilação do Arquivo:** Deve-se compilar o **RDMAKE** padrão do relatório no Repositório (Este procedimento deve ser realizado por sua Equipe de TI, após backup)

   * Extraia o arquivo [**ORCFAT.zip**](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/5165234551319) possui dois arquivos necessários para configuração: `orcfat.ch` e `ORCFAT.PRX`
3. Após a configuração e compilação, acesse a rotina **MATA415**, selecione o orçamento desejado, clique em **Outras Ações** > **Imprimir**.

**Observação 1: Quanto à customização:** Este RDMAKE é um modelo básico. Caso necessite de informações adicionais (impostos específicos ou layout diferenciado), o fonte `ORCFAT.PRX` pode ser editado pela sua equipe de TI ou parceiro de serviços para se adequar à sua necessidade.

**Observação 2****:** Se o erro persistir em um fonte já personalizado, orientamos verificar com o seu especialista de serviços ou com a equipe que realizou a personalização para ajustar e corrigir o *RDMAKE*.

**Saiba Mais:**

* TDN: [Impressão do Orçamento de Venda (MATA415) - RDMAKE (ORCFAT)](http://tdn.totvs.com/pages/releaseview.action?pageId=224452099)
* [Cross Segmentos - Backoffice Protheus - SIGAFAT - Em qual campo do pedido de venda (mata410), posso verificar qual foi o orçamento (MATA415) que gerou esse pedido, e no orçamento de vendas, o pedido vinculado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050824573-MP-FAT-Em-qual-campo-do-pedido-de-venda-mata410-posso-verificar-qual-foi-o-or%C3%A7amento-MATA415-que-gerou-esse-pedido-e-no-or%C3%A7amento-de-vendas-o-pedido-vinculado)
* [Cross-Segmentos-TOTVS-Backoffice-Linha-Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Planilha Financeira do Orçamento-Faturamento-SIGAFAT-Planilha-Financeira-do-Orçamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403795192599-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Planilha-Financeira-do-Or%C3%A7amento)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Orçamentos de Venda com Situação Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020143272-MP-FAT-Or%C3%A7amentos-de-Venda-com-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Conceito de uso do campo CK\_ITEM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008369162-MP-FAT-Conceito-de-uso-do-campo-CK-ITEM)
