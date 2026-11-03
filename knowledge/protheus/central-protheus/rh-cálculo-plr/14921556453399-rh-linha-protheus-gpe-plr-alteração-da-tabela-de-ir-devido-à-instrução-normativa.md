---
article_id: 14921556453399
category: RH - Cálculo PLR
content_hash: e9a1bb75e6c44dc1fed37dd2890f9940d9e2391eed898db6757409f0f730d486
fetched_at: '2026-06-28T22:43:12.908848+00:00'
product: protheus
section_id: 360010855894
source: central-protheus
title: RH - Linha Protheus - GPE - PLR - Alteração da Tabela de IR, devido à Instrução
  Normativa RFB nº 2.141, de 22 de Maio de 2023
type: support-article
updated_at: '2024-07-12T19:35:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14921556453399-RH-Linha-Protheus-GPE-PLR-Altera%C3%A7%C3%A3o-da-Tabela-de-IR-devido-%C3%A0-Instru%C3%A7%C3%A3o-Normativa-RFB-n%C2%BA-2-141-de-22-de-Maio-de-2023
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24857074408087) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**PLR - Alteração da Tabela de IR, devido à Instrução Normativa RFB nº 2.141, de 22 de Maio de 2023.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE Gestão de Pessoal - A partir da versão 12.1.33.  
  
**Causa**  
Ajuste na Tabela S044 da rotina Manutenção tabelas.  
  
**Solução**Com a Publicação da Instrução Normativa nº 2.141/2023, houve a atualização dos valores da Tabela de Participação nos Lucros e Resultados.

Além disso, vale ressaltar que a dedução simplificada conforme legislação não deve ser considerada para calcular o IR do PLR, pois o mesmo possuo tributação exclusiva.   
  
Conforme Anexo III - Participação nos Lucros ou Resultados das Empresas da IN º 1.500/2014, teve alteração a partir do mês de Maio do ano-calendário de 2023:

| Valor do PLR anual (em R$) | Alíquota (%) | Parcela a Deduzir do imposto (em R$) |
| --- | --- | --- |
| De 0,00 a 7.407,11 | zero | R$ zero |
| De 7.407,12 a 9.922,28 | 7,5 | R$ 555,53 |
| De 9.922,29 a 13.167,00 | 15 | R$ 1.299,70 |
| De 13.167,01 a 16.380,38 | 22,5 | R$ 2.287,23 |
| Acima de 16.380,38 | 27,5 | R$ 3.106,25 |

No Protheus, os valores são ajustados na tabela **S044**, conforme exemplo abaixo, pelo caminho **>Atualizações > Definições cálculos > Manutenção Tabelas > S044:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14921401243415)

**Saiba Mais:**

[Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE) 

[Orientação Consultoria de Segmentos - Como Tratar o Imposto de Renda sobre PLR](https://tdn.totvs.com.br/pages/releaseview.action?pageId=622214600#Orienta%C3%A7%C3%A3oConsultoriadeSegmentosComoTratardeImpostodeRendaSobrePLR-3.4TabeladeImpostodeRenda-Participa%C3%A7%C3%A3onosLucroseResultados-Instru%C3%A7%C3%A3oNormativan%C2%BA2.141/2023.)

[Orientação Consultoria de Segmentos - Cálculo Simplificado de IRRF](https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosC%C3%A1lculoSimplificadodoIRRF-2.5OdescontosimplificadopodeseraplicadonoParticipa%C3%A7%C3%A3onosLucroseResultados?)

[Instrução Normativa RFB Nº 2141,d e 22 de Maio de 2023.](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=130822)
