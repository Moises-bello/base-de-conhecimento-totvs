---
article_id: 4408224140951
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c46ccf507e097b6d2ccb64a35940e252ac6205ee697e5c32c4a04bd56ec3585d
fetched_at: '2026-06-28T22:37:22.890000+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CN130NOIT ao utilizar
  a rotina de Medição pela CNTA120
type: support-article
updated_at: '2022-02-09T11:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408224140951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CN130NOIT-ao-utilizar-a-rotina-de-Medi%C3%A7%C3%A3o-pela-CNTA120
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Ocorrência da Mensagem " CN130NOIT" na utilização da rotina de Medição pela CNTA120

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408219014935/mceclip2.png)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**Abaixo mostramos as possibilidades mapeadas da ocorrência deste Help CN130NOIT:

**- Possibilidade 1:**  
No modo padrão do sistema, ao inserir um tipo de contrato, cujo campo: **Med. Eventual=Sim**,  automaticamente o conteúdo do campo:  **"Cronog Fis"*(CN1\_CROFIS)***, ficará como **2=Não.**

Certifique-se quanto ao conteúdo do campo "***Cronog Fis" (CN1\_CROFIS)***, pois  via padrão do sistema, o mesmo sempre  será marcado como Não,  uma vez que o campo "***Med. Eventua*l" *(CN1\_MEDEV)*** for informado como Sim.

Atenção: Caso o campo "***Cronog Fis"(CN1\_CROFIS)*** esteja informado como ***"Sim"*** nesta situação, o mesmo pode ter sido inserido via banco, o que ocasionará o disparo do ***Help CN130NOIT***, ao incluir a medição.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408230392471/mceclip3.png)

Caso necessário, para verificar esta condição relatada acima em que os campos devam estar, realizar o  teste com o cadastro de um novo Tipo de Contrato pela rotina padrão atualizada ***CNTA021***, com o sistema atualizado com os pacotes de Expedição Continua do Gestão de Contratos mais atuais disponíveis, onde constam as validações existentes no cadastro para este cadastro.

**- Possibilidade 2:**

Será necessário verificar na tabela itens da planilha do contrato (**CNB**), o campo saldo da medição (**CNB\_SLMED**).

Verificar para todos os itens deste contrato se este campo está zerado.

Vejamos o cálculo para preencher o campo corretamente:  
  
**CNB\_QUANT - CNB\_QTDMED = CNB\_SLDMED**

(**QUANTIDADE**) - (**QUANTIDADE MEDIDA**) = **SALDO PARA MEDIR**  
  
Vejam as possibilidades do resultado do cálculo informado:

* Se o resultado do CNB\_SLDMED >= 1, então coloque o resultado direto no banco. Assim será possível medir até esta quantidade (quantidade do resultado do cálculo acima).
* Se CNB\_SLDMED = 0, então não há saldo para o mesmo. Terá que realizar revisões para acréscimos de saldo.
* Se CNB\_SLDMED < 0, será importante um consultor em campo para lhe auxiliar no rastreamento do que houve em seu contrato que o valor ficou negativo. As possíveis causas são manipulações direto no banco forçado sem avaliar antes os impactos do mesmo, pontos de entradas.

***Saiba Mais:***

* [MP - SIGAGCT - Principais Atualizações do Módulo de Gestão de Contratos (Expedição Contínua)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028332351)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Reajuste de Saldo em contratos, planilhas e cronograma financeiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
