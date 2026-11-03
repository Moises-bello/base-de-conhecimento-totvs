---
article_id: 360005036772
category: Materiais - Compras (SIGACOM)
content_hash: 0d1c1c266f9a83c3eb521e8213ef87852b010fb80a95176af7e6a177bfffe09f
fetched_at: '2026-06-28T22:41:08.894835+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help  MV_TPPLA ao Analisar
  Cotação
type: support-article
updated_at: '2022-05-12T21:19:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005036772-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-MV-TPPLA-ao-Analisar-Cota%C3%A7%C3%A3o
---

**Dúvida**Como resolver a mensagem de Help MV\_TPPLA gerado no momento de Analisar Cotação?

**Ambiente**Protheus – Compras – A partir da versão 12.17  
  
**Solução**A mensagem e gerada no momento da análise da cotação devido o campo (lado superior esquerdo da tela de análise) tipo de documento estar com a opção "Contrato de GCT".

Neste caso quando é gerado o contrato através da cotação é necessário informar o código da planilha no parâmetro MV\_TPPLA, porém quando o parâmetro está em branco seu conteúdo gera-se a mensagem de help.

Para solucionar siga o procedimento:

- Acessar o módulo de Gestão de Contratos

- Acesse o menu Atualizações ->Cadastro->Tipos->Planilhas

- Incluir a planilha conforme no exemplo da tela abaixo:

![Capturar6.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006690951/Capturar6.JPG)

No parâmetro MV\_TPPLA informe o código da planilha em seu conteúdo conforme tela abaixo:

![Capturar.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006654412/Capturar.JPG)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
