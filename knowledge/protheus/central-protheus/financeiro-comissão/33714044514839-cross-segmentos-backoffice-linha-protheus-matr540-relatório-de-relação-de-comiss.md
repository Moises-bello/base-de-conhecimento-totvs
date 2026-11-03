---
article_id: 33714044514839
category: Financeiro - Comissão
content_hash: e5b05c19afabdee4e70a6f1770056c4c892668f631323e118b7e4b8122aa6005
fetched_at: '2026-06-28T22:37:50.794633+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - MATR540 - Relatório de Relação
  de comissões
type: support-article
updated_at: '2025-07-25T14:41:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33714044514839-Cross-Segmentos-Backoffice-Linha-Protheus-MATR540-Relat%C3%B3rio-de-Rela%C3%A7%C3%A3o-de-comiss%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33714029105815) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Qual relatório permite visualizar a relação das comissões geradas?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
O relatório tem como objetivo apresentar, por vendedor, as comissões calculadas e geradas conforme os critérios definidos na rotina de cálculo de comissões.  
São exibidas todas as informações pertinentes, como o valor original do título, a base de cálculo, o percentual aplicado e o valor da comissão gerada.

Para emitir a **Relação de Comissões**, siga os seguintes passos:

1. Acesse a rotina **Relação de Comissões** e clique em **Parâmetros**.
2. Configure os parâmetros conforme as orientações disponíveis nos helps de campo.
3. Após revisar as configurações, confirme para gerar a impressão do relatório.

| **Parâmetro** | **Descrição** | **Observações** |
| --- | --- | --- |
| **Lista pela** | Define se serão consideradas comissões geradas na **Emissão**, **Baixa** dos títulos, ou **Ambas**. | Notas fiscais de devolução serão sempre listadas pela emissão. |
| **Considera Data** | Data inicial do intervalo de datas a considerar para emissão do relatório. |  |
| **Até a Data** | Data final do intervalo de datas a considerar. |  |
| **Do Vendedor** | Código inicial do intervalo de vendedores a considerar. | Tecla [F3] disponível para consulta ao cadastro de vendedores. |
| **Até o Vendedor** | Código final do intervalo de vendedores. | Tecla [F3] disponível para consulta ao cadastro de vendedores. |
| **Considera quais** | Define se o relatório considerará comissões **A Pagar**, **Pagas** ou **Ambas**. |  |
| **Demonstra ajuste** | Selecione **Sim** para incluir ajustes de comissão, ou **Não** para desconsiderá-los. | Os ajustes são efetuados pela rotina **Recálculo de Comissão** em **Miscelâneas**. |
| **Qual moeda** | Moeda de emissão do relatório: **Moeda 1** a **Moeda 5**. |  |
| **Comissões zeradas** | Selecione **Sim** para considerar comissões com valor zero ou **Não** para excluí-las. |  |
| **Alíquota de IR** | Percentual de alíquota de Imposto de Renda a ser aplicado sobre os valores de comissão. |  |
| **Salta Pág. por Vendedor** | Selecione **Sim** para imprimir um vendedor por página ou **Não** para impressão contínua. |  |
| **Tipo de relatório** | Modelo de apresentação a ser utilizado na emissão do relatório. |  |
| **Imprime detalhes origem** | Define se devem ser impressos os títulos que originaram a comissão. | **Não se aplica à rotina FINA460**: nestes casos, o título de origem sempre será impresso. |
| **Nome Cliente** | Define o formato de exibição do nome do cliente: **Nome Reduzido** (conforme cadastro) ou **Razão Social**. |  |
| **Tipo de Vendedor** | Tipo de vendedor a ser incluído na impressão do relatório. |  |
| **Seleciona Filial** | Define se será exibida a tela para seleção de filiais (**Sim**) ou se apenas a filial corrente do sistema será considerada (**Não**). |  |

Exemplo de impressão do relatório

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33714029107095)

**Saiba mais**

[**Relação de Comissões - MATR540**](https://tdn.totvs.com/pages/releaseview.action?pageId=566484310)
