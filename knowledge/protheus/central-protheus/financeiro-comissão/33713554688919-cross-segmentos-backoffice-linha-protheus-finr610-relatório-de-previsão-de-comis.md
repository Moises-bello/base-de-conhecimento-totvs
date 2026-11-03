---
article_id: 33713554688919
category: Financeiro - Comissão
content_hash: e4ef96d86e29b46bd3049c70cbcb8f251b9756181ddc9f0783462c7b3d4d957d
fetched_at: '2026-06-28T22:37:50.771946+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINR610 - Relatório de previsão
  de comissões
type: support-article
updated_at: '2026-02-24T18:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33713554688919-Cross-Segmentos-Backoffice-Linha-Protheus-FINR610-Relat%C3%B3rio-de-previs%C3%A3o-de-comiss%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33713554670231) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Qual relatório permite visualizar a relação das comissões pendentes de pagamento?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O relatório tem como objetivo apresentar, por vendedor, a estimativa dos valores de comissão a pagar, considerando os títulos já emitidos, os pedidos de venda ainda não concluídos, bem como os títulos já baixados, porém ainda não pagos por meio da rotina de **atualização de pagamento MATA530**.

Para emitir o relatório de **Previsão de Comissões**, siga os passos abaixo:

1. Acesse a rotina **Previsão de Comissões** e clique em **Parâmetros**.
2. Configure os parâmetros conforme a orientação disponível nos helps de campo.
3. Após a conferência, confirme a impressão do relatório.

| **Parâmetro** | **Descrição** |
| --- | --- |
| **Do Vendedor** | Informe o código inicial do intervalo de vendedores a ser considerado. Utilize a tecla [F3] para consultar o Cadastro de Vendedores. |
| **Até o Vendedor** | Informe o código final do intervalo de vendedores. [F3] disponível para consulta. |
| **Do Vencimento** | Data inicial do intervalo de vencimento dos títulos a considerar. |
| **Até o Vencimento** | Data final do intervalo de vencimento dos títulos a considerar. |
| **Qual Moeda** | Informe a moeda na qual o relatório será emitido. |
| **Da Emissão** | Data inicial do intervalo de emissão dos títulos. |
| **Até a Emissão** | Data final do intervalo de emissão dos títulos. |
| **Comissão Zero** | Selecione “Sim” para incluir comissões zeradas no relatório ou “Não” para excluí-las. |
| **Considera Ped. Venda** | Selecione “Sim” para considerar pedidos de venda não faturados ou “Não” para desconsiderá-los. |

> **Importante:**
>
> Para pedidos de venda, os valores apresentados podem sofrer alterações, pois o cálculo de certos impostos é realizado apenas no momento do faturamento.

| **Parâmetro** | **Descrição** |
| --- | --- |
| **Alíquota I. Renda** | Informe a alíquota do imposto de renda a ser considerada. |
| **Outras Moedas** | Escolha “Converter” para incluir títulos em outras moedas ou “Não Imprimir” para exibir apenas títulos na mesma moeda do relatório. |
| **Salta Pag. por Vend.** | Selecione “Sim” para imprimir um vendedor por página ou “Não” para impressão contínua. |
| **Nome Cliente** | Escolha entre “Nome Reduzido” ou “Razão Social” para exibição do nome do cliente. |
| **Considerar por** | Selecione “Títulos Originais” para basear a comissão nos títulos de origem ou “Títulos Renegociados” para considerar os títulos gerados por renegociação. |

> **Observação:**  
> Títulos não renegociados serão apresentados normalmente, independentemente da opção selecionada.  
> Quando selecionado “Títulos Originais”, o intervalo de datas de emissão e vencimento será aplicado apenas aos títulos de origem, independentemente de suas datas de vencimento atuais.

| **Parâmetro** | **Descrição** |
| --- | --- |
| **Seleciona Filiais** | Escolha “Sim” para selecionar filiais específicas ou “Não” para considerar apenas a filial corrente. |
| **Considera Juros** | Define se os juros informados na liquidação serão considerados no cálculo da comissão. |
| **Considera Desconto** | Define se os descontos informados na liquidação serão considerados no cálculo da comissão. |

Impressão do relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33713554672151)

**Saiba mais**

[Previsão de Comissões - FINR610](https://tdn.totvs.com/pages/releaseview.action?pageId=630358896)
