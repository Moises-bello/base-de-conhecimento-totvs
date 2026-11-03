---
article_id: 4418090784535
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 2c26890138b8baac549f4f605680e01d838d7a93422f1a5d9828632e225a02f6
fetched_at: '2026-06-28T22:37:21.645992+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar medição
  de contrato ?
type: support-article
updated_at: '2026-05-13T17:17:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418090784535-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-medi%C3%A7%C3%A3o-de-contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33642873085719) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como realizar medição de contrato ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Consulte os nossos videos How To:

[How To | MP-SIGAGCT - Medição - Gerando um Pedido](https://youtu.be/sPesGrjQTnc)

[How To | MP-SIGAGCT - Medição - Gerando um Título Financeiro](https://youtu.be/1kQBtPUvKiU)

A Medição de Contrato pode ser realizada para um contrato que após incluído tenha seu Status como "Vigente".

É realizada através da rotina Nova Medição (CNTA121) em Atualizações->Contratos->Nova Medição (CNTA121) na opção "Incluir":

***Obs:***

A opção Medição (CNTA120) estará descontinuada a partir de 04/04/2022.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418106434071)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418106442263)

Informar o Contrato no campo referente:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418090737047)

Selecionar a planilha que será medida e preencher os camps odos itens conforme o tipo de contrato e planilha do contrato e a necessidade de medição:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418098540695)

Após confirmar a medição ficará em Aberto, necessitando ser encerrada para finalizar o processo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418106498327)

Quando "em Aberto" a medição pode ser excluída na opção "Outras Ações->Excluir":

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418090757143)

Para encerrar a medição, deve-se utilizar a opção "Outras Ações->Encerrar":

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418098548247)

Ao encerrar a medição é gerado o Documento que foi definido para ser gerado podendo ser um Titulo (A Pagar se for Contrato de Compra, ou "A Receber" se for Contrato de Venda) ou Pedido (de Compra ou de Venda conforme o tipo de Contrato:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418106527383)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418098698519)

**Dúvidas Frequentes:**

**Obs:**

Para configuração se na medição será gerado Pedido ou Título orientamos a verificação do artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como configurar o Gestão de Contratos para gerar Títulos Financeiros ou Pedidos no encerramento da medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037188314-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-configurar-o-Gest%C3%A3o-de-Contratos-para-gerar-T%C3%ADtulos-Financeiros-ou-Pedidos-no-encerramento-da-medi%C3%A7%C3%A3o-?source=search)

**Obs2:**

Após incluir e encerrar a medição, o saldo do contrato é consumido ?

R. Sim. Ao encerrar a medição, o sistema gera automaticamente um **Pedido** (de Compra ou Venda) ou um **Título** (a Pagar ou a Receber), de acordo com o tipo de contrato e a configuração do campo **CNE\_PEDTIT** reportado no artigo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como configurar o Gestão de Contratos para gerar Títulos Financeiros ou Pedidos no encerramento da medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037188314-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-configurar-o-Gest%C3%A3o-de-Contratos-para-gerar-T%C3%ADtulos-Financeiros-ou-Pedidos-no-encerramento-da-medi%C3%A7%C3%A3o?source=search)

Essa movimentação impacta diretamente o contrato, **consumindo o saldo correspondente** ao valor medido.

**Obs3:**

Gostaria de saber em quais condições o sistema permite a edição manual dos campos CND\_PARC1 e CND\_DATA1 em tela, no cabeçalho da medição ?

**R:** Para utilização dos campos na mediçãoé necessário utilizar a  Condição de Pagamento "Tipo 9". Veja mais detalhes nas documentações abaixo:

[- Mensagem TMKTIP905 - A quantidade de parcelas não está compatível](https://tdn.totvs.com/pages/releaseview.action?pageId=225950783)

[- Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ocorrência do Help TMKTIP905 ao encerrar uma medição no Uso da Cond. Pagamento Tipo 9 – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016092392-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ocorr%C3%AAncia-do-Help-TMKTIP905-ao-encerrar-uma-medi%C3%A7%C3%A3o-no-Uso-da-Cond-Pagamento-Tipo-9)

***Saiba Mais:***

[DT Informações adicionais na consulta padrão da Medição](https://tdn.totvs.com/x/WaPAKQ)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Rotina Nova Medição CNTA121](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037700393)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como configurar o Gestão de Contratos para gerar Títulos Financeiros ou Pedidos no encerramento da medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037188314-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-configurar-o-Gest%C3%A3o-de-Contratos-para-gerar-T%C3%ADtulos-Financeiros-ou-Pedidos-no-encerramento-da-medi%C3%A7%C3%A3o-?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Trilha de Videos Gestão de Contratos Básico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008598705431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Trilha-de-Videos-Gest%C3%A3o-de-Contratos-B%C3%A1sico?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
