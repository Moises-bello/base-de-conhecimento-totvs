---
article_id: 19123604642199
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 53b2f371674a1e3d9026555a1f41886b3362585aaa8b70666f97536f71b88691
fetched_at: '2026-06-28T22:38:54.303469+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Apontamento de OP
  parcial com RE5 - Informa Saldo Insuficiente.
type: support-article
updated_at: '2023-11-17T10:27:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19123604642199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Apontamento-de-OP-parcial-com-RE5-Informa-Saldo-Insuficiente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19123550613143) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Quando se possui uma TM com a caracteristica, de atualizar os empenhos, e se efetua um documento de entrada contra OP, se gera um movimento do tipo RE5.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**

**Dada situação com o seguinte exemplo:**

MATA200 - Criar uma estrutura 1 para 1.   
MATA220 - Criar um saldo zerado para o armazém 10 para um produto matéria prima.   
MATA650 - Incluir uma OP com quantidade 15,00 e no momento que gera os empenhos altera o armazém 01 para 10 em um das materias primas e salvar.   
MATA103 - Criar uma nota de entrada para materia prima no armazém 10 vinculando a OP e salvar, nesse momento gera RE5 de quantidade 10.00.   
MATA103 - Criar uma outra nota de entrada para outra materia prima dando saldo no armazém 01 e salvar.   
MATA250 - Faço a inclusão do apontamento vinculando a OP e mudando a quantidade para 10.00 e salvo nesse momento sera apresentado a seguinte mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19123589463447)

Nesse caso, o cenário reportado não caracteriza uma não conformidade no produto, mas sim o comportamento esperado quando o usuário realiza um apontamento parcial de ordem de produção.

Pelo fato de utilizar a configuração para baixa automática de empenhos, ao realizar o apontamento o sistema realiza o cálculo da baixa a ser realizada conforme sua configuração de proporcionalização, conforme citado em nossa documentação:

[Manufatura - Linha Protheus - SIGAPCP - Cálculo realizado para a requisição do material no apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027252794-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-realizado-para-a-requisi%C3%A7%C3%A3o-do-material-no-apontamento%5D)

Independente de outras baixas de empenhos que já tenham sido realizadas anteriormente.

O mesmo cenário acontece caso a baixa contra OP seja realizada através de movimentação interna contra OP.

Dúvidas adicionais sobre esse processo podem ser sanadas com o time responsável pelo processo (Manufatura).

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
