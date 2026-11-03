---
article_id: 360016352292
category: Materiais - Compras (SIGACOM)
content_hash: be9186f6f95ddcdad07995077d68ecc2906a5fd23e78eda44cf1cfe6d2aff6f4
fetched_at: '2026-06-28T22:41:25.362380+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - TOTVS Colaboração -
  Ao processar um XML é gravado código de erro COM042 na tabela CKOCOL
type: support-article
updated_at: '2022-05-18T21:23:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016352292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-TOTVS-Colabora%C3%A7%C3%A3o-Ao-processar-um-XML-%C3%A9-gravado-c%C3%B3digo-de-erro-COM042-na-tabela-CKOCOL
---

**Dúvida**

No módulo Compras, ao tentar realizar o processo de importação de um XML pelo TOTVS Colaboração é gravada na tabela de Controle de Arq. TOTVS Colab. (CKOCOL) a ocorrência '**COM042 - Existe mais de uma Empresa/Filial para este XML'.**  
  
**Ambiente**Microsiga Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

Esse incidente normalmente ocorre, pois existe no arquivo **sigamat.emp** mais de uma empresa/filial com o mesmo número de CNPJ e Inscrição Estadual.

Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse a rotina Monitor(COMXCOL) através do caminho Miscelanea - Totvs Colaboração;  
2. Selecione a opção Reprocessar;  
3. Marque o documento com erro;  
4. Marque para qual filial deseja importar o documento e confirme.  
  
Observação: Caso o cliente não queria utilizar o botão reprocessar, poderá utilizar o ponto de entrada ***COLFILDUP***.

***Saiba Mais :***

[COLFILDUP - Ponto que permite informar um empresa e filial quando for encontrada duplicidade na importação](http://tdn.totvs.com/pages/viewpage.action?pageId=369628567)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
