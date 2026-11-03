---
article_id: 4417226545431
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 091071e59e98e007b2f77eef00eeeb25ef047ce35f64fb0eff613e33bbdfb4dc
fetched_at: '2026-06-28T22:38:28.613775+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre a
  data dos dicionários completos e diferenciais
type: support-article
updated_at: '2021-12-27T20:12:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417226545431-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-a-data-dos-dicion%C3%A1rios-completos-e-diferenciais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Em um processo de migração do release 12.1.25 para o 12.1.33, ocorreu a seguinte dúvida quanto ao dicionário de dados:

- O dicionário de dados completo/diferencial tem data de 27/09 e 01/10, respectivamente.  
Mas em meu ambiente tem dicionário desse módulo aplicado com data posterior ao do novo release.  
Como fica essa situação?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- todas a versões.  
  
**Solução**

Segue o posicionamento da nossa equipe GCAD, que expede os dicionários:

As alterações que são expedidas no pacotes de dicionários acumulados, que chamamos de Expedições Contínuas do módulo,  são alterações já feitas para o **próximo release** e l**iberadas para os release anteriores.**  
  
Além disso, o UPDDISTR tem uma inteligência para saber como se comportar nas diferentes situações que pode encontrar,  como campos novos, alterações de tamanho, novos índices, tabelas, etc.  
  
Se quiser ver mais tecnicamente o que é atualizado, essas regras do UPDDISTR estão documentadas em: **[Regras para atualização dos dicionários - UPDDISTR e migrador de versão](https://tdn.totvs.com/x/NfnzEQ)**  
  
Assim, mesmo que se tenha atualizado os pacotes de acumulados do 12.1.25 com datas, posteriores ao mês de out./2021, que foi a data da liberação do release 12.1.33, não devem haver problemas.  
  
O que se deve fazer na sequência da atualização de release, é aplicar o acumulados mais recentes do 12.1.33, pois , o RPO de outubro, que o que está no portal e no instalador de out./2021, não tem as correções após essa data, elas estão nestes acumulados.  E recomendo também a aplicação dos dicionários para o 12.1.33, e que cai no que foi explicado acima: sempre é uma liberação para releases anteriores e respeitando as regras de atualização do UPDDISTR.  
  
Dependendo da quantidade de módulos que uma empresa utilize, a quantidade de atualizações de Exp. Continua pode ser significativa.  No release 12.1.33, foi disponibizada uma nova ferramenta para ajudar na aplicação de pacotes de dicionários, chamada **UPDBATCH**. Ela é como o UPDDISTR (alias usa o mesmo mecanismo e regras), só que permite enfileirar a execução de diversos pacotes SDF de atualização.

Veja a documentação em: **[UPDBATCH - Atualização de pacotes em lotes](https://tdn.totvs.com/x/sFDoJQ)**
