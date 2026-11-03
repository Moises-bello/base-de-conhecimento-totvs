---
article_id: 360053359714
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 5a1da6a574b9215b578cceb7d1d585cbe9a7e1cdea46f940faedb0d88a15175f
fetched_at: '2026-06-28T22:40:47.646462+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB -  ECF : COMO GERAR  Y520
  CFQ_CODNAT / NAT_OPER '
type: support-article
updated_at: '2022-05-31T19:06:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053359714-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-COMO-GERAR-Y520-CFQ-CODNAT-NAT-OPER
---

**Ocorrência**

Campo de Natureza NAT\_OPER do registro Y520  sendo gerado incorreto ou não sendo gerado mesmo após preencher o campo  CFQ\_CODNAT  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - SIGACTB - todas as versões

**Requisitos**

* **Em base teste**
* [Como realizar a atualização do ECF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-MP-SIGACTB-ECF-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ECF-?source=search)
* Veja [como gerar o registro Y520](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025640474-MP-SIGACTB-ECF-Y520-COMO-GERAR-?source=search)

**Solução**

1º Verifique se a Consulta Padrão do campo CFQ\_CODNAT no SIGACFG está com C1N3, caso não, altere para este:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090991873/mceclip0.png)

2º Ao realizar o cadastro da Natureza da Operação dentro da rotina TAFA329 (Y520), e agora terá que ser amarrada a Natureza no Código:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088856754/mceclip1.png)

Escolha algum código, e cliente em Editar:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090992193/mceclip2.png)

Amarrar o Código da ECF:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090992233/mceclip3.png)

Após Confirmar todas as telas para salvar e após gerar o arquivo, deste modo o sistema irá gerar o código corretamente:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090992453/mceclip4.png)

|Y520|R|13|1|99671|5000,00|  
  
|Y520|: Identificação do tipo do registro.  
|R|: Rendimentos recebidos do exterior.  
|13|: País (13 = Afeganistão).  
|1|: Forma de recebimento (1 = Operação de Câmbio).  
|99671|: Natureza da operação (99671 = Câmbio Simplificado Simultâneo  
|5000,00: Valor recebido (R$ 5.000,00).
