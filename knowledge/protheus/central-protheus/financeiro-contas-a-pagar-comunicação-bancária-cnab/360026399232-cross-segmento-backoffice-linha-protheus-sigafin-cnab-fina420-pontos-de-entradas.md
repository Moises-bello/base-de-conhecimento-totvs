---
article_id: 360026399232
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 774bde97487620b53d2a3ab1deddfd87cb1f099aca56363bbc90fb355242c0b6
fetched_at: '2026-06-28T22:37:55.180577+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CNAB - FINA420 - Pontos
  de Entradas da rotina Arquivo de Pagamentos
type: support-article
updated_at: '2024-08-07T18:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026399232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-FINA420-Pontos-de-Entradas-da-rotina-Arquivo-de-Pagamentos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:10:00 min**

**Dúvida**Pontos de entrada da rotina **Arquivo de Pagamentos** (**FINA420**)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**Alguns Pontos de entradas da rotina Arquivo de Pagamentos.

**F420CIT -**O ponto de entrada **F420CIT s**erá utilizado no tratamento do arquivo gerado pelo Citibank e será executado após a geração do arquivo.  
[F420CIT - Trata arquivos Citibank](http://tdn.totvs.com/display/public/mp/F420CIT+-+Trata+arquivos+Citibank+--+11789) **F420FIL -** Ponto de entrada que permite substituir o filtro padrão na rotina de **Geração de CNAB a Pagar (FINA420)**  
[F420FIL - Substitui filtro padrão na geração de CNAB a pagar](https://tdn.totvs.com/pages/releaseview.action?pageId=648837635)  
  
**F420PORT -O P.E. F420PORT** tem como objetivo definir **Banco, Agencia e Conta** do arquivo de pagamento de acordo com os dados do borderô.[P.E. F420PORT - Definir Banco, Agencia e Conta do arquivo de pagamento de acordo com os dados do borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=638734008)

**F420FILIAL - Relacionar Filial x Borderô**<http://tdn.totvs.com/pages/releaseview.action?pageId=108658716>**FIN420\_1 - Looping do processamento**<http://tdn.totvs.com/display/public/mp/FIN420_1+-+Looping+do+processamento+--+12056>**F420SOMA -** O ponto de entrada **F420SOMA** tem como finalidade retornar o saldo para o titulo na **geração do arquivo CNAB.**[F420SOMA - Retorna saldo para título](http://tdn.totvs.com/pages/releaseview.action?pageId=6071052)  
  
**F420SUMA -** O ponto de entrada **F420SUMA** altera o valor de acréscimo do título.  
[F420SUMA - Altera valor de acréscimo do título](http://tdn.totvs.com/pages/releaseview.action?pageId=6071380)

**F420SUMD -** O ponto de entrada **F420SUMD** altera o valor de decréscimo do título.  
[F420SUMD - Altera valor de decréscimo do título](http://tdn.totvs.com/pages/releaseview.action?pageId=6071381)

**F420CRP -** Ponto de entrada utilizado para criptografia do arquivo de envio.  
[F420CRP - Permite a criptografia do arquivo de envio](http://tdn.totvs.com/display/public/mp/F420CRP+-+Permite+a+criptografia+do+arquivo+de+envio+--+90784)

**FA420CRI -**O ponto de entrada **FA420CRI** tem como finalidade permitir a criação do arquivo de envio CNAB a pagar e será executado antes de criar o arquivo de envio.  
[FA420CRI - Criação de envio CNAB](http://tdn.totvs.com/pages/releaseview.action?pageId=6071223)

**FA420NAR -**O ponto de entrada permite alterar o nome do arquivo de saída (variável**cArqSaida**).  
O ponto de entrada é executado antes da criação do arquivo de saída.  
[FA420NAR - Altera o nome variável cArqSaida](https://tdn.totvs.com/pages/releaseview.action?pageId=652849131)  
  
  
**F420CHK -** O ponto de entrada **F420CHK** trata da utilização ou não do borderô enviado anteriormente na geração do arquivo bancário*.*[DT\_F420CHK\_Tratamento\_de\_Bordero](http://tdn.totvs.com/display/public/PROT/DT_F420CHK_Tratamento_de_Bordero)  
  
**F420IDBP - Identificar processamento borderô**Ponto de entrada para identificação do momento em que o **borderô** foi processado.  
  
**F420ICNB - Tratamento variável**Ponto de entrada para tratamento da variável **cIdCnab**
