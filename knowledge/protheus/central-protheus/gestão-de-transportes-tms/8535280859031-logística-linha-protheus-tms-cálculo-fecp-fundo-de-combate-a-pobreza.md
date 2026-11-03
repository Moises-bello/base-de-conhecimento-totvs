---
article_id: 8535280859031
category: Gestão de Transportes (TMS)
content_hash: 676e90466d6feb8af73db390498ddf62667f9c21754c0142b45390cc4e62f57a
fetched_at: '2026-06-28T22:45:27.378520+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cálculo FECP - Fundo de Combate a Pobreza
type: support-article
updated_at: '2025-04-10T20:38:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8535280859031-Log%C3%ADstica-Linha-Protheus-TMS-C%C3%A1lculo-FECP-Fundo-de-Combate-a-Pobreza
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16022735620631) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**Como parametrizar o **TOTVS Logística TMS** para calcular o **FECP - Fundo de Combate a Pobreza?**  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O **FECP** é um imposto complementar do **ICMS - Imposto sobre Circulação de Mercadorias e Serviços**, onde será acrescido o percentual do **FECP** ao percentual do **ICMS.**Para que o **TOTVS Logística TMS** calcule o **FECP**, é necessário destacar os itens abaixo:

* **Produto de cálculo:**Na rotina **MATA010 - Produtos**, aba **Impostos**, campo **Aliq Fecp - B1\_FECP** = Percentual da alíquota **FECP.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8535915875095)**

* **Tipos de Entrada e Saída**Na rotina **MATA080 -** **Tipos de Entrada e Saída**, aba **Outros**, campo **Isen. FECP - F4\_ISEFECP** **= 2 - Não**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8536032699543)

* **UF x UF**Na rotina **FISA080 - UF X UF**, é necessário cadastrar as **UFs** de origem e destino que utilizarão o **FECP** e preencher o percentual do **FECP** na aba **ICMS**, no campo **CFC\_ALQFCP - Aliq. FECP**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8552690991383)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8552619515927)

Com os cadastros ajustados, o Sistema irá adicionar o percentual do **FECP** sobre o percentual do **ICMS** do documento.  
  
Vale ressaltar que, conforme manual do SEFAZ, não existe campo que destaque o valor do **FECP** no **DACTE - Documento Auxiliar de Conhecimento de Transporte eletrônico.** Caso o cliente deseje imprimir os valores relativos ao **FECP**, então, a impressão do **DACTE** deverá ser customizada.![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8552815378711)  
  
No *XML* do **CTe**, teremos os valores destacados nas tags:

* **pFCPUFFim** - Percentual do ICMS relativo ao Fundo de Combate à pobreza na UF de término da prestação do serviço de transporte;
* **vFCPUFFim** - Valor do ICMS relativo ao Fundo de Combate á Pobreza da UF de término da prestação.

No exemplo acima, utilizamos **ICMS** de 12% + 2% de **FECP.** Caso necessite utilizar outra alíquota, basta configurar o parâmetro **MV\_FRETEST** com a alíquota desejada, exemplo: RJ20.

Verifique o processo no *How To* a seguir:
