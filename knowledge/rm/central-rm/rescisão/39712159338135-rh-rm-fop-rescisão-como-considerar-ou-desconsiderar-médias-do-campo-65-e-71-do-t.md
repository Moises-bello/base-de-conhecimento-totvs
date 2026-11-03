---
article_id: 39712159338135
category: Rescisão
content_hash: 64bf32325e52bf2a1d96ebfc4b571dc06eae171606a5fefa569cc0711d2cb441
fetched_at: '2026-06-28T22:46:54.132111+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Como considerar ou desconsiderar médias do campo
  65 e 71 do TRCT'
type: support-article
updated_at: '2026-04-13T16:32:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39712159338135-RH-RM-FOP-Rescis%C3%A3o-Como-considerar-ou-desconsiderar-m%C3%A9dias-do-campo-65-e-71-do-TRCT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39712128010647) Tempo aproximado para leitura: **00:02:12 min**  
  
**Dúvida**  
Como considerar ou desconsiderar médias nos campos 65 (Férias Proporcionais) e 71 (Férias Vencidas) do Termo de Rescisão do Contrato de Trabalho (TRCT)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

O sistema utiliza códigos de cálculo específicos para compor os valores do TRCT. O campo 65 corresponde ao evento com Código de Cálculo 330, que representa o valor dos avos de Férias Proporcionais e suas respectivas médias, desconsiderando a projeção do aviso prévio indenizado. É importante destacar que este campo não busca o valor diretamente do Código de Cálculo 25 (Férias Proporcionais) lançado na rescisão, mas sim a composição baseada no CC 330.

Para gerenciar a exibição das médias, o usuário deve avaliar a parametrização do sindicato e as configurações específicas de discriminação de médias, que permitem separar os valores de proventos das médias correspondentes na TRCT.

A inclusão ou exclusão desses valores de médias no relatório final depende da marcação de parâmetros específicos na rotina de geração do termo. Caso o usuário opte por desconsiderar as médias nesses campos, o sistema deixará de somar os valores provenientes de médias, mantendo apenas o valor principal correspondente aos avos. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39712159311895)

Para **desconsiderar** as médias, marque as opções:

* Não somar média de férias vencidas (campo 66);
* Não somar média de férias prop. (campos 65 e 71);

Caso deseje **considerar** as médias, mantenha as opções acima **desmarcadas**;

**Saiba mais**

[RH- RM - FOP - Médias: Discriminando médias de férias na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015735392-RH-RM-FOP-M%C3%A9dias-Discriminando-m%C3%A9dias-de-f%C3%A9rias-na-rescis%C3%A3o)

[RH - RM - FOP - TRCT: Parametrização dos campos 65, 66 e 71](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022103911-RH-RM-FOP-TRCT-Parametriza%C3%A7%C3%A3o-dos-campos-65-66-e-71)
