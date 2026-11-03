---
article_id: 22646754502807
category: RH - 13º salário
content_hash: 0dae1a920376e3549bb7f8e9a02a678c7a2ff0d709a07fef9754f1af6de99dec
fetched_at: '2026-06-28T22:44:01.579908+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Rateio do 13º Salário
type: support-article
updated_at: '2025-08-15T18:56:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22646754502807-RH-Linha-Protheus-GPE-Rateio-do-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22646754471703) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como parametrizar o rateio do 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O 13º Salário pode ser Rateado por Centro de Custo, Item Contábil e Classe Valor (MV\_ITMCLVL). Para que o cálculo do rateio, realize as configurações abaixo:  
  
1. Acesse o Configurador (SIGACFG) Ambientes / Cadastros / Parâmetros, e verifique se o parâmetro **MV\_RATPROV** está configurado com **S**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22646754477079)  
  
2. Acesse o Módulo Gestão de Pessoal (SIGAGPE) Funcionários / Programação de Rateio, e informe o rateio do funcionário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22646754477847)  
Importante: Para que as colunas Item Contábil e Classe Valor sejam apresentadas, o parâmetro MV\_ITMCLVL deve estar configurado com 1 ou 3.  
  
3. Acesse Atualizações / Definições de Cálculo / Verbas / Localize as verbas de 13º salário que serão rateadas e altere o campo "**Rateio C. Cto**." (RV\_ENCARCC) para **B**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22646754481431)

4. Processe o Cálculo do 13º Salário;

5. Acesse Consultas / Cálculos / Por Funcionário, e Consulte o Cálculo do Roteiro 131 ou 132:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22646737881111)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22646737882519)   
Veja que cada verba foi gerada duas vezes, uma vez para cada centro de custo informado na Programação de Rateio.

**Saiba Mais:**  
[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Memória de Cálculo das Médias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiasMjTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNTQzMDU1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTWVtJUMzJUIzcmlhLWRlLUMlQzMlQTFsY3Vsby1kYXMtTSVDMyVBOWRpYXMGOwhUOg5zZWFyY2hfaWRJIik1NzdmNTQxYS03NjllLTRkNjgtYjY1NS05ODY5YTA2MDgxZmUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIkFSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gTWVtw7NyaWEgZGUgQ8OhbGN1bG8gZGFzIE3DqWRpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--2c637b1ae8fc28b688452e6004a584f742d1d87e)  
[RH - Linha Protheus - GPE - Geração da Memória de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjqkRPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzExNTExNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtR2VyYSVDMyVBNyVDMyVBM28tZGEtTWVtJUMzJUIzcmlhLWRlLUMlQzMlQTFsY3VsbwY7CFQ6DnNlYXJjaF9pZEkiKTJmZjAzODRmLTUxNDYtNDkxMS04ODgzLWI4OGQ5ZjU0MjAzNAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiQlJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBHZXJhw6fDo28gZGEgTWVtw7NyaWEgZGUgQ8OhbGN1bG8GOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--261c01401a9522cb5e139ceb70216518e0cf7afb)  
[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZUsrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjMxNDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbXByaW1pci1yZWxhdCVDMyVCM3Jpby1kZS1tZW0lQzMlQjNyaWEtZGUtYyVDMyVBMWxjdWxvLWRhcy1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTlkMDc0MjM0LTFiZDMtNGI0NC04NjI2LTRmMzdmOTY0NjVjZQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiXVJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGltcHJpbWlyIHJlbGF0w7NyaW8gZGUgbWVtw7NyaWEgZGUgY8OhbGN1bG8gZGFzIGbDqXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--69bc71cdcc2cdbc1c5628944339a857e77c00f94)  
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**
