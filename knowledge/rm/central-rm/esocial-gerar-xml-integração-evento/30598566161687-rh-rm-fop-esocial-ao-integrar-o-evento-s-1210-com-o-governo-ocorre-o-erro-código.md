---
article_id: 30598566161687
category: eSocial - Gerar XML/ Integração Evento
content_hash: 0eafc0ccb594e2f4a555a55d9963d1ff38fd47eed022e6499009d70219304b9e
fetched_at: '2026-06-28T22:47:11.979981+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao integrar o evento S-1210 com o governo ocorre
  o erro código 8: Grupo Informações relativas a planos de previdência complementar
  deve ser preenchido'
type: support-article
updated_at: '2026-05-26T19:58:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30598566161687-RH-RM-FOP-eSocial-Ao-integrar-o-evento-S-1210-com-o-governo-ocorre-o-erro-c%C3%B3digo-8-Grupo-Informa%C3%A7%C3%B5es-relativas-a-planos-de-previd%C3%AAncia-complementar-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30598566122775) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao integrar o evento S-1210 com o governo ocorre o erro código 8: Grupo #39;**Informações relativas a planos de previdência complementar**#39; deve ser preenchido. Verifique as condições de preenchimento no leiaute. Localização: /eSocial/evtPgtos/ideBenef/infoIRComplem.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2402.245, 12.1.2406.185, 12.1.2410.121 e Superiores.  
  
**Causa**  
Esse incidente ocorre ao enviar o S-1210 e, a no evento de remuneração das Informações dos pagamentos efetuados consta alguma rubrica, em que a incidência em IRRF seja igual a 46, 47, 48, 61, 62, 63, 64, 65, 66.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30598575067927)**

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Valide no XML S-1210 quais Informações dos pagamentos que foram gerados;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30598566125463)

2. No exemplo supracitado, será necessário validar no XML S-1200 se conta alguma rubrica com uma das incidências de IRRF: 46, 47, 48, 61, 62, 63, 64, 65, 66;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30598566127383)

2.1. Para isto, o usuário poderá utilizar o [Relatório Comparativo de Incidências de Rubricas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038280834-RH-RM-FOP-eSocial-Relat%C3%B3rio-Comparativo-de-Incid%C3%AAncias-de-Rubricas) e, caso não identifique nenhuma rubrica, acessar o portal do governo em Empregador | Tabelas | Tabela de Rubricas e valide todas as incidências de IRRF que estão cadastradas no governo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30598527724311)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30598527726103)

3. Após identificar a rubrica é necessário realizar as seguintes validações:  
3.1. Caso ela esteja cadastrada corretamente, ou seja com a incidência de IRRF de Previdência Complementar e seja um evento de Previdência complementar, será necessário associar essa rubrica em **eSocial | Previdência Complementar | Cadastro Previdência Complementar**. E após regerar o XML S-1210. Para mais informações [CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21711814151319-RH-RM-FOP-eSocial-Como-informar-no-S-1210-o-grupo-de-Previd%C3%AAncia-Complementar-S-1-2) **;**  
3.2. Caso ela não seja de Previdência Complementar, será necessário:

* Alterar a incidência de IRRF;
* Ajustar a competência da rubrica para igual ou anterior ao período referência constante no S-1210, no exemplo é 01/2025. Após enviar ao governo;
* Retificar o S-1200. No exemplo seria necessário reabrir o período 01/2025, enviar o S-3000 do S-1210 01/2025 e retificar o S-1200.

**Importante**  
Quando houver férias lançadas no recibo de férias ou no envelope de férias, é importante validar se os eventos do Parametrizador 6/7 e 7/7 constam cadastrados corretamente. Para validações, acesse:  
[- RH - RM - FOP - eSocial - Parametrizador eSocial: Configurações Gerais 6/7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17203402479255-RH-RM-FOP-eSocial-Parametrizador-eSocial-Configura%C3%A7%C3%B5es-Gerais-6-7)   
[- RH - RM - FOP - eSocial - Parametrizador eSocial: Configurações Gerais 7/7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6805437378455-RH-RM-FOP-eSocial-Parametrizador-eSocial-Configura%C3%A7%C3%B5es-Gerais-7-7?source=search) 

**Saiba mais**  
Para mais informações acesse:  
- [RH - RM - FOP - eSocial - Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos) ;  
- [RH - RM - FOP - eSocial - Como realizar a reabertura da folha de pagamento no eSocial utilizando o evento S-1298](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5676190571799-RH-RM-FOP-eSocial-Como-realizar-a-reabertura-da-folha-de-pagamento-no-eSocial-utilizando-o-evento-S-1298)
