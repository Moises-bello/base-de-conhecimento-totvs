---
article_id: 360021874551
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2ce6113e8c8da37523bdeb3a2a420926be2197d700f7c76bc33f473aed1f0619
fetched_at: '2026-06-28T22:38:55.437067+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração e Inclusão
  de Documento de Entrada em Trânsito - MV_LOCTRAN
type: support-article
updated_at: '2026-04-08T10:50:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021874551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-e-Inclus%C3%A3o-de-Documento-de-Entrada-em-Tr%C3%A2nsito-MV-LOCTRAN
---

O artigo explica como incluir um documento em trânsito no Protheus, destacando que o processo não é indicado para produtos com controle de localização ou qualidade. O procedimento envolve configurar o armazém de trânsito, criar o armazém, cadastrar o tipo de entrada/saída com transferência em trânsito, incluir e classificar a pré-nota de entrada, e realizar o retorno do saldo em trânsito para o armazém padrão.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21717607254295) Tempo aproximado para leitura: **00:04:15 min**

**Dúvida**

Como incluir um documento em trânsito no *Protheus*?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

|  |
| --- |
| **Observações importantes a serem consideradas antes de implementar essa funcionalidade:** |
| **No padrão este processo** ***não pode ser utilizado*** **nas seguintes situações:**   * Produtos que utilizam o controle de localização **B1\_LOCALIZ=S** (**Controle de Endereços**); * Produtos que utilizam o **Controle de Qualidade (**[**link FAQ**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque)**)** |

Seu objetivo é realizar a transferência do saldo em estoque (gerado pela classificação do pré-documento de entrada) para o armazém de trânsito, bloqueando assim a utilização deste saldo por outro processo, até que seja efetuado o retorno do saldo do armazém de trânsito para o armazém padrão.

Segue abaixo os procedimentos para incluir documento em transito:

* Através do módulo **Configurador** definir qual armazém será tratado como armazém de transito através do parâmetro **MV\_LOCTRAN**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099978854)

* Criar o armazém do processo caso ainda não tenha na base de dados na rotina Locais de Estoque (AGRA045):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38957491415063)

* Selecione a opção **Atualizações/Cadastros/Tipos Entrada e Saída** (**MATA080**) e inclua uma **TES** configurando, na aba "Outros", o campo **Trf.Transito** (**F4\_TRANSIT**), com conteúdo igual a **Sim**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001078662)

* Selecione a opção **Atualizações/Movimentos/Pré-Nota de Entrada** (**MATA140**) e inclua a pré-nota de entrada;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102159273)

* Selecione a opção **Atualizações/Movimentos/Documento de Entrada** (**MATA103**) e realize a classificação da pré-nota de entrada;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001078822)

* Informe a **TES** cadastrada para realizar a classificação da Pré-Nota de Entrada;
* Em **Estoque e Custos**, selecione a opção **Atualizações/Estoque/Saldo em Estoque**(**MATA225**) e visualize o saldo dos armazéns padrão e transito;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102159373)

* Em **Compras**, selecione a opção **Atualizações/Movimentos/Documento de Entrada**(**MATA103**) e realize o processo de retorno do saldo em trânsito, clicando em **"Outras Ações"** -> "**Docs. Em Trânsito"**;
* A janela **Retorno de Documentos em Trânsito** é exibida. Clique em **Outras Ações** e em seguida no botão **Atualizar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18206931092247)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18206950801943)

 Os campos **Documento** e **Série** permitem selecionar um documento específico;

* O documento em trânsito é exibido;

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102159753)

* Marque o documento em trânsito e confirme o retorno;
* Em **Estoque e Custos**, selecione a opção **Atualizações/Estoque/Saldo em Estoque**(**MATA225**) e visualize o saldo dos armazéns padrão e transito. Observe que o saldo que estava em trânsito foi transferido para o armazém original.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001079462)

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
