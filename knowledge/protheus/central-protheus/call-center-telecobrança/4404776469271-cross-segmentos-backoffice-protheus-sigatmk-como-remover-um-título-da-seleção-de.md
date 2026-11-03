---
article_id: 4404776469271
category: Call Center - Telecobrança
content_hash: 14e751a7eeafbd33eddff481f2099f945516b13894d99884f81e99d3ef443f2b
fetched_at: '2026-06-28T22:41:28.568580+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Como remover um título da
  Seleção de Títulos (TMKA180)
type: support-article
updated_at: '2026-01-26T18:25:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404776469271-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Como-remover-um-t%C3%ADtulo-da-Sele%C3%A7%C3%A3o-de-T%C3%ADtulos-TMKA180
---

**Dúvida**  
Como remover um título da Seleção de Títulos (TMKA180) tabela SK1?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - todas as versões

**Solução**

Após processar a "Seleção de Títulos" (TMKA180), o sistema carrega os títulos do Contas a Receber (Tabela SE1) para a "Seleção de Títulos" (Tabela SK1), porém caso tenha carregado algum título que não deseja realizar a cobrança, é necessário gerar uma **Exceção:**

1. Acesse a rotina "Seleção de Títulos" (TMKA180);  
2. No browse, posicione no título e selecione o botão outras ações, o sistema abrirá uma tela demonstrando os títulos do cliente posicionado;

3. Marque a opção "**Bloqueia e Libera os Títulos**" e **Confirme:**

**![p5.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4404769048855)**

Após isto o título não será mais apresentado nos atendimentos de telecobranças na filial logada, ficará marcado com "**XXXXXX**" no campo **Operador** (**K1\_OPERAD**) na "Seleção de Títulos" (TMKA180)**:**

**![titulo0.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4404769139351)**
