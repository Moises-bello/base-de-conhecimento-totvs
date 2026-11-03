---
article_id: 10591951273111
category: RH - Definições de Cálculo
content_hash: b20158f8b70a63913f30959c3cf984de8e5056205f371eadde31419aa627cc0e
fetched_at: '2026-06-28T22:43:22.471709+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do campo RCH_STATUS no Cadastro
  de Períodos
type: support-article
updated_at: '2025-08-25T13:40:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10591951273111-RH-Linha-Protheus-GPE-Funcionalidade-do-campo-RCH-STATUS-no-Cadastro-de-Per%C3%ADodos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24155688282903) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual a funcionalidade do campo **RCH\_STATUS** no Cadastro de Períodos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O campo **RCH\_STATUS** fica na rotina de **Cadastro de Períodos** em Atualizações > Definições de Cálculo > Períodos, e possui cinco opções:  
**0- Normal**  
**1- Pré-fechado**  
**2- Utilizado por outro usuário**  
**3- Recibos já foram impressos**  
**4- Em Processo de Fechamento**  
**5- Fechado**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10591644302999)

É um campo que pode ser **editado manualmente (exceto depois de Fechado)** para controle interno, servindo como ferramenta de comunicação quando existe mais de um usuário da Folha.   
**Exemplo:** O usuário do RH já calculou, imprimiu a Folha, realizou a conferência faltando apenas fechar, então é possível colocar o *status* manualmente como **Em Processo de Fechamento,** pois assim outro usuário acessando, entenderá que está em processo de fechamento e não precisa mais fazer nenhum procedimento.  
  
**IMPORTANTE:**  
Caso ocorra recálculo dentro do roteiro FOL, o *status* do período com dados INFORMATIVOS (Pré-Fechado/Utilizado por outro usuário/Recibos já foram impressos/Em processo de Fechamento) serão alterados para NORMAL, considerando que podem haver necessidade de nova conferência, impressão de recibos e validação por outro usuário.   
**O campo RCH\_STATUS será atualizado automaticamente quando realizar o fechamento do roteiro em questão, através da rotina GPEM120 - Fechamento Mensal, que o passará para *status*** **Fechado**

**Saiba Mais:**[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj9hsnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjI2MjY1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW8tY2FkYXN0cm8tZGUtcGVyJUMzJUFEb2RvBjsIVDoOc2VhcmNoX2lkSSIpMWVlMzA1NGYtMDVhZS00ZDJkLThkZTItMzhkODgzNDE1ZThkBjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYY2FkYXN0cm8gZGUgcGVyaW9kbwY7CFQ6EnJlc3VsdHNfY291bnRpAu0D--e17ea4b122d628b05a3783a144554a6f4270fb20)  
[RH - Linha Protheus - GPE - Como configurar bloqueio de período na rotina GPEA400 - Cadastro de Períodos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgFNdzUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzQ4Njg1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLWJsb3F1ZWlvLWRlLXBlciVDMyVBRG9kby1uYS1yb3RpbmEtR1BFQTQwMC1DYWRhc3Ryby1kZS1QZXIlQzMlQURvZG9zBjsIVDoOc2VhcmNoX2lkSSIpMWVlMzA1NGYtMDVhZS00ZDJkLThkZTItMzhkODgzNDE1ZThkBjsIRjoJcmFua2kNOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYY2FkYXN0cm8gZGUgcGVyaW9kbwY7CFQ6EnJlc3VsdHNfY291bnRpAu0D--5c5a1d1a82bdc5260f42cd9a0197a5f573f779b6)  
[RH - Linha Protheus - GPE - Tabelas utilizadas para o Cadastro de Período GPEA400](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXxuXhqQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzg0MjYyMjA3OTk1MTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVRhYmVsYXMtdXRpbGl6YWRhcy1wYXJhLW8tQ2FkYXN0cm8tZGUtUGVyJUMzJUFEb2RvLUdQRUE0MDAGOwhUOg5zZWFyY2hfaWRJIikxZWUzMDU0Zi0wNWFlLTRkMmQtOGRlMi0zOGQ4ODM0MTVlOGQGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjYWRhc3RybyBkZSBwZXJpb2RvBjsIVDoScmVzdWx0c19jb3VudGkC7QM%3D--1c443b5b957fb066f008fe7c1fb0e3296adee42a)
