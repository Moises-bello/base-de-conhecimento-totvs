---
article_id: 360052557233
category: RH - 13º salário
content_hash: 3c7f1b07854de60d00dfec535505ac4055c9363f46bab9d3a0fe95bad49082ba
fetched_at: '2026-06-28T22:44:00.428699+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Base FGTS 13º para funcionário afastado por Serviço
  Militar
type: support-article
updated_at: '2026-06-25T11:15:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052557233-RH-Linha-Protheus-GPE-Base-FGTS-13%C2%BA-para-funcion%C3%A1rio-afastado-por-Servi%C3%A7o-Militar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19055782015511) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Criação Ids 1848 e 1849 - Base FGTS 13º para funcionário afastado por Serviço Militar.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Criação dos Ids de cálculo 1848 e 1849 para **separação da base de FGTS** de 13º do período que o funcionário ficou afastado devido serviço militar.  
  
**1848**: Base Fgts 13 - Afast Militar    
**1849**: Base Fgts 13 Resc. - Afast Militar  
  
Os novos Ids deverão ser configurados com as seguintes incidências para o eSocial:   
**Natureza:** 9905  
**Código Incidência FGTS:** 12- Base de Calculo de FGTS 13º Salario.

**Exemplo de Cálculo**  
-Funcionário afastado por serviço militar (Ausência padrão 005 - AFASTAMENTO TEMPORÁRIO PARA PRESTAÇÃO SERVIÇO MILITAR).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28516820311447)

-Cálculo 1ª parcela  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28516820314775)

1ª Parcela 13º: Salário / 12 x Avos de Direito x 50%  
4.000,00 /12 x 10 x 50% = **1666,67 (verba 107 - id 0022)**  
  
Base FGTS 13º: Salário / 12 x Avos de Direito x 50%  
4.000,00 /12 x 10 x 50% = **1666,67 (verba 722 - id 0108)**  
  
Base FGTS 13º Serviço Militar: Salário / 12 x Meses de afastamento x 50%  
4.000,00 /12 x 2 x 50% = **333,33 (verba 482 - id 1848)**  
  
FGTS: Soma das Bases de FGTS (id 0108 + id 1848) e aplicado 8%  
1666,67 + 333,33 = 2.000,00   
2.000,00 \* 8 = **160,00 (verba 723 - id 0109)**  
  
-Cálculo 2ª parcela:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28516778956951)  
  
2ª Parcela 13º: Salário / 12 x Avos de Direito   
4.000,00 /12 x 10 = **1666,67 (verba 10 - id 0024)**  
  
Base FGTS 13º: Salário / 12 x Avos de Direito - Antecipação do 13º Salário   
4.000,00 /12 x 10 - 16667,67 = **1666,66 (verba 722 - id 0108)**  
  
Base FGTS 13º Serviço Militar: Salário / 12 x Meses de afastamento - Base FGTS Serviço Militar Antecipado   
4.000,00 /12 x 2 - 333,33 = **333,33 (verba 482 - id 1848)**

FGTS: Soma das Bases de FGTS (id 0108 + id 1848) e aplicado 8%  
1666,66 + 333,33 = 1999,99  
1999,99 \* 8 = **159,99 (verba 723 - id 0109)**

**Saiba Mais**  
[9074594 DRHESOCP-18605 DT Base de FGTS 13º - Criação de Ids de cálculo 1848 e 1849](https://tdninterno.totvs.com/pages/viewpage.action?pageId=555847781)  
[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)
