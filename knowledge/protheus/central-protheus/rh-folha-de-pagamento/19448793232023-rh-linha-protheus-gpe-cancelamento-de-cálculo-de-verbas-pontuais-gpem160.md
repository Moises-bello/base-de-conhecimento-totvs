---
article_id: 19448793232023
category: RH - Folha de Pagamento
content_hash: 75c52e4e271a8272e36b048960a1db4c3e86144d25d1bc43b73f251fc821b360
fetched_at: '2026-06-28T22:44:12.156403+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cancelamento de cálculo de verbas pontuais GPEM160
type: support-article
updated_at: '2025-04-22T18:50:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19448793232023-RH-Linha-Protheus-GPE-Cancelamento-de-c%C3%A1lculo-de-verbas-pontuais-GPEM160
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19448811710487) Tempo aproximado para leitura: **00:01:00 min** **Ocorrência**Não é mais possível efetuar o cancelamento de cálculo de verbas pontuais na rotina Cancelamento de cálculo GPEM160.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.33.  
  
**Causa**  
A rotina GPEM160 permite excluir apenas uma verba do cálculo de folha, o que deixa o cálculo divergente quando é excluído uma verba de provento ou desconto, por exemplo, já que o líquido ficará divergente com as verbas restantes.  
  
**Solução**A rotina GPEM160 não irá mais efetuar filtro de verba e/ou tipo ao efetuar a exclusão do cálculo de folha, efetuando a exclusão de todos os registros da tabela SRC do funcionário.   
Ao fim do processamento, será exibido um log contendo a matrícula de todos os funcionários que tiveram a exclusão do cálculo da folha.

**Importante:** Dessa forma, **todas** as verbas geradas na tabela SRC serão excluídas, sendo necessário efetuar o recálculo da folha do funcionário. Trata-se de uma **mudança** de conceito que visa evitar que o cálculo de folha do funcionário fique incorreta.

No entanto, essa mudança aplica-se apenas para a exclusão na tabela SRC; para a exclusão na tabela RGB ou SRK, o conceito antigo permanece, sendo possível excluir apenas uma ou algumas verbas, pois essas tabelas são intermediárias e não são a tabela final de cálculo. No entanto, para que a mudança reflita na folha, ainda sim continuará necessário efetuar o recálculo da folha.

Observe ainda que se na rotina GPEA580 de Lançamentos por Funcionário for efetuado a exclusão manual de uma verba que já foi calculada na folha, será exibido um aviso solicitando que seja efetuado recálculo para que a alteração reflita na folha. E no relatório da folha é possível avaliar divergências entre o líquido apurado e os proventos/descontos.  
  
  
**Saiba mais**  
Para adquirir maior conhecimento acesse o **link** abaixo  
[DT Cancelamento de cálculo da folha](https://tdn.totvs.com/pages/viewpage.action?pageId=698627791)  
[RH - Linha Protheus - GPE - Como efetuar cancelamento de cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052940993)
