---
article_id: 27339306688535
category: Originação de Grãos (OG)
content_hash: b9cf8e9866599b91e80a3beac928e097de0b2388d7cd6e6d2266db645c619978
fetched_at: '2026-06-28T22:45:42.609873+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetros SIGAGCP
type: support-article
updated_at: '2025-06-24T14:29:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27339306688535-Agro-Linha-Protheus-AGR-Par%C3%A2metros-SIGAGCP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27339306680727)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Para que serve os **Parâmetros SIGAGCP**? **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12 **Solução  
Parâmetros SIGAGCP:**

|  |  |  |
| --- | --- | --- |
| MV\_GCPACN | Ambiente utilizado na integração Comprasnet. 1= Treinamento. 2= Produção. | 1 |
| MV\_GCPDESP | Arquivo em formato *dot* com o modelo do Termo de Despacho. | GCP\_DESP |
| MV\_GCPDEST | Diretório de gravação dos documentos relatórios. | C:\WORDTMP\ |
| MV\_GCPDOC | Caminho para gravar os arquivos docs gerados. | \samples\documents\gcp\doc\ |
| MV\_GCPDOT | Caminho dos arquivos em formato *dot*. | \samples\documents\gcp\dot\ |
| MV\_GCPFIAP | Indica se os pedidos gerados por Edital na Compra Centralizada serão administrados pela filial de compra (C) ou pela filial de entrega (E). | C |
| MV\_GCPHOMG | Arquivo em formato *dot* com o modelo do Aviso de Homologação. | GCP\_EXTHOM |
| MV\_GCPLETS | Indica a TES de saída padrão usada para leilão no Gestão de Licitações. |  |
| MV\_GCPMCLI | Modalidades em que o participante é um cliente (SA1). | LL\ |
| MV\_GCPORG | É utilizado para identificar o órgão que representa a filial logada na Manutenção da Ata SRP. |  |
| MV\_GCPPARE | Ativa o cadastro de permissões. | .T. |
| MV\_GCPPRD | Arquivo em formato *dot* com o modelo da Proposta de Resolução de Diretoria. | GCP\_RESDIR |
| MV\_GCPRCPF | CPF do responsável pela autorização de compras no portal Comprasnet. |  |
| MV\_GCPRESP | Nome do responsável pela autorização de compras no portal Comprasnet. |  |
| MV\_GCPRFUN | Função do responsável pela autorização de compras no portal Comprasnet. |  |
| MV\_GCPTERM | Arquivo em formato *dot* com o modelo do Termo de Homologação. | GCP\_TERHOM |
| MV\_GCPUASG | UASG do órgão governamental. |  |
| MV\_INTEDIT | Habilita a integração do Edital. | .F. |
| MV\_NOTAEMP | Atende os critérios da Nota de Empenho e apresenta as opções:  ·   Verdadeiro: indica a utilização de Nota de Empenho e na geração de documentos do Edital será a abertura da Tela da Nota de Empenho carregando as informações do Edital de forma automática. Também, permite a geração de Nota de Empenho através da ATA de Registro de Preço.  ·   Falso: o comportamento continuará padrão. |  |
| MV\_REMADT | Código do tipo de revisão de aditivo de contrato revisado pelo processo remanescente no módulo de Gestão de Licitações. |  |
| MV\_TPPLA | Tipo da planilha utilizada na geração de contrato por meio de Editais ou cotações. |  |
| MV\_VLCOMPZ | Valida composições de lote zeradas que não sejam do licitante vencedor? | .T. |
