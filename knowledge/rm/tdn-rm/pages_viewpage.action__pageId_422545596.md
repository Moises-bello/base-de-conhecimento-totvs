---
content_hash: bd164c9f9caa605d7e1e3dff920d2ceea417ac56220c04aefde07c100cf717e3
fetched_at: '2026-06-29T00:09:19.477687+00:00'
page_id: '422545596'
product: rm
source: tdn-rm
title: Informações Gerais (DIRF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545596
version: 20
---

O processo de geração da DIRF grava um arquivo do tipo texto no diretório de arquivos temporários do TOTVS Gestão Fiscal previamente definido em seus parâmetros.

**Origem dos dados**

* ****TOTVS** Gestão Fiscal**

Serão considerados os **Lançamentos Fiscais de entrada** (somente serviço) com status diferentes de Cancelado e Estornado e cuja data pertença ao ano calendário de geração da rotina.

Somente serão considerados na geração da rotina os lançamentos que possuírem os tributos do tipo **IRRF, IRRFPJ, IRPJ** ou **Retenções Sociais**, Lançamentos Fiscais com CFOP do tipo fiscal ou não fiscal, com o Tributo “IRRFPJ” ou “CSRF” e CFOP's específicos de Transporte.

As informações selecionas  serão agrupadas por Código de receita, CNPJ/CPF do beneficiário e por período.

* **TOTVS Gestão Financeira**

Serão selecionados lançamentos de contas a pagar cuja data de emissão pertença ao ano calendário da geração da rotina e que estejam registrados com um documento que gere Imposto de renda ou que possuem retenção de Contribuições Sociais.

***Atenção***:

O usuário não deve marcar na tela de geração da rotina para buscar as mesmas retenções do **Totvs Gestão Fiscal** e **Gestão Financeira**. Isto pode causar duplicidade nos valores.  
  
O parâmetro **Lançamentos de tributos serão faturados pelo RM Gestão Fiscal** que quando marcado desabilitava as opções de origem financeira da tela de geração da rotina, agora não tem mais esse efeito, independente do estado do parâmetro ambas as origens estarão disponíveis, por isso deve ser reforçado o cuidado para não  buscar as mesmas retenções do **Totvs Gestão Fiscal** e **Gestão Financeira** o que causaria duplicidade.
