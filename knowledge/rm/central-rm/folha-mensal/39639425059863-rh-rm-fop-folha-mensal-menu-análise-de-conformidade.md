---
article_id: 39639425059863
category: Folha Mensal
content_hash: 945ad2d29bdbfc3c6f3848db2a036417f9110a018b8247b7bdb4b3c2c1757264
fetched_at: '2026-06-28T22:46:57.944375+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha mensal: Menu Análise de Conformidade'
type: support-article
updated_at: '2026-04-09T20:36:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39639425059863-RH-RM-FOP-Folha-mensal-Menu-An%C3%A1lise-de-Conformidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39639438860695) Tempo aproximado para leitura: **00:02:24 min**  
  
**Dúvida**  
Como utilizar o menu de Análise de Conformidade no módulo Folha de Pagamento para realizar a auditoria de processos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
A funcionalidade de Análise de Conformidade tem como objetivo permitir que o usuário audite os processos executados no sistema, garantindo a integridade das informações e o cumprimento das regras de negócio estabelecidas. O recurso centraliza a visualização de inconsistências e alertas gerados durante o processamento da folha.  
  
1. Acesse o menu **Serviços Globais | Segurança | Perfis |** Filtre por **Folha de pagamento** e permita o acesso para Análise de Conformidade, conforme o exemplo abaixo:

![](https://tdn.totvs.com/download/attachments/1008237029/image-2025-11-27_10-21-15.png?version=1&modificationDate=1764249675557&api=v2)

O usuário e seu perfil deve ter acesso a coligada e o filtro de usuário e perfil deve dar acesso aos dados da Filial, Funcionário e Seção do Funcionário. Pois as APIs consideram este filtro.

2. Acesse o menu **Serviços Globais | Segurança | Usuários | Selecione o usuário;**

![image-2026-2-17_18-12-12.png](https://tdn.totvs.com/download/attachments/1008237029/image-2026-2-17_18-12-12.png?version=1&modificationDate=1771362732470&api=v2)

3. Filtro de usuário em **Serviços de globais | Segurança | Usuário | Anexos | Filtro por Usuário;**

![](https://tdn.totvs.com/download/thumbnails/1008237029/image-2026-2-17_18-16-19.png?version=1&modificationDate=1771362979650&api=v2)

4. Filtro de perfil em **Serviços de globais | Segurança | Perfis | Anexos | Filtro por Perfil;**

![](https://tdn.totvs.com/download/thumbnails/1008237029/image-2026-2-17_18-21-20.png?version=1&modificationDate=1771363281967&api=v2)

5. Selecione a opção em **Folha mensal | Consulta | Análise de conformidade;**

![](https://tdn.totvs.com/download/attachments/1008237029/image-2025-11-27_10-18-35.png?version=1&modificationDate=1764249515337&api=v2)

6. No filtro de seleção, informe os parâmetros desejados para a análise (como Coligada, Chapa ou Período);

7. Clique em **Executar** para processar a verificação dos dados;

8. O sistema apresentará o **Painel de Conformidade** com o detalhamento das ocorrências encontradas;

9. Para cada item listado, é possível visualizar o detalhamento do erro ou aviso para realizar as correções necessárias no cadastro ou processo indicado.

**Saiba Mais**:  
  
Para mais detalhes técnicos sobre a implementação e campos desta rotina, acesse: [DT RM - Auditoria de Folha](https://tdn.totvs.com/display/public/AUDITPROJ/DT+RM+-+Auditoria+de+Folha)
