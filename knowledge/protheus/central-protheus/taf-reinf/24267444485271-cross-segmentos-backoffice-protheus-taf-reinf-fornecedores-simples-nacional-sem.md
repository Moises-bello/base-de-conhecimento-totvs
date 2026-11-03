---
article_id: 24267444485271
category: TAF - REINF
content_hash: 10c69873c407d7977cd1f16e8c307871e519d7f12febbffec183294415a924e2
fetched_at: '2026-06-28T22:41:34.686939+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Fornecedores simples
  nacional sem retenção e com natureza de rendimento como configurar para não habilitar
  no painel reinf
type: support-article
updated_at: '2024-06-18T19:48:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24267444485271-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Fornecedores-simples-nacional-sem-reten%C3%A7%C3%A3o-e-com-natureza-de-rendimento-como-configurar-para-n%C3%A3o-habilitar-no-painel-reinf
---

**Dúvida**

   Como configurar o ambiente para não habilitar documentos fiscais de fornecedores do simples nacional no Painel REINF   
  
**Ambiente**  
A Partir da release 12.1.2210

**Solução**

   Realizados ajustes na apuração do evento R-4020, para considerar movimentações (nota fiscal, fatura ou pagamento), que contém a natureza de rendimento informada mas não houve retenção do IR.

   Para que sejam geradas as apurações desses movimentos sem retenções e enviados para a REINF, foi criado o parâmetro MV\_TAFSTRI, onde T., considera movimentos com natureza de rendimento mas que não calcularam impostos (sem tributos) e .F. (Default) não considera movimentos sem tributos, exceto os movimentos que utilizam naturezas de rendimentos que não possuem retenções.

![FORNECEDOR.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24267444468247)

  Exemplo: Nota fiscal de fornecedor do simples nacional sem cálculo de impostos e com natureza de rendimento que incide IR/PIS/COFINS/CSLL, somente irá ser apurado para ser enviado ao REINF quando o parâmetro estiver configurado como .T. .

  Contudo, os pagamentos com natureza de rendimento que não prevê incidência de nenhum tributo (como, por exemplo, 12001), ou movimentos que não atingiram o mínimo de retenção, ou que seja do grupo 20 da tabela 01, estes mantém o envio para o Reinf independente da configuração do parâmetro.

**Documentação adicional:**

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Quais são os parâmetros utilizados no Painel Reinf?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22572358256407-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Quais-s%C3%A3o-os-par%C3%A2metros-utilizados-no-Painel-Reinf?source=search)

[EFD-REINF - Evento R-4020 - Serviços Prestados por empresas optantes do Simples Nacional](https://tdn.totvs.com/pages/viewpage.action?pageId=789980774)
