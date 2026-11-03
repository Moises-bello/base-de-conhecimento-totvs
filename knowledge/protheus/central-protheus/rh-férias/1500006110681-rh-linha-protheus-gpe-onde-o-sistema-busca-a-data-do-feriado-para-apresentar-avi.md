---
article_id: 1500006110681
category: RH - Férias
content_hash: 2574f02c6e77eb90ddb34d139ef841135593c57ad598aeca26c381ae317d4b14
fetched_at: '2026-06-28T22:43:58.337485+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Onde o sistema busca a data do feriado para apresentar
  aviso na programação de férias
type: support-article
updated_at: '2026-04-23T18:40:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006110681-RH-Linha-Protheus-GPE-Onde-o-sistema-busca-a-data-do-feriado-para-apresentar-aviso-na-programa%C3%A7%C3%A3o-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17282428723991) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Onde o sistema busca a data do feriado para apresentar aviso na programação de férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Ao programar férias com data de início 2 dias antes de um feriado sistema apresenta a mensagem:  
**Conforme Artigo 134 parágrafo 3° da CLT, é vedado o inicio das Férias no período de dois dias que antecede feriado ou DSR. Deseja continuar ?**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33997615006999)**

No exemplo acima, existe um feriado cadastrado em 04/07/2025 e o inicio do gozo está em 03/07/2025.  
O sistema emite o alerta de acordo com a Reforma Trabalhista, gerando mensagem de aviso ao usuário caso não esteja a **pelo menos 2 dias de antecedência** de um **feriado ou DSR.**   
Para isso, o parâmetro **MV\_REFTRAB** deve possui a letra "F" referente as validações de Férias. 

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26764607248663)**

O sistema fará a validação do feriado ou DSR de acordo com o calendário vinculado ao módulo de **Ponto Eletrônico (SIGAPON),** que pode ser acessado **no módulo SIGAGPE** em: **Atualizações/ Ponto Eletrônico/ Feriados.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33997653557783)

Caso não exista vínculo com este módulo, será considerado o calendário do período, acessando: **Atualizações/ Definições de Cálculo/ Períodos**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33997615016599)

Abaixo documentação completa: [Implementações da reforma trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=312149147)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Cálculo de férias com período inferior a 10 dias apresenta mensagem: Os dias de férias + abono não podem ser inferiores a 10 dias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhhqZ3UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB82h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0OTM4Nzg3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRlLWYlQzMlQTlyaWFzLWNvbS1wZXIlQzMlQURvZG8taW5mZXJpb3ItYS0xMC1kaWFzLWFwcmVzZW50YS1tZW5zYWdlbS1Pcy1kaWFzLWRlLWYlQzMlQTlyaWFzLWFib25vLW4lQzMlQTNvLXBvZGVtLXNlci1pbmZlcmlvcmVzLWEtMTAtZGlhcwY7CFQ6DnNlYXJjaF9pZEkiKTBjZDY2NTVkLWFhN2MtNDY5ZS05NmI4LTA0ZmM3ODg3Mzg0NwY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX1JFRlRSQUIGOwhUOhJyZXN1bHRzX2NvdW50aQKUBA%3D%3D--cdf3e016d182a1608981d580584c408d4ede01c7)  
[RH - Linha Protheus - GPE - Sistema apresenta mensagem de alerta referente às novas regras da reforma a cada férias calculada, não permitindo efetuar o cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwibsfbSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSICAQFodHRwczovL2NlbnRyYWxkZWF0ZW5kaW1lbnRvLnRvdHZzLmNvbS9oYy9wdC1ici9hcnRpY2xlcy8zNjAwMjE2NjgyNTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVNpc3RlbWEtYXByZXNlbnRhLW1lbnNhZ2VtLWRlLWFsZXJ0YS1yZWZlcmVudGUtJUMzJUEwcy1ub3Zhcy1yZWdyYXMtZGEtcmVmb3JtYS1hLWNhZGEtZiVDMyVBOXJpYXMtY2FsY3VsYWRhLW4lQzMlQTNvLXBlcm1pdGluZG8tZWZldHVhci1vLWMlQzMlQTFsY3Vsby1kZS1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTBjZDY2NTVkLWFhN2MtNDY5ZS05NmI4LTA0ZmM3ODg3Mzg0NwY7CEY6CXJhbmtpDDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX1JFRlRSQUIGOwhUOhJyZXN1bHRzX2NvdW50aQKUBA%3D%3D--90e296acacdc74209455ca501b965a873d3738d1)
