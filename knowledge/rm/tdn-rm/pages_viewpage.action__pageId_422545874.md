---
content_hash: aace12f388daf2c413525b05580a91b606d7657845a6d7e1773c1d88f720008f
fetched_at: '2026-06-29T00:09:21.377575+00:00'
page_id: '422545874'
product: rm
source: tdn-rm
title: Gerar Débito - Fornecimento de Refeições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545874
version: 4
---

Este processo somente estará visível se o parâmetro Apura ICMS Sobre Receita Bruta Aplicável some ao tributo ICMS. Para habilitar a opção acesse Ambiente | Parâmetros | TOTVS Gestão Fiscal | 03.01 - Identificação de Regras de Apuração | 03.01.01 - ICMS | Regra ICMS por Filial | editar a filial a ser alterada | Etapa 6 - Regime Especial. .

* **Informações do Cálculo**

Totaliza-se o campo Valor Total dos lançamentos de saída da coligada, filial e período da geração do processo respeitando as seguintes regras:

1. Lançamentos com status diferente de Cancelado e Estorno que não acobertam cupom fiscal;
2. Lançamentos associados a Natureza de Operação do tipo Devolução ou diferente de Transferência;
3. Lançamentos com tipo de emitente diferente igual a Cliente/Fornecedor ou Cliente/Fornecedor que não serja órgão estadual.

Aplica-se sobre o resultado a alíquota informada no período de apuração e com valor encontrado é criado um lançamento com tipo Outros Débitos e subtipo Não se Aplica.
