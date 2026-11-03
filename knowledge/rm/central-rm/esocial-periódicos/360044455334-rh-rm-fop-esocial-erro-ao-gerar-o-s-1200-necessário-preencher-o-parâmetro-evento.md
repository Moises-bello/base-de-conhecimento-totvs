---
article_id: 360044455334
category: esocial - Periódicos
content_hash: debcb30cc497c014eef93d70d94489c8acef2d92e4ad182705af1f15a4a65a28
fetched_at: '2026-06-28T22:47:09.294387+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar o S-1200: Necessário preencher o parâmetro
  "Evento INSS Férias Alíquota Normal Envelope"'
type: support-article
updated_at: '2022-06-15T21:07:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044455334-RH-RM-FOP-eSocial-Erro-ao-gerar-o-S-1200-Necess%C3%A1rio-preencher-o-par%C3%A2metro-Evento-INSS-F%C3%A9rias-Al%C3%ADquota-Normal-Envelope
---

**Ocorrência**Ao gerar evento S-1200 para funcionários que tiveram férias no mês, é exibido o erro **Necessário preencher o parâmetro Evento INSS Férias Alíquota Normal Envelope nos Parâmetros Gerais do eSocial**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre pois os campos **INSS Férias Alíquota Normal Envelope** e **INSS Férias Próximo Mês Alíquota Normal Envelope** localizados no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 6/7** não estão preenchidos.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6806461833751/mceclip0.png)

**Solução**Para correção dessa ocorrência, siga os passos abaixo:

1. Crie dois eventos como **base de cálculos, sem incidência, sem código de cálculo** e insira-os nos campos supracitados;   
2. Transmita o evento S-1010 das verbas criadas;  
3. Em seguida, gere novamente o evento S-1200 e transmita ao governo.

**Saiba mais**  
Para maiores informações, acesse:  
     • [Configurações Gerais 6/7](https://tdn.totvs.com/pages/releaseview.action?pageId=540899121)
