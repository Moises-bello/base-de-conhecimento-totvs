---
article_id: 9987315003543
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 433be7edac7e400552e0060c979609e88f86c7e443e83d9e43163307087cd329
fetched_at: '2026-06-28T22:37:55.173820+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CNAB - FINA260 - É possível
  conciliar com CNPJ diferente
type: support-article
updated_at: '2022-11-03T21:05:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9987315003543-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-FINA260-%C3%89-poss%C3%ADvel-conciliar-com-CNPJ-diferente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**É possível realizar a conciliação com CNPJ diferente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**A rotina **Conciliação DDA (FINA260)** vai fazer a verificação dos dados da tabela '**FIG**' com os dados da tabela '**SE2**' com a partir da chave - **Fornecedor+Loja+Filial+Vencimento+Valor** e exibirá o resultado em tela com a seguinte legenda:  
  
**DDA**  
[Conciliação DDA (FINA260 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312165346#ProcessamentosPr%C3%A9vios-002)   
  
Este procedimento é padrão e não há parâmetros para mudança no comportamento, como o vencimento esta diferente entre a **FIG** e **SE2** ele não irá conciliar.   
Na rotina existe o ponto de entrada **F260Comp -** Dados completares que poderá auxiliar na questão ou algum outro Ponto de entrada abaixo poderá ajudar a fazer o filtro por titulo.

**Pontos de entrada:**  
**FA260GRSE2** - Grava informações adicionais no título conciliado DDA  
**F260BUT** - Inclui botões no menu Padrão  
**FA260GRFIG** - Permite gravação na conciliação DDA  
**F260Comp** - Dados completares  
**F430GRAFIL** - Gravação da filial de origem na tabela FIG - Conciliação DDA
