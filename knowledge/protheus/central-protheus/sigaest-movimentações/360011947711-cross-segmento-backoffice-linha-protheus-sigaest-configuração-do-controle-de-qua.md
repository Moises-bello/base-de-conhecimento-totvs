---
article_id: 360011947711
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ce22c61a2d81f0827f29e0950e183aa5674ed95eec44812a61b6bf9d9c1218fb
fetched_at: '2026-06-28T22:38:53.991277+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração do Controle
  de Qualidade de Materiais no Protheus (MV_CQ)
type: support-article
updated_at: '2026-05-21T21:09:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011947711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-do-Controle-de-Qualidade-de-Materiais-no-Protheus-MV-CQ
---

O Protheus oferece controle de qualidade (CQ) no módulo Estoque/Custos, permitindo inspeção e avaliação de produtos via almoxarifado específico (parâmetro MV\_CQ). Configurações incluem definição de notas mínimas, tipo de CQ, frequência de inspeção por fornecedor e envio automático ao CQ por entrada ou produção. O processo usa a rotina "Baixa do CQ" para liberação ou rejeição dos materiais.

Tempo aproximado para leitura: **00:10:00 min**

**Dúvida**

Como fazer o Controle de Qualidade (CQ) dos produtos no *Protheus*?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Tendo em vista a evolução do controle de materiais, o Módulo *Estoque/Custos* oferece em suas rotinas a opção de Controle de Qualidade. Esta opção envolve toda a movimentação de materiais, permitindo que, mediante parametrizações, os produtos de sua empresa possam ser encaminhados ao Departamento de Controle de Qualidade, sendo inspecionados, avaliados e aprovados ou reprovados para utilização.

Este recurso deve ser utilizado pelas empresas que no recebimento ou fabricação de um produto necessitem verificar as suas especificações técnicas, através de um departamento de controle de qualidade.

Para este controle, o *Protheus* possui um almoxarifado (normalmente “98”, definido través do parâmetro MV\_CQ) destinado ao registro de materiais que estão no Controle de Qualidade e a rotina “Baixa do CQ”, onde é efetuada a liberação ou rejeição dos materiais.

Para utilizar essa funcionalidade, o usuário deve:

***- 1 -*** Definir o parâmetro **“MV\_CQ”** o almoxarifado destinado ao Controle de Qualidade (padrão “98”). **Importante:** Após definido esse parâmetro e realizar movimentações o mesmo não deve ser alterado;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008553172)

***- 2 -*** No Cadastro de Produtos (MATA010), definir os seguintes campos:

**Nota Mínima** (B1\_NOTAMIN) - A pontuação mínima do produto para o Controle de Qualidade, caso queira controlar o envio de materiais ao CQ pela nota.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008588371)

**Tipo de CQ** (B1\_TIPOCQ) - Define se o Controle de Qualidade será feito pelo Módulo de Compras e Estoque/Custos do Sistema Microsiga ou pelo Módulo de Inspeção de Entrada do Sistema Quality.

Se o usuário utilizar o Módulo de Inspeção de Entrada, o material será enviado ao almoxarifado definido pelo parâmetro “MV\_CQ”, porém todo o controle será efetuado no Módulo de Inspeção de Entrada, não sendo possível a liberação ou rejeição do material pela rotina “Baixa do CQ” do Módulo de Estoque/Custos.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008553612)

***- 3 -*** No Cadastro de Amarração Produto X Fornecedor (MATA061) definir os seguintes campos:

**Contr. Lote** (A5\_SKIPLOT) - Trata-se da frequência de inspeção do produto pelo Controle de Qualidade para um determinado fornecedor, isto é, o intervalo de vezes em que o produto deve ser enviado ao CQ.

Exemplo:  
Se um produto adquirido do fornecedor “A” tiver que ser enviado ao CQ a cada 2 compras, o campo ‘Contr. Lote’ deve ser preenchido com “2”. Caso este campo seja preenchido com “1”, o produto será enviado ao CQ todas as vezes em que for comprado e, se for preenchido com ‘0’ (zero), nunca será enviado ao CQ, mediante este critério.

**Nota** (A5\_NOTA) - Nota de avaliação do fornecedor para o produto, caso queira controlar o envio de materiais ao C.Q. pela nota.

Desta forma, cada produto possui uma pontuação mínima para o controle de qualidade. Na digitação da nota fiscal de entrada, é feito uma avaliação entre a pontuação da amarração Produto X Fornecedor e a pontuação do produto. Caso a pontuação da amarração **não atinja** a pontuação do produto, este lote do material será enviado ao almoxarifado do controle de qualidade (especificado no parâmetro MV\_CQ); caso a pontuação da amarração **atinja** a pontuação mínima do Produto, este lote do material passará pelo processo de avaliação do Skip-Lote (se configurado A5\_SKIPLOTE), caso não, será enviado diretamente ao Armazém Padrão (definido na B1\_LOCPAD).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000634081)

***- 4 -*** Quanto à entrada de Material no Armazém de CQ:

* **Por Documento de Entrada (MATA103):**

O TES - Tipo de Entrada e Saída, utilizado na inclusão do documento de entrada deve atualizar o estoque. Certifique-se de que o campo **Atu. Estoque** (F4\_ESTOQUE) no cadastro da TES (MATA080) esteja definido com “Sim”.

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008588751)**

* **Por Produção:**

Para que um produto seja enviado ao CQ quando da sua produção são necessários alguns passos:

- No Cadastro de Produtos o campo B1\_NUMCQPR ("Produções CQ") deve conter o número de intervalos a serem considerados para que a produção seja enviada ao CQ.

Exemplo: Se desejar enviar o produto ao CQ a cada 2 produções este campo deve conter 2. Se o campo for preenchido com 1 todas as produções serão enviadas ao CQ.  
Obs.: A cada produção deste produto será incrementado 1 ao campo B1\_CONTCQP. Quando o valor deste campo for igual ao valor do campo B1\_NUMCQPR a produção será enviada ao CQ e o campo B1\_CONTCQP será zerado.

- O Tipo de Movimentação utilizado (F5\_CODIGO = <500 e F5\_TIPO = "P") deve ter o campo F5\_ENVCQPR ("Envia Produções ao CQ?") preenchido com "S"  
Será enviado ao CQ um produto com os campos supracitados preenchidos corretamente, e onde o Tipo de Movimentação-Produção indicado acima for utilizado.

***5 -*** **Produto sucata configurado na estrutura com o quantidade negativa, sendo direcionado para a baixa do CQ, sendo que o mesmo não tem configuração de qualidade no cadastro do produto:**

Como configurar para que o produto sucata **não seja enviado** para baixa da qualidade, pela rotina MATA175.

É necessário avaliar no configurador se o parâmetro MV\_QIPMAT = N, e também verificar no configurador se o **parâmetro MV\_PRAPONT** esteja configurado como 1 (**Tipo de Movimentação)** alterar parâmetro para o conteúdo igual 2 (**Cadastro de Produto)** dessa forma o produto sucata, negativo na estrutura não será enviado para baixa de qualidade(MATA175).

**Para mais informações sobre o parâmetro:**

[Manufatura - Linha Protheus - SIGAPCP - Parâmetro MV\_PRAPONT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046693993-Manufatura-Linha-Protheus-SIGAPCP-Par%C3%A2metro-MV-PRAPONT)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008553952)

**Veja no vídeo abaixo um exemplo simulado das Configurações necessárias para utilzar a  rotina Baixa de CQ:**

Clique [***nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque) e verifique ***mais detalhes e particularidades*** de utilização da rotina Baixas do CQ (MATA175).  
Caso deseje utilizar o controle de qualidade com intregrações de rotinas no Quality, como por exemplo QIEA215, visualize também a documentação [SIGAQIE - Inspeção de Entradas](https://tdn.totvs.com/pages/releaseview.action?pageId=438288367)

**Saiba mais:**

[SIGAEST - Rotina MATA175 - Instruções padrões sobre Controle de Qualidade no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque)

[Para informações sobre como efetuar a Baixa de C.Q (MATA175) clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011962151-MP-SIGAEST-Como-efetuar-Baixa-do-C-Q-MATA175-)

[*Clique aqui e veja mais artigos sobre Movimentações em Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
