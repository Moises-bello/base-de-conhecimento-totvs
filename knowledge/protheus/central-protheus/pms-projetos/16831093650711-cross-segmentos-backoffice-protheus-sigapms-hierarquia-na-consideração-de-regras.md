---
article_id: 16831093650711
category: PMS - Projetos
content_hash: 1e6f814cb6374cf7d55cffa29c0a92d97e4216d40d5b3a53d69a28dd51a97d3c
fetched_at: '2026-06-28T22:37:15.928304+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Hierarquia na consideração
  de regras em projetos
type: support-article
updated_at: '2024-12-12T17:13:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16831093650711-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Hierarquia-na-considera%C3%A7%C3%A3o-de-regras-em-projetos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16831110289175) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Qual a hierarquia na consideração de regras do módulo SIGAPMS?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
  
**Solução**Dentro do módulo SIGPMS, é possível definir regras ao projeto, para que certos usuários consigam fazer funções distintas de outros, variando do cargo e fase do projeto.

Há dois tipos de regras, por fase do projeto/orçamento e por usuário:

A - Por fase do projeto (Caminho: Rotina "PMSA070" > Incluir):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830523649815)

A tabela usada acima é a AEA.

B - Por usuário/grupo de usuário (Caminho: Rotina "PMSA070" > Outras Ações > Usuário):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830548575767)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830727782167)

A tabela usada acima é a AFX.

Caso exista a mesma regra com valores diferentes na **regra de projeto (PMSA070, tabela AEA)**, **regra de usuário no projeto (tabela AFX)**, **regra de usuário na EDT (tabela AFX)** e **regra de usuário na tarefa (tabela AFX)**, a hierarquia é:

1 - **Regra de usuário na tarefa (tabela AFX):**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830600737943)**

**2 - Regra de usuário no projeto (tabela AFX):**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830619361303)**

**3 - Regra de usuário na EDT (tabela AFX):**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830643075351)**

**4 - Regra por fase de projeto (tabela AEA):**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830652921751)**

**OBSERVAÇÃO:** Só será utilizado controle por usuário caso no projeto o campo **"Ctr. Usuario (AF8\_CTRUSR)"** esteja como **"1 - Habilitado"** na rotina **"Caminho: Rotina PMSA410 > Alterar Cadastro"**

**Exemplo 1:**

Se houverem 4 regras para controle de inclusão de solicitação de Compras dessa maneira:

* Regra de usuário na tarefa (tabela AFX): AFX\_GERSC = '4 - Controle total'
* Regra de usuário na EDT (tabela AFX): AFX\_GERSC = '1 - Bloqueado'
* Regra de usuário no projeto (tabela AFX): AFX\_GERSC = '1 - Bloqueado'
* Regra por fase de projeto (tabela AEA): AEA\_EVEN52 = '2 - Nao'

Será possível incluir uma solicitação de compras, pois a primeira regra da hierarquia está permitindo.

**Exemplo 2:**

Se houverem 3 regras para controle de inclusão de solicitação de Compras dessa maneira:

* Regra de usuário na EDT (tabela AFX): AFX\_GERSC = '1 - Bloqueado'
* Regra de usuário no projeto (tabela AFX): AFX\_GERSC = '4 - Controle total'
* Regra por fase de projeto (tabela AEA): AEA\_EVEN52 = '2 - Nao'

Será possível incluir uma solicitação de compras, pois a regra de usuário no projeto tem mais prioridade que a regra de usuário na EDT e consequentemente, mais prioridade que a regra por fase de projeto (tabela AEA).
