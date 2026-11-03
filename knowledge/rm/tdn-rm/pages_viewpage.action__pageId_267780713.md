---
content_hash: d4d8106331186663d27b00f9107abd49ad6e2232f5c0fbcc159fbee25681fb32
fetched_at: '2026-06-29T00:08:19.313067+00:00'
page_id: '267780713'
product: rm
source: tdn-rm
title: TVXMUY_DT_Integração_SAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267780713
version: 113
---

# INTEGRAÇÃO SAP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Integração SAP* |
| **Situação/Requisito:** | *O processo de Integração SAP possui algumas peculiaridades que devem ser ajustadas:*   * **Não é necessariamente regra para a integração, a* definição de uma máscara para o código do lote ao gerar a contabilização e um filtro por Tipo de Integração durante o processo de Integração com o SAP.* * *Durante a geração dos lotes para integração o processo deverá efetuar o acerto entre os valores de débito e crédito para cada lote zerar a contabilização.* |
| **Solução/Implementação:** | * Para não utilizar o filtro Tipo de Integração e a máscara no código do lote ao gerar a contabilização foi definido um parâmetro - "Inibir Filtro Tipo de Integração". Que deverá ser selecionado em caso de opção por não utilização do recurso. Parâmetro disponibilizado em Folha de Pagamento - Folha Normal - Contabilização - Integração SAP - aba Integração SAP * Cada lote será validada a contabilização de débito/crédito e em caso de necessidade de acerto será incorporado um item com o valor a ser ajustado. Para a inserção deste item será necessário parametrizar a conta e o centro de custo transitório disponibilizado no parametrizador: Folha de Pagamento - Folha Normal - Contabilização - Integração SAP - aba Integração SAP |
| **Chamados relacionados:** | *TVXMUY* |

divs
