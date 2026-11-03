---
article_id: 360049370653
category: RH - Funcionários
content_hash: c6737589013483a6cac2ab257cc2344429944360470f54c975481afd690bcb43
fetched_at: '2026-06-28T22:43:27.577392+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como fazer o controle de bloqueio de Funcionários
  demitidos
type: support-article
updated_at: '2025-08-19T22:40:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049370653-RH-Linha-Protheus-GPE-Como-fazer-o-controle-de-bloqueio-de-Funcion%C3%A1rios-demitidos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15522878339351)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como fazer o controle de bloqueio de Funcionários demitidos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Todos os Funcionários cadastrados na tabela **SRA (Cadastro de Funcionários)**, quando desligados da empresa, ficam automaticamente bloqueados para uso em processamentos nas demais rotinas.  
Este controle é realizado pelo campo **RA\_MSBLQL,** mas para flexibilizar o bloqueio ou não bloqueio, existe o parâmetro **MV\_MSBLQL** que pode ser configurado com as seguintes opções:  
**.T.** - determina o **bloqueio** de todos os funcionários da tabela SRA quando desligados pela rotina Rescisão Contratual  
**.F.** - determina o **não bloqueio** dos funcionários da tabela SRA quando desligados pela rotina de Rescisão Contratual, mantendo-os disponíveis para uso em processamentos nas demais rotinas do Protheus.  
  
**Procedimentos para Implementação:  
1.** No menu do Configurador (SIGACFG), selecione as opções: **Ambiente > Cadastros > Parâmetros:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073370093)  
  
  
2.** Busque/Crie o parâmetro **MV\_MSBLQL**: **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072146694)  
  
As especificações são:**  
**Nome:** MV\_MSBLQL  
**Tipo:** 3 - Lógico  
**Descrição:  T** - determina o bloqueio de todos os funcionários da tabela SRA quando desligados pela rotina de Rescisão Contratual (padrão);  
**F** – não bloqueia.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34304983586711)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34304983587863)

**Saiba Mais:**[Campo Reservado \_MSBLQD e \_MSBLQL](https://tdn.totvs.com/display/public/framework/Campo+Reservado+_MSBLQD+e+_MSBLQL)  
[RH - Linha Protheus - GPE - Como habilitar o campo Reg.Habilita](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhaal4%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDY3Mzg1MjItUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8taGFiaWxpdGFyLW8tY2FtcG8tUmVnLUhhYmlsaXRhBjsIVDoOc2VhcmNoX2lkSSIpMWNkOWM0MWMtOTViMS00NzZmLTkwMDItODMzOTFjYTEzZmJkBjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIOUkFfTVNCTFFMBjsIVDoScmVzdWx0c19jb3VudGkCOwI%3D--63e209ac59f4e917d886e1af8e9d2fbcf4867187)  
[RH - Linha Protheus - GPE - Como bloquear a readmissão de funcionários demitidos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjm4C7TUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNTM1MDM3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1ibG9xdWVhci1hLXJlYWRtaXNzJUMzJUEzby1kZS1mdW5jaW9uJUMzJUExcmlvcy1kZW1pdGlkb3MGOwhUOg5zZWFyY2hfaWRJIikxZmM5MGNkMC1mODkxLTQ4MWMtYTNkZi1jMzg3YzBhMTc2OTkGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhByZWFkbWlzc8OjbwY7CFQ6EnJlc3VsdHNfY291bnRpFg%3D%3D--27fad1e21326f86b253029619881c090a6bc39c4)  
[RH - Linha Protheus - GPE - Por que aparece o Help REGBLOQ ao tentar vincular o departamento no cadastro do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXCCG%2BIQ06D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE0NDM4NTc0OTE3NjU1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Qb3ItcXVlLWFwYXJlY2Utby1IZWxwLVJFR0JMT1EtYW8tdGVudGFyLXZpbmN1bGFyLW8tZGVwYXJ0YW1lbnRvLW5vLWNhZGFzdHJvLWRvLWZ1bmNpb24lQzMlQTFyaW8GOwhUOg5zZWFyY2hfaWRJIilhNzFlMTA3ZS00YWJlLTRlN2EtODNlOC05N2QwOGFmOWI2N2MGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg5NVl9NU0JMUUwGOwhUOhJyZXN1bHRzX2NvdW50aQJtBA%3D%3D--0dd5bde1912d053975a5051098995c0a18e0f525)
