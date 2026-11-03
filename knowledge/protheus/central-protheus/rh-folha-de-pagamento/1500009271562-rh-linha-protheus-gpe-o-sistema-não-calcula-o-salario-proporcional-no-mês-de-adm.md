---
article_id: 1500009271562
category: RH - Folha de Pagamento
content_hash: 8ca8894386b026aa3c342bc2cb38e3be88407827ed82a122d3861b518f13cb6c
fetched_at: '2026-06-28T22:44:16.114137+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - O sistema não calcula o salario proporcional no
  mês de admissão dos funcionários horista
type: support-article
updated_at: '2025-10-08T16:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009271562-RH-Linha-Protheus-GPE-O-sistema-n%C3%A3o-calcula-o-salario-proporcional-no-m%C3%AAs-de-admiss%C3%A3o-dos-funcion%C3%A1rios-horista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26192351914647) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No mês de admissão de funcionários horistas, o Sistema não calcula o salário proporcional aos dias trabalhados, calcula o salário integral.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal -  A partir da versão 12.  
  
**Causa**  
Isso ocorre pois a configuração do parâmetro MV\_TPCALEN está com 2-Sintético, dessa forma, no cadastro do Período, na aba Cadastro de Calendário o Sistema não monta o calendário analítico, descriminando dia a dia do mês se é trabalhado, não trabalhado, DSR, feriado ou compensado, sendo assim, o Sistema não tem como validar a proporcionalidade dos dias normais e DSR, então calcula os valores de forma integral:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014388021)  
  
**Solução**Para ajustar essa ocorrência realize os passos abaixo:

**1.** Altere o parâmetro **MV\_TPCALEN** para 1-Analítico via modulo configurador **SIGACFG**:![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014407421)

**2.** Após alteração do parâmetro, entre na rotina **Períodos**, pelo caminho **Atualizações** > **Definições Cálculo** > **Períodos (GPEA400)** e **Altere** o período do processo do horista, será apresentado o calendário conforme abaixo:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014113482)

**3.** Conforme data de admissão do funcionário horista, ao realizar o calculo da folha será gerado as horas normais e DSR de forma proporcional:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014390381)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014390621)

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como conferir o cálculo de funcionário horista?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015195412-MP-GPE-Como-conferir-o-c%C3%A1lculo-de-funcion%C3%A1rio-horista-?source=search)  
[RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_TPCALEN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010081347)
