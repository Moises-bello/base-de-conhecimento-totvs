---
article_id: 360021148112
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 3bba208e71fdd008149f04fc790d12cef2f8c4d9dcc54a528c4b02d62fe9fc70
fetched_at: '2026-06-28T22:42:05.354066+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar o registro F100 para Multa de títulos recebidos
type: support-article
updated_at: '2022-09-15T21:32:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021148112-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-o-registro-F100-para-Multa-de-t%C3%ADtulos-recebidos
---

**Dúvida**Como gerar o registro F100 para Multa de títulos recebidos?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Crie uma natureza no módulo financeiro para multa e juros, preenchendo os campos conforme abaixo:  
**Apur. Pis** (**ED\_APURPIS**)= DEBITO;  
**Apur. Cofins** (**ED\_APURCOF**)=DEBITO;  
**% Ap. PIs** (**ED\_PCAPPIS**) = 0,65;  
**% Ap. Cofins** (**ED\_PCAPCPF**) = 4,00;  
**Tipo Naturez** (**ED\_TIPO**) = cumulativa ou não cumulativa;  
**Cond Naturez** **(ED\_COND**) = Receita;  
**Tp Reg** (**ED\_TPREG**) = Cumulativo ou não cumulativo;  
**CST Cofins** (**ED\_CSTCOF**) = 02;  
**CST Pis** (**ED\_CSTPIS**) = 02;  
**Ind Cmulat** (**ED\_INDCMLT**) = cumulativo ou não cumulativo.  
  
2. Altere no **Configurador** os parâmetros:  
**MV\_RENTRIB** = .T.   
**MV\_NATRNT** = Preencher com a Natureza criada para multa e juros.  
  
3. Crie uma TES com as configurações abaixo:  
**Gera Dupl.** (**F4\_DUPLIC**) = Sim;  
**Livro ICMS, IPI ou ISS** = diferentes de **Não** -> Deve ser configurado no campo de um dos livros com opção diferente de não para geração dos valores de PIS COFINS nas tabelas **SF3** e **SFT**;  
**PIS/COFINS** (**F4\_PISCOF**) = Ambos;  
**Cred. PIS/COF** (**F4\_PISCRED**) = Debita(Saída);  
**Tp Regime** (**F4\_TPREG**) = Cumulativo, Não Cumulativo ou AMBOS (Cumul/N Cumul);  
**Sit trib PIS F4\_CSTPIS** = Saida (01 a 49);  
**Sit. trib. COF F4\_CSTCOF** = Saida (01 a 49).  
  
4. Acesse o módulo de Faturamento:  
Realize o pedido de venda utilizando **TES** configurada;  
Prepare o **documento de saída** gerando a Nota Fiscal.  
  
6. Acesse o módulo Financeiro:  
Realize a baixa do título gerado acrescentando o valor no campo da Multa.  
  
7. Acesse o Módulo Livros Fiscais, Apuração EFD Contribuições, processe a apuração preenchendo as principais perguntas.  
  
8. Gere o arquivo **EFD Contribuições** dentro da rotina de apuração.
