---
article_id: 11170364072087
category: Originação de Grãos (OG)
content_hash: 23b2ecdd3af2998361358b517f55ff19214489deffbcd6fbddedab2ced3734dd
fetched_at: '2026-06-28T22:45:44.884322+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Serviço de armazenagem - Encerrar serviço com
  status "Negociação Pendente"
type: support-article
updated_at: '2025-06-21T15:38:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11170364072087-Agro-Linha-Protheus-AGR-Servi%C3%A7o-de-armazenagem-Encerrar-servi%C3%A7o-com-status-Negocia%C3%A7%C3%A3o-Pendente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30603690185623) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Como encerrar um serviço de armazenagem quando seu status é apresentado como N**egociação Pendente**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Este tipo de serviço é gerado quando a **tabela de serviço** esta configurada para o **tipo de cobrança** igual a **retenção** e o t**ipo de retenção** igual a **cobrança**.  
Este tipo de serviço **calcula a quantidade a ser retida a título de cobrança**, para que tenha uma referência do volume a ser cobrado. No acerto do serviço existe ainda a opção de **Bonificação** para os casos de negociar um volume diferente ou mesmo nenhum.  
A negociação referente a esta retenção pode ser realizada a parte e assim que a negociação estiver ok, faz a bonificação, liberando a quantidade retida para devolução.

Um exemplo de como pode ser negociado:  
- Efetuar uma negociação de compra para o volume, gerando um contrato de compras.  
- Bonificar a quantidade retida a titulo de cobrança  
- Efetuar retorno simbólico da remessa para armazenagem  
- Gerar ou receber uma nota de compra do produtor via romaneio  
- Gerar pagamento ao produtor  
- Gerar uma nota de prestação de serviços de armazenagem no mesmo valor líquido da compra contra o produtor no faturamento.  
- Efetuar o encontro de contas no financeiro, pois não haverá desembolso ou recebimento financeiro.
