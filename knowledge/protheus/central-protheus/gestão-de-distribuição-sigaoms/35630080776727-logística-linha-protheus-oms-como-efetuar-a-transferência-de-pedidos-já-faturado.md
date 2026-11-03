---
article_id: 35630080776727
category: Gestão de Distribuição (SIGAOMS)
content_hash: 68670ee8329c3183ce6ec050a06d25664da96cdb273837dc228857867c25ab2e
fetched_at: '2026-06-28T22:45:49.677644+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como efetuar a transferência de pedidos
  já faturados entre cargas
type: support-article
updated_at: '2026-04-08T18:29:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35630080776727-Log%C3%ADstica-Linha-Protheus-OMS-Como-efetuar-a-transfer%C3%AAncia-de-pedidos-j%C3%A1-faturados-entre-cargas
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35630080760727)Tempo aproximado para leitura: 00:01:30 min  
  
**Dúvida**  
Como efetuar a transferência de pedidos já faturados entre cargas?  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - A partir da versão 12.1.2510  
  
**Solução**  
Na rotina **Montagem de Cargas - OMSA200** é possível realizar a transferência de pedidos já faturados entre cargas, desde que algumas validações sejam atendidas.  
  
**Validações necessárias:**

* As cargas de origem e de destino devem estar **totalmente em aberto** ou **totalmente faturadas**.
* Não é permitida a transferência de pedidos em cargas integradas ao **SIGAGFE**.
* Também não é permitida a transferência em cargas integradas aos sistemas **TOL** e **TRE**.

**Exceção – Integração com Coleta Entrega:**  
  
A transferência será permitida somente quando:

* A nota fiscal vinculada ao pedido estiver com o status **FINALIZADA\_COM\_INSUCESSO.**
* A carga de destino não estiver integrada ao **Coleta Entrega SaaS**.

**Procedimento:**

1. Acesse a rotina **OMSA200**.
2. Navegue até **Carregamento > Manutenção**.
3. Selecione o pedido de venda que deseja transferir.
4. Clique no campo **Cod. Carga**.
5. Informe o código da carga de destino.

![tela_1_manut_carga.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/39544486427031)

**Importante**  
Para habilitar a manutenção de cargas faturadas, configure o parâmetro **MV\_MANCARG = S**.

**Saiba mais**  
Para mais informações, consulte o Boletim Técnico: [Transferência de pedidos entre Cargas](https://tdn.totvs.com/pages/releaseview.action?pageId=889684037)  
  
**Glossário**  
SIGAGFE - Gestão de Frete Embarcador  
TOL - Totvs Otimização e Logistica  
TRE - Totvs Roteirização e Entregas
