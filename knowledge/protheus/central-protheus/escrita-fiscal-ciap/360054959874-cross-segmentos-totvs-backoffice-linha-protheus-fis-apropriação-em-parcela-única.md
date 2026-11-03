---
article_id: 360054959874
category: Escrita Fiscal - CIAP
content_hash: ba743a4c745f0ff39c9a24d6d4861dcf8f774e37198c4bdee55095ae6a80668c
fetched_at: '2026-06-28T22:39:33.732239+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Apropriação em parcela
  única - CIAP
type: support-article
updated_at: '2021-07-29T13:15:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054959874-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Apropria%C3%A7%C3%A3o-em-parcela-%C3%BAnica-CIAP
---

**Dúvida**

Existe a possibilidade de apropriação em única parcela o credito de ativo (CIAP) cujo valor não seja maior que R$ 1.000,00 ?  
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Implementação de rotina no documento de entrada, para que o cliente possa ter a possibilidade através do preenchimento de um parâmetro, definir o número de parcelas que será utilizada para apropriação do CIAP de acordo com o valor.

**Para utilização da funcionalidade:** O parâmetro MV\_CIAPVPA deverá ser preenchido em forma de Array, contendo o número de parcela e o valor da apropriação.

**Exemplo de Preenchimento**: {1,1000}

* Não é necessário colocar aspas no conteúdo do parâmetro, conforme o exemplo acima preencha com {}. Na primeira posição temos o número de parcela e após a virgula temos o valor da apropriação.

Na gravação da nota fiscal de entrada, no momento da geração do CIAP, o sistema irá verificar o conteúdo do parâmetro, caso o valor da apropriação que está sendo grava seja menor ou igual ao valor da apropriação preenchida no parâmetro MV\_CIAPVPA, o sistema então definirá que o número de parcela será o que estiver no parâmetro.

Link contendo a legislação citada:  
<http://legislacao.sef.sc.gov.br/legtrib_internet/html/decretos/2016/dec_16_0703.htm>
