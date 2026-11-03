---
article_id: 22220575753623
category: Gestão de Armazenagem (WMS)
content_hash: 86e344cbeb5cbb102bc1032bbcf165e191346d109079f9f4f1abad3ed1a09137
fetched_at: '2026-06-28T22:45:48.162022+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Requisição de produção no SIGAWMS
type: support-article
updated_at: '2024-08-13T12:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22220575753623-Log%C3%ADstica-Linha-Protheus-WMS-Requisi%C3%A7%C3%A3o-de-produ%C3%A7%C3%A3o-no-SIGAWMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22220499016983) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como é realizado a Requisição de produção com **SIGAWMS - Gestão de Armazenagem**?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Versão 12  
  
**Solução**Quando a **MP- Matéria Prima** tem controle de **WMS**, para requisição da produção com **WMS**, deve seguir os passos:  
  
1. **PCPA200 - Configuração da Estrutura**;   
Cadastro da estrutura do produto acabado com componentes com controle **WMS - Warehouse Management System.**  
  
2. **MATA650 - Ordens de Produção;**Criação e empenho da **OP - Ordem de Produção**.  
  
3. **WMSA505 Separação Ordem de Produção;**Lista de ordens de produção empenhadas, onde deverá ser requisitado ao armazém a matéria-prima para execução da **OP**. Caso já tenha saldo nem endereço de produção, e seja suficiente para atendimento da **OP**, o saldo será apenas empenhado no endereço.

4. **WMSA150 - Execução de Serviço;**Execução do serviço, caso seja necessário a movimentação de Matéria prima para o armazém/endereço de produção.  
  
5. **WMSA332 - Monitor de Serviço ou Coletor;**Finalização do serviço de requisição.  
  
6. **MATA250 - Apontamento da Produção**.   
Ao apontar a produção, será consumida a matéria prima do endereço de produção e se o produto acabado for também for controlado pelo **WMS**, será gerado uma ordem de serviço de endereçamento.  
  
**Importante**  
No passo 2, a **MP** é empenhada no armazém, obrigatóriamente para o endereço de produção;  
No passo 3, a **OS** será sempre gerada baseada no armazém destino, caso o armazém de estoque seja diferente de produção, deverá ser informado no campo **Armazém Origem**;  
No passo 4, caso a **MP** tenha controle de rastro, e não for designado um lote no empenho, o **WMS** fará a escolha do melhor lote, baseado na **Regra WMS** estabelecida.  
  
**Saiba mais**Para mais informações acesse: [Separação da Ordem de Produção (WMSA505 - SIGAWMS)](https://tdn.totvs.com/x/f0-6IQ)
