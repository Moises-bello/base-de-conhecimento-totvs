---
article_id: 4406594861335
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 242b8a35dddc296bd94a054880b8c6950754ec755b0ac44050eafd3f2375972e
fetched_at: '2026-06-28T22:39:57.341548+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - E16 - A data
  da emissão do RPS não poderá ser superior a data de hoje
type: support-article
updated_at: '2025-07-18T14:46:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406594861335-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-E16-A-data-da-emiss%C3%A3o-do-RPS-n%C3%A3o-poder%C3%A1-ser-superior-a-data-de-hoje
---

**Ocorrência**No módulo Faturamento, ao tentar realizar a transmissão de um RPS é apresentado a rejeição:   
*"E16 - A data da emissão do RPS não poderá ser superior a data de hoje"***Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre especificamente quando a data ou hora de emissão do RPS são superiores à data/hora do servidor da prefeitura.  
  
**Solução**Para esses casos é necessário checar como estão sendo gerados os campos F2\_EMISSAO e F2\_HORA, pois eles serão os conteúdos montados no XML do RPS.  
Caso estejam sendo gravados de forma incorreta nesses campos, deverá checar os parâmetros abaixo:  
  
**MV\_HORARMT**1 = Grava no RPS o horário/data da máquina que está acessando o SmartClient;  
2 = Grava no RPS o horário/data do servidor onde o Protheus está instalado;  
3 = Grava no RPS o horário/data do servidor, mas será levado em consideração o horário da filial utilizada para a geração do documento de acordo com o Sigamat.emp ou SYS\_COMPANY. **MV\_HVERAO**.T. = Define se servidor está em horário de verão;  
.F. = Define se servidor não está em horário de verão.O primeiro é utilizado para definir de onde será considerado esses valores e o segundo para ativar/desativar o horário de verão no ambiente.  
  
Vale lembrar que por exemplo, caso o parâmetro MV\_HORARMT esteja como 1 ou 2, deverá verificar se a hora da máquina ou servidor acessado estão corretos para que o protheus obtenha esses valores e grave corretamente na tabela SF2.
