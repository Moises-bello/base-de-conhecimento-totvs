---
article_id: 40051166644887
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ddf46ba332c612279cccedfd1dda805124613084e8ea3f8bf790d66a9df25361
fetched_at: '2026-06-28T22:42:40.940947+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Cálculo da quantidade da OP Intermediária
  e Solicitação de Compra gerada a partir de uma Ordem de Produção
type: support-article
updated_at: '2026-04-27T20:28:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40051166644887-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-da-quantidade-da-OP-Intermedi%C3%A1ria-e-Solicita%C3%A7%C3%A3o-de-Compra-gerada-a-partir-de-uma-Ordem-de-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40051166605847) Tempo aproximado para leitura: **00:02:53 min**  
  
**Dúvida**  
Ao gerar **Ordem de Produção Intermediária** e **Solicitação de Compra** a partir de uma **ordem de produção** a quantidade desses documentos é diferente do empenho da OP pai, como é feito o cálculo?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Quando o parâmetro **MV\_CONSEST - Considera Estoque na Geração da Ordem de Produção** está igual a **S**, o Sistema avalia o estoque dos produtos para gerar as **OPs Intermediárias** e **Solicitações de Compra**.  
  
Ao avaliar o estoque, o Sistema pode gerar as **OPs Intermediárias** e **Solicitações de Compra** numa quantidade maior ou menor à necessária para a OP. Ou ainda, não gerar as **OPs Intermediárias** e **SCs** caso encontre estoque disponível.  
  
Para o cálculo o Sistema vai considerar o saldo em estoque registrado no campo **B2\_QATU - Saldo Atual**, empenhos do campo **B2\_QEMP - Quantidade Empenhada** e quantidade prevista de entrada do campo **B2\_SALPEDI - Qtde prevista p/ entrar** para gerar as quantidades das **OPs intermediarias** e **Solicitações de Compra**.   
  
**Exemplo 1**:  
Quantidade empenhada do produto para a OP: 10  
B2\_QATU=10  
B2\_QEMP=10  
B2\_SALPEDI=0

Não gera OP Intermediária ou SC  
  
**Exemplo 2**:  
Quantidade empenhada do produto para a OP: 10  
B2\_QATU=0  
B2\_QEMP=10  
B2\_SALPEDI=0  
  
Será gerada uma OP Intermediária ou SC de quantidade 10  
  
**Exemplo 3**:  
Quantidade empenhada do produto para a OP: 10  
B2\_QATU=1  
B2\_QEMP=10  
B2\_SALPEDI=5  
  
Será gerada uma OP Intermediária ou SC de quantidade 4  
  
**Exemplo 4**:  
Quantidade empenhada do produto para a OP: 10  
B2\_QATU=0  
B2\_QEMP=15  
B2\_SALPEDI=0  
  
Será gerada uma OP Intermediária ou SC de quantidade 15  
  
**Importante**  
Caso o produto em questão tenha quantidade nos campos **B2\_QEMPPRE - Empenho previsto** e/ou **B2\_SALPPRE - Quantidade prevista OP**, e o parâmetro **MV\_QTDPREV - Soma quantidade dos campos de OPs previstas nos cálculos de quantidade empenhada e quantidade prevista de entrada** estiver como **S**, essas quantidades serão consideradas no cálculo.                                
  
**Saiba mais**  
Para mais informações sobre os parâmetros envolvidos na verificação do saldo em estoque, acesse: [Manufatura - Linha Protheus - SIGAPCP - Não gera solicitação de compra e/ou ordem de produção intermediária automaticamente ao abrir uma ordem de produção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024976531-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-gera-solicita%C3%A7%C3%A3o-de-compra-e-ou-ordem-de-produ%C3%A7%C3%A3o-intermedi%C3%A1ria-automaticamente-ao-abrir-uma-ordem-de-produ%C3%A7%C3%A3o)
