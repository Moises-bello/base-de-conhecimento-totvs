---
article_id: 360020136592
category: RH - Rescisão
content_hash: ee6f967dfe9fc9bb55b04e564474f99fcf89bd67141e4ef987a03ec76162741c
fetched_at: '2026-06-28T22:43:50.882468+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina de rescisão permite manipular os dias de
  aviso prévio trabalhado
type: support-article
updated_at: '2025-08-12T12:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020136592-RH-Linha-Protheus-GPE-Rotina-de-rescis%C3%A3o-permite-manipular-os-dias-de-aviso-pr%C3%A9vio-trabalhado
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19204313082263)* Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Rotina de rescisão permite manipular os dias de aviso prévio trabalhado?

**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para que o sistema permita manipular a quantidade de dias trabalhados na rotina GPEA925, faça as **verificações** abaixo:

1. Na tabela S043, para o Tipo de Rescisão que será cadastrada, verifique se a coluna **Projeta Aviso Prévio** está com S;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13060400717079)  
  
2. No cadastro de Sindicato, na aba Rescisão verifique se o campo **Projeta Aviso Trabalhado** está com **Sim**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13060352296599)

Obs: Campos Dias Av. Prev zerado corresponde a 30 dias, caso tenha preenchimento indevido impacta no cálculo rescisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25668054367895)

3. Verifique se a LIB está atualizada, abaixo link para fazer o *download*  
 <https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/>

4. Verifique se sua base esta atualizada com a Expedição Continua

Release 12.1.33 <https://suporte.totvs.com/portal/p/10098/download?e=1039093>

Release 12.1.2210 <https://suporte.totvs.com/portal/p/10098/download?e=1080347>

Release 12.1.2310 <https://suporte.totvs.com/portal/p/10098/download?e=1123885>

OBS.: Para a release 12.1.33 deve ser aplicado o pacote apenas para clientes com GARANTIA ESTENDIDA, se aplicado em ambiente sem garantia estendida, o ambiente é BLOQUEADO!

**Saiba mais:**Para adquirir mais conhecimento acesse o(s) link(s) abaixo:

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Quais os tipos de Aviso Prévio que temos no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021960552-MP-GPE-Quais-os-tipos-de-Aviso-Pr%C3%A9vio-que-temos-no-sistema?source=search)

[RH - Linha Protheus - GPE - Como alterar aviso prévio após suspensão por afastamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025006374-RH-Linha-Protheus-GPE-Como-alterar-aviso-pr%C3%A9vio-ap%C3%B3s-suspens%C3%A3o-por-afastamento?source=search)

[RH - Linha Protheus - GPE - Como é realizado o cálculo de Aviso Prévio Indenizado?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059193913-RH-Linha-Protheus-GPE-Como-%C3%A9-realizado-o-c%C3%A1lculo-de-Aviso-Pr%C3%A9vio-Indenizado-?source=search)
