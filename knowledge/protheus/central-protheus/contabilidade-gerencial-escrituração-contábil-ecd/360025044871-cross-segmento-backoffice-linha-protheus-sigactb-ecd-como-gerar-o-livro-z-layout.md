---
article_id: 360025044871
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 0a61b35565924fa50804b4d1c703b452d07ec3eeee7276a33bbe37fa0f30001b
fetched_at: '2026-06-28T22:40:44.793904+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB ECD COMO GERAR O LIVRO
  Z (Layout parametrizável)
type: support-article
updated_at: '2024-04-26T13:00:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025044871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-COMO-GERAR-O-LIVRO-Z-Layout-parametriz%C3%A1vel
---

**Dúvida**Como gerar o livro Z da ECD no Protheus?  
  
**Ambiente**Protheus– Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

* Registro I510: Definição de Campos do Livro Razão Auxiliar com Leiaute Parametrizável       Rotina CTBS100 (Cad. Layout auxiliares)

Neste registro devem ser informados os campos que serão utilizados no livro “Z” (Livro Razão Auxiliar com Leiaute Parametrizável), tais como: nome do campo, descrição do campo, tipo (numérico ou caractere), tamanho do campo, quantidade de casas decimais e largura da coluna na impressão.  
Os campos devem ser informados, neste registro, na mesma ordem em que devam figurar da visualização/impressão. O conteúdo dos campos especificados no registro I510 será informado no  registro I550.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023391332)

* Registro I550: Detalhes do Livro Razão Auxiliar com Leiaute Parametrizável Informa o conteúdo dos  campos especificados no Registro I510
* [Pelo artigo de lei, este livro deve ser custormizado pelo cliente. Dentro do Protheus, disponibilizamos uma interface de integração e importação de livros. Esses livros devem seguir um padrão, conforme os modelos disponibilizados neste topico.](https://tdn.totvs.com/pages/releaseview.action?pageId=6068513)
* Veja [Modelo de Layout](https://tdn.totvs.com/download/attachments/6068515/Mon+May+21+18%3A22%3A53+BRT+2012Layout_Exemplo.xls?version=1&modificationDate=1337635373262)e [Modelo de Criação para cadastramento do layout do razão auxiliar](https://tdn.totvs.com/pages/releaseview.action?pageId=6068515)

Configurar um arquivo TXT, com o conteúdo dos campos criados na rotina CTBS100

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14550172336023)

Na Central de escrituração (CTBS001) + IMP RAZAO, na tela seguinte será relacionado o layout e txt configurado.

![](https://totvssuporte.zendesk.com/attachments/token/QMBNGJqZJjHkZCGqpArFHOwa0/?name=inline-507911471.png)

Para livros A ou Z, clique em **Sel. Conta**. Será apresentada tela para cadastro manual e/ou importação do plano de contas a serem utilizadas no registro I015. Informar conta sintética.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025167411)

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025836991-MP-SIGACTB-ECD-REGISTRO-I015-LIVRO-A-ou-Z?source=search>

Sistema irá gerar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14550225461783)

Importante!

1) No TXT o primeiro “Pipe” (|) deve corresponder ao primeiro campo criado no I510, ou seja, não precisa digitar "|I550|" pois o xml irá preencher todas as linhas com o registro.

2) Deve ser definido em quantidade de caracteres, respeitado o tamanho da fonte definido no registro I500 e o espaço de um caractere entre as colunas. (Padrão com tamanho 7).

3)Para campos numéricos, considerar também os separadores de milhar e a vírgula. Considerar que o livro será impresso/visualizado em papel A4, com a orientação paisagem, margens de 1,5 cm e com fonte Courier.

Essa documentação demonstra somente um exemplo , veja no manual da receita como estrutura o Layout e quais o campos deve ser preenchidos.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099409053)

Manual ECD 2019 :

<http://sped.rfb.gov.br/arquivo/show/2911>
