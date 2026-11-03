---
article_id: 360046962373
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: fee6ab23502e85abea4043e16bbddcb97a227bb6be42ea8d22a07b445818e32e
fetched_at: '2026-06-28T22:42:11.744639+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Importação do
  arquivo de retorno da prefeitura de SP (rotina MATA915) "A importação do arquivo
  de retorno não foi realizado por não existirem informações de retorno no arquivo
  texto informado"
type: support-article
updated_at: '2023-02-09T19:59:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046962373-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Importa%C3%A7%C3%A3o-do-arquivo-de-retorno-da-prefeitura-de-SP-rotina-MATA915-A-importa%C3%A7%C3%A3o-do-arquivo-de-retorno-n%C3%A3o-foi-realizado-por-n%C3%A3o-existirem-informa%C3%A7%C3%B5es-de-retorno-no-arquivo-texto-informado
---

**Dúvida**Ao importar o Arquivo de retorno da **prefeitura de SP** pela rotina **MATA915** ocorre o alerta abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067235473/mceclip0.png)

**Ambiente**  
Microsiga Protheus– Livros Fiscais– A partir da versão 11.80  
  
**Solução**Verificar o arquivo de retorno informado na *wizard* da rotina **MATA915** se é o arquivo enviado pela prefeitura no *Layout* TXT.txt.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066175134/mceclip1.png)

No site da prefeitura, há a opção de gerar o arquivo para ser importado com os números das NF-es geradas. Nesta opção, será necessário informar qual o layout a ser gerado entre os disponíveis ***(Formato txt, Formato csv, Formato txt tabulado, Formato txt retorno).***

Para que seja possível a importação do arquivo de retorno, a opção a ser escolhida deverá ser **TXT(Somente TXT).**

Verificar se os campos abaixo no cadastro de Filial no configurador estão preenchidos corretamente:

**M0\_CIDENT** =SAO PAULO

**M0\_CODMUN** =3550308 (código IBGE)

Parâmetros:

**MV\_TAMCPO=.F.  
MV\_ESTADO=SP**

**Informações Adicionais sobre a rotina MATA915:**

 No diretório \*SYSTEM* deve conter arquivo de configuração **NFESP.INI**

**SPISS - Layout de Importação de Nota Fiscal Eletrônica de Serviços de São Paulo/SP**

<https://tdn.totvs.com/pages/releaseview.action?pageId=700501853#SPISSLayoutdeImporta%C3%A7%C3%A3odeNotaFiscalEletr%C3%B4nicadeServi%C3%A7osdeS%C3%A3oPaulo/SP-PROCEDIMENTOSPARAUTILIZA%C3%87%C3%83O>
