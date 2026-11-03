---
article_id: 31464500018071
category: esocial - Periódicos
content_hash: a5a5ff7b466ca06ebf72e5513559cb71dab92d1960098f1133c1f4c377ceb732
fetched_at: '2026-06-28T22:47:09.204838+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Como informar devolução do plano de saúde nos eventos
  S-1200 e S-1210
type: support-article
updated_at: '2026-02-23T10:58:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31464500018071-RH-RM-FOP-eSocial-Como-informar-devolu%C3%A7%C3%A3o-do-plano-de-sa%C3%BAde-nos-eventos-S-1200-e-S-1210
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31464500007959) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar a devolução de plano de saúde, nos casos em que o valor de uma mensalidade ou desconto de coparticipação foi lançado incorretamente em uma competência anterior?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as releases.  
  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Acesse o menu Folha Mensal | Lançamentos | Retificação da Folha de Pagamento, conforme print abaixo:

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_19-27-31.png?version=1&modificationDate=1744328004237&api=v2)

2. No nosso exemplo, estamos na competência 05/2024. No período 1, foi descontado o valor de R$100,00 de plano de saúde para o funcionário na competência 04/2024, porém o valor correto seria R$50,00.

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_19-29-28.png?version=1&modificationDate=1744328004153&api=v2)

3. Criação do evento de ajuste:  
Foi criado um evento do tipo **provento**, com o **Código de Cálculo (CC) "14-Assistência Médica"** e rubrica **"9219 - Desconto de assistência médica ou odontológica"**.

O evento poderá utilizar fórmula customizada para retorno automático do valor já pago ou como alternativa, o valor poderá ser informado manualmente, conforme a estratégia adotada pela empresa para controle do ajuste.

**Tratamento do histórico de Assistência Médica**

Importante destacar que o processo de retificação não gera automaticamente o valor negativo no Histórico de Assistência Médica, que representa o ajuste necessário para geração dos encargos: Informe de Rendimentos, eSocial dentre outros.

Dessa forma, a inclusão do valor negativo deverá ser realizada por uma das seguintes formas:

* + Lançamento manual no Histórico de Assistência Médica; ou
  + Importação do Histórico de Assistência Médica, utilizando o processo específico de importação.

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_19-32-4.png?version=1&modificationDate=1744328004080&api=v2)

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_19-37-4.png?version=1&modificationDate=1744328004007&api=v2)

4.Após o lançamento da retificação, a competência 04/2024 passou a conter os seguintes envelopes:

Envelope original (1): com o desconto de R$ 100,00 referente à assistência médica.

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_19-38-58.png?version=1&modificationDate=1744328003920&api=v2)

**Envelope de retificação (10000):** com o valor do estorno da assistência médica, corrigindo o desconto indevido.

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_19-40-21.png?version=1&modificationDate=1744328003840&api=v2)

5. No menu **Administração de Folha de Pagamento | Funcionário | Anexos | Históricos | Histórico Assistência Saúde**, ficará conforme abaixo:

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_21-38-35.png?version=1&modificationDate=1744331915673&api=v2)

6. Na competência **05/2024**, foi lançado o valor líquido referente à devolução do desconto de assistência médica ao funcionário, efetuando a devolução na competência atual.

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_19-49-6.png?version=1&modificationDate=1744328003770&api=v2)

7. Na fila de eventos, foram gerados **dois XMLs** de retificação para a competência 04/2024, que deverão ser enviados para atualizar corretamente o desconto de assistência médica do funcionário.

**S-1200:** contendo o envelope 10000, com o evento de estorno da assistência médica.

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_20-29-45.png?version=1&modificationDate=1744328003680&api=v2)

**S-1210:** com o detalhamento correto do plano de saúde, refletindo o valor ajustado após a retificação.

![](https://tdn.totvs.com/download/attachments/931626352/image-2025-4-10_20-32-44.png?version=1&modificationDate=1744328003573&api=v2)
