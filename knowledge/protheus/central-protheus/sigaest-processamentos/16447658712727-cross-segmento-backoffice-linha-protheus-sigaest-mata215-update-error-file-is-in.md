---
article_id: 16447658712727
category: SIGAEST - PROCESSAMENTOS
content_hash: 5996b4ff07909f2f7d56c422919b98f52d9d8e2ec56f79e8243dfa89acc5223c
fetched_at: '2026-06-28T22:39:04.947536+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Update error
  - File is in EOF - SA1010 in file on GRAVALOG(APLIB060.PRW)
type: support-article
updated_at: '2023-08-01T14:33:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16447658712727-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Update-error-File-is-in-EOF-SA1010-in-file-on-GRAVALOG-APLIB060-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16447687412503) Tempo aproximado para leitura: **00:03:12 min** **Dúvida**Ao processar a rotina Refaz Acumulados (MATA215) ocorre o error.log "*Update error - File is in EOF - SA1010 in file on GRAVALOG(APLIB060.PRW)".*O que fazer para resolver?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**   
Como possível solução, basta habilitar o parâmetro **MV\_A215CHK** e em seguida reiniciar todos os serviços do Protheus, para em seguida, processar a rotina novamente.   
   
Em caso de persistência, abrir o error.log e pesquisar os campos D1\_CLIENTE/D2\_CLIENTE/C9\_CLIENTE/C5\_CLIENTE/C6\_CLIENTE. Normalmente na maioria deles apontará o mesmo código de cliente. E quando isso ocorre, é porque o fonte está fazendo uma varredura para recomposição do empenho e no momento de validar os dados do cliente há alguma inconsistência no registro do mesmo.

As validações no cliente podem ser:

- Se há duplicidade cadastral no código dele;

- Se o cliente existe na base de dados (SA1);

- Se o pedido de venda vinculado ao cliente existe nos arquivos SC9/SC6/SD2 ou se está deletado (D\_E\_L\_E\_T\_ = '\*')

Caso o cliente ou pedido estejam deletados, validar a possibilidade de recuperar o registro, ou validar se há alguma anomalia no mesmo e tratar internamente para que o Refaz consiga varrê-lo corretamente de acordo com a integração que existe entre as tabelas de cliente e pedido de venda/documento de entrada. 

Saiba mais:

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)
