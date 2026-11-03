---
article_id: 30601489960727
category: eSocial - Gerar XML/ Integração Evento
content_hash: 60791dc3fb1bea84b9ec367206857886838668df045526ed7a35de714f645c31
fetched_at: '2026-06-28T22:47:11.975620+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao integrar o evento S-1210 com o governo ocorre
  o erro código 8: Grupo Informação dos beneficiários da pensão alimentícia deve ser
  preenchido'
type: support-article
updated_at: '2026-05-27T21:15:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30601489960727-RH-RM-FOP-eSocial-Ao-integrar-o-evento-S-1210-com-o-governo-ocorre-o-erro-c%C3%B3digo-8-Grupo-Informa%C3%A7%C3%A3o-dos-benefici%C3%A1rios-da-pens%C3%A3o-aliment%C3%ADcia-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30601503780119) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao integrar o S-1210 com o governo ocorre o erro código 8: Grupo #39;**Informação dos beneficiários da pensão alimentícia**#39; deve ser preenchido. Verifique as condições de preenchimento no leiaute.  
Localização: /eSocial/evtPgtos/ideBenef.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30602064297751)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da release 12.1.24  
  
**Causa**  
Esse incidente ocorre ao enviar o S-1210 e, a no evento de remuneração das Informações dos pagamentos efetuados consta alguma rubrica, em que a incidência em IRRF seja igual a 51, 52, 53, 54.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30601503781271)

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Valide no XML S-1210 quais Informações dos pagamentos que foram gerados;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30601503782935)

2. No exemplo supracitado, será necessário validar no XML S-1200 se conta alguma rubrica com uma das incidências de IRRF: 51, 52, 53, 54;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30601489923735)

2.1. Para isto, o usuário poderá utilizar o [Relatório Comparativo de Incidências de Rubricas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038280834-RH-RM-FOP-eSocial-Relat%C3%B3rio-Comparativo-de-Incid%C3%AAncias-de-Rubricas) e, caso não identifique nenhuma rubrica, acessar o portal do governo em Empregador | Tabelas | Tabela de Rubricas e valide todas as incidências de IRRF que estão cadastradas no governo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30601503788695)

3. Após identificar a rubrica é necessário realizar as seguintes validações:  
3.1. Caso ela esteja cadastrada corretamente, ou seja com a incidência de IRRF de Pensão Alimentícia e seja um evento de Pensão Alimentícia, será necessário validar a movimentação da pensão, com o envelope. Para mais informações [CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036360433-RH-RM-FOP-eSocial-Ao-gerar-o-evento-S-1210-ocorre-o-erro-N%C3%A3o-foi-encontrado-Movimenta%C3%A7%C3%A3o-da-Pens%C3%A3o-de-Dependente-e-a-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-o-eSocial-S-1-2) **;**  
3.2. Caso ela não seja de Pensão Alimentícia, será necessário:

* Alterar a incidência de IRRF;
* Ajustar a competência da rubrica para igual ou anterior ao período referência constante no S-1210, no exemplo é 01/2025. Após enviar ao governo;
* Retificar o S-1200. No exemplo seria necessário reabrir o período 01/2025, enviar o S-3000 do S-1210 01/2025 e retificar o S-1200.

**Importante**  
Quando houver férias lançadas no envelope, é importante validar se **Evento Pensão Férias envelope (Desconto) do Parametrizador 6/7**, consta sem incidência de IRRF de Pensão no governo. Esse evento deverá ser  Desconto, sem código de cálculo, sem incidências e com natureza da rubrica 9299 - Outros descontos não previstos nos itens anteriores. Para mais informações [CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17203402479255-RH-RM-FOP-eSocial-Parametrizador-eSocial-Configura%C3%A7%C3%B5es-Gerais-6-7).

**Saiba mais**  
Para mais informações acesse:  
- [RH - RM - FOP - eSocial - Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos) ;  
- [RH - RM - FOP - eSocial - Como realizar a reabertura da folha de pagamento no eSocial utilizando o evento S-1298](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5676190571799-RH-RM-FOP-eSocial-Como-realizar-a-reabertura-da-folha-de-pagamento-no-eSocial-utilizando-o-evento-S-1298)
