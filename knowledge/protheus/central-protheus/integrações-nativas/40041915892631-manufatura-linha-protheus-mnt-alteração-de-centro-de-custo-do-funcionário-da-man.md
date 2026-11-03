---
article_id: 40041915892631
category: Integrações Nativas
content_hash: c08d25e00fa906ac49aad4b7b68abdc857c68fa6877e9802d219946ff3543277
fetched_at: '2026-06-28T22:42:35.306747+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Alteração de centro de custo do funcionário
  da manutenção
type: support-article
updated_at: '2026-04-27T14:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40041915892631-Manufatura-Linha-Protheus-MNT-Altera%C3%A7%C3%A3o-de-centro-de-custo-do-funcion%C3%A1rio-da-manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40041915881751) Tempo aproximado para leitura: **00:00:55 min**  
  
**Dúvida**  
Como alterar o centro de custo de um **Funcionário da manutenção - MNTA020**, quando o parâmetro **MV\_NGMNTRH - Integração Manutenção (MNT) com Recursos Humanos** é **S** ou **X**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Execute a rotina **Transferências - GPEA180**. Essa rotina tem por objetivo realizar a transferência de um ou mais funcionários entre **Centros de custo** dentro do módulo de **SIGAGPE - Gestão de Pessoal**;  
2. Pressione o menu **Outras ações - Transferir**;  
3. Selecione o funcionário que será transferidos de centro de custo;  
4. No quadro **Dados Destino**, informe o novo centro de custo e o pressione o botão **Confirmar**;  
5. Consulte na rotina **MNTA020** que o campo **Centro Custo** para o funcionário foi alterado.
