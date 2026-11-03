---
article_id: 25453375859863
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 1e33f2afb2781c95a75f6465741767c96593cb7201bc619d20fe12f06340d9f0
fetched_at: '2026-06-28T22:42:04.832204+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como avaliar
  Performance no EFD Contribuições?
type: support-article
updated_at: '2024-08-07T11:46:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25453375859863-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-avaliar-Performance-no-EFD-Contribui%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25453375828375) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como avaliar a **performance** de geração do arquivo txt do **EFD Contribuições**?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**Sugerimos que valide quanto aos passos abaixo, a fim de identificarmos a origem da **lentidão** na geração do arquivo:  
   
1° - Avalie a utilização da quantidade de **Multithreads** habilitadas para a geração do arquivo:  
[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições parâmetros de Multithread da Rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005048041-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-par%C3%A2metros-de-Multithread-da-Rotina?source=search)  
   
2° - Caso com a M**ultithread** o problema ainda persista, sugerimos que valide alguns cenários a fim de detectar se o problema ocorre de um modo geral apenas em período cheio ou se também ocorre em um número menor de dias de processamento, valide abaixo:  
 

* Em período cheio **(01/06/2024** a **30/06/2024**) qual a média de tempo para processamento do arquivo? Com e sem **Multithreads** habilitada.
* Em período menor (**01/06/2024** a **05/06/2024**) qual a média de tempo para processamento do arquivo? Com e sem **Multithreads** habilitada.
* Há uma movimentação mensal muito grande entre as empresas selecionadas? Ao selecionar as filiais para gerar o arquivo, é selecionado um grupo grande de empresas? Qual seria a quantidade total de notas processadas no período inteiro?

   
3° -  Caso o problema ainda persista nos cenários pontuados acima, para concluirmos a análise quanto a **lentidão**, peço que nos encaminhe os seguintes dados abaixo:

* Logprofile da geração do arquivo (Período completo e com todas as empresas): [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar o LogProfiler](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhOH8jUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjE3MDU3NC0tQ3Jvc3MtU2VnbWVudG9zLUJhY2tvZmZpY2UtUHJvdGhldXMtRG9jLUVsZXRyJUMzJUI0bmljb3MtQ29tby1nZXJhci1vLUxvZ1Byb2ZpbGVyBjsIVDoOc2VhcmNoX2lkSSIpNTAzOTc3Y2QtMTRhMS00MzhkLWE5YjEtMTNhZjY2ZTNlNTY4BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIQbG9ncHJvZmlsZXIGOwhUOhJyZXN1bHRzX2NvdW50aSE%3D--cd261141372c78c758c21f41038732ca682ef36a)
* Dbtrace: [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Gerar o Log DbTrace Para Monitorar Baixa Performance?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024300052-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Gerar-o-Log-DbTrace-Para-Monitorar-Baixa-Performance?source=search)
* Responder o checklist (Em anexo);
* Inspetor de objetos;
* Teste realizado com a configuração do MallocIO, conforme a documentação: <https://tdn.totvs.com/display/public/PROT/MallocIO>

**Importante:** Os Logs de processamento da rotina precisam ser encaminhados com o **período e processamento completo** da rotina em questão, para que seja possível darmos continuidade as devidas análises de **Performance**.
