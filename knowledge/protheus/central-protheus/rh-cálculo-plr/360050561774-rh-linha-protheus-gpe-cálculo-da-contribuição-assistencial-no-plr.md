---
article_id: 360050561774
category: RH - Cálculo PLR
content_hash: 6c51c06f3be0cbb43a6fb4a20c39bc23bec326051b819951cc562354d4075525
fetched_at: '2026-06-28T22:43:12.837448+00:00'
product: protheus
section_id: 360010855894
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo da Contribuição Assistencial no PLR
type: support-article
updated_at: '2025-02-26T14:39:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050561774-RH-Linha-Protheus-GPE-C%C3%A1lculo-da-Contribui%C3%A7%C3%A3o-Assistencial-no-PLR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26357393151511)**Tempo aproximado para leitura: **00:02:30 min****Dúvida**Cálculo da Contribuição Assistencial no PLR  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Solução**

1. Acesse no menu **Atualizações > Definições de Cálculo > Mnemônicos (GPEA300)**. Pesquise pelo Mnemônico **P\_VCASSPLR** e informe o **código das verbas** (entre aspas duplas e caso queira informar mais de uma verba separe por vírgula), que deverão ser a **base de desconto** da **Contribuição Assistencial** no cálculo de PLR. No exemplo abaixo foi informado apenas o código de **Provento de PLR** (verba com id de cálculo 0151). Caso tenham mais de um código de verba para compor a base do desconto, o preenchimento deve ser: "001,002,003,004,005" por exemplo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251203781271)  
  
**2.** Acesse o cadastro de roteiros em **Atualizações > Definições de Cálculo > Roteiros (GPEA160)** e selecione o roteiro **PLR.** Clique em **Alterar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251225456279)

**3.** Posicione o cursos na **última linha** e pressione **seta para baixo** no teclado. Será inserida uma nova linha. **Inclua** a formula **S\_CONASSIS()**, a sequencia deve ser **configurada abaixo da Gravação do Calculo da PLR** e clique em **Salvar**. No exemplo abaixo a Gravação do calculo de PLR é a sequencia 00130, então inserimos a sequencia 00131 para a formula S\_CONASSIS();

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251225456919)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251203785879)  
  
**4.** Confirme se as informações relacionadas a **Contribuição Assistencial** estão corretas no **Cadastro do Sindicato em Atualizações > Cadastros > Sindicatos (GPEA340)** na aba **Assistencial.** Deve ser informado o tipo do desconto e o tipo de salário a ser considerado para descontado do funcionário mês a mês. No exemplo abaixo utilizamos a configuração para 5% sobre o salário base;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251203788183)  
  
**Importante**: Caso tenham que realizar algum ajuste no cadastro do sindicato, acesse a rotina alterando a data base do Sistema para o último dia do mês anterior ao cálculo da folha atual. **Exemplo**: Cálculo de Setembro de 2024 - Deve ser utilizada data base 31/08/2024.

**5.** Confirme se existe verba cadastrada com id de cálculo **0069** em **Atualizações > Definições de Cálculo > Verbas (GPEA040)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251203791511)  
  
**6.** Confirme no cadastro do funcionários em **Atualizações > Funcionários > Funcionários (GPEA010)** na aba Funcionais os campos **Sindicato** está informado e campo **Contribuição Assistencial = 1-Sim**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251225465239)  
  
**7.** Calcule o roteiro PLR em **Miscelânea > Cálculos > Por Roteiros (GPEM020)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251203794199)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251203795479)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251225470359)  
  
**8.** Verifique se a contribuição Assistencial foi calculada corretamente conforme a base de cálculo definida para cada roteiro, e de acordo com os percentuais informados no Sindicato em **Consultas > Cadastro > Recibo de Pagamento (GPEA630)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30251225472151)

 

**Saiba Mais**

[Contribuicao Assistencial nos roteiros 132 e PLR](https://tdn.totvs.com/display/PROT/214391+MRH-2712+DT+Contribuicao+Assistencial+nos+roteiros+132+e+PLR)

[RH - Linha Protheus - GPE - Como calcular PLR no roteiro PLR para funcionários demitidos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXX6gwAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDMxNTc4MTkyODctUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY2FsY3VsYXItUExSLW5vLXJvdGVpcm8tUExSLXBhcmEtZnVuY2lvbiVDMyVBMXJpb3MtZGVtaXRpZG9zBjsIVDoOc2VhcmNoX2lkSSIpZTQ5OGNhN2MtYmNhNC00M2EzLTgzOTAtMTczZWYyYmNmMWY5BjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIIUExSBjsIVDoScmVzdWx0c19jb3VudGkBmA%3D%3D--0b0a4d38aa91e88cf6b60068dc7b57182287d950)

[RH - Cálculo PLR](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855894-RH-C%C3%A1lculo-PLR)
