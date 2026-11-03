---
article_id: 360021182892
category: CRM - Dúvidas Gerais
content_hash: ca8f3b665f3d4537e48c9680adae1f9af2a86959095795c622e2f5ea847f77bb
fetched_at: '2026-06-28T22:40:27.664466+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Controle de Privilégios do
  CRM
type: support-article
updated_at: '2024-04-25T12:06:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021182892-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Controle-de-Privil%C3%A9gios-do-CRM
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20262800317207) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Qual a Configuração e Funcionalidade do Controle de Privilégios do CRM?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Solução**

Definir quem terá acesso a **alterar, visualizar, excluir** e **compartilhar** os registros incluídos pelos usuários CRM.  
Os privilégios podem ser compartilhados **por usuário**, **equipe de venda** ou **unidade de negócio** ou **todos eles** (**Soma**). É possível definir mais de um modo de compartilhamento ao mesmo tempo.

Por padrão, todo registro incluído é criado como a opção **Soma.**

**Exemplos de Uso:**

Base de Dados:

![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15919007544983)

**Usuário Logado:** Robson

**Cenário 1:** Compartilhamento por Equipe de Vendas

Incluir um novo cliente:

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15918985112215)

Posicionar sobre o cliente, clicar em **Outras Ações** e depois em **Privilégios**:

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15918985114135)

No campo **Seq. Virtual**, o usuário pode definir qual a regra de priorização do registro. Nesse caso, vamos selecionar apenas a **Equipe de Vendas**:

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15918985116055)

Na aba **Equipes** será definido que apenas a equipe **000010** terá acesso total ao registro, enquanto a equipe **CRM001** poderá apenas visualizar:

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15919007565335)

Confirmando a operação, ficaremos com o seguinte cenário:

![a1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15918985123735)

**Cenário 2**: Compartilhado por Usuário e Equipe de Venda.

**Cliente Utilizado: CRM991**

Equipe de Venda compartilhada:

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15919007580183)

Usuário compartilhado:

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15919007582615)

Confirmando a operação, ficaremos com o seguinte cenário:

![a2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15918985132951)

**Saiba mais:**

**[Restrições de usuário no Faturamento e CRM](https://tdn.totvs.com/pages/viewpage.action?pageId=336403802)**

**[Controle de Privilégios do CRM](https://tdn.totvs.com/pages/viewpage.action?pageId=439692702)**

**[COMO REFAZER OS PRIVILÉGIOS DOS REGISTROS NO SIGACRM PROTHEUS 12](https://tdn.totvs.com/display/PROT/CRM0020_REFAZER_PREVILEGIOS_REGISTROS_CRM)**

**[Como habilitar os privilégios no configurador](https://tdn.totvs.com/pages/viewpage.action?pageId=271180996)**
