---
article_id: 40308008638231
category: TAF - eSocial - Eventos Periódicos
content_hash: 04ac713aa77e8211c3a8a55a26d762416d6b6c7e7ac8a664d850c4bca669cb5f
fetched_at: '2026-06-28T22:45:19.151033+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - Periódicos- S-1210 -  Erro de schema nrRec1210Orig'':
  [facet ''pattern''] The value '''' is not accepted by the pattern'
type: support-article
updated_at: '2026-05-08T13:45:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40308008638231-RH-Linha-Protheus-TAF-Peri%C3%B3dicos-S-1210-Erro-de-schema-nrRec1210Orig-facet-pattern-The-value-is-not-accepted-by-the-pattern
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40308025281175) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
A inconsistência abaixo é apresentada ao tentar transmitir o evento do eSocial S-1210 (Pagamentos de Rendimentos do Trabalho):

Erro de schema: Element '{<http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_03_00>}nrRec1210Orig': [facet 'length'] The value has a length of '0'; this differs from the allowed length of '23'. Element '{<http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_03_00>}nrRec1210Orig': [facet 'pattern'] The value '' is not accepted by the pattern '[1]{1}\.\d{1}\.\d{19}'.

**Ambiente**

TOTVS RH - TOTVS RH - eSocial - TAF eSocial - Periódicos - S-1210 - TAFA407 - Todas as versões.  
  
  
**Solução**  
  
1. Acesse a rotina do evento S-1210 e clique em editar no registro que está com a inconsistência

Atualizações > Eventos Esocial > Periódicos > Pgto Rend Trab

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40308008613399)

2. Valide se existe alguma informação na coluna ' informações complementares de período anteriores', caso sim, deixe essa coluna sem nenhuma informação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40308100313879)

3. Exemplo correto. Após, clique em confirmar e transmita o evento novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40308025283223)

**Obs: Se apresentar alguma mensagem: Na Fonte (MODEL\_T8E) precisa ser preenchido.**

Seguir o KCS:   
[RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1210 - Não é permitido informar dados sem referência superior. O formulário Info. Relac. Retenção Na Fonte (MODEL\_T8E) precisa ser preenchido.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30280365481367-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1210-N%C3%A3o-%C3%A9-permitido-informar-dados-sem-refer%C3%AAncia-superior-O-formul%C3%A1rio-Info-Relac-Reten%C3%A7%C3%A3o-Na-Fonte-MODEL-T8E-precisa-ser-preenchido)

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
