---
article_id: 31870229424151
category: Financeiro - Configurador de Tributos
content_hash: 8acdcfc15cc908c21b134ed8f5ff2992b9317cc0ecfe4c6313aff50918a40b2d
fetched_at: '2026-06-28T22:37:46.254682+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Regra financeira
  - É possível gerar via configurador de tributos o PCC aglutinado no módulo financeiro
  vindo integrado de outro módulo?
type: support-article
updated_at: '2025-10-20T16:44:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31870229424151-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regra-financeira-%C3%89-poss%C3%ADvel-gerar-via-configurador-de-tributos-o-PCC-aglutinado-no-m%C3%B3dulo-financeiro-vindo-integrado-de-outro-m%C3%B3dulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31870238312983) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
É possível gerar, via configurador de tributos, o PCC aglutinado no módulo financeiro, vindo integrado de outro módulo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12  
  
**Solução:**  
No Configurador de Tributos (FISA170), cada regra fiscal cadastrada está vinculada exclusivamente a um único tipo de tributo (relação 1 para 1). Como a geração dos títulos no módulo Financeiro está diretamente associada a esse cadastro, não é possível aglutinar dois ou mais tributos em um único registro.

Isso se deve ao fato de que a entrega das obrigações fiscais ocorre de forma individual — cada tributo é tratado e entregue separadamente. Assim, o módulo Financeiro não tem a possibilidade de reunir diferentes tributos em um único título para, posteriormente, desagregá-los no momento da integração com outros módulos, como o TAF.

**Recomendações**

Bases migradas para o Configurador devem ajustar suas rotinas e processos, considerando que os tributos serão gerados e tratados separadamente.

**Saiba mais**

[Como fica a geração de impostos aglutinados no Configurador de Tributos](https://tdn.totvs.com/pages/releaseview.action?pageId=979816086)  
[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Configurador de Tributos - How to](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33852958399767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Configurador-de-Tributos-How-to)
