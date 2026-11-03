---
article_id: 37807515269655
category: Meu RH - Férias
content_hash: 1b7c61077eb611d4f69fea42f15d607add27b83d951a65819154efc454d13df1
fetched_at: '2026-06-28T22:47:31.610679+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Como identificar o responsável pela aprovação ou reprovação
  das férias?
type: support-article
updated_at: '2026-01-23T19:41:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37807515269655-RH-RM-Meu-RH-Como-identificar-o-respons%C3%A1vel-pela-aprova%C3%A7%C3%A3o-ou-reprova%C3%A7%C3%A3o-das-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37807496140055) Tempo aproximado para leitura: **00:03:55 min**  
  
**Dúvida**  
Como rastrear o chefe ou supervisor responsável pela aprovação ou reprovação das férias?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas as versões   
  
**Solução**  
O Meu RH não gera registros de quem foi o responsável por aprovar as férias. Entretanto, existem algumas formas de rastrear as alterações realizadas na tabela, permitindo identificar o usuário que efetuou a aprovação ou reprovação. Segue um exemplo:

No momento da**solicitação das férias**, é possível verificar qual usuário realizou a sugestão por meio da consulta SQL abaixo:

```
SELECT RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY, RECMODIFIEDON
FROM pfuferiasper
WHERE chapa = 'XXXX';
```

### Descrição dos campos retornados:

* **RECCREATEDBY**: Identificação do usuário que criou a solicitação de férias.
* **RECCREATEDON**: Data de criação da solicitação de férias.
* **RECMODIFIEDBY**: Identificação do último usuário que realizou qualquer alteração na solicitação.
* **RECMODIFIEDON**: Data da última alteração realizada na solicitação de férias.

### Observações importantes:

Os registros dessa tabela contêm as seguintes informações:

* O usuário que criou a solicitação é gravado em `RECCREATEDBY` e a data correspondente é armazenada em `RECCREATEDON`.
* Caso haja qualquer alteração na solicitação de férias, os campos `RECMODIFIEDBY` e `RECMODIFIEDON` serão atualizados com o usuário responsável pela alteração e a data da modificação, respectivamente.

Neste exemplo abaixo, informamos a chapa **00002** e a data de início das férias a partir de **2021**, para restringir a consulta somente a esse período. O retorno indicou que na coluna **RECCREATEDBY** o usuário **mestref** foi quem inseriu a sugestão de férias.

![](https://totvssuporte.zendesk.com/attachments/token/vLrCKc422P5txk6idgTsGgQlg/?name=inline1566346207.png)

Ao realizar a primeira aprovação pelo Meu RH, é possível observar que a coluna **RECMODIFIEDBY** é alterada de **mestref** para **mestre**, que corresponde ao usuário do **chefe/gestor** que aprovou as férias.

![](https://totvssuporte.zendesk.com/attachments/token/5fJ7P6FkEe5Z4xgD8t52zdXpm/?name=inline-1135046725.png)

Na aprovação final das férias pelo RM, a coluna **RECMODIFIEDBY** passa a conter o valor **DP**, identificando o usuário doDepartamento Pessoal que concluiu a aprovação.

![](https://totvssuporte.zendesk.com/attachments/token/AoKdJsbrHcjpT32MlgPi7rmW7/?name=inline1968886166.png)

![](https://totvssuporte.zendesk.com/attachments/token/Cq1dsJfuT6JjoZgYC23EBtQQz/?name=inline-74946959.png)

Para este rastreamento, é necessário analisar a tabela `PFUFERIASPER` seguindo a **ordem do fluxo**, conforme demonstrado em cada etapa de alteração.  
Caso as férias **já estejam totalmente aprovadas**, será possível identificar apenas o **usuário que sugeriu as férias** e o **usuário do DP que aprovou**, não sendo possível visualizar o chefe, pois essa etapa já foi concluída e sobreposta pela aprovação do DP.

Dessa forma, para identificar o **chefe que realizou a aprovação**, é necessário utilizar o [**Log de Auditoria**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003811551-Framework-Framework-RM-BD-Como-habilitar-TOTVS-Audit), visto que esse passo já foi executado.

**Importante:** O log de auditoria irá conter registros apenas das movimentações de férias que foram realizadas após sua ativação na tabela. Caso a solicitação de férias que deseja rastrear tenha sido realizada antes de habilitar o Log de auditoria, não será possível consultar as movimentações.

Com o **Log de Auditoria ativo**, ao acessar o módulo **Serviços Globais | Administração | Log de Alterações**, será possível verificar as alterações por **data** ou por **nome do módulo**. No exemplo demonstrado, é possível identificar a seguinte sequência de usuários:

1. **rm** – realiza a ativação do Log de Auditoria
2. **mestref** – realiza a sugestão de férias
3. **mestre (gestor)** – realiza a aprovação
4. **DP** – realiza a aprovação final  
     
   ![](https://totvssuporte.zendesk.com/attachments/token/Xqw669WBWkmzb2qcqE0f45Uah/?name=inline458935777.png)

Todas as tabelas de cada módulo estão listadas na tela **Configuração do Log de Auditoria**. Ao selecionar o módulo no menu esquerdo, é possível identificar, no lado direito, a **tabela correspondente**.

![](https://totvssuporte.zendesk.com/attachments/token/vzeOe9yksUjK4geZtQS5JLeQn/?name=inline374751173.png)

Para confirmar o nome das tabelas, é possível acessar diretamente a tela desejada no RM, clicar com o botão direito do mouse e selecionar a opção [**visualizar nome dos campos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9321865600919-RH-RM-FOP-Visualizar-nome-dos-campos-da-tabela).

![](https://totvssuporte.zendesk.com/attachments/token/rRHr90M66FZ2VAVOGGfbPbZgb/?name=inline-196779716.png)

![](https://totvssuporte.zendesk.com/attachments/token/aTPH4iqWe9qveI3wYhy6cWraN/?name=inline957163580.png)

**Saiba mais:**

[Framework - Framework RM - BD - Habilitar novo Log de Auditoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003811551-Framework-Framework-RM-BD-Habilitar-novo-Log-de-Auditoria-?source=search)  
[RH - RM - Meu RH - Onde são armazenadas as aprovações de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005394901-RH-RM-Meu-RH-Onde-s%C3%A3o-armazenadas-as-aprova%C3%A7%C3%B5es-de-f%C3%A9rias?source=search)
