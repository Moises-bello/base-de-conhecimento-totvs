---
article_id: 5722551396759
category: RH - Rescisão
content_hash: a843a7eb62ef2807cfc32a423c344116d5213b6428a6e0f1a46447cbff6b8b23
fetched_at: '2026-06-28T22:43:49.679105+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Desconto INSS rescisão complementar
type: support-article
updated_at: '2025-09-09T13:23:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5722551396759-RH-Linha-Protheus-GPE-Desconto-INSS-rescis%C3%A3o-complementar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34806534694423) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Para o desconto do INSS na rescisão complementar qual tabela deverá ser usada para desconto: O da época ou a atual no momento do calculo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Os tipos de rescisões atuais são:  
\* Complementar por dissídio;  
\* Complementar por pagamento de comissões;  
\* Complementar por Erro/Omissão de Valores.

Nos casos de **complementares para pagamento de comissão ou por erro/Omissão de Valores,** consideramos as seguintes informações:

"Para a complementar de Comissões Pendentes é considerada a soma das Bases das rescisões Original + Complementar pagas dentro da mesma competência que a complementar em questão, conforme § 2º do art. 466 da CLT."

Ou seja, quando a rescisão for por pagamento de comissão e a data de pagamento for em competência diferente da rescisão original o cálculo deve ser individual, desconsiderando a base de cálculo da rescisão original.

Para o caso de rescisões complementares **que não são por dissídio retroativo,** o sistema irá calcular o INSS de acordo com a tabela vigente.

Exemplo: Rescisão original outubro/2021 o calculo do desconto do INSS será de acordo com a tabela de INSS da época no caso 2021.

Em março/2022 precisa pagar uma rescisão complementar. A empresa está pagando uma comissão, ou hora extra, por exemplo. 

O desconto do INSS será de acordo com a tabela vigente.

Mesmo que tenha ocorrido o desconto do TETO na primeira rescisão nesta complementar será aplicado os novos índices.

Logo, o INSS descontado na rescisão do mês 10 não terá reflexo no INSS calculado na complementar do mês 03.

Para o caso de rescisões complementares **por dissídio retroativo** (usuário escolhe a opção dissídio retroativo no calculo da complementar) o desconto do INSS será sobre a tabela da época.

**Para o 13º o recolhimento de INSS** em rescisão complementar, a contribuição do segurado será calculada mês a mês, considerando os valores originalmente pagos em cada competência, ou seja, soma-se a base de INSS da rescisão normal com a base da rescisão complementar, aplica-se a tabela vigente no mês da rescisão complementar sempre respeitando o teto máximo de recolhimento e, depois de aplicada a tabela, subtrai-se o valor de INSS descontado na rescisão normal.

Se a empresa já estiver entregando a obrigação via eSocial, a orientação do MOS é a seguinte: No eSocial quando se tratar de rescisão complementar, deverá ser retificado o evento S-2299, tendo em vista que ele determina que ao enviar esse evento encerra-se o vínculo contratual existente com aquele empregador e antecipa todas as parcelas salariais devidas e já reconhecidas, tais como comissões pendentes e percentagens, que devem ser liquidadas e informadas neste evento.

E o pagamento destas parcelas após o desligamento implica na \*\*retificação do evento S-2299.\*\*

Links adicionais sobre o assunto:

13º <https://tdn.totvs.com/pages/releaseview.action?pageId=450153114>

Tributária <https://tdn.totvs.com/pages/viewpage.action?pageId=454825762>

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
