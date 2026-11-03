---
article_id: 38361262439319
category: SIGAACD - Automação e Coleta de Dados
content_hash: 219c925211a09f06eb6f683c56c22f9d869d56c2860163653bfc17d263c62257
fetched_at: '2026-06-28T22:39:12.753624+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Impressora não localizada!
  Deseja selecionar impressora?
type: support-article
updated_at: '2026-02-12T17:47:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38361262439319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Impressora-n%C3%A3o-localizada-Deseja-selecionar-impressora
---

O artigo orienta como corrigir o erro "Impressora não localizada!" ao imprimir etiquetas nos emuladores VTDEBUG ou TERA TERM no TOTVS Protheus, recomendando instalar o WebApp e WebAgent, habilitar o agente local e configurar a impressora no campo CB5\_PRINTR da rotina Local de Impressão (ACDV060).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38361262412951) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao acessar as rotinas do Emulador VTDEBUG ou TERA TERM, para impressão de etiqueta apresenta a mensagem "Impressora não localizada! Deseja selecionar impressora?" como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
Para selecionar a impressora nas rotinas de impressão de etiqueta, é necessário realizar o procedimento abaixo:

1. Para imprimir as etiquetas pelos emuladores(VTDEBUG)e(TERA TERM),utilizar o WebApp e o WebAgent para instalação.
2. Baixe os instaladores do WebAgent a partir da[Central de Downloads.](https://suporte.totvs.com/portal/p/10098/download#company/)
3. Ao acessar o Protheus via SIGAMDI via navegador, instalar o **WebApp**e o **WebAgent**marcando a opção **"Habilitar Agente Local"** em configurações.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38361262415895)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38361262418199)
4. Configure a rotina  Local de Impressão(ACDV060) e informar a impressora, no campo **CB5\_PRINTR.**  
     [Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Configurar Local de impressão (ACDA060) para    utilizar na impressão de Etiquetas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas)  
     
   [Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV060 - Como criar o campo CB5\_PRINTR?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15310825405719-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV060-Como-criar-o-campo-CB5-PRINTR)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
