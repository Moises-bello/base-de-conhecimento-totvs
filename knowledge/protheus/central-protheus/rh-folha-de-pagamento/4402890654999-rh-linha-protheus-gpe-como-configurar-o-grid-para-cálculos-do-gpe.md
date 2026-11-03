---
article_id: 4402890654999
category: RH - Folha de Pagamento
content_hash: a3c1ad3be489007f45f2aaf26a4b130d717100d89e975558b6e6b44783b3af10
fetched_at: '2026-06-28T22:44:13.311797+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o GRID para cálculos do GPE
type: support-article
updated_at: '2025-09-12T14:38:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402890654999-RH-Linha-Protheus-GPE-Como-configurar-o-GRID-para-c%C3%A1lculos-do-GPE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26264887280791) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como configurar o **GRID** para cálculos do GPE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução****1.** Para efetuar a configuração de GRID é necessário seguir o passo a passo do link abaixo:  
<https://tdn.totvs.com/display/framework/GridServer+-+Como+configurar>  
 **2.** Configure também os parâmetros corretamente conforme seu ambiente:  
**MV\_GRID** - Indica se utilizará GRID no Cálculo da Folha **MV\_GPEGRID** - Caso MV\_GRID ativado, habilita rotinas p/ Grid: 1=Provisão, 2=Cálculo Folha/13o., em branco=Todas as opções **MV\_REGGRID** - Indica o numero de registros a serem processados por *Thread* no calculo com GRID  
**MV\_MINGRID** - Desliga o GRID automaticamente se o numero de funcionários a ser processado for menor que o numero definido neste parâmetro  
  
Também é possível configurar o GRID através de um *Wizard*, abaixo segue documentação de como realizar o processo:  
[RH - Linha Protheus - GPE - *Wizard* para criação de ambiente com GRID](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10013228512023)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
