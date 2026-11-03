---
article_id: 37221035991575
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 188fd2dba5ff6f3df7f54cd970d799455aae70095001f5e4e6344de0c7bca2c1
fetched_at: '2026-06-28T22:39:58.664334+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE São Paulo/SP
  (IBS e CBS)
type: support-article
updated_at: '2026-05-20T19:00:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37221035991575-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-S%C3%A3o-Paulo-SP-IBS-e-CBS
---

**Dúvida**  
Como realizar o destaque de IBS e CBS no XML da prefeitura de São Paulo/SP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
  
**ATUALIZAÇÕES**  
  
**PROTHEUS**  
Aplicar o pacote:  
12.1.2410: <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>   
12.1.2510: <https://suporte.totvs.com/portal/p/10098/download?e=1224039>

Compilar o rdmake NFSEXMLENV:  
12.1.2410: <https://r.totvs.io/p/1247193>  
12.1.2510: <https://r.totvs.io/p/1247194>  
  
**TSS**  
Atualização dos schemas: [Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
  
**PARAMETRIZAÇÃO**

Para geração ou não dos imposto de IBS/CBS os parâmetros precisa está configurados conforme abaixo:

Produção gerar IBS/CBS:  
MV\_RTC56=01/01/2026 (SX6) + MV\_RTCNFSE=01/01/2026 (SPED000)  
  
Produção não gerar IBS/CBS:  
MV\_RTC56=01/04/2026 (SX6) + MV\_RTCNFSE=01/04/2026 (SPED000)  
  
Homologação gerar IBS/CBS:  
MV\_RTC56=01/01/2026 (SX6) + MV\_RTHNFSE=01/01/2026 (SPED000)   
  
Homologação não gerar IBS/CBS:  
MV\_RTC56=01/04/2026 (SX6) + MV\_RTHNFSE=01/04/2026 (SPED000)  
  
**Obs.: Caso o TSS esteja em cloud TOTVS, deverá acionar o suporte para inclusão do parâmetro, informando:** URL do TSS Cloud e CNPJ emissor da nota.

É necessário garantir que a **configuração tributária** no **Configurador de Tributos** inclua os tributos **IBS/CBS**. Dúvidas, sobre a escrituração, a equipe fiscal deverá ser acionada.  
  
**Com isso, o XML deverá ser gerado conforme exemplo abaixo, contendo o grupo <IBSCBS>:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38279122459031)  
  
**IMPORTANTE**  
  
**I.** Se observar, o Grupo <gIBSCBS> **não possui tags próprias para os valores de cada imposto,** somente a informação de CCLASSTRIB, isso por conta de uma **limitação do próprio layout do governo.**Ou seja, no layout atual não é possível enviar outras informações, porém serão implementadas e divulgadas pelo governo durante o ano de 2026;  
  
**II.** Quanto à impressão do PDF da NFS-e na prefeitura, é de responsabilidade integral da própria prefeitura a disponibilização da segunda página com os dados de IBS/CBS, qualquer eventual problema, os mesmos deverão ser acionados.  
  
**COMPLEMENTO**  
[Acesse aqui o artigo com os erros mapeados para a prefeitura de São Paulo-SP no novo layout.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37496812676759-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-S%C3%A3o-Paulo-SP-Erros-mapeados-no-novo-layout-da-NFSE)
