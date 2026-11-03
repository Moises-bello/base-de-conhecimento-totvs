---
article_id: 19293534942615
category: SIGAEST - CUSTOS
content_hash: d91629feee0e92ee01bc3477c8631535c3b4ced08ccb945a3d7b60dc7924afcf
fetched_at: '2026-06-28T22:39:00.773736+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como processar o custo
  médio sem concorrência com movimentações de Estoque?
type: support-article
updated_at: '2025-03-12T12:25:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19293534942615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-processar-o-custo-m%C3%A9dio-sem-concorr%C3%AAncia-com-movimenta%C3%A7%C3%B5es-de-Estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19293525969431) Tempo aproximado para leitura: **00:03:20 min****Dúvida**

Como processar o custo médio sem concorrência com movimentações de Estoque?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - A partir da versão 12.1.33  
  
**Solução**

Durante a execução do recálculo do custo médio (MATA330), o saldo final do período é atualizado na tabela de saldos físico/financeiro (SB2) e, caso o ambiente onde a execução ocorre seja operado por vários usuários, pode ocorrer concorrência na gravação da tabela SB2, causando lentidão no recálculo do custo e em outros processos.

Ao habilitar o parâmetro **MV\_A330SB2**, o recálculo do custo médio passa a considerar a tabela TR2XXSP (onde XX é o código do grupo de empresas) como a tabela de saldos físico/financeiro para a execução, minimizando a concorrência com a SB2. Ao término do recálculo, antes da geração dos lançamentos contábeis, os **saldos finais\*** calculados na TR2 são gravados na SB2 conforme disponibilidade dos registros.

**Atenção**

O parâmetro MV\_A330SB2 estará disponível para os releases 12.1.33 e 12.1.2210; a partir da 12.1.2310, o parâmetro passará a ser obsoleto, pois a funcionalidade estará sempre ativa.

Tabela TR2

A tabela TR2XXSP é uma tabela auxiliar para processamento do recálculo e, por isso, não faz parte do dicionário de dados

**Atenção**

A tabela TR2 é de uso **EXCLUSIVO** da rotina Recálculo do Custo Médio (MATA330) e de suas procedures.

|  |  |
| --- | --- |
| Tipo | 3-Lógico |
| Nome | MV\_A330SB2 |
| Descrição | .F. - o MATA330 utiliza a tabela SB2 para o processamento ou .T. o Recálculo utiliza a tabela TR2 para o processamento e, ao término, grava na SB2. |
| Conteúdo | .F./.T. |

**Uso de Procedures**

Para correta execução do recálculo, sempre que o conteúdo do parâmetro MV\_A330SB2 for alterado, é necessário reinstalar o pacote de procedures 19 - Custo médio através do configurador, para assegurar que as procedures instaladas acessem a tabela TR2XXSP e não a SB2XX0.

**Mais detalhes sob a utilização do parametro e conceitos aplicados em pontos de entrada:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=722655643>

**Saiba mais:**

*[MP - SIGAEST - Recálculo do Custo Médio (MATA330) - Conceito e Informações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013945671)*

*[MP - SIGAEST - Rotina MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
