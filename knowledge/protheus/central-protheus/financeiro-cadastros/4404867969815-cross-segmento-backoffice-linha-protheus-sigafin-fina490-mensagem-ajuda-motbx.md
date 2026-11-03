---
article_id: 4404867969815
category: Financeiro - Cadastros
content_hash: 0a7fe9745b92075d2c9f00e0938a1c12b4f370311881473f2c5ad2d2ac756eb8
fetched_at: '2026-06-28T22:37:53.096115+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -SIGAFIN - FINA490 - MENSAGEM AJUDA:
  MOTBX'
type: support-article
updated_at: '2026-03-26T11:16:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404867969815-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA490-MENSAGEM-AJUDA-MOTBX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39306922360087) Tempo aproximado para leitura: **00:05 min**

**Ocorrência**  
No processo da substituição (FINA050/FINA750), ao confirmar, aparece a seguinte mensagem:  
MENSAGEM AJUDA: MOTBX

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404859248663)  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 17  
  
**Solução**  
O help é exibido porque o motivo de baixa mencionado na mensagem não está cadastrado na tabela **SIGAADV.MOT**.

Para correção, acesse a rotina **FINA490** e realize o cadastro do motivo de baixa informado, conforme a imagem de referência. Após a inclusão, execute um novo teste para a substituição do título.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404859315351)

Para criar um novo motivo de baixa, é importante verificar:

* Se o motivo irá movimentar banco;
* A qual carteira ele pertence (Pagar, Receber ou Ambas);
* Se haverá geração de cheque;
* Se incide comissão bancária.

Realize o cadastro conforme essas definições.

Após a criação do novo motivo de baixa, será necessário efetuar **log off** e acessar o sistema novamente para que o cadastro passe a ser considerado nas rotinas.

**Saiba mais**  
[MP - SIGAFIN- Como ordenar os motivos de baixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015878251-MP-SIGAFIN-Como-ordenar-os-motivos-de-baixa?source=search)  
[MP - SIGAFIN - Motivo de baixa corrompido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018384491-MP-SIGAFIN-Motivo-de-baixa-corrompido?source=search)
