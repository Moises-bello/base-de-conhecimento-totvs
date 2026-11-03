---
article_id: 4411443277719
category: Manutenção de Ativos (SIGAMNT)
content_hash: 07735b7d58c07d9a5414756013af5e4122bc6e7d9d3ddf3834d144bc4bcf4b48
fetched_at: '2026-06-28T22:42:34.145756+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Inconsistências - MNTA845
type: support-article
updated_at: '2021-10-27T14:45:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411443277719-Manufatura-Linha-Protheus-MNT-Inconsist%C3%AAncias-MNTA845
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min  
  
Dúvida**Para que serve a rotina **Inconsistências - MNTA845**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**A rotina **Inconsistências - MNTA845** tem por objetivo corrigir inconsistências geradas no **Cadastro de Multas - MNTA765**, criando uma tela que exibe qual o erro e logo abaixo uma ou mais multas que devem ser corrigidas. Ao imprimir será gerado um relatório exibindo o erro e as multas com este erro.  
  
Existem 4 tipos de inconsistências, são elas:

* **Inconsistência de Data** - quando a **Data da notificação** é maior que 30 dias após a **Data da infração**.
* **Inconsistência de Local** - quando o **Local** não bate com a rota, necessário integração com o **TMS - Sistema de Gerenciamento de Transporte**.
* **Inconsistência de Recurso** - quando o campo **Cabe Recurso -** **TRX\_CABREC** está como **Sim**, mas não existe um recurso cadastrado.
* **Pendência de Restituição** - quando a multa está paga, classificada como recurso deferido e indicando também um pedido de restituição em aberto.

**Saiba mais**Acesse a documentação completa da rotina no *link* [Inconsistências - MNTA845](https://tdn.totvs.com/pages/viewpage.action?pageId=438276198)[.](https://tdn.totvs.com/pages/viewpage.action?pageId=435111882)
