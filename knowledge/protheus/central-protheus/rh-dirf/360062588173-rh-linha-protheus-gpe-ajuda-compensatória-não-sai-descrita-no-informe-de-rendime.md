---
article_id: 360062588173
category: RH – DIRF
content_hash: ca38f98270af513adf89dfe3bd5ab4c144f239dbc6fc7d85cd10095e16ca6c48
fetched_at: '2026-06-28T22:44:06.746611+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Ajuda compensatória não sai descrita no Informe
  de Rendimentos do Validador da DIRF
type: support-article
updated_at: '2025-08-19T19:25:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062588173-RH-Linha-Protheus-GPE-Ajuda-compensat%C3%B3ria-n%C3%A3o-sai-descrita-no-Informe-de-Rendimentos-do-Validador-da-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34299658545943)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida** **Ajuda compensatória** não sai descrita no Informe de Rendimentos do **Validador da DIRF**, está correto uma vez que no Informe de Rendimentos gerado no Protheus sai a descrição?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Após a análise da regra apresentada na tela inicial do validador da DIRF a alteração não será feita para informar a descrição **Ajuda Compensatória** no Informe de Rendimentos gerado no validador da DIRF.  
  
Segue análises realizadas:

O rendimento pago como ajuda compensatória deve estar no campo **Outros (especificar)** da subficha Rendimento Isentos   
Está de acordo com o funcionamento do nosso sistema;

Na hipótese do beneficiário ter recebido mais de uma rubrica referente a rendimentos isentos que devam ser informados no campo Outros (especificar)   
Não temos controle sobre isso, porque qualquer verba pode estar com o conteúdo "I" no campo Coluna da DIRF, não sabemos o que foi totalizado na tabela de dados da DIRF;

O declarante **poderá** informar cada uma, detalhadamente....  
Aqui, está claro que é uma opção do usuário e não uma obrigatoriedade.

Além disso, na IN da DIRF, não há orientação específica em relação a esta verba.

**Atualmente:**

Na ficha **RIO** - Pode constar a totalização de diversas verbas que estava com o campo Coluna da DIRF igual a "I", desta forma não temos como diferenciar;

Na ficha de **Informações Complementares "INF",** conforme orientação que consta na tela inicial da DIRF, você "poderá" informar, não que seja obrigado

Não é viável efetuar a alteração porque o processamento da DIRF, tanto na geração de dados para manutenção, como na geração do TXT, já é bastante moroso. Realizar a "busca" desses dados na SRD/SR8, poderá onerar ainda mais a performance.

O valor está sendo acumulado corretamente na parte de Rendimentos Isentos  e no Informe impresso pelo Protheus, a descrição da Rubrica está sendo impressa corretamente, podendo ser utilizado caso a empresa necessite dessas informações descritas.

**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)

[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
