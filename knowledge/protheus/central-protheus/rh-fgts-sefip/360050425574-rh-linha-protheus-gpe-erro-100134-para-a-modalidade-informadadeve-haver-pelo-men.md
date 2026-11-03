---
article_id: 360050425574
category: RH - FGTS / SEFIP
content_hash: fc7a8175231ca92f807880ec4e20a6c8e7938c1120a2dcdc36e116c52f268242
fetched_at: '2026-06-28T22:43:41.394510+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro 100134 (Para a modalidade informada,deve haver
  pelo menos um trabalhador com recolhimento de FGTS)  SEFIP
type: support-article
updated_at: '2021-07-17T03:27:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050425574-RH-Linha-Protheus-GPE-Erro-100134-Para-a-modalidade-informada-deve-haver-pelo-menos-um-trabalhador-com-recolhimento-de-FGTS-SEFIP
---

**Dúvida**

Como corrigir o erro 100134 ( Para a modalidade informada,deve haver pelo menos um trabalhador com recolhimento de FGTS)   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.

**Solução**Para solucionar essa dúvida, realize os seguintes passos:

Esse erro ocorre quando não existe recolhimento de FGTS  na competência informada e a SEFIP é gerada com a modalidade **Branco - Recolhimento ao FGTS e Declaração à Previdência***.*  
Exemplo: quando a empresa demite todos os funcionários e recolhe o FGTS na GRRF( Guia de Recolhimento Rescisório do FGTS), neste caso, na competência informada não há recolhimento de FGTS porém é necessário gerar o arquivo para a SEFIP declarar à Previdência.  
O erro em questão gerado e validado pela caixa econômica, pois para a modalidade informada deveria ter pelo menos um trabalhador com recolhimento,  
Para que a inconsistência não seja mais apresentada ao validar o arquivo, realize os passos a seguir:

1. Acesse o aplicativo do **SEFIP** - aba **Movimento;**

2. Selecione os colaboradores que estão alocados na Filial ou Obra que estão todos em rescisão;

3. Arraste estes para a modalidade Declaração ao FGTS e à Previdência;

4. Após execute o fechamento como de costume.   
  
Saiba mais:  <https://tdn.totvs.com/display/public/PROT/FGTS>
