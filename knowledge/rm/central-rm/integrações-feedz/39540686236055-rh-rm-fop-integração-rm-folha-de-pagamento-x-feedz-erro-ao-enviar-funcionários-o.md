---
article_id: 39540686236055
category: Integrações - Feedz
content_hash: d4394efe78baa1d6f5ba587e42ba14b1d4d2d62002d1709058720a77b6bd9f60
fetched_at: '2026-06-28T22:46:41.424648+00:00'
product: rm
section_id: 28212337440791
source: central-rm
title: 'RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Erro ao enviar
  funcionários: "Ocorreu uma falha crítica no processo."'
type: support-article
updated_at: '2026-04-07T14:25:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39540686236055-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-ao-enviar-funcion%C3%A1rios-Ocorreu-uma-falha-cr%C3%ADtica-no-processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39540637084951) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao realizar o envio de funcionários do RM para a Feedz, o sistema apresenta a mensagem de erro: "Ocorreu uma falha crítica no processo".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39540637085079)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2310  
  
**Solução**  
Esta mensagem de erro geralmente ocorre quando as parametrizações de máscara e quebra da coligada no módulo de Folha de Pagamento estão configuradas de forma incorreta. Para corrigir o incidente, realize os seguintes passos:

1. Acesse o módulo **Folha de Pagamento > Configurações | Parametrizador | RH Máscaras e Quebras** para realizar o ajuste. Para informações sobre como parametrizar as **Máscaras e Quebras**, consulte: [RH - RM - FOP - RH Máscaras e Quebras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8872536849431-RH-RM-FOP-RH-M%C3%A1scaras-e-Quebras)

2. Após ajustar, execute a rotina de **manutenção do cadastro de seções**: [RH - RM - FOP - Manutenção do Cadastro de Seções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058029994-RH-RM-FOP-Manuten%C3%A7%C3%A3o-do-Cadastro-de-Se%C3%A7%C3%B5es)

Após os ajustes, realize uma nova tentativa de envio/integração para a Feedz.

**Saiba mais:**

[RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Como realizar o envio de colaboradores e associação de líderes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29903246172695-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-realizar-o-envio-de-colaboradores-e-associa%C3%A7%C3%A3o-de-l%C3%ADderes)

[RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Erro na integração com a Feedz código XXXX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29909362246039-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-na-integra%C3%A7%C3%A3o-com-a-Feedz-c%C3%B3digo-XXXX)
