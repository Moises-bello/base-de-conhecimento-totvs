---
article_id: 360028663652
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 591c8b32f21975f67daa1872cde58a41ab49bf736f8e6ce3150b29d0dda33fe9
fetched_at: '2026-06-28T22:42:11.860665+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sintegra - Geração
  do registro 54 para a CFOP 1556
type: support-article
updated_at: '2022-08-18T14:27:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028663652-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sintegra-Gera%C3%A7%C3%A3o-do-registro-54-para-a-CFOP-1556
---

**Dúvida**Como gerar o registro 54 para a CFOP 1556 no Sintegra  
  
**Ambiente**Microsiga Protheus - Livros Fiscais – A partir da versão 11.80]  
  
**Solução**

Primeiramente é importante ressaltar tal ponto sobre a CFOP 1556, conforme abaixo:

Em atenção ao item 14.1.1.1 do Manual de Orientação da Portaria CAT Nº 32/96, que dispõe sobre a geração dos registros 54 (Mercadoria e Serviço) do Sintegra, é gerado um registro para cada mercadoria/produto ou serviço constante no documento fiscal, exceto para aqueles que se refiram aos seguintes CFOPs:

* CFOPs de 3 dígitos: 1.73, 2.73, 1.74, 2.74, 1.91, 2.91, 3.91, 1.92, 2.92, 1.97, 2.97, 3.97, 1.98, 2.98, 5.91, 6.91, 6.92, 5.95,6.96
* CFOPs de 4 dígitos: 1.406, 2.406, 1407, 2407, 1551, 1556, 2551, 2556, 3551, 3556, 1552, 1557, 2552, 2557, 5551, 6551, 7551, 5552, 5557, 6552, 6557, 5553, 5556, 6553, 6556, 7553, 7556

O Sistema trata esse procedimento automaticamente, mas, caso o contribuinte necessite alterar os CFOPs citados, deve editar o parâmetro **MV\_SINTEG**, pelo módulo **Configurador (SIGACFG),** atribuindo ao seu conteúdo todos os CFOPs que devem ser desconsiderados na geração do registro.O registro 54 referente à PIS/COFINS (número sequencial do item 993) deve ser gerado apenas quando houver destaque do valor no corpo do documento fiscal. Assim, somente é gerado quando a pergunta**Destaca PIS/COFINS** estiver preenchida com **Sim.**  
Esse registro não é gerado quando o documento fiscal for Modelo 4 (Produtor Rural). Consequentemente, também não é gerado o Registro Tipo 75.  
Caso seja uma Nota Fiscal conjugada que contenha vários CFOPs diferentes na mesma Nota Fiscal, sendo pelo menos um deles de serviço, também é pré-requisito para a geração do Registro Tipo 54.  
  
  
Entretanto, para que consiga gerar a CFOP 1554 no registro 54, deverá preencher o parâmetro MV\_SINTEG com todas as CFOPs que não se deve gerar o registro 54, **exceto** a CFOP 1556.  
  
Por exemplo: 1406/2406/1407/2407  
  
Só não será gerado o registro 54 para essas CFOPs, para as demais serão geradas.

Print com exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029811372/mceclip0.png)

173/273/174/274/191/291/391/192/292/197/297/397/198/298/591/691/592/692/595/695/1406/2406/1407/2407/1551/2551/2556/3551/3556/1552/1557/2552/2557/5551/6551/7551/
