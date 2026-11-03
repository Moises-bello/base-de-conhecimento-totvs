---
content_hash: 0e3c6c1497cf1378d9d8cc6db02396855174a3cc6b40ca995441c1fde4316afe
fetched_at: '2026-06-29T00:11:46.464300+00:00'
page_id: '822685303'
product: rm
source: tdn-rm
title: serv/locPrest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822685303
version: 6
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **locPrest** | **DPS/serv/** | **Sim** | **Grupo** | **Grupo de informações relativas ao local da prestação do serviço.** |
| cLocPrestacao | DPS/serv/locprest | Sim | Código do Município, Informado no Movimento em Integrações, Fiscal, de acordo com a tabela de classificação informada nos parâmetros de ambiente por filial da NFSe Municipal (Modelo Nacional) | Código de Classificação definido para o  município da Prestação conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI)  **Obs**: Esta tag será gerada com base na seguinte regra:  **Origem**: Município do Cadastro do Filial (Movimento de Venda\Lançamento de Saída)  ou município do cadastro Cliente\Fornecedor (Movimento de Compra\Lançamento de Entrada)  **Destino**:  Município do cadastro Cliente\Fornecedor(Movimento de Venda\Lançamento de Saída) e  Município do Cadastro do Filial (Movimento de Compra\Lançamento de Entrada)  **Local** **Incidência:**Município informado no movimento (Integrações | Fiscal | Município).   Imagem   **Importante**: quando o movimento possuir mais de um item e os itens possuírem locais de prestação diferentes, a tag será gerada como **Local de Incidência.** |
| cPaisPrestacao | DPS/serv/locprest | Sim | Código do país onde ocorreu a prestação do serviço. (Tabela de Países ISO) | Código do país de duas letras definido na norma ISO 3166-1 alpha-2.  Exemplo: MX (México), US (Estados Unidos).  sobre como parametrizar corretamente a tabela de classificação usada. |
