---
article_id: 19752807239191
category: eSocial - Cadastros
content_hash: d179179f1ea0aa277182368ca3a8a65ea50e94b37421f28300a3c614cf13c1ad
fetched_at: '2026-06-28T22:47:14.474653+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Como cadastrar evento de plano de saúde para gerar
  os dados do dependente no XML S-2200 ou S-2205 (S-1.2)
type: support-article
updated_at: '2026-04-17T19:31:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19752807239191-RH-RM-FOP-eSocial-Como-cadastrar-evento-de-plano-de-sa%C3%BAde-para-gerar-os-dados-do-dependente-no-XML-S-2200-ou-S-2205-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19752807185559) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como realizar o desconto do plano de saúde no envelope do funcionário e a informação ser gerada no XML?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) TOTVS Folha de Pagamento - eSocial  - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e superiores.  
  
**Solução**  
Para atender as alterações realizadas no leiaute S-1.2, para os funcionários que possuem dependentes com incidência de assistência médica ou assistência odontológica, realize os seguintes passos:  
  
1. O desconto de plano de saúde ocorre por um evento específico, através de uma fórmula para cálculo de desconto, seguindo as regras da empresa.  O evento poderá ser de Código de cálculo 0, ou poderá utilizar o evento de Código de cálculo 14, sendo parametrizado uma fórmula no mesmo. Além disto, é necessário que conste no campo Natureza de Rubrica eSocial, a natureza 9219.  
Realize o cadastro de um evento conforme orientado acima, caso tenha dúvida neste cadastro [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6683553867159-RH-RM-FOP-Cadastro-de-evento-para-desconto-de-plano-de-sa%C3%BAde-)  
  
2. Após a parametrização, acesse o cadastro de dependente do funcionário localizado em: Funcionário | Anexos | Folha de Pagamento| Dependente e marque a flag Assistência Saúde e/ou Assistência Odontológica. Conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26461955943191)

**Importante**

Para que o XML S-2200 ou S-2205 seja enviado as informações do dependente para plano de saúde ou plano odontológico, o sistema não valida a flag marcada no campo **Outras Incidências**, este campo é apenas para controle interno da empresa. O sistema irá validar a flag marcada em **Incidências**.

Para novas admissões , é necessário parametrizar as informações acima antes de gerar o XML S-2200.

O evento para desconto de plano de saúde deverá ser lançado via grupo de eventos na movimentação dos funcionários.

**Saiba mais**  
Para mais informações, acesse:

* [RH - RM - FOP - eSocial - Operadoras de plano de saúde no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003869592-RH-RM-FOP-eSocial-Operadoras-de-plano-de-sa%C3%BAde-no-eSocial?source=search)
* [RM - RH - RM - FOP - eSocial - Operadora de Assistência à Saúde não exibe evento para inclusão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009051751-RM-eSocial-Operadora-de-Assist%C3%AAncia-%C3%A0-Sa%C3%BAde-n%C3%A3o-exibe-evento-para-inclus%C3%A3o)
* [Alterações - S-2205 - S-1.2](https://tdn.totvs.com/pages/releaseview.action?pageId=777274034)
