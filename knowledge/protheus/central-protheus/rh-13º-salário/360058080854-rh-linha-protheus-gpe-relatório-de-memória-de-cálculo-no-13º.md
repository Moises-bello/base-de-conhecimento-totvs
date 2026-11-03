---
article_id: 360058080854
category: RH - 13º salário
content_hash: 8184d411bfae01ba6bcd8a2a5f5ce95c754de333e03e2a39f31f5f46ecc7b4aa
fetched_at: '2026-06-28T22:44:01.585871+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Memória de Cálculo no 13º
type: support-article
updated_at: '2026-06-25T18:47:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058080854-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Mem%C3%B3ria-de-C%C3%A1lculo-no-13%C2%BA
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26731884814487) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Relatório de Memória de Cálculo no 13º  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que possamos entender as médias geradas no cálculo do 13º, devemos gerar a **memória de cálculo** das médias.

Quando o mnemônico **P\_LMEMCALC**for ativado, as fórmulas serão atualizadas para executar a gravação do Log de Cálculo por Funcionário. Se o mnemônico **P\_LMEMCALC**estiver desativado, a chamada para gravação de log não ocorrerá.

Para ativar a memoria de cálculo acesse **Atualizações > Definições de cálculo > Mnemônicos (GPEA300) e** pesquise pelo mnemônico **P\_LMEMCALC.** Segue link contendo passo a passo para parametrização da memoria de calculo: <https://tdn.totvs.com/pages/releaseview.action?pageId=330831446>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26731884824599)  
  
Após parametrização faça a geração do relatório ou consulta da memoria de calculo:  
**1.** Acesse **Consulta > Cálculo > Por Funcionário (GPEA090)**.  
**2.** Selecione o funcionário e clique em **Outras Ações > Relatório Memória de Cálculo**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000094941)  
  
Na tela Memoria de Calculo por Funcionário : clique em **Outras Ações > Parâmetros**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000098462)  
  
Informe nos parâmetros as informações necessárias para gerar o relatório  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000098482)  
  
Relatório gerado para conferencia:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000098502)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100691273)  
  
**Saiba Mais**  
[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio?page=1#articles)  
[RH - Linha Protheus - GPE - Memória de Cálculo das Médias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiasMjTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNTQzMDU1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTWVtJUMzJUIzcmlhLWRlLUMlQzMlQTFsY3Vsby1kYXMtTSVDMyVBOWRpYXMGOwhUOg5zZWFyY2hfaWRJIik1NzdmNTQxYS03NjllLTRkNjgtYjY1NS05ODY5YTA2MDgxZmUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIkFSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gTWVtw7NyaWEgZGUgQ8OhbGN1bG8gZGFzIE3DqWRpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--2c637b1ae8fc28b688452e6004a584f742d1d87e)  
[RH - Linha Protheus - GPE - Geração da Memória de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjqkRPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzExNTExNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtR2VyYSVDMyVBNyVDMyVBM28tZGEtTWVtJUMzJUIzcmlhLWRlLUMlQzMlQTFsY3VsbwY7CFQ6DnNlYXJjaF9pZEkiKTJmZjAzODRmLTUxNDYtNDkxMS04ODgzLWI4OGQ5ZjU0MjAzNAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiQlJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBHZXJhw6fDo28gZGEgTWVtw7NyaWEgZGUgQ8OhbGN1bG8GOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--261c01401a9522cb5e139ceb70216518e0cf7afb)  
[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZUsrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjMxNDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbXByaW1pci1yZWxhdCVDMyVCM3Jpby1kZS1tZW0lQzMlQjNyaWEtZGUtYyVDMyVBMWxjdWxvLWRhcy1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTlkMDc0MjM0LTFiZDMtNGI0NC04NjI2LTRmMzdmOTY0NjVjZQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiXVJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGltcHJpbWlyIHJlbGF0w7NyaW8gZGUgbWVtw7NyaWEgZGUgY8OhbGN1bG8gZGFzIGbDqXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--69bc71cdcc2cdbc1c5628944339a857e77c00f94)  
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**
