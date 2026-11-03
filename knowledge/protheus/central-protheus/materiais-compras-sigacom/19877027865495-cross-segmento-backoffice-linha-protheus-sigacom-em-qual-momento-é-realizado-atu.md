---
article_id: 19877027865495
category: Materiais - Compras (SIGACOM)
content_hash: 49306951d8bad1c26a26ebf3ede6733bd041c0272f3eee4d21aa1c960ef75ad6
fetched_at: '2026-06-28T22:41:10.492535+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM -  Em qual momento é
  realizado atualização do Status do Importador XML no Portal do Trasnsmite?
type: support-article
updated_at: '2026-05-20T17:08:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19877027865495-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Em-qual-momento-%C3%A9-realizado-atualiza%C3%A7%C3%A3o-do-Status-do-Importador-XML-no-Portal-do-Trasnsmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19877070915863) Tempo aproximado para leitura: **00:02 min**  
  
**Dúvida**  
Em qual momento é realizado atualização do Status do Importador XML no Portal do Transmite?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução**

Alterações de status:

1. **Integração ERP está com status** [**Pendente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20341622133527-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGGACOM-Importador-XML-X-TOTVS-Transmite-A-integra%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-ocorrendo-permanecendo-com-o-status-de-integra%C3%A7%C3%A3o-ERP-como-Pendente)**:**

   Os documentos permanecem com este status quando não houve nenhuma requisição realizada pela rotina SCHEDIMPTRA;
2. **Integração ERP está com status** [**Disponível:**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23138650080663-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-Integra%C3%A7%C3%A3o-ERP-no-Transmite-Disponivel)

   Após a execução da rotina SCHEDIMPTRA e a realização de uma requisição, os documentos passam para o status "Disponível", indicando que foram totalmente liberados pela SEFAZ.
3. **Integração ERP está com status** [**Exportada**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23130965724823-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-status-ERP-no-Transmite-Exportada)**:**

   Este status é atribuído quando os documentos são baixados para a tabela CKOCOL (documento disponível no reprocessar do monitor do Importador XML) pela rotina SCHEDIMPTRA  
     
   - Neste momento, o campo CKO\_STRAN será gravado com valor 2;
4. **Integração ERP está com status** [**Integrada**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23130208065303-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-status-ERP-no-Transmite-Integrada)**:**

   Este status é alcançado quando os documentos são gerados na tabela SF1 e SD1, indicando que houve integração com sucesso, porém a nota fiscal ainda não foi classificada (Pré-Nota)  
     
   - Neste momento, o campo CKO\_STRAN será gravado com valor 3;

     5. **Integração ERP está com status** [**Classificada**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22989114562839-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-status-ERP-no-Transmite-Classificada)**:**

          Este status é alcançado a nota fiscal foi integrada e classificada com sucesso;

          - Neste momento, o campo CKO\_STRAN será gravado com valor 4;

Esses status representam diferentes fases do processo de integração, desde a pendência inicial até a conclusão da classificação dos documentos nas tabelas correspondentes.

***Saiba Mais:***

* [IX10 - Integração Importador XML x TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=678583195)
* [Cross Segmentos - Totvs Backoffice Protheus - Importador XML X TOTVS Transmite - A integração não está ocorrendo, permanecendo com o status de integração ERP como "Pendente".](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20341622133527)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
