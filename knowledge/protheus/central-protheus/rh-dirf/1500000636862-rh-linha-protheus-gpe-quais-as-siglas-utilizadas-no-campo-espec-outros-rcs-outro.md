---
article_id: 1500000636862
category: RH – DIRF
content_hash: 7d0fb211f3c0537bf42fe390a4e6db690281f4171484bba08407232c4c7c38e1
fetched_at: '2026-06-28T22:44:07.169067+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Quais as siglas utilizadas no campo Espec. Outros
  (RCS_OUTROS) em Informações complementares da rotina Manutenção de arquivos
type: support-article
updated_at: '2022-12-22T23:48:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000636862-RH-Linha-Protheus-GPE-Quais-as-siglas-utilizadas-no-campo-Espec-Outros-RCS-OUTROS-em-Informa%C3%A7%C3%B5es-complementares-da-rotina-Manuten%C3%A7%C3%A3o-de-arquivos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quais as siglas utilizadas no campo Espec. Outros (RCS\_OUTROS) em Informações complementares da rotina Manutenção de arquivos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**O campo  **Espec. outros** (RCS\_OUTROS), tem siglas obrigatórias, a exemplo das siglasTMED, FMED02, CMCD01, que tem que existir para que o sistema carregue as informações corretas do plano de saúde no arquivo magnético da DIRF:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11159285442583)

Estas siglas são carregadas de forma automática pelo sistema quando executada a rotina de Geração de Dados da DIRF, onde o Sistema busca informação das tabelas do plano de saúde RHP, RHS e RHN, quando todo o processo de cadastro, cálculo e fechamento do plano de saúde é feito no padrão.

Se observou que o sistema não gerou os códigos neste campo, provavelmente os registros não estão corretos na tabela RHP, RHS, RHN, ou seja, o valor do plano encontra-se somente na tabela SRD - acumulado anuais. Sem o conteúdo deste campo **Espec. outros,** o Sistema não montará o arquivo magnético corretamente.

Abaixo a descrição de cada sigla:

**TMED** - TITULAR ASSISTENCIA MEDICA

**CMED** - CONJUGE ASSISTENCIA MEDICA

**FMED** - FILHO ASSISTENCIA MEDICA

**EMED** - ENTEADO ASSISTENCIA MEDICA

**PMED** - PAI/MAE ASSISTENCIA MEDICA

**OMED** - OUTROS

**TODO** - TITULAR ASSISTENCIA ODONTOLOGICA

**CODO** - CONJUGE ASSISTENCIA ODONTOLOGICA

**FODO** - FILHO ASSISTENCIA ODONTOLOGICA

**EODO** - ENTEADO ASSISTENCIA ODONTOLOGICA

**PODO** - PAI/MAE ASSISTENCIA ODONTOLOGICA

**OODO** - OUTROS ASSISTENCIA ODONTOLOGICA

**AMED** - AGREGADO

No caso dos dependentes e agregados deve ser adicionado o número na frente do tipo, conforme o fornecedor, exemplos:   
  
1 - Fornecedor A tem dois dependentes em Informações complementares, logo, deve ficar uma linha com FMED01 e outra com FMED02:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11159400765975)

2 - Fornecedor B tem um dependente em Informações Complementares, logo, deve ficar uma linha com FMED01 apenas:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11159457659287)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como realizar a conferência do plano de saúde, coparticipação e reembolso para a DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836972)   
[RH - Linha Protheus - GPE - Quando os planos de saúde são informados manualmente para o funcionário o que fazer para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052)
