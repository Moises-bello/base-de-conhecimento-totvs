---
article_id: 360015786532
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 64d84023fbc7aeab1a1568e0651f802b66b3cba69f89362c7fed6b1635bc8145
fetched_at: '2026-06-28T22:42:04.971901+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar
  o registro A100 do EFD Contribuições '
type: support-article
updated_at: '2023-07-13T12:41:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015786532-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-A100-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o registro A100 do EFD Contribuições?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12.1.17  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1.Verifique o parâmetro **MV\_CFAREC**;  
Para operações de SAÍDA, estes são os **CFOP’s** que o Protheus considera como Receita. Se o **CFOP** utilizado não constar nesta relação deverá ser informado no parâmetro **MV\_CFAREC**.   
**CFOP’s** que caracterizam Receita no **Protheus**:  
**Estadual:**  
5101,5102,5103,5104,5105,5106,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5122,5123,5124,5125,5251,5525,5253,5254,5255,5256,5257,5301,5302,5303,5304,5305,5306,5307,5351,5352,5353,5354,5305,5306,5307,5351,5352,5353,5354,5355,5356,5357,5359,5401,5402,5403,5405,5651,5652, 5653,5654,5655,5656.  
**Interestadual:**  
6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6122,6123,6124,6125,6251,6252,6253,6254,6255,6256,6257,6258,6301,6302,6303,6304,6305,6306,6307,6351,6352,6353,6354,6355,6356,6357,6359,6401,6402,6403,6404,6501,6502,6651,6652,6653,6654, 6655,6656.  
**Exterior:**  
7101,7102,7105,7106,7127,7251,7301,7358,7501,7651,7664.

2.Verifique o parâmetro **MV\_CFEREC**;  
Caso o usuário queira excluir algum **CFOP** que é considerado como receita, informar o **CFOP** neste parâmetro.

3.Verifique a espécie do documento.  
As Espécies consideradas para serviços são:  
Espécie="**NFS**" modelo " " // **NF Serviço**  
Espécie = "**NFPS**" modelo " " // **NF Prestação de Serviço**  
Espécie="**RPS**" modelo " " // **Recibo Provisório de Serviços - Nota Fiscal Eletrônica**  
Espécie = **SPED** modelo "55" // **Exclusiva para DF - DISTRITO FEDERAL - Nota fiscal eletrônica**

4. Verifique as tabelas e campos abaixo;

Tabelas SF1 – Nota de entrada  
Campo **F1\_ESPECIE** = **NFS, NFPS, RPS ou SPED "Distrito Federal"**  
Tabela SF2 – Nota de saída  
**SF2\_ESPECIE** = **NFS, NFPS, RPS ou SPED "Distrito Federal"**  
Tabela SF3  
Campo **F3\_ESPECIE** = **NFS, NFPS RPS ou SPED "Distrito Federal"**  
**F3\_TIPO = S**  
Tabela SFT  
Campo **FT\_ESPECIE** = **NFS, NFPS RPS ou SPED "Distrito Federal"**  
**FT\_TIPO = S**

5.Verifique os cadastros abaixo;

**CLIENTE**   
Rec. ISS = Sim   
ISS no preço (**A1\_INCISS**) = Sim (não agrega o valor de ISS a base de cálculo)/ Não (agrega o valor do ISS a base de cálculo)  
**FORNECEDOR**   
Rec. ISS = Não   
Amarrar natureza ao cadastro de Fornecedor  
**PRODUTOS**   
A alíquota de ISS, se o conteúdo for igual a 0, será valido o conteúdo do parâmetro **MV\_ALIQISS**.   
Informar o campo Cód. Serv. ISS (**B1\_CODISS**), caso não haja o código referente ao serviço, deve ser incluído na tabela 60 do configurador.  
A conta contábil deve ser preenchida no campo **B1\_CONTA.*****Link* Boletim conta contábil:**<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015964612-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-e-EFD-Contribui%C3%A7%C3%B5es-Preenchimento-da-Conta-Cont%C3%A1bil?source=search>  
  
  
**NATUREZA**   
Calcula ISS (**ED\_CALDISS**) = Sim  
**TES**   
Calcula ISS = S   
Livro Fiscal de ISS = Tributado/Outros/Isento  
PIS/COFINS (**F4\_PISCOF**) = Ambos   
Cred. PIS/COF (**F4\_PISCRED**) = Debita(Saída)/Credita (Entrada)  
**Aba Outros**   
Tp Regime (**F4\_TPREG)** = **Cumulativo**, **Não Cumulativo ou AMBOS** (**Cumul/N Cumul**)   
Sit. Trib PIS (**F4\_CSTPIS**) = **Entrada (50 a 66)** / **Saída (01 a 49)** lembrando que as **CST** de credito estão no intervalo 50 a 66  
Sit. Trib COFINS (**F4\_CSTCOF**) = **Entrada (50 a 66)** / **Saída (01 a 49)** lembrando que as **CST** de credito estão no intervalo **50 a 66**  
Dessa forma será gravado o campo **F3\_TIPO = S** -> Serviço.  
  
Observação: O campo **7 NAT\_BC\_CRED  do registro A170**, só deve ser preenchido em documentos que geram créditos.  
O campo **F4\_CODBCC** deve estar preenchido, assim a informação será gravada no campo **FT\_CODBCC**.  
  
6. Processe a **Apuração** do **EFD Contribuições** e gere o **Arquivo txt,** atenção as perguntas abaixo:  
**LIVRO = \* (****asterisco sempre)  
Instituição Financeira = NÃO  
Indicador Nfe/Cupom? = 2- Individ.****Informações:**- Na *wizard* do **processamento da Apuração** caso se a pergunta **INSTITUIÇÃO FINANCEIRA** estiver como SIM **será gerado APENAS o Bloco I do EFD Contribuições**, **o sistema não busca as movimentações da SFT e SF3, buscará exclusivamente as integrações com módulos Financeiro Saúde, e apurar PIS e COFINS conforme cadastros e operações destes módulos,** por isso importante a **pergunta INSTITUIÇÃO FINANCEIRA = NÃO.**- Para escriturar as **Notas de Serviço** de forma **Individualizada** gerando os registros **A100/A170**, preencha a pergunta "**Indicador Nfe/Cupom? 2- Individ.**" na *wizard* da geração do arquivo.

Atenção:  
Caso a operação **não tenha crédito**, **CST = 70 para PIS e COFINS**, por favor avalie o *link* abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404184065687-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Configura%C3%A7%C3%A3o-para-n%C3%A3o-gerar-no-arquivo-txt-opera%C3%A7%C3%B5es-de-Entrada-Aquisi%C3%A7%C3%A3o-sem-direito-a-cr%C3%A9dito?source=search>  
  
Só será considerado no **arquivo txt** caso nota fiscal tenha um item com **CST de Credito 50 a 66** e outra item **CST sem direito a credito 67 a 99**.
