---
article_id: 360026142334
category: RH - Rescisão
content_hash: c4b4ca426343091ddc4e023c687023b6f030491e9ff3b0e6da23ec450e8a0dd5
fetched_at: '2026-06-28T22:43:48.445845+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - "Valor atribuído difere do tamanho do campo (HORAS/DIAS)"
  ao calcular rescisão
type: support-article
updated_at: '2025-05-07T21:07:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026142334-RH-Linha-Protheus-GPE-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-HORAS-DIAS-ao-calcular-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24285571182359)  Tempo aproximado para leitura: 00:02:00 min  
  
**Dúvida**Ao calcular rescisão, sistema calcula apenas uma verba, e ao confirmar o cálculo sistema apresenta a mensagem "Valor atribuído difere do tamanho do campo (HORAS/DIAS)".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O sistema apresenta essa mensagem por alguns motivos, abaixo quais são para que seja verificado:  
  
1. No cadastro de alguma verba que está sendo calculada na rescisão o campo TIPO está em branco:  
Então liste o cadastro de verbas e filtre pelo campo em questão e preencha todas as verbas que estão com o campo TIPO em branco:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041593273)  
  
2. Para alguma verba LANÇADA a coluna Nr.PARCELAS está preenchida com 99, então ao calcular a rescisão, é apresentada a mensagem, zere a coluna Nr.PARCELAS e lance o total em apenas uma verba se necessário:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040763854)  
  
3. A coluna HORAS esta preenchida com um valor que não corresponde com o cálculo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040764594)

**Saiba mais:**[RH - Linha Protheus - GPE - Como gerar relatório com todo o cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgUPlLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMDg5MDc3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1nZXJhci1yZWxhdCVDMyVCM3Jpby1jb20tdG9kby1vLWNhZGFzdHJvLWRlLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKTZhNjAxY2MxLTQ3MWEtNDhlNS1hMzQyLTMzMmEzYzVjYWFlOQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiVFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGdlcmFyIHJlbGF0w7NyaW8gY29tIHRvZG8gbyBjYWRhc3RybyBkZSB2ZXJiYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--39a9e56849f8a930b0c6c543be58daaf35469aaf)   
[RH - Linha Protheus - GPE - Cálculo de rescisão apresenta somente uma verba e ao confirmar o cálculo é gerado aviso: FWNOLIST Valor atribuído difere da lista de valores válidos (Tipo)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXuTQFEgY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSICEwFodHRwczovL2NlbnRyYWxkZWF0ZW5kaW1lbnRvLnRvdHZzLmNvbS9oYy9wdC1ici9hcnRpY2xlcy82Njc0NDY2NTE5MzE5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtcmVzY2lzJUMzJUEzby1hcHJlc2VudGEtc29tZW50ZS11bWEtdmVyYmEtZS1hby1jb25maXJtYXItby1jJUMzJUExbGN1bG8tJUMzJUE5LWdlcmFkby1hdmlzby1GV05PTElTVC1WYWxvci1hdHJpYnUlQzMlQURkby1kaWZlcmUtZGEtbGlzdGEtZGUtdmFsb3Jlcy12JUMzJUExbGlkb3MtVGlwbwY7CFQ6DnNlYXJjaF9pZEkiKTljMGFlMDllLWFjNGMtNGQwZS05M2M5LWMwNGZmODVkMzg0YgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiAb1SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ8OhbGN1bG8gZGUgcmVzY2lzw6NvIGFwcmVzZW50YSBzb21lbnRlIHVtYSB2ZXJiYSBlIGFvIGNvbmZpcm1hciBvIGPDoWxjdWxvIMOpIGdlcmFkbyBhdmlzbzogRldOT0xJU1QgVmFsb3IgYXRyaWJ1w61kbyBkaWZlcmUgZGEgbGlzdGEgZGUgdmFsb3JlcyB2w6FsaWRvcyAoVGlwbykGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--76971fa4f65fcf0f93b08bcde7cf3f5351a0a3c9)  
[RH - Linha Protheus - GPE - Sistema não está apresentando tela de opções para a geração de rescisões complementares](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060953013-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-est%C3%A1-apresentando-tela-de-op%C3%A7%C3%B5es-para-a-gera%C3%A7%C3%A3o-de-rescis%C3%B5es-complementares?source=search)
