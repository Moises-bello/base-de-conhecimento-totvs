---
article_id: 360025671132
category: Integrações Nativas
content_hash: 3438ee6f30d75a4b3ed26c1bfb93384dbacd322a796f66057629d146f78a4718
fetched_at: '2026-06-28T22:42:35.512186+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Procedimento para gerar empenho e S.C para
  O.S
type: support-article
updated_at: '2023-12-27T17:25:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025671132-Manufatura-Linha-Protheus-MNT-Procedimento-para-gerar-empenho-e-S-C-para-O-S
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20142063875863)*** Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual é o procedimento para gerar o empenho e **S.C** para **O.S**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**Para gerar o empenho e **S.C - Solicitação de Compra** para **O.S - Ordem de Serviço**, o Sistema verifica se existe saldo disponível em estoque. Caso não tenha saldo disponível, o processo gera uma **S.C**, desde que o parâmetro **MV\_NGGERSA**- Indica se deve gerar Solicitação ao Armazém em vez de gerar Solicitação de Compra esteja igual a **N - Não** ou **P - Produto**, nesse caso apenas insumos do tipo **Terceiro** geram **S.C**.  
  
Neste caso, utilize o parâmetro **MV\_NGCORPR** **- Permite gerar Empenho e SCs para OS. Corretivas** configurando como **S - Sim**. Deve-se observar se os parâmetros de integração com os módulos envolvidos estão ligados.  
  
Para configuração do parâmetro, acesse o **Configurador - SIGACFG**. Em base de dados, acesse **Dicionário**, **Base de dados**, **Parâmetros**, e em seguida altere o parâmetro **MV\_NGCORPR** para **S**.  
  
**Importante**  
Segue abaixo os parâmetros das integrações que devem ser configurados:

* **MV\_NGMNTES - Integração Manutenção (MNT) com Estoque (EST)** igual a **S**
* **MV\_NGMNTCM - Integração Manutenção (MNT) com Compras (COM)** igual a **S**
* **MV\_NGMNTPC - Integração Manutenção (MNT) com Planej. e Contr. da Produção (PCP)** igual a **S**
