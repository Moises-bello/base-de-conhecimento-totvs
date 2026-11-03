---
article_id: 360053697053
category: RH - Definições de Cálculo
content_hash: 7d33dab6a19870a64f69b77721b6eda62f5e48645ede423154d56c65333d6285
fetched_at: '2026-06-28T22:43:22.570890+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: 'RH - Linha Protheus - GPE - Cadastro da tabela S037 - Encargos Empresa '
type: support-article
updated_at: '2024-02-29T13:47:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053697053-RH-Linha-Protheus-GPE-Cadastro-da-tabela-S037-Encargos-Empresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21368563703831) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como alterar % empresa de inss, percentual acidente do trabalho, entre outros encargos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Acesse **Atualizações**/ **Definições Cálculo**/ **Manutenção Tabelas**: selecione a tabela S037 - Encargos Empresa.   
Nela são definidos os percentuais de encargos da empresa, tais como INSS, FGTS, por tipo de contrato entre outros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21368508264855)

Detalhamento de cada campo a ser preenchido:

* **Tipo de Contrato**: Informar qual tipo de contrato pertence os encargos. Existem dois tipos:

Tipo 1 – Encargos a serem aplicados nos funcionários com contrato por tempo indeterminado.

Tipo 2 – Encargos a serem aplicados nos contratos por prazo determinado, lei 9601/98.

* **Percentual Empresa**:Informar a alíquota referente à contribuição da empresa ao INSS.
* **Percentual Acidente de Trabalho**: Informar o percentual definido de acordo com a atividade da empresa. Devem ser seguidas as determinações do INSS para seu preenchimento (GRPS).
* **Percentual Risco de Acidente de Trabalho (RAT)**: Informar o percentual de encargo de risco de acidente de trabalho a ser recolhido.
* **Percentual FGTS**: Indicar o percentual a ser aplicado sobre as remunerações pagas, para depósito de FGTS.
* **Recolhe S/ Faturamento**: Definir se a empresa efetua o recolhimento da contribuição previdenciária apurada sobre o faturamento ou efetua o recolhimento da contribuição previdenciária apurada sobre o total da folha de pagamento. Opções válidas: S = Sim/ N = Não/ M = Mista/ C = Concomita
* **Opt Simples**: Definir se a empresa é optante do SIMPLES, sendo considerado na geração da RAIS: 1 = Sim (Optante) e 2 = Não (Não optante).
* **Código de Pagamento GPS**: Uma vez o código da GPS informado aqui, não será considerado o código da configuração de parâmetros de emissão da GPS.
* **Valor Mínimo GPS**: Informar o valor mínimo considerado para recolhimento dos valores da Guia da Previdência Social (GPS).
* **Código Empresa FGTS**: Informar o código de identificação da empresa no sistema de controle do FGTS, fornecido normalmente pela CEF ou pelo órgão competente da sua região.
* **Percentual Provisão 13º Salário**: Informar o percentual a ser aplicado sobre as verbas mensais da folha de pagamento para cálculo dos valores de provisão 13º salário.
* **Percentual Provisão Féria**: Informar o percentual a ser aplicado sobre as verbas mensais da folha de pagamento para cálculo dos valores de provisão férias.
* **Percentual Provisão Rescisão**: Informar o percentual a ser aplicado sobre as verbas mensais da folha de pagamento para cálculo dos valores de provisão rescisão.
* **Id. Contribuição Substituída**: Informar:

  1 = Contribuição Substituída Integralmente.

  2 = Contribuição não substituída.

  3 = Contribuição não substituída concomitante com contribuição substituída.

**Observação:**

**-**Caso preencha o campo ‘Recolhe S/ Faturamento’ com a opção ‘S’, é necessário possuir registros na Tabela Auxiliar S033 - Faturamento Mensal, da competência em que está sendo efetuado o cálculo para apuração dos encargos da contribuição previdenciária.

- Ao preencher os campos referente a percentuais sobre Provisão 13º Salário, Férias e Rescisão é necessário relacionar as verbas que entrarão para a provisão no cadastro de verbas, através do campo Custo.  
  
**Saiba Mais**[RH - Linha Protheus - GPE - eSocial - S-1005 - Como realizar alteração do FAP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041285873)[RH - Linha Protheus - GPE- Onde alterar o % do FAP e como informar o RAT (acidente de trabalho) no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028194571)  
[RH - Linha Protheus - GPE - Como cadastrar % INSS acidente de trabalho quando o percentual é diferente por filial](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX8UQj4ww6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE0MTY5Njg4ODMwMjMxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWNhZGFzdHJhci1JTlNTLWFjaWRlbnRlLWRlLXRyYWJhbGhvLXF1YW5kby1vLXBlcmNlbnR1YWwtJUMzJUE5LWRpZmVyZW50ZS1wb3ItZmlsaWFsBjsIVDoOc2VhcmNoX2lkSSIpNGNmMGE5NWUtZjc1NC00N2QwLThkZTYtNjUyMzZkZjJhNjZhBjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIJUzAzNwY7CFQ6EnJlc3VsdHNfY291bnRpAX4%3D--5acba35933d8f446e3fefc9d774f007c62460992)  
[RH - Linha Protheus - GPE - Atenção: Tabelas S037 e S038 não estão cadastradas para o período de cálculo na Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXHuPImQw6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB2Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEzODU0NjM5ODU3MTc1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1BdGVuJUMzJUE3JUMzJUEzby1UYWJlbGFzLVMwMzctZS1TMDM4LW4lQzMlQTNvLWVzdCVDMyVBM28tY2FkYXN0cmFkYXMtcGFyYS1vLXBlciVDMyVBRG9kby1kZS1jJUMzJUExbGN1bG8tbmEtUHJvdmlzJUMzJUEzbwY7CFQ6DnNlYXJjaF9pZEkiKTRjZjBhOTVlLWY3NTQtNDdkMC04ZGU2LTY1MjM2ZGYyYTY2YQY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiCVMwMzcGOwhUOhJyZXN1bHRzX2NvdW50aQF%2B--aaa94de3c5adb727f9bf3dcada7b48d9d33cbd18)  
[RH - Linha Protheus - GPE - Como calcular em folha de pagamento FGTS 2% para aprendiz, quando em tabela S037 contrato Determinado está vinculado com 8%](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXTFF8AQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB2mh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDQ0MjcxODEyMDctUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY2FsY3VsYXItZW0tZm9saGEtZGUtcGFnYW1lbnRvLUZHVFMtMi1wYXJhLWFwcmVuZGl6LXF1YW5kby1lbS10YWJlbGEtUzAzNy1jb250cmF0by1EZXRlcm1pbmFkby1lc3QlQzMlQTEtdmluY3VsYWRvLWNvbS04BjsIVDoOc2VhcmNoX2lkSSIpNGNmMGE5NWUtZjc1NC00N2QwLThkZTYtNjUyMzZkZjJhNjZhBjsIRjoJcmFua2kNOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIJUzAzNwY7CFQ6EnJlc3VsdHNfY291bnRpAX4%3D--2d891cde5a0ad7d278b7960dd4bfe3bcf5b93429)
