---
article_id: 34722314376343
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 02cc4db3c931c8b460837a8955d4dc15bfbb29031eae1764d34ffbaebdd474d8
fetched_at: '2026-06-28T22:38:54.367934+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como corrigir o Help
  A240LOCPRC na rotina Solicitação ao Armazém?
type: support-article
updated_at: '2026-01-16T12:51:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34722314376343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-corrigir-o-Help-A240LOCPRC-na-rotina-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

Ao fazer uma Solicitação ao Armazém com produto indireto (B1\_APROPRI) e aparecer o Help A240LOCPRC, a correção é usar exclusivamente a rotina de Movimentos Internos (MATA241) para transitar o produto entre armazéns, pois o sistema Protheus trava essa operação fora dessa rotina para produtos com apropriação indireta e armazém 99 (MV\_LOCPROC).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34722321578519) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao fazer uma Solicitação ao Armazém, com o produto indireto(**B1\_APROPRI**) preenchido e apresenta o Help A240LOCPRC, como corrigir ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34722314368791)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
No nativo do Protheus, o conceito da apropriação Indireta (**MV\_LOCPROC/B1\_APROPRI = I**) realmente é travado para que o usuário só consiga usar exclusivamente a rotina de **Movimentos Internos (MATA241)** para transitar o produto entre o armazém padrão/outros armazéns para o Armazém delegado no parâmetro **MV\_LOCPROC**, conforme documentação abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e usabilidade de Apropriação Indireta (MV\_LOCPROC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020688571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-usabilidade-de-Apropria%C3%A7%C3%A3o-Indireta-MV-LOCPROC?source=search)

Portanto, somente via Movimentação Interna (**MATA241**) é possível o saldo sair do armazém **99**. Em outras rotinas ele estoura o Help **A240LOCPRC** por validar a apropriação **indireta** do produto e o armazém **99** sendo o **MV\_LOCPROC**.

**Saiba Mais**:

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
