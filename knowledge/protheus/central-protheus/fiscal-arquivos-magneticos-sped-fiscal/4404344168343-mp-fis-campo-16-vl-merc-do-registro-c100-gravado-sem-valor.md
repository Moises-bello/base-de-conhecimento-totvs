---
article_id: 4404344168343
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: b3af0c339335ad02dcdbc0f7eff5a9f536a8473ed6f0197fda36b109ce520587
fetched_at: '2026-06-28T22:42:03.768416+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Campo 16 (VL_MERC) do Registro C100 Gravado Sem Valor
type: support-article
updated_at: '2021-07-15T17:56:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404344168343-MP-FIS-Campo-16-VL-MERC-do-Registro-C100-Gravado-Sem-Valor
---

**Dúvida**

O que verificar quando o campo 16 (VL\_MERC) do registro C100 é gravado sem valor?

**Ambiente**  
Exemplo:  
Cross Segmento - Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

É gravado com valor zerado quando se trata de regime especial, fornecedor do simples nacional. Segue abaixo tratativa no Protheus:

Para informar que o documento foi emitido sob norma específica ou regime especial, além da tratativa já existente do campo **Reg. Esp.CIAP (F4\_RGESPCI)** da tabela **Tipos de Entrada/Saída (SF4),** está disponível a partir do mês de Março de 2012 o tratamento para indicar que a Nota Fiscal foi emitida sob norma específica, pelo campo **Norma Esp. (F4\_NORESP)**, também da tabela SF4.

Além disso, para as UF (**MV\_ESTADO**) contidas no parâmetro **MV\_UFRESPD**, são considerados como regime especial (cód. 08) os clientes/fornecedores optantes pelo **Simples Nacional A1\_SIMPNAC/A2\_SIMPNAC = SIM**.

Também serão consideradas como regime especial (cód. 08) as Notas Fiscais de série 890 a 899, conforme cita a Exceção 7 (sete) do registro C100.

Abaixo configuração do parâmetro **MV\_UFRESPD**:

<https://tdn.totvs.com/display/public/PROT/FIS0005_SPED_FISCAL>

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404343656343/mceclip1.png)

Abaixo link do Guia Prático da EFD ICMS/IPI, página 59, "Exceção 4" no qual contém explicação do tratamento acima:   
  
<http://sped.rfb.gov.br/estatico/30/5EC21565F41BC9D392045D71E5706429186705/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.0.6.pdf>

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404343911063/mceclip2.png)
