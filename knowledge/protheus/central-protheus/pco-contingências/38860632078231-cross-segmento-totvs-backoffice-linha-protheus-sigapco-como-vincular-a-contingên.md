---
article_id: 38860632078231
category: PCO - Contingências
content_hash: ede27f3289cc0a7860fd970b5f59bfe3cf99254fb96d632c0592b8185d4e22f6
fetched_at: '2026-06-28T22:37:12.170776+00:00'
product: protheus
section_id: 1500001539761
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - Como Vincular
  a Contingência ao Processo Solicitante
type: support-article
updated_at: '2026-03-09T12:36:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38860632078231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPCO-Como-Vincular-a-Conting%C3%AAncia-ao-Processo-Solicitante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38860595614615) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
É possível a contingência  amarrada ao lançamento que a originou, evitando que seja aplicada em outro documento?  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - A partir da versão 12  
  
  
**Solução**  
Atualmente, o comportamento padrão do sistema vincula a contingência de maneira abrangente, não vinculando ao processo originador, mas empenhando o saldo na solicitação.   
  
Para garantir a exclusividade desse saldo ao processo solicitante, impedindo o consumo do orçamento já validado por outros processos ou usuários, a alternativa sistêmica recomendada é a utilização do processo de Empenho de Contingência.   
  
Ao empenhar o valor na solicitação, você assegura a reserva exata daquele saldo orçado no sistema.

Para preparar o módulo Planejamento e Controle Orçamentário (SIGAPCO) para a utilização de bloqueios e contingências com empenho, siga o roteiro abaixo:

1. Acesse o configurador e certifique-se de que o parâmetro `MV_PCOSDCT` (que controla o saldo de contingência) tenha seu conteúdo configurado como verdadeiro (`.T.`).
2. Cadastre os bloqueios e lançamentos referentes aos processos que exigem controle.
3. Realize o cadastro do lançamento de LIBERAÇÃO DE SOLICITAÇÃO DE CONTINGÊNCIA (Processo 000356 - Item 002)
4. Configure o Item 02 deste processo (Liberação de solicitação de contingência - empenho de contingência) com o valor empenhado na solicitação da contingência, efetivando o controle do empenho.

Exemplo prático de configuração de saldos:

* Realizado: Soma dos Tipos de Saldos Realizado (RE) e Empenhado (EM).

> Atenção: Ao solicitar a contingência, o usuário deve empenhar o valor orçado por meio do processo de lançamento `000356`, item `02`, no tipo de saldo `EM`.

Detalhamento do processo de empenho:

|  |  |
| --- | --- |
| **Parte 1** | **Parte 2** |
|  |  |

**Saiba Mais**

[SIGAPCO Utilização de Contingência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018523352-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Utiliza%C3%A7%C3%A3o-de-Conting%C3%AAncia)

[SIGAPCO Empenho de saldo PCO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38860948518551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPCO-Empenho-de-saldo-PCO)
