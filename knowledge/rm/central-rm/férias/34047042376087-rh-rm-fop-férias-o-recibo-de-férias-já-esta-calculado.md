---
article_id: 34047042376087
category: Férias
content_hash: e1cbcf5486bcbd3156e76e8c5d662f3a70089fb6792864dcdd4fe839d726d485
fetched_at: '2026-06-28T22:46:56.141416+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: O recibo de férias já esta calculado'
type: support-article
updated_at: '2025-08-08T17:33:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34047042376087-RH-RM-FOP-F%C3%A9rias-O-recibo-de-f%C3%A9rias-j%C3%A1-esta-calculado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34047042338583) Tempo aproximado para leitura: **00:01:36 min**  
  
**Ocorrência**  
No módulo Folha de Pagamento, ao tentar modificar o cadastro das férias, é apresentada a mensagem de erro: **"O recibo de férias já esta calculado, para modificar o cadastro de férias é necessário excluir o recibo"**. Como corrigir? 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34046984583959)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O erro ocorre porque as férias já estão na situação M (Marcadas) ou seja, já foram processadas e calculadas e possuem recibo gerado.

O sistema não permite edição direta de férias marcadas, pois isso comprometeria a integridade dos cálculos já realizados.  
  
**Solução**  
Para realizar qualquer alteração no cadastro de férias, siga os passos abaixo:

1.  Acesse o menu **Férias | Cancelamento**, selecione  o colaborador e cancele o processo de férias já marcado, conforme a documentação orienta: [RH - RM - FOP - Férias: cancelamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421071626007-RH-RM-FOP-F%C3%A9rias-cancelamento)

2.  Após o cancelamento, retorne ao cadastro de férias e refaça o lançamento com os dados corretos (datas, dias, período, etc.).

Importante ⚠️

Modificar férias sem cancelamento prévio pode gerar inconsistências nos recibos e nos cálculos da folha. Por isso, sempre realize o cancelamento antes de qualquer ajuste.

**Saiba Mais:**

[RH - RM - FOP - Férias: Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6044826136727-RH-RM-FOP-F%C3%A9rias-C%C3%A1lculo)
