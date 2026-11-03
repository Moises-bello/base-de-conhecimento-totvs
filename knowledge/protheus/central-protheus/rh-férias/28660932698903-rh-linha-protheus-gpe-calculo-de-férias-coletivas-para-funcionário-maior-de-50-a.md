---
article_id: 28660932698903
category: RH - Férias
content_hash: fba4e69e617dced7084985006cab8969301d55e5a892b8c73226560b2834c2e5
fetched_at: '2026-06-28T22:43:57.981782+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo de Férias Coletivas para Funcionário maior
  de 50 anos não considera Dias Coletivas
type: support-article
updated_at: '2025-08-11T11:16:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28660932698903-RH-Linha-Protheus-GPE-Calculo-de-F%C3%A9rias-Coletivas-para-Funcion%C3%A1rio-maior-de-50-anos-n%C3%A3o-considera-Dias-Coletivas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28660947012119) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ao realizarmos o calculo de Férias Coletivas para Funcionários maiores de 50 anos, sistema não considera o parâmetro Dias Coletivas e calcula dias integrais ou de direito para o Funcionário, demonstrando a mensagem no log de calculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28660932641303)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28660932645143)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) GPE Gestão de Pessoal - Todas as versões  
  
**Solução**O incidente ocorre pois o parâmetro **MV\_REFTRAB** está configurado com **SRI** desprezando a Reforma trabalhista para o calculo de Férias.   
Para calcular corretamente as Férias Coletivas, **cancele** o calculo das Férias, ajuste a configuração do parâmetro **MV\_REFTRAB para FSRI**, saia da rotina e acesse novamente para dar carga e recalcule as Férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28660947025559)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28660947028119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28660932661271)

**Saiba Mais**[Reforma Trabalhista](https://tdn.totvs.com/pages/releaseview.action?pageId=312149147)[RH - Linha Protheus - GPE - Documentações relacionadas ao Cálculo de Férias Coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28586423896215-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-ao-C%C3%A1lculo-de-F%C3%A9rias-Coletivas)
