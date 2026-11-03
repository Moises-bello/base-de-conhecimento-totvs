---
content_hash: 1d4a48c68b55e43db4565b33f0aaec012f8ec0048112a432992f906979bb68d3
fetched_at: '2026-06-29T00:11:21.536036+00:00'
page_id: '696702163'
product: rm
source: tdn-rm
title: DT Importação/Exportação de Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=696702163
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Backoffice (Linha RM) - TOTVS Gestão de Estoque |
| Função: | Conceito, Gerador de Saídas |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-11815 |

## **02. SITUAÇÃO/REQUISITO**

Com a intenção de facilitar os processos de integração do ERP com bases e sistemas legados, ou mesmo a extração de dados do ERP, a TOTVS disponibilizou os layouts de importação e exportação de produtos como objetos gerenciais padrões e distribuídos junto ao instalador da biblioteca TOTVS a partir da versão 12.1.4.

## **03. SOLUÇÃO**

**Exportação de produtos**

Para realizar a exportação dos produtos utiliza-se o **Gerador de Saídas.** O Gerador de Saídas é uma ferramenta criada para exportar dados de qualquer módulo da Linha TOTVS através de um layout pré-definido pelo sistema.

Neste caso deve-se primeiro ter importado o layout de exportação disponibilizado na pasta de objetos gerenciais.

**Importação de produtos**

Para realizar a importação de produtos, é necessário antes, importar o layout de importação através da ferramenta **Conceito**, que compõe o TOTVS Business Conector (TBC).

Neste caso deve-se primeiro ter importado o layout de importação disponibilizado na pasta de objetos gerenciais.

Exportação de Produtos, Importação de Produtos, Passo 03, Passo 04passo1,passo2yespasso1

1. Para Acessar o Gerador de Saídas, acesse primeiro o Módulo Integrações, e navegue para a aba **Integrações | Gerador de Saídas | Layouts**.
2. Na visão da tela do Gerador de Saídas, selecione a opção **Processos | Importar Layout**. Selecione o arquivo de layout disponível na pasta de objetos gerenciais e informe um nome e a categoria para a importação.
3. Após a importação selecione o layout na visão e execute o processo **Geração de Saídas.**
4. Após a conclusão do processo o arquivo com os produtos selecionados estará disponível em: C:\totvs\CorporeRM\RM.Net\Saídas (Caso o sistema esteja instalado na pasta default).
nopasso2

1. Para acessar o Conceito, primeiro acesse o modulo Integrações, e navegue para a aba **Integrações | Conceito**.
2. Na visão da tela do Conceito, selecione a opção **Processos | Importar de Conceito**. Selecione o arquivo de conceito disponível na pasta de objetos gerenciais e informe o nome para a importação.
3. Após a importação selecione o conceito na visão e execute o processo **Processar novo conceito** selecionando o arquivo desejado no mesmo formato do layout de exportação.
4. Após a conclusão do processo os produtos informados no arquivo de importação estarão atualizada no sistema.

## **04. DEMAIS INFORMAÇÕES**

Tanto o Layout de saída quanto o conceito podem ser customizados para se adequarem a realidade de cada empresa.

### **Informações Técnicas**

|  |  |
| --- | --- |
| **Tabelas Utilizadas** | * TPRODUTO * TTRBPRD * TPRDCOMPOSTO * TPRDCOMPL * TPRDCFO * TPRDCONT * TPRDCODIGO * TPRDUND * TPRDFISCAL * DTRBMUNICIPIOPRD * TLINHA * TGRADE * TCOLUNA * TPRDSIMILAR * TPRDHISTORICO * TPRDRAT * TPRDGRUPOPRODUTO |

**A partir da versão 12.1.2209 é possível exportar e importar dados de Grupos de ProdutosIMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**
