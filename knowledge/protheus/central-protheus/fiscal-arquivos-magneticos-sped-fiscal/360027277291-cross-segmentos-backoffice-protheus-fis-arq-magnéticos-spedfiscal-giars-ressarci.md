---
article_id: 360027277291
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 332be853ec4ddfd58436d5e81f65fd59780e28853a85e3335498fb581feff443
fetched_at: '2026-06-28T22:42:02.593984+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL/
  GIARS - Ressarcimento ICMSST/ RS - Registros 1900, 1921, 1923 e E220
type: support-article
updated_at: '2025-02-11T20:49:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027277291-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-GIARS-Ressarcimento-ICMSST-RS-Registros-1900-1921-1923-e-E220
---

**Dúvida**  
Quais parametrizações devo configurar para gerar os Registros 1900,1921,1923 e o E220?  
   
 **Ambiente**  
Protheus - Livros Fiscais a partir da versão 12.1.17

**Solução**

**Registro tipo 1900/ 1921 Ajuste/Benefício/Incentivo da Apuração do ICMS**  
Estes ajustes são os códigos de subitens lançados manualmente na **Apuração de ICMS**, que serão transportados para o meio magnético.  
  
Configuração dos parâmetro:  
  
Exemplo:

Descrição  
**MV\_GIAEFD = .T.**  
Indica se as Informações Adicionais de Apuração - Valores Declaratórios, serão Apurados através da **Apuração de ICMS**.

**MV\_APUSEP** =1/2/3  
Informar o número dos livros que indicam as Apurações Separadas para gerar os **registros 1900** e filhos no **EFD ICMS/IPI**.

**MV\_RLCSPD** = {{'3','1','LIVRO SEPARADO 1'}, {'4','2','LIVRO SEPARADO 2'}, {'5','3','LIVRO SEPARADO 3'}}  
Relação dos Livros do Parâmetro **MV\_APUSEP** com os livros do **SPED Fiscal**. Usado para gerar o **Registro 1900**

**Registro tipo 1923** - Informações Adicionais dos Ajustes da Apuração do ICMS – Identificação dos documentos fiscais

Este registro contém informações adicionais dos ajustes gerados no **Registro 1921**.  
Para que seja gerado **Registro 1923** é necessário configurar parâmetro **MV\_ESTE113**esteja configurado.

Exemplo:**MV\_ESTE113** = RS  
  
Para geração do **Registro E220** preencher os parâmetros abaixo:  
  
**MV\_STUF=**AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO  
**MV\_STUFS**=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO  
  
Caso tenha inscrição preencher o parâmetro a seguir.  
  
**MV\_SUBTRIB** = preenchido com estado + inscrição estadual (todos os estados que possuírem inscrição estadual para recolhimento do **ICMS ST**)

Exemplo  
**MV\_SUBTRIB** = Preenchido com UF + Inscrição Estadual  
Exemplo: **MV\_SUBTRIB**=SP1234567/ RS1234567  
  
Se não houver inscrição estadual, preencher o parâmetro a seguir.  
  
**MV\_STNIEUF** = Preencher com as unidades onde não é necessário ter inscrição estadual para recolhimento do ST. Preencher com UF concatenadas : RSPR/RSRJ (Rio Grande do Sul para Paraná, Rio Grande do Sul para Rio de Janeiro).

Lembrando que antes da geração dos registros deve-se realizar apuração na rotina **FISA196** seguindo as orientações para varejista e não varejista, a seguir o link com os procedimentos da apuração:

<http://tdn.totvs.com/pages/releaseview.action?pageId=463811572>
