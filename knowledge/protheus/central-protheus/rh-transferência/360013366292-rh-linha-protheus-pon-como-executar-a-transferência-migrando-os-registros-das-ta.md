---
article_id: 360013366292
category: RH - Transferência
content_hash: a99e274ff4080e0b3e3db5d672c7f32f8e711e8b60ef4bfa22c9ff85299a5bd9
fetched_at: '2026-06-28T22:43:23.420164+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - PON - Como executar a transferência migrando os registros
  das tabelas do Ponto para a Filial e Centro de Custo Destino
type: support-article
updated_at: '2025-09-15T18:46:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013366292-RH-Linha-Protheus-PON-Como-executar-a-transfer%C3%AAncia-migrando-os-registros-das-tabelas-do-Ponto-para-a-Filial-e-Centro-de-Custo-Destino
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16775172107159) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como executar a transferência migrando os registros das tabelas do Ponto para a Filial e Centro de Custo Destino?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Quando é realizada uma transferência de funcionários, o Sistema atualiza as **tabelas do** **SIGAGPE,** referente as informações dos funcionários de forma automática.  
O parâmetro **MV\_ARQTRAN** é utilizado na transferência, para atualizar os dados do funcionário para **tabelas de outros módulos**, a exemplo do Ponto Eletrônico, Medicina e Segurança, entre outros. O conteúdo deve ser preenchido com o *alias* - nome da tabela, dos arquivos a serem transferidos, sem espaços ou pontos de separação, **como no exemplo abaixo**, que contém as tabelas do Ponto Eletrônico. Caso precise que mais alguma tabela seja atualizada, basta ir adicionando a mesma no parâmetro.  
  
**Para ajustar o parâmetro, acesse o configurador - SIGACFG, em Ambiente -> Cadastros ->Parâmetros;** Ao acessar a rotina, localize o parâmetro na opção de busca ![](https://centraldeatendimento.totvs.com/hc/article_attachments/16775436286487) , e preencha o Conteúdo informando as tabelas.  
  
**Exemplo:** SP8SPCRFESP5SPISPBSPKRF0RFFSP2RH3RH4RS3RGK  
 **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11588792614423)**

Além do parâmetro **MV\_ARQTRAN,** existe o parâmetro **MV\_TRFDELM,** que tem por finalidade eliminar os registros da Origem nas tabelas, após realizada as transferências das informações para o Destino.  
  
**Exemplo:** Foi efetuado a transferência de filial, da 01 para 02 e o funcionário possui movimentações nas tabelas do Ponto referente a filial 01, serão transferidos os registros para o destino da filial 02 e na filial origem 01, o sistema marcará os registros como deletados, caso a tabela transferida conste neste parâmetro.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16775483502615)  
 **Tabelas listadas acima:**

SP8 - Marcações  
SPC - Apontamentos  
RFE - Pré-leitura  
SP5 - Movimento Refeitório  
SPI - Banco de horas   
SPB - Resultados do Período  
SPK - Eventos abonados  
RF0 - Pré-Abono  
RFF - Pré-ACJEF  
SP2 - Exceções  
RH3 - Solicitações ao RH   
RH4 - Alteração cadastral   
RS3 - Tabelas Auxiliares Portais - Ponto  
RGK - Histórico Aprovações Portal  
  
**Importante:   
Recomendamos não utilizar arquivos de acumulados pois são dados de históricos de períodos já fechados e devem permanecer na origem.   
O parâmetro já deve estar preenchido, antes da execução do processo de transferência, para transferências já executadas sem a configuração não surtirá efeito.**  
  
**Saiba Mais:**[Transferências - V12 (GPEA180 - SIGAGPE - V12)](https://tdn.totvs.com/pages/viewpage.action?pageId=445655177)  
[RH - Linha Protheus - GPE - Tabelas envolvidas na transferência rotina GPEA180](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgh90DTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNjUzNTcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtVGFiZWxhcy1lbnZvbHZpZGFzLW5hLXRyYW5zZmVyJUMzJUFBbmNpYS1yb3RpbmEtR1BFQTE4MAY7CFQ6DnNlYXJjaF9pZEkiKWE0YjI3NzZmLWVjNDctNDA4Yy05YjkyLTJlMjBkZTA0ZTA3NQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiF3RhYmVsYXMgZW52b2x2aWRhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--bdf076232aa72e4cedddf01466b65d270cf4c8a5)  
[RH - Linha Protheus - GPE - Procedimento para transferências de funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017732931-RH-Linha-Protheus-GPE-Procedimento-para-transfer%C3%AAncias-de-funcion%C3%A1rios?source=search)  
[RH - Linha Protheus - GPE - Como funciona o processo de transferências na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021889312-RH-Linha-Protheus-GPE-Como-funciona-o-processo-de-transfer%C3%AAncias-na-vers%C3%A3o-12?source=search)  
[RH - Linha Protheus - GPE - Movimentação de Tabelas em Transferência entre Empresas/Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhucBXVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzIzNzYxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTW92aW1lbnRhJUMzJUE3JUMzJUEzby1kZS1UYWJlbGFzLWVtLVRyYW5zZmVyJUMzJUFBbmNpYS1lbnRyZS1FbXByZXNhcy1GaWxpYWlzBjsIVDoOc2VhcmNoX2lkSSIpYTZiODBlNWItZDcwNC00YjJlLWI4ZTEtMjlhYTA5OWVlNzEyBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJjUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIE1vdmltZW50YcOnw6NvIGRlIFRhYmVsYXMgZW0gVHJhbnNmZXLDqm5jaWEgZW50cmUgRW1wcmVzYXMvRmlsaWFpcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--d410682d520934dea591f3b9f9f59831fd430acf)
