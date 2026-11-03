---
article_id: 360035158573
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 011d737b6fd90378f769147c8609dc277cedd4d83f04eeeb7a1f64eddc626d21
fetched_at: '2026-06-28T22:37:56.433277+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Segmento J-52 – Identificação
  do Cedente/Beneficiário
type: support-article
updated_at: '2026-05-13T18:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035158573-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Segmento-J-52-Identifica%C3%A7%C3%A3o-do-Cedente-Benefici%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40448139790487)**Tempo aproximado para leitura: **00:03 min**

**Dúvida**  
Como tratar o envio do **CNAB** com as informações descritas pelo Segmento J-52, detalhando os campos do Cedente/Beneficiário?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da versão 12.1.17  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes procedimentos:

1. Atualize o pacote conforme a release utilizada em seu ambiente, disponível no portal da TOTVS.  
   Para realizar o download, siga o caminho abaixo:

[Acumulado financeiro - Download](https://Cross%20Segmento%20Protheus%20-%20Backoffice%20Linha%20Protheus%20-%20SIGAFIN%20-%20Atualiza%C3%A7%C3%A3o%20do%20Ambiente%20Modulo%2006%20Financeiro%20Acumulado)

**Importante**

Em cada pacote de release também disponibilizamos o Dicionário de Dados correspondente, sendo necessária a sua atualização juntamente com o pacote.

2 - No Configurador:

Configure o modelo layout e ajuste o arquivo CNAB de pagamento no segmento J-52, utilizando a função `CNABCED()`, conforme demonstrado na imagem abaixo:  
![TELA_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045026974)

Altere o conteúdo do parâmetro **MV\_PAGJ52** para 0 ( Zero):  
![TELA_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045027574)

4 - No **Módulo Financeiro**:

Na inclusão do título no **Contas a Pagar**, informe o Cedente/Beneficiário em **Outras Ações -> Complemente de título:**  
  
![TELA_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045039294)

Na aba CNAB, informe os dados do Cedente:  
  
![TELA_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045899513)

O Sacador Avalista **(Fornecedor do Título –** `E2_FORNECE`**)** assumirá automaticamente o papel de Cedente quando essa informação não for preenchida.

O procedimento descrito acima é aplicável aos layouts **CNAB Modelo 2.**

Abaixo segue o link com os detalhes da função `CNABCED`, mencionada na documentação:

[CNABCED - Retorna o cedente/beneficiário do boleto bancário.](https://tdn.totvs.com/pages/releaseview.action?pageId=513430989)

Segue link com os detalhes das funções e variáveis para o **CNAB** **Modelo 2.**  
[19 - CNAB / SISPAG - Funções e Variáveis](https://tdn.totvs.com/pages/releaseview.action?pageId=353273209)
