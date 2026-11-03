---
article_id: 360021429931
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 4b91c5899bf7d08989078ed3071edf445798eeb11c56c4add52e452885aea1fd
fetched_at: '2026-06-28T22:42:05.375427+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar o registro F500 e F525 para Multa de títulos recebidos
type: support-article
updated_at: '2024-01-11T12:06:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021429931-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-o-registro-F500-e-F525-para-Multa-de-t%C3%ADtulos-recebidos
---

**Dúvida**Como gerar o registro F100 para Multa de títulos recebidos?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

Esse processo tem o funcionamento também para registros inclusos direto no módulo financeiro.

1. Crie uma natureza no módulo financeiro para multa e juros, preenchendo os campos conforme abaixo:

**Tipo Naturez** (**ED\_TIPO**) = 2 - Analítico;

**Cond Naturez** **(ED\_COND**) = R - Receita;

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20491858838295)**](https://centraldeatendimento.totvs.com/hc/article_attachments/20491858838295)

**Tp Reg (ED\_TPREG) = Cumulativo;**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20491858840215)](https://centraldeatendimento.totvs.com/hc/article_attachments/20491858840215)

**Apur. Pis** (**ED\_APURPIS**)= DEBITO;  
**Apur. Cofins** (**ED\_APURCOF**)=DEBITO;  
**% Ap. PIs** (**ED\_PCAPPIS**) = 0,65;  
**% Ap. Cofins** (**ED\_PCAPCOF**) = 4,00;  
**CST Pis** (**ED\_CSTPIS**) = 02;  
**CST Cofins** (**ED\_CSTCOF**) = 02;  
**Ind Cmulat** (**ED\_INDCMLT**) = cumulativo.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20492153853335)](blob:https://totvssuporte.zendesk.com/ee3584f6-0dc0-48cb-bc2d-bbd409f21e72)  
  
[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20491875372951)](https://centraldeatendimento.totvs.com/hc/article_attachments/20491875372951)  
  
  
2. Altere no **Configurador** os parâmetros:  
**MV\_RENTRIB** = .T.   
**MV\_NATRNT** = Preencher com a Natureza criada para multa e juros. (No meu exemplo deixei F500)

Exemplo de preenchimento do parâmetro **MV\_NATRNT**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20491858850711)](https://centraldeatendimento.totvs.com/hc/article_attachments/20491858850711)

Foi criado um título e baixado

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20491875383191)](https://centraldeatendimento.totvs.com/hc/article_attachments/20491875383191)

Na rotina FINA100 veja qual o código da natureza gravado no Juros

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20491858855447)](https://centraldeatendimento.totvs.com/hc/article_attachments/20491858855447)

FISA001 -  Processando

Veja que foi gerado o registro

Valor do título + Juros

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20491875388951)](https://centraldeatendimento.totvs.com/hc/article_attachments/20491875388951)

3. Crie uma TES com as configurações abaixo:  
**Gera Dupl.** (**F4\_DUPLIC**) = Sim;  
**Livro ICMS, IPI ou ISS** = diferentes de **Não** -> Deve ser configurado no campo de um dos livros com opção diferente de não para geração dos valores de PIS COFINS nas tabelas **SF3** e **SFT**;  
**PIS/COFINS** (**F4\_PISCOF**) = Ambos;  
**Cred. PIS/COF** (**F4\_PISCRED**) = Debita(Saída);  
**Tp Regime** (**F4\_TPREG**) = Cumulativo;  
**Sit trib PIS F4\_CSTPIS** = Saida (01 a 49);  
**Sit. trib. COF F4\_CSTCOF** = Saida (01 a 49).  
  
4. Acesse o módulo de Faturamento:  
Realize o pedido de venda utilizando **TES** configurada;  
Prepare o **documento de saída** gerando a Nota Fiscal.  
  
6. Acesse o módulo Financeiro:  
Realize a baixa do título gerado acrescentando o valor no campo da Multa.

7. Acesse o Módulo Livros Fiscais, Apuração EFD Contribuições, Processe a apuração preenchendo as principais perguntas conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20344406083607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20344360755735)  
Confirme a apuração.

8. Gere o arquivo **EFD Contribuições** dentro da rotina de apuração, preencher os principais campos conforme a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20344360763799)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20344406124311)

**Saiba mais:**

Somente alguns registros são gerado no bloco, caso o seu registro venha de integração será necessário utilizar o ponto de entrada abaixo e incluir a origem do módulo que o seu registro está vindo para que esse será gerado no bloco.

[- SPDF1003 - Selecionar origens de titulos para serem considerados nos blocos F100 e F500 do Sped Pis Cofins.](https://tdn.totvs.com/pages/releaseview.action?pageId=6071681)

[- Origem dos títulos considerados nos blocos F100 e F500 do Sped Contribuições](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=808455799)

[- Descontos, multas e juros no SPED PIS/COFINS](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=651685109)
