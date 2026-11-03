---
article_id: 28999966851991
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: bd54932306d55fdc236f633a654014e58ed7eaae9e4cd696df7c15d1e88e58f0
fetched_at: '2026-06-28T22:37:49.190503+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA713 - Alteração da Data de
  Vencimento do boleto via api
type: support-article
updated_at: '2026-01-07T19:56:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28999966851991-Cross-Segmentos-Backoffice-Linha-Protheus-FINA713-Altera%C3%A7%C3%A3o-da-Data-de-Vencimento-do-boleto-via-api
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28999929060119) Tempo aproximado para leitura: **02:00 min**  
  
**Dúvida**  
É possível alterar a data do desconto no FINA713?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**  
Alteração e Cancelamento de Boletos: Atualmente, apenas os bancos **Banco do Brasil e Itaú** permitem a **alteração** e o **cancelamento** de boletos registrados de forma on-line.

#### **Regras por Banco:**

* **Banco do Brasil**  
  Permite exclusivamente a alteração da **data de vencimento**, por meio dos campos **E1\_VENCTO** ou **E1\_VENCREA**.
* **Itaú**  
  Permite a alteração da **data de vencimento** (**E1\_VENCTO** ou **E1\_VENCREA**) e/ou do **valor do título** (**E1\_VALOR**).  
  Ressalta-se que, por regra do banco, a alteração de boletos do Itaú deve ser realizada obrigatoriamente em **ambiente de produção**, sendo possível alterar apenas boletos que tenham sido originalmente transmitidos nesse ambiente.

#### **Critérios para Transmissão Automática (Boleto On-line)**

Será considerada uma **alteração passível de transmissão automática** (boleto on-line, utilizando o **job FINA713**) somente quando forem alterados **exclusivamente** os campos permitidos para cada banco, conforme descrito acima.

Caso qualquer outro campo do título seja alterado isoladamente ou em conjunto e que não esteja entre os campos contemplados, o sistema **não** tratará a alteração como boleto on-line. Nessa situação, a modificação será considerada uma **alteração padrão via CNAB**, sendo exibida na tela de **Ocorrências CNAB**, e não será acompanhada pelo **Monitor de Pendências**.

#### Alterações via CNAB

É possível gerar instruções de ocorrência de alteração via **CNAB** para boletos que tenham sido registrados on-line (job **FINA713**), inclusive para outros campos, como **histórico**, **juros**, entre outros.  
Entretanto, é imprescindível verificar previamente a viabilidade dessas alterações junto à instituição bancária.

#### **Geração Automática de Ocorrências**

Quando a alteração de boleto on-line estiver em conformidade com as regras dos bancos e com os campos permitidos, ao confirmar a alteração, o sistema gerará automaticamente a instrução correspondente na tabela **FI2**, a qual será acompanhada pelo **Monitor de Pendências**.  
Nesse cenário, não será exibida a tela para inserção manual de ocorrências, como ocorre no processo via CNAB.

As alterações realizadas por meio do **ExecAuto do FINA040** ou pelo **botão Facilitador** seguem a mesma regra.  
Para a geração automática de ocorrências via ExecAuto no processo CNAB, é obrigatório o uso dos **Pontos de Entrada** [**F040VAUT**](https://tdn.totvs.com/pages/releaseview.action?pageId=536718746) e [**A040ATOK**](https://tdn.totvs.com/pages/releaseview.action?pageId=536718676).

### Procedimento para Alteração ou Cancelamento de Boleto Registrado

Para realizar a alteração de um boleto registrado, siga os passos abaixo:

1. Acesse a rotina **Contas a Receber (FINA040)**:  
   **Atualização → Contas a Receber → Contas a Receber**.
2. Posicione-se sobre o título transmitido via **API**, com os campos **EA\_BORAPI = S** e **EA\_TRANSF = S**.
3. Clique em **Alterar**, realize a modificação desejada (por exemplo, a data de vencimento) e confirme a operação.

Após a confirmação, será gravado um registro na tabela **FI2** para o título em questão, com os seguintes campos:

* **FI2\_BORAPI = S**
* **FI2\_OPEAPI = A** (Alteração)

Para **cancelar** o boleto, basta retirar o título do **borderô**. Nesse caso, será gerado um registro na tabela **FI2** com:

* **FI2\_BORAPI = S**
* **FI2\_OPEAPI = C** (Cancelamento)

Ao executar o **job FINA713**, a alteração ou o cancelamento será transmitido ao banco, sendo possível acompanhar o status do processamento por meio do **Monitor de Boletos com Pendências (FINA710)**.

Para os demais bancos, é necessário remover o título do **borderô** para que o cancelamento seja efetivado no sistema, bem como solicitar diretamente à instituição bancária o cancelamento do boleto.

Após a conclusão desse processo, o título deverá ser gerado novamente e retransmitido com os devidos ajustes.

Saiba mais

[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392#Contasareceber(Comunica%C3%A7%C3%A3obanc%C3%A1riaonline)-ALTERA%C3%87%C3%83O/CANCELAMENTODEBOLETOS)
