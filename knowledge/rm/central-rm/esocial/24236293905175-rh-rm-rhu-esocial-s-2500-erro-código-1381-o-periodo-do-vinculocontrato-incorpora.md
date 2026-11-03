---
article_id: 24236293905175
category: eSocial
content_hash: d31880026e2548372d558811dd76cfa952b07f98306f3f498eefce7b1e0d62c7
fetched_at: '2026-06-28T22:47:15.324558+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - eSocial - S-2500: Erro código 1381: O periodo do vinculo/contrato
  incorporado de matricula XXXXX devera estar contido no periodo a que se refere o
  contrato de trabalho de matricula XXXXXX do processo trabalhista.'
type: support-article
updated_at: '2026-03-06T17:15:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24236293905175-RH-RM-RHU-eSocial-S-2500-Erro-c%C3%B3digo-1381-O-periodo-do-vinculo-contrato-incorporado-de-matricula-XXXXX-devera-estar-contido-no-periodo-a-que-se-refere-o-contrato-de-trabalho-de-matricula-XXXXXX-do-processo-trabalhista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24236307187607) Tempo aproximado para leitura: **00:02:04 min** **Dúvida**Ao gerar o XML do evento S-2500, a mensagem de erro abaixo é emitida, o que devo fazer?

***Erro código 1381: O periodo do vinculo/contrato incorporado de matricula XXXXX devera estar contido no periodo a que se refere o contrato de trabalho de matricula XXXXXX do processo trabalhista.***

***Localização: /eSocial/evtProcTrab/ideTrab/infoContr/unicContr/matUnic.***

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2209.155 e superiores.**  
  
**Solução**Este erro ocorre quando o Contrato de Trabalho trata-se do tipo **9 - Trabalhador cujos contratos foram unificados (unicidade contratual).**

Para casos em que há unificação de vínculos, fica estabelecido pelo Governo as seguintes orientações:  
  
**4 - Unificação de vínculos**

*4.1. Se houver decisão judicial reconhecendo unicidade contratual de vínculos previamente declarados ao eSocial, o período do contrato de trabalho a ser declarado neste evento deve abranger os períodos referentes a todas as matrículas incorporadas.*

*4.2. Se o contrato reconhecido judicialmente já estiver encerrado deve ser criado neste evento uma nova matrícula, para incorporar os vínculos unificados pela decisão judicial. Neste caso, o campo {indContr} deve ser preenchido com [N] e o campo {tpContr} com [9]. Caso o contrato reconhecido judicialmente ainda esteja ativo, o declarante deve retificar o evento S-2200 mais recente para alterar a data de admissão de forma a abranger todo o período contratual definido na decisão e preencher o campo {indAdmissao} com [3] e o campo {nrProcTrab} com o número do processo.*

*4.3. Se houver incorporação de vínculo(s) encerrado(s) em período anterior à substituição da GFIP para fins previdenciários, o declarante deve:*  
*a) enviar previamente o(s) evento(s) S-2200 relativo a esse(s) vínculo(s) com o grupo [desligamento] preenchido; e*  
*b) preencher o campo {matUnic} do evento S-2500 com a(s) matrícula(s) utilizada(s) no(s) evento(s) S-2200.*

*4.5. O(s) vínculo(s) incorporado(s) cujo(s) desligamento(s) ainda não tenha(m) sido informado(s) deve(m) ser previamente encerrado(s), mediante o envio do correspondente evento S-2299, indicando o motivo de desligamento [44 - Agrupamento contratual], ou do correspondente evento S2399, conforme a hipótese. Deve ser informado o número do processo no campo {nrProcTrab}. A data do desligamento a ser informada é a indicada na decisão judicial.*

*4.6. Após a unificação dos vínculos, não devem ser feitas alterações nos contratos incorporados. Caso haja necessidade de exclusão ou retificação de um vínculo incorporado, é necessária a prévia exclusão do evento S-2500 e, se for o caso, do evento S-2501.*Deverá validar as condições prescritas no Manual de Orientação do eSocial - MOS acima para verificar qual caso caberia ao seu processo e realizar o cadastro corretamente.

**Importante** *Qualquer dúvida, gentileza entrar em contato com a equipe RM Gestão de Pessoas & SSO em nossos canais de atendimento.*

**Saiba mais**Para maiores informações, acesse:  
[RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855)
