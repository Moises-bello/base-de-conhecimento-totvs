---
article_id: 360051143213
category: NFe - Nota Fiscal Eletrônica
content_hash: da2c1a83d8eda34d7e36dae801dfc8b758de3b2cd26f495cbc70a21634cba50a
fetched_at: '2026-06-28T22:40:01.906137+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.003'
type: support-article
updated_at: '2021-09-09T14:45:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051143213--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-t%C3%A9cnica-2020-003
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2020.003   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Conforme o link abaixo foi lançada a nota técnica **2020.003:**

[Nota Técnica 2020.003 - v.1.00 - Publicada em 25/06/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=BjvxuI3ZnOM=)

No qual, houve a divulgação de orientações para emissão de NF-e pelo **Transmissor de energia elétrica,** de acordo com o disposto no **Ajuste SINIEF 11/2020.**

1- Essa **Nota técnica não alterou ou acrescentou** nenhuma validação da nota fiscal eletrônica, sendo assim **não será necessário** realizar manutenções em nossos fontes.

2- Conforme 2.1 Grupo B. Identificação da Nota Fiscal Eletrônica deve ser informado a natureza da operação **“Transmissão de energia elétrica - encargo de uso/conexão”**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078213673/mceclip0.png)

Para informar Natop com a descrição da natureza da operação  há o parâmetro no configurador **MV\_SPEDNAT:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077090794/mceclip1.png)**

**MV\_SPEDNAT =****.T.** = TAG é gerada através da **tabela 13 (tabela genérica no configurador)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078214673/mceclip2.png)

**MV\_SPEDNAT =** .F. = Do campo no TES **F4\_TEXTO**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078215073/mceclip0.png)

3- Conforme 2.2 Grupo I. Produtos e Serviços da NF-e na **descrição do produto ou serviço**  Conforme o caso, informar o valor:  **“Energia Elétrica – Encargo de Uso do Sistema de Transmissão”;** ou  **“Energia Elétrica - Encargo de Conexão”**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078215913/mceclip3.png)

Para informar **Xprod** há os campos abaixo

4 - O fonte padrão do **NFESEFAZ**  leva conteúdo para a TAG **<xProd>:**  
  
Da tabela **SB1**do campo**B1\_DESC ou** de amarração da tabela SA7 **produto x cliente** ou SA5 da tabela SA7 **produto x fornecedor**.

5- Ao utilizar amarração da tabela SA7 **produto x cliente** ou SA5 da tabela SA7 **produto x fornecedor**.  
  
No **TES** o poder de terceiro precisa ser **diferente** de **não controla campo F4\_PODER3  "Poder Terc."**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078215633/mceclip1.png)

6 - Se for utilizar a rotina de amarração de produto X cliente ou produto X fornecedor os campos abaixo devem estar preenchidos:

**Produto x cliente**  
  
**SA7->**A7\_CODCLI  
**SA7->**A7\_DESCCLI ​

**Produto x fornecedor**

**SA5->**A5\_CODPRF  
  
**SA5->**A5\_DESREF

7 - Além disso deve ser habilitado o parâmetro:

**MV\_NFPTER**

**.T. =** SA5 ou SA7

**.F. =** SB1

8- Conforme 2.2 Grupo I. Produtos e Serviços da NF-e o **NCM informar o valor “27160000” = Energia Elétrica**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078215913/mceclip3.png)

Para informar o NCM  preencher o NCM no cadastro de Produto deve estar preenchido **Pos.IPI/NCM** "**B1\_POSIPI"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077383874/mceclip0.png)

9 - Conforme 2.2 Grupo I. Produtos e Serviços da NF-e o CFOP **informar “5949”, no caso de operações internas; ou  “6949”, no caso de operações interestaduais**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078215913/mceclip3.png)

Para informar o CFOP preencher no TES o campo **Cod. Fiscal "F4\_CF"**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077092734/mceclip4.png)

10 - Conforme 2.5 Grupo Tributação do ICMS = 40, 41, 50**Informar a origem o valor “0” = Nacional – exceto as indicadas nos códigos 3, 4, 5 e 8**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077093194/mceclip6.png)

Para informar a origem campo no cadastro de Produto deve estar preenchido **B1\_ORIGEM "Origem"**  
  
  
  
![mceclip1.png](https://totvssuporte.zendesk.com/hc/article_attachments/360065821393/mceclip1.png)

11 - Conforme 2.5 Grupo Tributação do ICMS = 40, 41, 50 Informar  o CST  valor “41” = Não tributada

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077093194/mceclip6.png)

Para informar a situação tributária do ICMS no **TES** preencha o campo **Sit. trib. ICMS****(F4\_SITTRIB)**

![mceclip2.png](https://totvssuporte.zendesk.com/hc/article_attachments/360041920134/mceclip2.png)

12 - Conforme 2.6 Grupo X. Informações do Transporte da NF-e deve ser informado  **o valor “9” = Sem frete**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077093874/mceclip7.png)

Para informar  **"S"** = **9=**Sem Ocorrência de Transporte  deve ser preenchido o campo no pedido de vendas **C5\_TPFRETE  "Tipo Frete"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069140574/mceclip0.png)

 13 - Conforme 2.7 Grupo Z. Informações Adicionais da NF-e deve ser informado  **“Não incidência de ICMS, nos termos da cláusula primeira do Convênio ICMS 117/2004.” Após o texto acima, informar os dados do aviso de crédito emitido pelo NOS**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077099954/mceclip9.png)

Para informar as mensagens há os campos padrões do sistema conforme os links das documentações abaixo:

[MP - NFE - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)

[MP - NFE - Gerar mensagem em informações complementares do Danfe utilizando fórmula ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

* **Saiba mais:**

Essa operação deve ser realizada apenas para nota de saída.
