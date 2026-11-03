---
article_id: 9785087547287
category: eSocial - Gerar XML/ Integração Evento
content_hash: d11631fc40194dd1bc542906689e25d5494474b31dc0279c984417329edf7eae
fetched_at: '2026-06-28T22:47:13.018672+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Eventos para empresas optante pelo Simples Nacional
type: support-article
updated_at: '2024-06-07T20:49:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9785087547287-RH-RM-FOP-eSocial-Eventos-para-empresas-optante-pelo-Simples-Nacional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24037755838103)Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como enviar eventos quando sua empresa é optante pelo Simples Nacional?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas versões  
  
**Solução**Abaixo algumas validações que devem ser realizadas para empresas Optante pelo Simples para envio ao eSocial.

**• S-1000 - Informações do Empregador/Contribuinte/Órgão Público**

A **C****lassificação Tributária** deverá ser incluída conforme **Tabela 8 - Classificação Tributária**, constante na **Documentação Técnica do Governo.** No modulo Folha de Pagamento, no menu **eSocial | Informações do Empregador**, preencha os dados de acordo com as tributações da empresa.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10014186509847)

**• S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos** Para o envio das informações deste evento, é necessária a análise dos estabelecimentos do declarante e definição dos dados relativos ao [CNAE preponderante, alíquotas GILRAT, FAP](https://tdn.totvs.com/pages/releaseview.action?pageId=452719324), dentre outros.   
  
**•  S-1020 - Tabela de Lotações Tributárias**No evento **S-1020 - Tabela de Lotações Tributárias**, deverá ser informado o **FPAS** conforme sua atividades (verificar a **Tabela 4 - Códigos e Alíquotas de FPAS/Terceiros** ).  
  
**• S-1280 - Informações Complementares aos Eventos Periódicos**  
Evento utilizado para prestar informações que afetam o cálculo da contribuição previdenciária patronal sobre as remunerações pagas, devidas ou creditadas por declarantes, quando este for optante pela desoneração de folha de pagamento e pelo Simples Nacional com [tributação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028307112-RH-RM-FOP-eSocial-Como-desonerar-uma-empresa-no-eSocial-?source=search) [previdenciária substituída e não substituída.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028307112-RH-RM-FOP-eSocial-Como-desonerar-uma-empresa-no-eSocial-?source=search)   
  
**Observação**  
Após envio dos eventos supracitados com as tributações devidas da sua empresa, poderá gerar os demais [Eventos Periódicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003044711-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-dos-eventos-peri%C3%B3dicos?source=search).   
  
**Saiba mais:**Para mais informações acesse

* [Informações do Empregador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718306)
* [Identificação da origem da Lotação Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015506452-RH-RM-FOP-eSocial-Identifica%C3%A7%C3%A3o-da-origem-da-Lota%C3%A7%C3%A3o-Tribut%C3%A1ria?source=search)
* [Documentação Técnica — eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
