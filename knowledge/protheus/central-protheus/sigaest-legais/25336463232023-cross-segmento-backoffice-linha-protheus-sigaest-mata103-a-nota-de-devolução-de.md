---
article_id: 25336463232023
category: SIGAEST - LEGAIS
content_hash: e2673ab000f55d5550aeb604b8cd9343e1ea1368a10595dc0aea8cf84dd10eff
fetched_at: '2026-06-28T22:38:51.700879+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 A nota de
  devolução de Poder de Terceiros foi recusada, como proceder?
type: support-article
updated_at: '2024-08-01T18:31:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25336463232023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-A-nota-de-devolu%C3%A7%C3%A3o-de-Poder-de-Terceiros-foi-recusada-como-proceder
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25336463203095) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao devolver uma NF de saída de um saldo de terceiros que estava em meu poder foi recusada, como proceder para que não fique com esse impasse no meu Sistema?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus todas as versões.  
  
**Solução**

O Poder de Terceiros requer que todos os itens enviados sejam devolvidos eventualmente, e é um processo de duas etapas, onde nesse cenário a etapa 1 é o recebimento de mercadoria pela (MATA103) - Documento de Entrada, e na etapa 2 a mercadoria é enviada pelo (MATA410) - Pedido de Venda e ambas controlando o poder terceiro (F4\_PODER3 = R/D) através do TES, conforme a documentação abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar o Controle de Poder De/Em Terceiros?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-Controle-de-Poder-De-Em-Terceiros-?source=search)  
  
Quando a NF recusada é emitida, o sistema baixa o poder terceiros e concluiu esse processo. Para esse cenário temos as seguintes possibilidade    
  
**1 - Realizar uma nova remessa no Protheus**.   
Neste cenário ao gerar uma nova NF de remessa, o sistema irá iniciar um novo ciclo de poder terceiros, independente do ciclo anterior. Isso significa que você terá que passar pelo ciclo completo novamente, pois o sistema não associará essa nova remessa à devolução anterior. Em outras palavras, o sistema iniciará um novo processo. Onde após esse nova remessa você poderá realizar a devolução realizando as alterações necessárias.  
  
É essencial avaliar internamente se este novo processo está alinhado com as regras de negócio.  
 **2 - Estornar o Documento no Protheus.**    
Nesse cenário ao você estornar no sistema a NF recusada pelo o cliente, o saldo passa a ficar novamente disponivel na SB6 para a geração de uma nova NF, não sendo necessário reiniciar o ciclo.  
  
No entanto, esse comportamento pode exigir validação interna com sua equipe fiscal, para validação da NF recusada (Possibilidade de cancelamento na SEFAZ), e se a nova NF será enviada ou não para a SEFAZ.  
  
  
É importante saber que o controle de poder de terceiros dentro do sistema (SB6) independe do envio da NF para o SEFAZ, onde apenas a geração do pedido de venda, com a etapa de preparar o documento de saída já é o suficiente para atualizar o saldo poder terceiros.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
