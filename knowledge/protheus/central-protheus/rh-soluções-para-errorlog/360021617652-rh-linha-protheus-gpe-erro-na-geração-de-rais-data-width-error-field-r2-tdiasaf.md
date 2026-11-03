---
article_id: 360021617652
category: RH - Soluções para error.log
content_hash: 8331618ab4e263b5d3a1f2ae90c713f88d1d973d6d7ca586f2cae7288325b2a3
fetched_at: '2026-06-28T22:44:08.865741+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro Na Geração de Rais - Data width error - Field:
  R2_TDIASAF'
type: support-article
updated_at: '2025-08-20T18:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021617652-RH-Linha-Protheus-GPE-Erro-Na-Gera%C3%A7%C3%A3o-de-Rais-Data-width-error-Field-R2-TDIASAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34323863744919)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao tentar **gerar o Arquivo - Rais**, através da rotina **GPEM500,** gera ***error log - Data width error - Field:* R2\_TDIASAF *Value: \_\_\_\_\_\_ on* FGRAVAFA(GPEM500.PRX)**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**O erro é gerado quando o funcionário possui um afastamento cujo os dias pagos pela empresa é maior que 15 dias referentes aos afastamentos.  
  
**Solução**Verifique se existe em **Lançamentos/ Ausência (SR8)** alguma matrícula com afastamento cujo campo Dias Pagos Empresa (R8\_DPAGOS) está **maior** que 15 dias. Se sim, será necessário ajuste.  
Execute novamente a geração dos dados para a RAIS (GPEM500) e em seguida a geração do Magnético da RAIS (GPEM530).  
  
No programa da RAIS, o arquivo importado deve ser excluído e importado novamente para não gerar duplicidade de informações.  
Se os campos acima mencionados estiverem com conteúdo correto, execute o backup do RPO e a aplicação do pacote abaixo, opte pelo pacote de acordo com a versão de seu sistema:  
  
[MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)  
  
**Importante:**O campo Dias Pagos Empresa (R8\_DPAGOS) é alimentado a partir da informação do campo Dias Pg Empre - localizado em definições de cálculo/ tipos de ausência.  
  
Para análise dos afastamentos maior que 15 dias é de **extrema importância** observar o tipo de afastamento, pois alguns deles tem mais que 15 dias pagos pela empresa e está correto. Exemplo: Férias e Licença maternidade.   
  
Recomendamos que o ajuste seja feito de forma manual em casos pontuais. Se existir mais funcionários no mesmo cenário, sugiro que execute o RDMAKE UPDDPGSR8, que fará o ajuste do campo mencionado de forma automática para vários funcionários.  
Doc.: *<https://tdn.totvs.com/display/public/PROT/DRHGCH-9769+-+Ajuste+campo+R8_DPAGOS+com+valor+negativo>*

**Saiba mais**[RH Expedição Contínua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)
