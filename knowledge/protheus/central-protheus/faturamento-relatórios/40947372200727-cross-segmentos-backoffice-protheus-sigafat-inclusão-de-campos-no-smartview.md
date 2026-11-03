---
article_id: 40947372200727
category: FATURAMENTO - RELATÓRIOS
content_hash: 0e5bb3f497242bbf1283fdd28198903babfcc37c108aadb4f24792c15559dde5
fetched_at: '2026-06-28T22:38:22.945027+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Inclusão de Campos no SmartView
type: support-article
updated_at: '2026-06-12T22:13:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40947372200727-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Inclus%C3%A3o-de-Campos-no-SmartView
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40947388196247) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**

Como incluir campos padrões ou customizados no SmartView do módulo Faturamento (SIGAFAT)?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Ao implementar o Smart View, é possível que alguns campos necessários para a sua operação não estejam disponíveis no Objeto de Negócio padrão.

Nesses casos, a Personalização de Campos de visões do Protheus permite alguns recursos para adicionar estes campos.

|  |
| --- |
| Assista o vídeo HowTo para mais detalhes:  [How To | MP - SIGAEST - Inclusão de Campos no SmartView](https://www.youtube.com/watch?v=HelxcMHLmCA) |

**Pré-requisitos para Campos Customizados:**

* Para que um campo (padrão ou customizado) apareça na listagem de estrutura, ele precisa obrigatoriamente estar configurado como "Usado" na tabela SX3 (Dicionário de Dados).
* Não é possível adicionar campos do tipo MEMO ou Virtual.
* **IMPORTANTE**: Após a confirmação da inclusão do campo no Objeto de Negócio, não será possível excluí-lo, devido a possibilidade dele estar sendo utilizado em algum recurso ativo do Smart View. A tentativa de exclusão forçada do campo pode causar erros graves de execução no sistema.
* Caso o relatório não permita a edição verifique as orientações da documentação:   
   [Criar campo em relatório Smart View com proprietário Smartview.Owner](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37481314839831-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Criar-campo-em-relat%C3%B3rio-Smart-View-com-propriet%C3%A1rio-Smartview-Owner)

**Passo a Passo para Inclusão:**

1 - Acesse pelo configuração, na opção Ambiente > Smartview > Integração Smartview

2 - No canto superior esquerdo, clique no ícone "P. Campos":

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40947372170519)

3 - Procure pelo Objeto de Negócio a qual deseja personalizar, em seguida clique em "Editar":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40947388198295)

4 - Procure pela Tabela e Campo a qual deseja incluir no Objeto de Negócio selecionado e clique em "Adicionar":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40947388199447)

**Observação 1:**

A inclusão de campos através da opção Personalização de Campos impacta exclusivamente a **Visão de Dados (listagem)** do SmartView.

Essa personalização **não altera automaticamente o layout da Visão de Design (Relatório/PDF)**. Os relatórios analíticos possuem um modelo de apresentação próprio e, para que novos campos sejam exibidos no PDF, é necessário realizar a personalização do design do relatório. Para maiores informações orientamos contatar a equipe Protheus Framework.

**Saiba mais:**

* [Amarração Protheus x Smart View](https://tdn.totvs.com/x/Nbs0Kg)
* [Configuração do SmartView](https://tdn.totvs.com/x/8WTCMQ)
* [Ocorrências no Smart View](https://tdn.totvs.com/x/WoyLN)
* [Design de Relatórios](https://tdn.totvs.com/x/Us_cM)
* [Iniciando o Fluxo de Criação de Recursos](https://tdn.totvs.com/x/Sv_WK)
