---
article_id: 37565560662423
category: PCO - Bloqueios
content_hash: dd2b30a7724b64b79ff71ff45489e52c003ada19aeca61ea898169b1f40aefa4
fetched_at: '2026-06-28T22:37:13.481466+00:00'
product: protheus
section_id: 1500001550782
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Integração/Bloqueio
  não valida saldo corretamente.
type: support-article
updated_at: '2026-01-12T12:08:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37565560662423-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Integra%C3%A7%C3%A3o-Bloqueio-n%C3%A3o-valida-saldo-corretamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37565567598231) Tempo aproximado para leitura: 00:20 min  
  
**Dúvida**  
Ao realiza a integração/bloqueio, o sistema não está bloqueando corretamente.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Planejamento e Controle Orçamentário - Todas as versões.  
  
**Solução**  
Quando o saldo não é validado corretamente, deve verificar os passos abaixo:

### **1° Configurações do Cubo na rotina Cubos Orçamentário (PCOA193)**

* Verificar se o Tipo de Atualização de saldo esta para atualização On-line:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37565560619671)

* Verificar se possui tipo de bloqueio configurado e ativo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37565567600535)

### **2° Procedures, realizar analise via configurador se as procedures 12, 13 e 35 se estão instaladas/atualizadas:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37565560625687)

### **3° Configuração dos Processos (PCOA030) e Bloqueios (PCOA035):**

* PCOA030, verificar se o processo que esta integrando, esta configurado, ativo e com uma regra de valor valido:

  Exemplo processo 00052 Pedido de compras:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37565567609239)
* PCOA035, verificar se o processo que esta integrando, esta configurado, ativo e com uma regra de valor valida e se esta com o vínculo:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37565560630551)

***Nota***: Para que a tela de bloqueio seja disparada corretamente, é necessário existir uma correspondência exata entre a sequência configurada no **Lançamento de Bloqueio** e a sequência configurada no **Bloqueio Ativo**.

Caso os campos Sequencia (**AKI\_SEQ)** e Sequência (**AKH\_SEQ)** apresentem numerações distintas, o sistema não reconhecerá a regra de bloqueio para o processo em questão.

Pode ser visto este processo no GIF acima onde demonstro os campos de Sequências com a mesmas informações, e comportamento está descrito na documentação:

[Bloqueios por processos (PCOA035 - SIGAPCO)](https://tdn.totvs.com/pages/releaseview.action?pageId=312175424&searchId=PG53FTTLC)

---

## 

**Saiba mais:**  
[PCOA193 Exemplo de como configurar um Cubo Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018810031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA193-Exemplo-de-como-configurar-um-Cubo-Gerencial)  
[Configuração de Lançamentos por Processo (PCOA030)](https://tdn.totvs.com/pages/releaseview.action?pageId=691437643)  
[Bloqueios por processos (PCOA035 - SIGAPCO)](https://tdn.totvs.com/pages/releaseview.action?pageId=312175424&searchId=PG53FTTLC)

**Vídeos**:  
[How To PCO - Planejamento e Controle Orçamentário.](https://tdn.totvs.com/pages/viewpage.action?pageId=763235880&draft=true)
