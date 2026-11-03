---
article_id: 360048552134
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: c6d32167d90ae27923c5f1b11f43a5dedbed703f6c410256d10e073ed6a08185
fetched_at: '2026-06-28T22:39:48.742081+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem: E_SEMGIPO
  Problema: não existe P.L.I para o P.O informado'
type: support-article
updated_at: '2021-11-16T18:22:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048552134-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-E-SEMGIPO-Problema-n%C3%A3o-existe-P-L-I-para-o-P-O-informado
---

**Dúvida**Ao incluir o Embarque apresenta a mensagem - Help: E\_SEMGIPO Problema: não existe P.L.I para o P.O informado?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071971634/mceclip0.png)  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.

**Solução**A mensagem é ocasionada caso na Purchase Order o item encontra-se como Anuente, porém não tem o cadastro da PLI (Licença de Importação).  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073199853/mceclip1.png)

Sendo assim, pode ser alterada a Purchase Order, modificando o campo anuente para "Não-Anuente":  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071972314/mceclip2.png)  
  
Ou realizada a inclusão da PLI, acessando: Atualizações \ Licenca de Import \ Manutencao P.l.i. (EICGI400).

Caso a P.L.I esteja cadastrada na rotina Manutencao P.l.i. (EICGI400) e apresentar a inconsistência reportada, verifique o tamanho dos campos na tabela SW5- "W5\_PO\_NUM', tabela SW2- "W2\_PO\_NUM" e tabela SW6 - "W6\_PO\_NUM" . Deve ser analisado o tamanho dos campos no banco e no Configurador (SIGACFG). Para alterar o tamanho dos campos temos o grupo de campo "148  - Imp.Purchase/Hawb/Invoice/Prof" .  
  
**Saiba mais:** [EIC0018\_Grupo de campos do Purchase Order, Proforma, Invoice e Hawb](https://tdn.totvs.com/display/public/PROT/EIC0018_Grupo+de+campos+do+Purchase+Order%2C+Proforma%2C+Invoice+e+Hawb)
