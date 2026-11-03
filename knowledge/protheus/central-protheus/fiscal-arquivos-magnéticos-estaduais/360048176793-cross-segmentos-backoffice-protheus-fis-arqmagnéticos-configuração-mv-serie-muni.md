---
article_id: 360048176793
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 0b79b17f7bd060180d1157afa75114d6288bac7689b8a85a36a7f74d496ceec5
fetched_at: '2026-06-28T22:42:10.371952+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  MV_SERIE - Município de Araçoiaba
type: support-article
updated_at: '2022-08-17T20:05:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048176793-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-MV-SERIE-Munic%C3%ADpio-de-Ara%C3%A7oiaba
---

**Dúvida**Configuração MV\_SERIE - DMS Município de Araçoiaba  
**Ambiente**  
Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**A prefeitura de Araçoiaba solicita que seja enviado no xml o conteúdo 2 nas tags abaixo:  
  
<Serie></Serie>

<Especie></Especie>

Para correta gravação das TAGs acima com o conteúdo 2, é necessário efetuar as configurações conforme abaixo:   
  
MV\_SERIE = Definido pelo cliente

Exemplo de preenchimento:

O parâmetro MV\_SERIE deve ser preenchido como segue:

SSS-DD/AAA-DD/

• SSS: série do documento fiscal no Microsiga Protheus® com 3 dígitos. Caso a série a ser informada seja menor que 3 dígitos, complete com espaços em branco.  
  
• DD: Serie que deverá ser apresentada na Nota Fiscal Paulista, com 2 dígitos. O validador só aceita 2 dígitos e seu preenchimento deve seguir a seguinte regra:  
Série D - Preencher com 01

Série D Única - Preencher com 02

Série Única - Preencher com 03

• Para separar a configuração utilize o Hífen ("-"). Para separar grupos de configuração, utilize a barra ("/").

Cadastrar a especie 2 na tabela 42 do configurador através do caminho abaixo:

Ambiente - Cadastros - Tabelas.
