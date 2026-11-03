---
article_id: 360020733952
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 0dda318fe0f2ae012d4c327e5f8d8156152e81234f073d1453b7e48abf615ad8
fetched_at: '2026-06-28T22:42:05.381552+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar o registro F550 e 1900
type: support-article
updated_at: '2022-09-15T21:37:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020733952-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-o-registro-F550-e-1900
---

**Dúvida**Como gerar o registro F550 e 1900 ?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Altere no **Configurador** os parâmetros:  
**MV\_M996TPR** =1, assim o sistema buscará as informações da **TES;  
MV\_TXPIS =** 0.65 (separado por ponto); **MV\_TXCOFIN =** 3.00 (separado por ponto);  
**MV\_1DUPNAT =** A1\_NATUREZ ou C5\_NATUREZ.  
  
2. Crie uma TES com as configurações abaixo:  
**Gera Dupl.** (**F4\_DUPLIC**) = Sim;  
**Livro ICMS, IPI ou ISS** = diferentes de **Não** -> Deve ser configurado no campo de um dos livros com opção diferente de não para geração dos valores de PIS COFINS nas tabelas **SF3** e **SFT**;  
**PIS/COFINS** (**F4\_PISCOF**) = Ambos;  
**Cred. PIS/COF** (**F4\_PISCRED**) = Debita(Saída);  
**Tp Regime** (**F4\_TPREG**) = Cumulativo;  
**Sit trib PIS F4\_CSTPIS** = Saida (01 a 49);  
**Sit. trib. COF F4\_CSTCOF** = Saida (01 a 49).  
  
3. Crie uma natureza no módulo financeiro, preenchendo os campos conforme abaixo:  
**Apur. Pis** (**ED\_APURPIS**)= DEBITO;  
**Apur. Cofins** (**ED\_APURCOF**)=DEBITO;  
**% Ap. PIs** (**ED\_PCAPPIS**) = 0,65;  
**% Ap. Cofins** (**ED\_PCAPCPF**) = 3,00;  
**Tipo Naturez** (**ED\_TIPO**) = cumulativa;  
**Cond Naturez** **(ED\_COND**) = Receita;  
**Tp Reg** (**ED\_TPREG**) = Cumulativo;  
**CST Cofins** (**ED\_CSTCOF**) = 01 a 49;  
**CST Pis** (**ED\_CSTPIS**) = 01 a 49;  
**Ind Cmulat** (**ED\_INDCMLT**) = cumulativo;  
  
4. Realize o vinculo da natureza criada:  
Caso escolha o parâmetro **MV\_1DUPNAT** como **A1\_NATUREZ**, vincule utilizando o campo **Natureza** no cadastro de Cliente (**TABELA SA1**);  
Caso escolha o parâmetro **MV\_1DUPNAT** como **C5\_NATUREZ**, vincule utilizando o campo **Natureza** no momento em que realizar o pedido de venda (**TABELA SC5**).  
  
5. Acesse o módulo de Faturamento:  
Realize o pedido de venda utilizando **TES** configurada;  
Processe o **documento de saída** gerando a Nota Fiscal.  
  
6. Acesse o Módulo Livros Fiscais, Apuração EFD Contribuições, Processe a apuração preenchendo as principais perguntas conforme abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017543132/mceclip0.png)

7. Gere o arquivo **EFD Contribuições** dentro da rotina de apuração, preencher os principais campos conforme a seguir:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013708231/mceclip4.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017543852/mceclip18.png)
