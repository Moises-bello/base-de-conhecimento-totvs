---
article_id: 360000659308
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4c3e04a0c6dcf8c19260dfbdbe4777c974caff396833484b071f373521054649
fetched_at: '2026-06-28T22:38:29.879658+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Restrição de Liberação Manual
  de Pedidos para evitar Estoque Negativo
type: support-article
updated_at: '2026-03-10T11:39:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000659308-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Restri%C3%A7%C3%A3o-de-Libera%C3%A7%C3%A3o-Manual-de-Pedidos-para-evitar-Estoque-Negativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38929268207511)** **Tempo aproximado para leitura:****00:03:00 min**

**Dúvida**  
Como impedir a liberação manual de pedidos de venda para evitar a geração de estoque negativo no faturamento?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

No módulo Faturamento, a melhor prática para evitar que um produto seja faturado sem saldo (gerando estoque negativo) é utilizar exclusivamente a Liberação Automática.

A análise automática bloqueia o pedido ao identificar que não há saldo disponível.

Já a **liberação manual** desconsidera as regras do ERP, "forçando" a saída do item e ignorando bloqueios de crédito ou estoque.

|  |
| --- |
| Assista ao vídeo abaixo para entender o fluxo de bloqueio e como realizar a restrição:  [How To | MP - SIGAFAT - Impedir Liberação Manual de ped. de venda](https://www.youtube.com/watch?v=Heyv6OaJ_cc) |

**Como restringir o acesso à Liberação Manual:**

Para garantir que os usuários não "forcem" a liberação, você deve retirar o privilégio de acesso através do módulo Configurador (SIGACFG):

1. Acesse o **SIGACFG** > Usuários > Senhas > **Privilégios**.
2. Clique em **Incluir**.
3. Na aba **Regras por transação/Rotina**, informe a rotina desejada (Ex: `MATA450`, `MATA455` ou `MATA456`).
4. Na aba **Funcionalidades da transação/Rotina**, selecione a funcionalidade (Ex: **Item 3 - Manual**).
5. Na coluna **Acesso**, altere para **4 - Negado**.
6. Clique em **Confirmar** e associe este privilégio ao usuário ou grupo de usuários desejado.

Ao tentar realizar a liberação manual, o sistema apresentará um aviso de acesso negado, garantindo a integridade do seu estoque.

**Observação 1**: O parâmetro MV\_ESTNEG não possui efeito no módulo Faturamento. Ele é exclusivo para movimentações internas do módulo Protheus Estoque/Custos (SIGAEST).

**Observação 2**: Existe a possibilidade de geração de nota com atualização tardia de estoque, onde o sistema controla a atualização do saldo por meio job  e schedule, para mais informações acesse: [**MP - FAT - Atualização de Estoque tardia na geração da NF de Saída MV\_NFS\_JOB**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020914632-MP-FAT-Atualiza%C3%A7%C3%A3o-de-Estoque-tardia-na-gera%C3%A7%C3%A3o-da-NF-de-Sa%C3%ADda-MV-NFS-JOB)

**Saiba mais:**

* [Retirar Permissões para Liberação Manual do Pedido de Vendas](https://tdn.totvs.com/x/VUBtDQ)
* [Parâmetro MV\_ESTNEG não impede Saldo Negativo na Liberação Manual do Estoque](https://tdn.totvs.com/pages/viewpage.action?pageId=225950880)
* Webinar: [Análise e Bloqueio de Estoque no Faturamento (SIGAFAT)](https://youtu.be/6XfctVxULuY)
