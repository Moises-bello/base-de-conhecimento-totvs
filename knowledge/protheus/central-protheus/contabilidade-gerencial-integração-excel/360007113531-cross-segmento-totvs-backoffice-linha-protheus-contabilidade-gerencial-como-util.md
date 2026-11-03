---
article_id: 360007113531
category: Contabilidade Gerencial - Integração EXCEL
content_hash: 2962d17b69e9c5c4f4421bf1c5466ce21124b745eb61abc518c044e67592f72e
fetched_at: '2026-06-28T22:40:54.758551+00:00'
product: protheus
section_id: 1500001548582
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial
  - Como utilizar as funções da Integração Excel (ApExcel)
type: support-article
updated_at: '2026-02-18T18:36:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007113531-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Contabilidade-Gerencial-Como-utilizar-as-fun%C3%A7%C3%B5es-da-Integra%C3%A7%C3%A3o-Excel-ApExcel
---

A integração do Protheus com Excel permite utilizar funções do sistema diretamente em planilhas para extração de dados, via assistente de função, digitação direta, ou função SIGA. Diversas funções contábeis estão disponíveis, facilitando a montagem de relatórios e análises financeiras no Excel.

**Dúvida:**  
Como utilizar as funções e fórmulas do Protheus através da rotina de Integração com Excel (ApExcel)?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - Versões 11 e 12  
  
  
**Solução:**

A integração do Protheus com o Microsoft Excel® permite utilizar funções do sistema diretamente em planilhas para a extração de dados e montagem de relatórios.

Para utilizar este recurso, realize os seguintes passos:

1. Acesse o módulo desejado no Protheus.
2. No menu principal, navegue até: **Miscelânea > Integrações > Planilha Excel**.

   ![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2011%3A38%3A9.png?version=1&modificationDate=1481219338000&api=v2)
3. O sistema apresentará uma janela de confirmação. Clique em **OK** para iniciar a comunicação com o Microsoft Excel®.

   ![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2011%3A45%3A13.png?version=1&modificationDate=1481219338000&api=v2)
4. Aguarde a barra de progresso de conexão.

   ![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2011%3A44%3A52.png?version=1&modificationDate=1481219338000&api=v2)
5. Com o Excel aberto, existem **4 formas** de utilizar as funções do Protheus. Confira abaixo os métodos disponíveis:  
     
   ![](https://tdn.totvs.com/download/thumbnails/312160907/triright.png?version=2&modificationDate=1519067047000&api=v2)**Opção 1: Assistente de Função (Recomendado)**

   Este método é indicado para facilitar a visualização dos parâmetros necessários.

   No Excel, clique no botão Inserir Função (fx).

   ![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2014%3A48%3A26.png?version=1&modificationDate=1481219338000&api=v2)

   Na categoria, selecione Definido pelo Usuário.

   Selecione a função desejada na lista (Ex: Ap5BarButtons, Posicione, etc.).

   ![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2014%3A6%3A52.png?version=1&modificationDate=1481219338000&api=v2)

   Ao clicar em OK, será aberta a janela de argumentos da função. Preencha os campos solicitados (Alias, Ordem, Chave, Campo) e confirme.

   ![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2014%3A14%3A2.png?version=1&modificationDate=1481219338000&api=v2)

[![](https://tdn.totvs.com/download/thumbnails/312160907/triright.png?version=2&modificationDate=1519067047000&api=v2)](https://tdn.totvs.com/pages/viewpage.action?pageId=311066572)**Opção 2: Digitação Direta**

Caso conheça a sintaxe da função, é possível digitá-la diretamente na célula, iniciando com o sinal de igual `=`.  
  
**Exemplo:** `=MesExtenso("04")`  
**Resultado:** Retornará "Abril".

![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2014%3A32%3A7.png?version=1&modificationDate=1481219338000&api=v2)

![](https://tdn.totvs.com/download/thumbnails/312160907/triright.png?version=2&modificationDate=1519067047000&api=v2)**Opção 3: Função SIGA (Parâmetros separados)**

Utiliza-se a função `SIGA()` como um interpretador para chamar funções do Protheus. Neste formato, o nome da função Protheus deve estar entre aspas, e os parâmetros separados por ponto e vírgula (ou o separador padrão do seu Excel).  
  
**Sintaxe:** `=SIGA("NomeDaFuncao"; Parâmetro1; Parâmetro2...)`  
**Exemplo:** `=Siga("MesExtenso";"04"`)

![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2014%3A37%3A12.png?version=1&modificationDate=1481219338000&api=v2)

![](https://tdn.totvs.com/download/thumbnails/312160907/triright.png?version=2&modificationDate=1519067047000&api=v2)**Opção 4: Função SIGA (Parâmetros encapsulados)**

Nesta variação, a função Protheus e seus parâmetros são passados como uma única string (texto) dentro da função `SIGA()`.  
  
**Sintaxe:** `=SIGA("NomeDaFuncao(Parâmetros)")`  
**Exemplo:** `=Siga("MesExtenso(04)")`

![](https://tdn.totvs.com/download/attachments/269441698/image2016-12-8%2014%3A38%3A58.png?version=1&modificationDate=1481219338000&api=v2)

**Observação****:** A conexão pode ser cancelada através do Protheus, clicando no botão **“Sair**”, ou fechando o **Microsoft Excel®**. 

---

O módulo **SIGACTB** possui algumas funções disponíveis para extração de dados, abaixo estão listas as funções disponíveis:

|  |  |
| --- | --- |
| Função | Descrição da função |
| [SALDOITEM](https://tdn.totvs.com/pages/viewpage.action?pageId=6068545) | Retorna o Saldo de uma Conta Contábil + Centro de Custo + Item Contábil |
| [SALDOCCUS](https://tdn.totvs.com/display/PROT/SaldoCCus+-+Retorna+saldo+de+um+centro+de+custo+--+10919) | Retorna o Saldo de uma Conta contábil + Centro de custo |
| [SALDOCLASS](https://tdn.totvs.com/display/PROT/SaldoClass+-+Retorna+saldo+de+uma+classe+de+valor+--+10920) | Retorna o Saldo de uma Conta Contábil + Centro de Custo + Item Contábil + Classe de Valor |
| [MOVITEM](https://tdn.totvs.com/pages/viewpage.action?pageId=6068541) | Retorna o Movimento de uma Conta Contábil + Centro de Custo + Item Contábil |
| [MOVCUSTO](https://tdn.totvs.com/display/PROT/MovCusto+-+Retorna+valor+de+um+centro+de+custo+--+10917) | Retorna o Movimento de uma Conta Contábil + Centro de Custo |
| [MOVCONTA](https://tdn.totvs.com/pages/viewpage.action?pageId=6068539) | Retorna o Movimento de uma Conta Contábil |
| [MOVCLASS](https://tdn.totvs.com/display/PROT/MovClass+-+Retorna+valor+de+uma+classe+de+valor+--+10915) | Retorna o Movimento de uma Conta Contábil + Centro de Custo + Item Contábil + Classe de Valor |
| [CTSMCONTA](https://tdn.totvs.com/pages/viewpage.action?pageId=312160915) | Retorna o saldo de um grupo de Contas Contábeis na data e moeda informadas. |
| [CTSMCUSTO](https://tdn.totvs.com/pages/viewpage.action?pageId=312160884) | Retorna o saldo de um grupo de Centros de Custo na data e moeda informadas. |
| [CTSMITEM](https://tdn.totvs.com/pages/viewpage.action?pageId=312160860) | Retorna o saldo de um grupo de Itens Contábeis na data e moeda informadas. |
| [CTSMMOV](https://tdn.totvs.com/pages/viewpage.action?pageId=312160893) | Retorna a soma de movimentos de um intervalo e/ou conjunto de entidades (Conta e/ou Centro de Custo e/ou Item Contábil e/ou Classe de Valor) dentro de um intervalo de datas com a livre combinação das entidades |
| [SALDOCONTA](https://tdn.totvs.com/pages/viewpage.action?pageId=6068544&searchId=RUDXY6CY9) | Retorna o saldo de uma Conta Contábil na data e moeda informadas. |
| [CTSMENTMOV](https://tdn.totvs.com/pages/viewpage.action?pageId=312156311) | Retorna a soma de movimentos do intervalo de códigos de uma das entidades (Conta, Centro de Custo, Item Contábil ou Classe de Valores) e de um intervalo de datas. |
| [CTBSMSALDOS](https://tdn.totvs.com/pages/viewpage.action?pageId=312160858) | Retorna o saldo de um grupo de entidades em uma determinada data. |
| [CTSMCLVL](https://tdn.totvs.com/pages/viewpage.action?pageId=312160908) | Retorna o saldo de um grupo de Classes de Valores na data e moeda informadas. |

**Saiba Mais**  
[Planilha Excel](https://tdn.totvs.com/display/framework/Planilha+Excel)  
[Validar funções advpl na integração Excel](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018993631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Validar-fun%C3%A7%C3%B5es-advpl-na-integra%C3%A7%C3%A3o-Excel)
