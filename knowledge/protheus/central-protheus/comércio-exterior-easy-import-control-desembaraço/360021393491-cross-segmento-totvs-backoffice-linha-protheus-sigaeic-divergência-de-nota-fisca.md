---
article_id: 360021393491
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 6ef80dd8ddfd85cdadf8d8787fccbdd617204105dd0982b3166b193408f9334d
fetched_at: '2026-06-28T22:39:51.022200+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Divergência de
  Nota Fiscal de Importação
type: support-article
updated_at: '2024-03-13T11:20:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021393491-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Diverg%C3%AAncia-de-Nota-Fiscal-de-Importa%C3%A7%C3%A3o
---

**Dúvida**Ao gerar uma Nota Fiscal de Importação apresenta Divergência nos valores de impostos e despesas (FOB, Frete, Seguro, Imposto de Importação, IPI, PIS, Cofins e ICMS), como verificar?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**A nota fiscal de importação representa a entrada da mercadoria no país. O SIGAEIC não emite Nota fiscal, ele apenas gera um espelho da nota e preenche as tabelas do SIGACOM (SF1 e SD1), quando o MV\_EASY estiver habilitado, ou seja, integrado ao módulo SIGACOM.  
A nota fiscal representa o custo da importação, e contêm o valor descrito na Declaração de Importação com as despesas aduaneiras.

**1. Nota primeira, mãe ou única**

* Contêm todos os valores de impostos, bem como suas respectivas bases;
* Contêm todas as despesas base de imposto e base de ICMS;
* Deve estar de acordo com a D.I. (Declaração de Importação);
* A nota Única contempla também as Despesas base de Custo;

**2. Como realizar a conferência dos impostos da nota de importação?**  
Divergência no **Impostos de Importação (II)**: [Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Conferência do Imposto de Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5328635061783)  
Divergência no **IPI, PIS e/ou Cofins**: [Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Conferência do IPI, PIS e COFINS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5377019309719)  
Divergência no **ICMS**: [Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Conferência do ICMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5380076189079)

**3. Parâmetros**  
Relação de parâmetros para quebra da nota fiscal de importação:

* **MV\_NUMITEN** - Numero máximo de itens por nota fiscal, para controlar a quebra de nota automaticamente;
* Quebra da nota por **CFO e Operação CFO**: [Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Quebra de nota de importação por CFO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034643674)

**Saiba mais:**

**[How To | MP-SIGAEIC - Recebimento de Importação - ICMS](https://www.youtube.com/watch?v=gz8DbzxExH4&ab_channel=TOTVSSolu%C3%A7%C3%B5es)**

**[How To | MP - SIGAEIC - Recebimento de Importação ICMS Parâmetros](https://www.youtube.com/watch?v=CNZHyyEw7sk&ab_channel=TOTVSSolu%C3%A7%C3%B5es)**

**[How To MP-SIGAEIC - Recebimento de Importação - EICDI154](https://www.youtube.com/watch?v=P6JICIwDHJs&ab_channel=TOTVSSolu%C3%A7%C3%B5es)**
