---
article_id: 360016258051
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 64451e60e8ecd30f89dba1d072dc79bd202e3584961eea696f26a0de8678af70
fetched_at: '2026-06-28T22:42:05.072536+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como gerar a CPRB considerando as Informações do Faturamento
type: support-article
updated_at: '2025-03-20T13:15:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016258051-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-a-CPRB-considerando-as-Informa%C3%A7%C3%B5es-do-Faturamento
---

**Ocorrência** Como gerar a CPRB considerando as Informações do Faturamento.  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**   
Esse incidente ocorre, pois a parametrização do sistema está incorreta para a geração do CPRB considerando o **Faturamento** como origem para o cálculo da CPRB.  
  
**Solução**É possível gerar a CPRB tendo o cálculo da CPRB oriundo do **Faturamento Total, dos Documentos Fiscais ou do módulo de RH**. Neste artigo será apresentada a configuração para gerar o cálculo considerando os valores do **Faturamento**.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique os parâmetros abaixo:  
**MV\_SPCBPRH = .F.**  
**MV\_CFAREC** = Informe os CFOPs a serem incluídos, além dos já pré-definidos, para que sejam considerados como receitas no bloco P e no registro 0111 do SPED PIS/COFINS.  
**MV\_CFEREC** = Informar os CFOPs para não que não sejam considerados como receita no bloco P e no registro 0111 do SPED PIS/COFINS.  
  
CFOPs já pré-definidos como Receita no Protheus:  
  
**Estadual:**5101,5102,5103,5104,5105,5106,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5122,5123,5124,5125,5251,5525,5253,5254,5255,5256,5257,5301,5302,5303,5304,5305,5306,5307,5351,5352,5353,5354,5305,5306,5307,5351,5352,5353,5354,5355,5356,5357,5359,5401,5402,5403,5405,5651,5652,5653,5654,5655,5656.

**Interestadual:**6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,c6112,6113,6114,6115,6116,6117,6118,6119,6120,6122,6123,6124,6125,6251,6252,6253,6254,6255,6256,6257,6258,6301,6302, 6303,6304,6305,6306,6307,6351,6352,6353,6354,6355,6356,6357,6359,6401,6402,6403,6404,6501,6502,6651,6652,6653,6654,6655,6656.

**Exterior:**7101,7102,7105,7106,7127,7251,7301,7358,7501,7651,7664.

Caso o CFOP utilizado na nota fiscal não esteja informado acima, deve ser incluído no parâmetro **MV\_CFAREC**.

2. Verifique o cadastro do**Complemento do produto** (tabela SB5)**:**

Acesse: Faturamento> Atualizações> Cadastros> Complemento de Produto> Aba Outros.  
Verif Ind (**B5\_VERID**)= 2-Não ou Em branco. Por Default o sistema busca 2-Não.  
INSS Patron (**B5\_INSPA**T)= 1-Sim  
Cod. Ativ. (**B5\_CODATIV**) = ? - Código de atividade **tabela CG1** - com data inicial e final válidas para período de geração do arquivo.

É muito importante verificar se no campo **B5\_CODATIV,** a tabela CG1 está atualizada. Os campos **CG1\_DTINI** e **CG1\_DTFIM** devem estar preenchidos da seguinte forma:

-**CG1\_DTINI:**atualizado conforme a Tabela da Receita Federal;  
-**CG1\_DTFIM**: em branco.

3. Realize a apuração e geração da EFD Contribuições (**FISA001**) observando as perguntas da wizard:

* Parâmetros da Wizard da apuração: **Tributos= 3-PIS/COF+CPRB**Após o processamento da apuração os valores referentes ao CPRB serão apresentados na ABA CPRB.
