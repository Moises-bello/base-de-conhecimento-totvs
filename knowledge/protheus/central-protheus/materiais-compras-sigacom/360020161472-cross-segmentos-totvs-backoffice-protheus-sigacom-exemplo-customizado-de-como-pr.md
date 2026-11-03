---
article_id: 360020161472
category: Materiais - Compras (SIGACOM)
content_hash: 9ec5e05171b76851c3e7641c1d93e7e5cc5fee1298947c31d47237c2b58aefd4
fetched_at: '2026-06-28T22:41:17.692081+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo customizado
  de como preencher o campo de Número do Documento com zeros a esquerda após digitação
type: support-article
updated_at: '2022-05-18T20:50:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020161472-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-customizado-de-como-preencher-o-campo-de-N%C3%BAmero-do-Documento-com-zeros-a-esquerda-ap%C3%B3s-digita%C3%A7%C3%A3o
---

**Dúvida**Exemplo customizado de como preencher o campo de Número do Documento com zeros a esquerda após digitação  
  
**Ambiente**Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Solução**Para atender esta necessidade deverá criar uma *User Function* e adicionar a mesma na validação de usuário (X3\_VLDUSER) do campo Número (F1\_DOC) conforme exemplo abaixo:  
  
USER FUNCTION SF1DOC()  
If !Empty(M->F1\_DOC) .Or. !Empty(cNFISCAL)  
  M->F1\_DOC := StrZero(Val(M->F1\_DOC),9)  
  CNFISCAL := M->F1\_DOC  
Endif    
Return(.T.)

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016260411/Capturar.PNG)

Por não se tratar de uma configuração padrão do sistema, para maiores dúvidas é orientada a verificação por um analista especialista desenvolvedor para as tratativa customizada.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
