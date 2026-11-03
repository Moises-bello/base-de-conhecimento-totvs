---
article_id: 360015782552
category: RH - 13º salário
content_hash: f0df63a1cb34a9cba67cb7173ea0f87f66efbf14be4b872dcabf01129463e24a
fetched_at: '2026-06-28T22:44:00.461496+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de 13º Salário não é efetuado para funcionários
  admitidos antes do ano corrente
type: support-article
updated_at: '2026-06-26T19:15:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015782552-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-13%C2%BA-Sal%C3%A1rio-n%C3%A3o-%C3%A9-efetuado-para-funcion%C3%A1rios-admitidos-antes-do-ano-corrente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18696802896279) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Ao tentar realizar Cálculo de 13º Salário este não é efetuado para funcionários admitidos antes de 2024, por exemplo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre por motivo cadastral, ausências ou dados contidos em tabelas relacionadas a cálculo de 13º  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1 - Verifique se o funcionário possui Salário preenchido em seu cadastro através da rotina **Cadastro de Funcionários**(GPEA010)

2 - Verifique se o Funcionário possui **afastamento** através da rotina de **Ausências** (GPEA240) para o ano corrente, o qual abaterá avos de 13º e, por consequência, não terá 13º a receber -

3 - Verifique se na **tabela SRD** (Acumulados) existe a verba referente a 1ª Parcela calculada (**ID's de Cálculo 0022, 0023 e 0024**) dentro do ano corrente.

4 - Confira a documentação: [RH - Linha Protheus - GPE - Sistema não calcula para alguns funcionários 1ª parcela do 13º salario, Pela EndCalc() - S\_ADT13PGT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgyKwHUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzOTEzMTk1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtU2lzdGVtYS1uJUMzJUEzby1jYWxjdWxhLXBhcmEtYWxndW5zLWZ1bmNpb24lQzMlQTFyaW9zLTElQzIlQUEtcGFyY2VsYS1kby0xMyVDMiVCQS1zYWxhcmlvLVBlbGEtRW5kQ2FsYy1TLUFEVDEzUEdUBjsIVDoOc2VhcmNoX2lkSSIpNTYzODA0NGUtYTNlOC00NzA5LTkyM2EtMzRiZGM4OGViYjZjBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBg1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBTaXN0ZW1hIG7Do28gY2FsY3VsYSBwYXJhIGFsZ3VucyBmdW5jaW9uw6FyaW9zIDHCqiBwYXJjZWxhIGRvIDEzwrogc2FsYXJpbywgUGVsYSBFbmRDYWxjKCkgLSBTX0FEVDEzUEdUBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--c64fc8cb50798cb8db008a0fc4bab9117370d5be)

**Observações:**  
Em casos de Migração, verifique **tabela SRC** (Movimento mensal), se há registro da verba referente a 2ª parcela do 13º com competência do ano anterior. Caso exista, exclua este registro e realize novamente cálculo da primeira parcela.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXpNm%2FAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4NTUxNTczOTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZGEtMSVDMiVBQS1wYXJjZWxhLWRvLTEzLVNhbCVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKTk5ZjU0YTUyLTQ4OTYtNDY4Ny1hZTg1LTU1ZjFhNDhhZTQ3NwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkid1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFpcyBzw6NvIGFzIGRvY3VtZW50YcOnw7VlcyByZWxhY2lvbmFkYXMgYW8gY8OhbGN1bG8gZGEgMcKqIHBhcmNlbGEgZG8gMTPCsCBTYWzDoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--7679154522cbf03f540d7fcceaa52fbd4b270b1d)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do Décimo Terceiro](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXmUm%2BAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4Mjg5NDAwNTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRvcy1hby1jJUMzJUExbGN1bG8tZGEtMiVDMiVBQS1wYXJjZWxhLWRvLUQlQzMlQTljaW1vLVRlcmNlaXJvBjsIVDoOc2VhcmNoX2lkSSIpMTYwMWZlZTgtMjZlMS00MzMwLTk0MmItNjI1NmY5MDMyZGM5BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ6UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFF1YWlzIHPDo28gYXMgZG9jdW1lbnRhw6fDtWVzIHJlbGFjaW9uYWRvcyBhbyBjw6FsY3VsbyBkYSAywqogcGFyY2VsYSBkbyBEw6ljaW1vIFRlcmNlaXJvBjsIVDoScmVzdWx0c19jb3VudGkCvAc%3D--56328d9f407e7284fb3d443c340c1915cbc01a5b)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIillNjU1NzM2ZC03N2IwLTQwZWMtYjQ5Yi0zYmRhMmM1NjhiY2IGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIm5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvIGNvbXBsZW1lbnRvIGRlIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--362f3c9db01aba6853070030c2ef3ea88df12d25)  
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**
