---
article_id: 360019502091
category: SIGAEST - LEGAIS
content_hash: 372a6443399d6d8497bcf303f1927a0b6c28df81d236bf88c180c29f907edda8
fetched_at: '2026-06-28T22:38:51.500037+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como o Protheus gera
  no SPED o Registro K200: Estoque Escriturado?'
type: support-article
updated_at: '2025-12-23T17:06:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019502091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-o-Protheus-gera-no-SPED-o-Registro-K200-Estoque-Escriturado
---

O Registro K200 no Protheus representa o Estoque Escriturado, incluindo produtos da empresa e em poder de terceiros. São enviados produtos dos tipos 00, 01, 02, 03, 04, 05 e 10, excluindo produtos fantasmas. Para gerar o SPED com K200, é necessário configurar documentos e TES específicos para os indicadores de estoque 0, 1 e 2, e gerar o arquivo via rotina SPEDFISCAL com a opção "Gerar Bloco K" ativada.

**Dúvida**  
Como gerar o Registro K200 no Protheus?

[How To | MP - SIGAEST - K200 divergente do Saldo Final do Estoque](https://www.youtube.com/watch?v=4Ykj5v34I7c)

##### [How To MP - SIGAEST - Bloco K Registro K200](https://www.youtube.com/watch?v=d7xyzU14w7s)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**O que é o Registro K200?**

O Registro K200 nada mais é do que o Estoque Escriturado, isto é, o estoque de cada produto na Empresa, além do estoque de produtos que a empresa enviou para um terceiro ou recebeu de um terceiro para ficar em seu poder.

**Estrutura do Registro K200 de acordo com o Manual do EFD:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101613973)**

**Quais produtos são enviados para o Bloco K - Registro K200 do SPED?**

Serão enviados para o Registro K200 apenas os produtos com os Tipos 00, 01, 02, 03, 04, 05 e 10. [Para maiores informações sobre tipos de produtos a serem considerados ou não no Registro K200, clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554) Produtos configurados como Fantasmas (B1\_FANTASM = S) também não serão considerados.

**Indicadores do tipo do Estoque no Registro K200**

0 = Estoque de propriedade do informante e em seu poder;   
1 = Estoque de propriedade do informante e em posse de terceiros (EM terceiros)  
2 = Estoque de propriedade de terceiros e em posse do informante;(DE terceiros em seu poder)

**Passos e premissas para se gerar o SPED com Registro K200 de um Produto (Com um exemplo de produto que contenham os indicadores do tipo de estoque 0, 1 e 2 conforme explicado acima):**

* Ter produto com um dos tipos: 00, 01, 02, 03, 04, 05 e 10;
* Ter feito um um documento de entrada utilizando TES com (F4\_PODER3 = Não Controla) - **Para gerar o indicador do tipo do estoque 0**;

![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015146252)

* Ter feito um Pedido de Venda (MATA410) utilizando TES com (F4\_PODER3 = R); - **Para gerar o indicador do tipo do estoque 1;**  
  ![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015146292)

* Ter feito um um Documento de Entrada utilizando TES com (F4\_PODER3 = R); - **Para gerar o indicador do tipo do estoque 2;**  
  ![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015188631)

* Gerar o SPED (rotina SPEDFISCAL) - Parametrizar a rotina para o período em que vai ser apurado e selecionar a opção **"Gerar Bloco K?" = Sim**, escolher o local e nome do arquivo a ser gerado e confirmar a geração  
    
  ![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015189651)![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015146812)![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015146792)

Ao finalizar a geração será apresentada a informação de sucesso:

![arquivo.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015188111)

Desta forma o SPED gerará, com o Registro K200 da seguinte forma (lembrando que os números são meramente ilustrativos):

|K200|09112018|TESTE K200 01|5,000|0||

|K200|09112018|TESTE K200 01|5,000|1|SA10100000101|

|K200|09112018|TESTE K200 01|20,000|2|SA20100000102|

**Gerando o relatório do Bloco K no Protheus através do relatório MATR241 (Relação do Bloco K Analítico):**

![7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015147232)

![8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015190031)

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais são as tabelas relacionadas para composição do saldo do registro K200 no bloco K?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021629091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-s%C3%A3o-as-tabelas-relacionadas-para-composi%C3%A7%C3%A3o-do-saldo-do-registro-K200-no-bloco-K)

[*Como definir um tipo de produto que não é padrão do Protheus para ser considerado no Registro K200?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554)

[*Clique aqui e saiba mais sobre Legais/Fiscais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
