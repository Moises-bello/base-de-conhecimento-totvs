---
article_id: 4409298098583
category: RH - Cálculo Adiantamento
content_hash: fef384769b21c33bd2a49a34409f691b3e9bf9bbd05e28e11f51694a3fb0b758
fetched_at: '2026-06-28T22:43:14.227778+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular adiantamento de salário com definição
  de percentuais por dias trabalhados, através da tabela S143
type: support-article
updated_at: '2025-10-17T11:41:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409298098583-RH-Linha-Protheus-GPE-Como-calcular-adiantamento-de-sal%C3%A1rio-com-defini%C3%A7%C3%A3o-de-percentuais-por-dias-trabalhados-atrav%C3%A9s-da-tabela-S143
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24572245428503)** Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**  
Como calcular adiantamento de salário com definição de percentuais por dias trabalhados, através da tabela S143?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.17.  
  
**Solução**Para possibilitar o cálculo do **adiantamento** de acordo com os **dias trabalhados** foi criada a tabela auxiliar S143, que deverá ser preenchida conforme o exemplo abaixo:

![](https://tdn.totvs.com/download/attachments/636525530/image2021-8-31_8-14-47.png?version=1&modificationDate=1630408487237&api=v2)

No exemplo acima, os funcionários que pertencerem ao sindicato **01**, irão utilizar as **três primeiras faixas,** enquanto os demais irão utilizar as três últimas. Supondo um funcionário do sindicato 01, o cálculo se dará da seguinte forma:

* Caso o funcionário tenha trabalhado 26 dias ou mais no período, o adiantamento será de 50%
* Caso o funcionário tenha trabalhado entre 20 a 25 dias, o adiantamento será de 40%
* Caso o funcionário tenha trabalhado entre 15 e 19 dias, o adiantamento será de 30%
* Se o funcionário tiver trabalhado menos de 15 dias, não receberá adiantamento no mês.

Para obter os dias trabalhados o sistema irá **subtrair** os **dias afastados** e as **faltas** do período. As faltas serão obtidas através da **tabela de apontamentos** do **ponto eletrônico (SPC)** do período que estiver ativo no ponto. Os eventos de falta do ponto que devem ser consideradas devem ser incluídos no novo mnemônico **P\_CDFALADI**, separados por vírgula, da seguinte forma:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409304629271)

**Importante**

Apenas os funcionários que possuam **percentual de adiantamento** definido no cadastro de funcionários (RA\_PERCADT) serão calculados. Se o percentual no cadastro estiver zerado, o cálculo **não** será feito.

Da mesma forma, estando o percentual do cadastro de funcionário preenchido, o sistema **sempre** irá buscar na tabela **S143** o percentual adequado, apenas se não encontrar nenhuma faixa, o percentual do cadastro será utilizado.

Para possibilitar que a verba de insuficiência de saldo transite para o roteiro de adiantamento, ao invés do de folha, foi criado o mnemônico **P\_INSUFADI**, cujo conteúdo padrão é **.F.**, e deve ser alterado para **.T.** para que a verba de insuficiência de saldo seja movimentada para o roteiro de adiantamento.  
  
**Observações**O conceito da tabela **S143** é **prioritário** em relação ao parâmetro **MV\_ADTOPRO**, ou seja, mesmo que o parâmetro esteja ativo e o funcionário tiver **mais** de um dia trabalhado, caso os dias trabalhados seja **menor** do que o configurado na tabela **S143,** o adiantamento **NÃO** será calculado.

**Saiba Mais**

[DT Adiantamento - Definição de percentuais por dias trabalhados](https://tdn.totvs.com/pages/viewpage.action?pageId=636525530)

[RH - Linha Protheus - GPE - Como funciona o adiantamento em meses de trabalho proporcional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034364453-RH-Linha-Protheus-GPE-Como-funciona-o-adiantamento-em-meses-de-trabalho-proporcional)

[RH - Linha Protheus - GPE - Adiantamento Salarial - Configurações e Conceitos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052166714-RH-Linha-Protheus-GPE-Adiantamento-Salarial-Configura%C3%A7%C3%B5es-e-Conceitos?source=search)

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
