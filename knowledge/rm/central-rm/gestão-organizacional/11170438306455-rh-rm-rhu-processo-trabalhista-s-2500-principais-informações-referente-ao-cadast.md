---
article_id: 11170438306455
category: Gestão organizacional
content_hash: d3d284478ff93c1c650c980569cc01580286b9fcd2dd3f39b967aadf53e41082
fetched_at: '2026-06-28T22:47:22.288308+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processo Trabalhista - S-2500: Principais informações referente
  ao cadastro'
type: support-article
updated_at: '2025-12-16T16:34:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11170438306455-RH-RM-RHU-Processo-Trabalhista-S-2500-Principais-informa%C3%A7%C3%B5es-referente-ao-cadastro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15863827490071) Tempo aproximado para leitura: **00:02:50 min** **Dúvida**Quais as principais informações quanto ao cadastro do S-2500 - Processo Trabalhista?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - 12.1.34 e superiores.  
  
**Solução****O que é o evento S-2500?**  
O evento S-2500 registra informações de processos trabalhistas na Justiça do Trabalho, bem como acordos firmados nas Comissões de Conciliação Prévia (CCP) ou nos Núcleos Intersindicais (Ninter). Ele contempla:

* Informações cadastrais e contratuais do vínculo;
* Bases de cálculo de FGTS, contribuição previdenciária (RGPS);
* Valores de verbas remuneratórias ou indenizatórias.

**Quem deve enviar?**  
Todos os declarantes que, em processos trabalhistas, acordos via CCP/Ninter ou determinações judiciais:

* Reconhecerem ou alterarem vínculo trabalhista;
* Pagarem verbas de natureza remuneratória ou indenizatória ao trabalhador;
* Forem obrigados a recolher FGTS, INSS ou IRRF.

**Obs:** Mesmo que não haja valores devidos, se houver impacto fiscal (como IRRF), o evento deve ser enviado para possibilitar o envio do S-2501.  
  
  
**Prazo de envio**  
O evento deve ser enviado até o dia 15 do mês subsequente à ocorrência de:

* Trânsito em julgado de decisão líquida;
* Homologação de acordo judicial;
* Celebração de acordo na CCP/Ninter;
* Determinação judicial de cumprimento antecipado (mesmo parcial).

Se o dia 15 cair em feriado ou fim de semana, prorroga-se para o próximo dia útil.  
  
  
**Retificações e Reenvios**

* Deve ser enviado mesmo que não haja valores a recolher (previdência, FGTS ou IR).
* Caso haja nova decisão ou acordo, o evento deve ser retificado até o dia 15 do mês seguinte.
* Se já tiver sido enviado um S-2501 correspondente, este deve ser excluído antes da retificação.

**Observações no evento**

* {obsProcTrab}: observações sobre o processo (não aparecem na CTPS Digital);
* {observacao} em [infoVinc]: aparece na CTPS Digital, como anotações gerais.

**Tipo de Contrato - Campo {tpContr} (RM: No cadastro do Contrato de Trabalho > Guia Informações Gerais > Tipo de Vínculo):**1 ⟶ Sem alteração nas datas de admissão/desligamento  
2 ⟶ Alteração na data de admissão  
3 ⟶ Alteração/inclusão da data de desligamento  
4 ⟶ Alteração na admissão e no desligamento  
5 ⟶ Reconhecimento de vínculo de emprego (sem info prévia no eSocial)  
6 ⟶ Trabalhador sem vínculo empregatício (TSVE)  
7 ⟶ Vínculo encerrado antes da obrigatoriedade do eSocial  
8 ⟶ Responsável indireto (conforme item 8 do manual)  
9 ⟶ Unificação de contratos (unicidade contratual)

**Casos especiais – Rescisão indireta**  
✔️ Reconhecida:

* Evento S-2299 já enviado? → Retificar, com motivo [17].
* Não enviado? → Enviar S-2299 com motivo 17, sem [verbasResc].
* Sempre enviar o S-2500, com os devidos códigos e valores.

❌ Não reconhecida:

* Reconheceu-se extinção por outro motivo?  
   - Enviar S-2299 (ou retificar);  
   - S-2500 com {indMotDeslig} = [S] ou [N], conforme o caso.
* Não houve extinção do vínculo?  
  - Enviar S-2298, ou S-2230 (se aplicável);  
  - S-2500 só se houver impacto tributário.

**Vínculo informado previamente no eSocial**  
Se o vínculo já foi enviado anteriormente:

* Use a mesma matrícula;
* Preencha {indContr} com [S];
* Não preencher o grupo [infoCompl];
* Se houve alteração contratual determinada judicialmente → enviar S-2206;
* Alterações de categoria/atividade devem constar em [mudCategAtiv].

**Vínculo não informado previamente**Se o vínculo nunca foi enviado ao eSocial:

* {indContr} = [N]
* Preencher [infoCompl] com:  
  - Evolução salarial (grupo [remuneracao], até 99 ocorrências);  
  - Demais dados contratuais atualizados (CBO, natureza da atividade etc);  
  - Informações cadastrais vigentes à data da decisão (ex: nome);
* Alterações devem constar em [mudCategAtiv].

**Importante**Apenas decisões/acordos ocorridos **a partir de 01/10/2023** são obrigatórios no S-2500.

**Saiba Mais**Para maiores informações, acesse:

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [Manual de Orientação eSocial - Leiaute S-1.3 NT 03/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf)

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
