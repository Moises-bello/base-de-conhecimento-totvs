---
article_id: 1500012096142
category: RH - Provisão
content_hash: 55bf9224800620106689455309f75d58fd627b3687c0aa442fdf9e250371d41c
fetched_at: '2026-06-28T22:43:55.737961+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir a média na provisão com o mnemônico
  P_ADISMED habilitado
type: support-article
updated_at: '2024-05-21T17:54:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012096142-RH-Linha-Protheus-GPE-Como-conferir-a-m%C3%A9dia-na-provis%C3%A3o-com-o-mnem%C3%B4nico-P-ADISMED-habilitado
---

**Dúvida**Como conferir a média na provisão com mnemônico P\_ADISMED habilitado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.17.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1) Atualizações - Definições - mnemônicos:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019269482)

2) Cálculo de folha:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019518781)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019517421)  
  
No exemplo acima, configuramos a verba 602- Gratificação como SIM para periculosidade, de modo que o  valor será somado ao salário base para compor a verba 097 – Periculosidade sobre verbas.

Salário base + gratificação = total base da periculosidade  
Total base periculosidade x 20% = total periculosidade   
  
R$ 2000,00 + R$ 100 = R$ 2.100,00  
R$ 2.100,00 x 20% = R$ 420,00

3)  Cálculo da provisão:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019519221)  
  
Com o mnemônico P\_ADISMED habilitado, as médias serão consideradas na provisão efetuando o seguinte cálculo:

R$ 420,00 /12 = R$35,00 (valor cheio da periculosidade / 12)  
R$ 100,00/12 = R$ 8,33   (Valor cheio da gratificação /12)  
R$ 8,33/12 + 20 % = R$ 0,83 (Média da gratificação /12 e acrescido 20% da periculosidade)

Total = R$ 44,16

**Saiba mais:**  
Para adquirir mais conhecimento acesse os *links* abaixo:  
**Conceito do Mnemônico:** [MP - GPE - Cálculo de adicionais sobre médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016550212-MP-GPE-C%C3%A1lculo-de-adicionais-sobre-m%C3%A9dias)

**Como configurar periculosidade sobre verbas:** [MP - GPE - Como configurar o cálculo de periculosidade sobre Salário + Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038877614-MP-GPE-Como-configurar-o-c%C3%A1lculo-de-periculosidade-sobre-Sal%C3%A1rio-Verbas)
