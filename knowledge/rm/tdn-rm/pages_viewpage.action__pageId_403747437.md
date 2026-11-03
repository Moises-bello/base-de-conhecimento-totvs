---
content_hash: c13def7360eaad5a1e7d770400e4e83805b798681948b42bbda154721933396a
fetched_at: '2026-06-29T00:09:11.423913+00:00'
page_id: '403747437'
product: rm
source: tdn-rm
title: Procedimento para conferência de valores nos eventos de fechamento periódico
  do eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403747437
version: 8
---

1.     Objetivo e orientações **TOTVS Folha de Pagamento**

A Receita emitiu um comunicado possibilitando a geração da DARF Avulsa. Esta geração pode ser realizada: a) quando o cliente não conseguir realizar a transmissão de todas as etapas do eSocial até o fechamento da Folha (envio do evento **S-1299-Fechamento dos Eventos Periódicos**), para isso é necessário enviar o evento S-1295-Solicitação de Totalização para Pagamento em Contingência; b) ou quando envia o evento **S-1299-Fechamento dos Eventos Periódicos** e há divergência de valores.

O valor da DARF Avulsa deverá ser a diferença apurada entre o calculado pela DCTFWeb e a apuração do sistema TOTVS Folha de Pagamento.

A geração da DARF avulsa complementar, deverá ser feita através do sistema [SicalcWeb](http://idg.receita.fazenda.gov.br/orientacao/tributaria/pagamentos-e-parcelamentos/darf-calculo-e-impressao-programa-sicalc-1/programa-para-calculo-e-emissao-de-darf-on-line-de-tributos-e-contribuicoes-federais-exceto-contribuicoes-previdenciarias), conforme determinação da Receita Federal.

**Atenção:**

É de responsabilidade do cliente a conferência das informações geradas pelo TOTVS Folha de Pagamento e pelas diferenças para o pagamento da Darf Avulsa.

2.     Confrontando Valores:

Para realizar o processo de comparação dos valores de contribuição previdenciária calculados pelo TOTVS Folha de Pagamento, o usuário pode executar os processos abaixo.

Lembrando que, o cálculo efetuado pelo sistema DCTFWEB centraliza os valores devidos por Contribuinte, entende-se como “Contribuinte” a Matriz e suas filiais, assim para um melhor entendimento, orientamos que estes relatórios sejam impressos por empresa e não por filiais.

**Processo 1**

Gerar a folha analítica em Folha de Pagamento | Folha Mensal | Folha Analítica.

Este relatório traz o demonstrativo de todas as bases para calculo da guia de INSS.

****Processo**2**

Gerar a Guia de INSS em Folha de Pagamento | Encargos | Guia de INSS | Guia de INSS 

**Atenção:**

     É muito importante que, antes de qualquer ação, sejam feitas as conferências dos parâmetros utilizados para o cálculo da Contribuição Previdenciária, realizado pelo TOTVS Folha de Pagamento e das informações enviadas nos eventos:

* + S-1005 – Estabelecimentos  X Dados da Seção
  + S-1020 – Lotações  X Dados da Lotação Tributária
  + Valores informados na REINF X Valores da Retenção 9711/98
  + Valores informados nos eventos S-1250 X  Valores de Produtor Rural

A disparidade entre essas informações pode estar ocasionando a diferença apresentada entre a GPS calculada pelo ERP e a DARF calculada pelo DCTFWeb.

**Informações complementares:**
