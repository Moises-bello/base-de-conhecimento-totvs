---
article_id: 360015439951
category: eSocial - Tabelas/Não Periódicos
content_hash: f7d205906fe25bd0ff708b11a97deb45121bd2ec10a9778690bf772504b08277
fetched_at: '2026-06-28T22:47:10.599854+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RM - eSocial - Tributação/Incidência exclusiva do segurado e suspensão de incidência
  para o evento S-1010
type: support-article
updated_at: '2025-12-23T13:25:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015439951-RM-eSocial-Tributa%C3%A7%C3%A3o-Incid%C3%AAncia-exclusiva-do-segurado-e-suspens%C3%A3o-de-incid%C3%AAncia-para-o-evento-S-1010
---

**Dúvida**  
Como transmitir ao governo a tributação exclusiva do segurado dos eventos do RM (S-1010)?  
  
**Ambiente**  
RM – eSocial - Todas as versões  
  
**Solução**

Segundo o Manual de Orientação do eSocial:

"Caso o empregador/órgão público possua processo administrativo ou judicial com decisão/sentença favorável, suspendendo a incidência tributária sobre determinada rubrica, devem ser informados, nos campos códigos de incidências tributárias {codIncCP}, {codIncIRRF} e {codIncFGTS}, os códigos de incidência suspensa. Nesse caso, o evento “S-1070 – Tabela de Processos Administrativos/Judiciais” deve ser enviado antes deste evento."

[MOS 2.4.02](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

*• Layout do*eSocial onde considera a incidência de INSS (CP) e o processo de não-incidência:

Observação: CP = Contribuição Previdenciária

![Sem_t_tulo2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010425451)

Para geração do *XML* do evento S-1010 atendendo às exigências do governo e o *layout* do eSocial:

- Caso o evento tenha **incidência exclusiva do segurado (mensal) sem processo judicial**:

1. Acesse o cadastro do evento em "Administração de Pessoal > Eventos > Eventos";
2. Na aba "Inc. Proventos" marque a *flag* "Incidência exclusiva do segurado";
3. Gere o *XML* do evento S-1010 para aquela rubrica e verifique se o retorno para *tag* 'codIncCP' será "15 - Exclusiva do segurado - mensal".

Observação 1: Se a *flag* "Incidência exclusiva do funcionário" for marcada no cadastro do evento, a verba não entrará para base de INSS da parte empresa, terceiros e acidente de trabalho.

Observação 2: Caso o evento tenha **incidência exclusiva do segurado (13º salário) sem processo judicial**, ao invés de marcar a incidência de **INSS de Folha** marque a flag de incidência de **INSS de 13º Salário** na aba "Inc. Proventos" no cadastro do evento. O retorno para tag 'codIncCP' neste caso será "16 - Exclusiva do segurado - 13º salário".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010435111)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010410312)

- Caso o evento tenha **suspensão de incidência devido a processo judicial**:

1. Acesse o cadastro do evento em "Administração de Pessoal > Eventos > Eventos";
2. Na aba "Inc. Proventos" marque a devida *flag* de suspensão em "Incidência(s) suspensa(s) em decorrência de decisão judicial" e na aba "Processo de Suspensão de Incidência" crie um novo registro para informar os dados do processo;
3. Gere o *XML* do evento S-1010 para aquela rubrica e verifique se o retorno para *tag*'codIncCP' será de "91" até "94" conforme *layout* do eSocial e se será informado os dados do processo dentro da *tag* 'ideProcessoCP'.

Observação: Na aba "Processo de Suspensão de Incidência" é informado se a suspensão de INSS é somente de Contribuições Patronais ou Contribuições Patronais + Segurados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010435371)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010410492)

**Saiba mais**

Para mais informações sobre o evento S-1070 (Processos Judiciais), acesse o *link*:

[RM - eSocial - Informações que compõem o evento S-1070](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008847432-RM-eSocial-Informa%C3%A7%C3%B5es-que-comp%C3%B5em-o-evento-S-1070-)
