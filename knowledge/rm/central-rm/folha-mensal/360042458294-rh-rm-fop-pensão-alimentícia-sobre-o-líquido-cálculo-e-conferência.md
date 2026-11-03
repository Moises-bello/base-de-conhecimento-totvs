---
article_id: 360042458294
category: Folha Mensal
content_hash: d2673d4b82a2d1cd0fc09cd4066b9b29a051b8dee85dfe631c9d4c0269c03013
fetched_at: '2026-06-28T22:46:59.524598+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Pensão Alimentícia sobre o Líquido: cálculo e conferência'
type: support-article
updated_at: '2024-06-17T15:00:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042458294-RH-RM-FOP-Pens%C3%A3o-Aliment%C3%ADcia-sobre-o-L%C3%ADquido-c%C3%A1lculo-e-confer%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24231120928407)**Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como é realizado o calculo de Pensão Alimentícia do tipo Liquido de Folha, no módulo Folha de Pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Quando há desconto de pensão alimentícia sobre o líquido do funcionário e o salário atinge alguma faixa de desconto de IRRF, devemos desenvolver um sistema de duas equações com duas incógnitas, para se apurar os valores da pensão e do IRRF, a equação deve ser realizada 7 vezes até chegar ao valor final, esse procedimento é necessário pois para o cálculo do IRRF existe o abatimento da Pensão e vice versa pois a Pensão é sobre o Liquido.  
  
**Importante**No final será demonstrado a Fórmula utilizada pelo RM - Folha de Pagamento, é mais simples e resulta exatamente no mesmo valor do cálculo das 7 equações, facilitando a conferência e demonstração dos valores.   
  
**Cenário de exemplo:**

Salário = R$ 17093,99

INSS = R$ 671,11

Tabela do IRRF = 27,5% e dedução R$ 869,36

Pensão = 45%  
  
**Equação:**

**1º Cálculo:**  
IRRF.................... (TPIRRF – TDDIR – INSS - DDEP) = BLI \* FAIXA = BAF - VDF = VIRRF  
PENSÃO ............. (TPIP – TDDP – VIRRF) = BLP \* %PENSAO = VPENS  
  
**A Partir do 2º Cálculo:**  
IRRF ................... (TPIRRF - TDDIR – INSS – DDEP - VPENS) = BLI \* FAIXA = BAF - VDF = VIRRF  
PENSÃO ............. (TPIP – TDDP - VIRRF) = BLP \* %PENSAO = VPENS  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057612213)  
  
**Cálculo do exemplo:**

IRRF.................... (TPIRRF|17093,99 – INSS|671,11) = BLI|16422,88 \* FAIXA|0,275 = BAF|4516,292 - VDF|869,36 = VIRRF|**3646,932**  
PENSÃO .......... (TPIP|17093,99 – TDDP|671,11 – VIRRF|3646,932) = BLP|12775,948 \* %PENSAO|0,45 = VPENS|**5749,1766****A Partir do 2º Cálculo:**  
IRRF...(TPIRRF|17093,99 – INSS|671,11 - VPENS|**5749,1766**) = BLI|10673,7034 \* FAIXA|0,275 = BAF|2935,26843 - VDF|869,36=VIRRF|**2065,908**  
PENSÃO .(TPIP|17093,99 – TDDP|671,11 – VIRRF|**2065,908**) = BLP|14356,972 \* %PENSAO|0,45 = VPENS|**6460,637****3º Cálculo:**  
IRRF ...(TPIRRF|17093,99 – INSS|671,11 - VPENS|**6460,637**) = BLI|9962,243 \* FAIXA|0,275 = BAF|2739,616825 - VDF|869,36 =VIRRF|**1870,257**  
PENSÃO .(TPIP|17093,99 – TDDP|671,11 – VIRRF|**1870,257**) = BLP|14552,623 \* %PENSAO|0,45 = VPENS|**6548,680****4º Cálculo:**  
IRRF ...(TPIRRF|17093,99 – INSS|671,11 - VPENS|**6548,680**) = BLI|9874,2 \* FAIXA|0,275 = BAF|2715,405 - VDF|869,36 =VIRRF|**1846,045**  
PENSÃO .(TPIP|17093,99 – TDDP|671,11 – VIRRF|**1846,045**) = BLP|14576,835 \* %PENSAO|0,45 = VPENS|**6559,576****5º Cálculo:**  
IRRF ...(TPIRRF|17093,99 – INSS|671,11 - VPENS|**6559,576**) = BLI|9863,304 \* FAIXA|0,275 = BAF|2712,4086 - VDF|869,36 =VIRRF|**1843,0486**  
PENSÃO .(TPIP|17093,99 – TDDP|671,11 – VIRRF|**1843,0486**) = BLP|14579,8314 \* %PENSAO|0,45 = VPENS|**6560,924****6º Cálculo:**  
IRRF ...(TPIRRF|17093,99 – INSS|671,11 - VPENS|**6560,924**) = BLI|9861,956 \* FAIXA|0,275 = BAF|2712,0379 - VDF|869,36 =VIRRF|**1842,6779**  
PENSÃO .(TPIP|17093,99 – TDDP|671,11 – VIRRF|**1842,6779**) = BLP|14580,2021 \* %PENSAO|0,45 = VPENS|**6561,091****7º Cálculo:**  
IRRF ...(TPIRRF|17093,99 – INSS|671,11 - VPENS|**6561,091**) = BLI|9861,789 \* FAIXA|0,275 = BAF|2711,991975 - VDF|869,36 =VIRRF|**1842,62**  
PENSÃO .(TPIP|17093,99 – TDDP|671,11 – VIRRF|**1842,62**) = BLP|14580,248 \* %PENSAO|0,45 = VPENS|**6561,11**

Valor final do IRRF: **R$ 1842,62**

Valor final da Pensão: **R$ 6561,11****Demonstrando via RM - Folha de Pagamento o envelope e log de calculo:****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056736034)**Através do Log de Cálculo do envelope, será mostrado a Fórmula da Pensão utilizada pelo RM - Folha de Pagamento, é mais simples e resulta no mesmo valor demonstrado na conferência inicialmente:  
  
Base Pensão = ( RendBrutoPerAtual + RendBrutoOutrosPer + RendBrutoSemIRRF + RendBrSemIRRFOutPer - DescontosPerAtual - DescontosSemIRRF - DescSemIRRFOutPer + DeduzirIRRF - DeducaoIRRF65 - (PercentualIRRF \* (RendBrutoPerAtual + RendBrutoOutrosPer + IncideApenasIRRF - EstornaApenasIRRF)) + (PercentualIRRF \* NroDependentes \* DeducaoIRRFDep) + (PercentualIRRF \* (DescontosPerAtual + DescontosSemIRRFOutrosPer)) - (PercentualIRRF \* DeducaoIRRF65) )

Pensão = Base \* PercentualPensao  
Pensão = Pensão / (1 - (PercentualPensao \* PercentualIRRF))  
  
**Cálculo do exemplo:**

Base Pensão = ( 17093,99 + 0 + 0 + 0 - 671,11 - 0 - 0 + 869,36 - 0 - (0,2750 \* (17093,99 + 0 + 0 - 0)) + (0,2750 \* 0 \* 189,59) + (0,2750 \* (671,11 + 0)) - (0,2750 \* 0) ) = 12.775,948000  
  
Pensâo = 12.775,948000 \* 0,45 = **5.749,176600**  
Pensâo = **5.749,176600** / (1 - (0,45 \* 0,2750)) = **6.561,114522**  
  
Total da Pensão: **6.561,114522**  
  
Base de IRRF:   
Proventos = 17.093,99  
Descontos = 0,00  
Valor Dedutível = 6.561,11  
Base Líquida = 10.532,88  
  
Nro. dependentes de IRRF: 0  
Valor do INSS: 671,11  
Base de IRRF: 9.861,77  
Percentual da Faixa na Tabela de IRRF: 27,5000 %  
Valor do IRRF: Base(9.861,77) \* 27,5000% - 869,36 = 1842,626750  
**Valor do evento: 1.842,62**Valor final do IRRF: **R$ 1842,62**

Valor final da Pensão: **R$ 6561,11**Não existem dispositivos legais que regulamente o cálculo de pensão alimentícia. A fórmula de cálculo disponibilizada no produto segue um padrão foi pautada por exemplo em uma solução disponível a partir de uma consulta número 354 da Cosit junto a Receita Federal disponível neste link:  
  
[SOLUÇÃO DE CONSULTA COSITNº 354, DE 17 DE DEZEMBRO DE 2014](%20http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=59828)

**Veja também exemplo de formula para cálculo de pensão. [Saiba mais](https://tdn.totvs.com/pages/releaseview.action?pageId=452719842)**
