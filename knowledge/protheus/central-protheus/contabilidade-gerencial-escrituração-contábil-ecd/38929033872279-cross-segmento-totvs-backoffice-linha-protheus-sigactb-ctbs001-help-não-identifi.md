---
article_id: 38929033872279
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: b7c816eb88028092ac15938a47e203227fdb0a3627f2e1e590cb891067130ea1
fetched_at: '2026-06-28T22:40:52.760239+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - CTBS001 - Help
  "Não identificamos o uso do Validador ECD/ECF..."
type: support-article
updated_at: '2026-03-10T11:50:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38929033872279-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Help-N%C3%A3o-identificamos-o-uso-do-Validador-ECD-ECF
---

Ao acessar a rotina Central de Escrituração (CTBS001) no Protheus, pode aparecer a mensagem sobre o uso do Validador ECD/ECF fora do período de 30 dias. Para corrigir, acesse a rotina Validador ECD/ECF (CTBS480), que atualiza automaticamente o parâmetro MV\_ULTVECD. Alternativamente, atualize manualmente a data deste parâmetro no módulo Configurador para o formato AAAAMMDD. Após isso, a mensagem de alerta será removida.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38929047653911) Tempo aproximado para leitura: **10 min**  
  
**Dúvida**  
Ao acessar a rotina Central de Escrituração (CTBS001), apresenta a mensagem: "Não identificamos o uso do Validador ECD/ECF nos últimos 30 dias." ou "Identificamos a utilização do validador ECD/ECF em período maior que 30 dias."

![](https://tdn.totvs.com/download/attachments/695203717/image2022-6-22_17-10-55.png?version=1&modificationDate=1655928655897&api=v2)![](https://tdn.totvs.com/download/attachments/695203717/image2022-6-22_17-10-34.png?version=1&modificationDate=1655928635067&api=v2)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - a partir da versão 12  
  
  
  
**Solução**  
Para a correção do erro, é necessário que seja acessado a rotina Validador ECD/ECF (CTBS480)  
  
O sistema gerencia o controle de exibição da mensagem de alerta sobre o validador por intermédio do parâmetro `MV_ULTVECD`. A data registrada neste parâmetro não deve ultrapassar o intervalo estipulado de 30 dias retroativos.   
  
O Protheus realiza validações constantes sobre o parâmetro `MV_ULTVECD` para certificar que o uso ocorreu dentro deste período. Na ausência de execução da rotina nos últimos 30 dias, é imprescindível realizar uma atualização para inibir a notificação.

**Passos**

1. Efetue o acesso à rotina Validador ECD/ECF (CTBS480). O sistema está programado para atualizar a data deste parâmetro automaticamente a cada novo ingresso na referida rotina.  
     
   [CTBS480 - Validador ECD/ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6112312502295-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS480-Validador-ECD-ECF?source=search)
2. Como método alternativo, é possível proceder com a alteração da data do parâmetro `MV_ULTVECD` de forma manual e direta pelo módulo Configurador.

   Preencha o parâmetro com a data corrente, adotando estritamente o formato AAAAMMDD (como, por exemplo, 20260127).

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38929047655703)
3. Concluída esta configuração, o sistema deixará de apresentar a respectiva mensagem de advertência.

**Saiba Mais**  
[CTBS480 - Validador ECD/ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6112312502295-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS480-Validador-ECD-ECF?source=search)  
[Adesão validador ECD/ECF](https://tdn.totvs.com/pages/releaseview.action?pageId=695203717)
