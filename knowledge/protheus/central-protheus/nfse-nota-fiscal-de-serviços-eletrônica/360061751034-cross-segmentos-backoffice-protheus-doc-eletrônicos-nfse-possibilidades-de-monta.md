---
article_id: 360061751034
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 16b8168eab8a58c688b2c21977205cec8e0f0a6e1448d0c42f369f633e4a1d83
fetched_at: '2026-06-28T22:39:57.633688+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Possibilidades
  de montagem de Código de Serviço, Código de Tributação e CNAE (NFSEXMLENV e NFSEXMLNAC)
type: support-article
updated_at: '2025-10-28T12:16:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061751034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Possibilidades-de-montagem-de-C%C3%B3digo-de-Servi%C3%A7o-C%C3%B3digo-de-Tributa%C3%A7%C3%A3o-e-CNAE-NFSEXMLENV-e-NFSEXMLNAC
---

**Dúvida**Quais são as possibilidades de campos para montagem das tags de Código de Serviço, Código de Tributação Municipal e Código de Atividade (CNAE) **do remessa gerado pelos rdmakes NFSEXMLENV e NFSEXMLNAC?**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Atualmente as possibilidade são essas abaixo:  
  
Código de Serviço:  
**B1\_CODISS** (Cadastro de Produto)   
*Caso os parâmetros estejam: MV\_ARQPROD = SB1, MV\_ARQPROP = .T. e *MV\_ISSXMUN = .F.**  
  
**BZ\_CODISS** (Indicador de Produtos)  
*Caso os parâmetros estejam: MV\_ARQPROD = SBZ , MV\_ARQPROP = .T. e e *MV\_ISSXMUN = .F.**  
*Para utilizar o Indicador de produtos para montagem do XML, favor seguir a documentação: [MP - NFSE - Indicador de Produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026420011-MP-NFSE-Indicador-de-Produto)* **CE1\_CPRISS** (Rotina FISA052)*Caso o parâmetro MV\_ISSXMUN esteja = .T. e o campo CE1\_CPRISS não esteja vazio.*  
*Porém vale lembrar que há uma particularidade para o rdmake filtrar corretamente por esse campo, favor verificar a documentação: [MP - NFSE - Código de Serviço através da CE1 (FISA052).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052466194-MP-NFSE-C%C3%B3digo-de-Servi%C3%A7o-atrav%C3%A9s-da-CE1-FISA052-)*

Código de Tributação Municipal   
**FT\_TRIBMUN**  
*Conteúdo já pronto e gravado através de rotinas Fiscais como MATA018 e FISA052.*Caso parâmetro MV\_ENVSF3 esteja criado e com conteúdo = .T.  
  
**B1\_TRIBMUN** (Cadastro de Produto)   
*Caso os parâmetros estejam: MV\_ARQPROD = SB1, MV\_ARQPROP = .T. e MV\_ENVSF3 = .F.*  
  
**BZ\_TRIBMUN** (Indicador de Produtos)  
*Caso os parâmetros estejam: MV\_ARQPROD = SBZ, MV\_ARQPROP = .T. e MV\_ENVSF3 = .F.*  
*Para utilizar o Indicador de produtos para montagem do XML, favor seguir a documentação: [MP - NFSE - Indicador de Produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026420011-MP-NFSE-Indicador-de-Produto)*  
  
  
Código de Atividade (CNAE)  
**FT\_CNAE***Conteúdo já pronto e gravado através de rotinas Fiscais como MATA018 e FISA052.*Caso parâmetro MV\_ENVSF3 esteja criado e com conteúdo = .T.  
  
**B1\_CNAE** (Cadastro de Produto)   
*Caso os parâmetros estejam: MV\_ARQPROD = SB1, MV\_ARQPROP = .T. e MV\_ENVSF3 = .F.*  
  
**BZ\_CNAE** (Indicador de Produtos)  
*Caso os parâmetros estejam: MV\_ARQPROD = SBZ, MV\_ARQPROP = .T. e MV\_ENVSF3 = .F.*  
*Para utilizar o Indicador de produtos para montagem do XML, favor seguir a documentação: [MP - NFSE - Indicador de Produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026420011-MP-NFSE-Indicador-de-Produto)*  
  
 **OBSERVAÇÕES IMPORTANTES!**I. Vale lembrar que todas essas opções (pela CE1 e SFT) estão disponíveis no rdmake NFSEXMLENV a partir de **19/03/2020** ([Download](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061699513-MP-NFSE-Atualiza%C3%A7%C3%A3o-rdmake-NFSEXMLENV)).  
II. Qualquer dúvida quanto ao uso das rotinas fiscais: FISA052 e MATA018 **deverá ser verificado com o suporte fiscal.**
