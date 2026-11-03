---
article_id: 34524494782359
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 169021479756c164a4e9b3dfd9a41a0bcf4bcfc2c37f488b51af250fc696014e
fetched_at: '2026-06-28T22:37:55.138692+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - Contas a Pagar
  - FINA435 - Arquivo de entrada não localizado
type: support-article
updated_at: '2025-08-29T11:28:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34524494782359-Cross-Segmentos-TOTVS-Linha-Backoffice-Protheus-Financeiro-Contas-a-Pagar-FINA435-Arquivo-de-entrada-n%C3%A3o-localizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34524494708503) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a baixa via retorno CNAB via FINA435 - Schedule, os títulos não são baixados e no console.log apresenta a mensagem de "Arquivo de entrada não localizado", apesar do arquivo está sendo apontado corretamente na pasta e no relatório de retorno CNAB - FINR650.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34538526891031)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**  
Esse incidente ocorre, pois o arquivo foi baixado em formato UNIX e está sendo processado em Sistema Operacional Windows - Client e Servidor   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34524486043031)  
  
**Solução**  
Necessário avaliar junto à equipe financeira ou serviço de VAN que faz o envio dos arquivos se o arquivo deve ser baixado em formato Windows - UTF-8.

Posteriormente, o arquivo será encontrado e baixado na pasta.  
  
**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB)
