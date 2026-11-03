---
article_id: 360048560713
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 459dc8520aa7bd54dcc8db8ac11b19fb4eb6bbc83b576c6341781839bfbfd6c3
fetched_at: '2026-06-28T22:42:00.934384+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - EFD Contribuições
  - Preenchimento do COD_GEN - Gênero do Item de Mercadoria/Serviço
type: support-article
updated_at: '2024-06-14T19:47:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048560713-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Preenchimento-do-COD-GEN-G%C3%AAnero-do-Item-de-Mercadoria-Servi%C3%A7o
---

**Dúvida**Preenchimento do COD\_GEN - Gênero do Item de Mercadoria/Serviço  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
COD\_GEN - Campo 10 - Preenchimento: obrigatório para todos os contribuintes na aquisição de produtos primários.   
  
A Tabela "Gênero do Item de Mercadoria/Serviço", referenciada no Item 4.2.1 do Manual de Orientação do Leiaute da EFD Contribuições (ADE Cofis nº 34/2010), corresponde à tabela de "Capítulos da NCM", acrescida do código "00 - Serviço".  
  
Para o preenchimento deste campo fonte realizar a seguinte verificação:  
  
  
I. Posição 9 do Array do Ponto de entrada SPEDPROD;  
  
II.  Configuração do parâmetro MV\_PRDPRI;

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Nome da Variável** | MV\_PRDPRI |
| **Tipo** | Carácter |
| **Conteúdo** | <definido pelo cliente> |
| **Descrição** | Indica campo da tabela SB5 que contém a classificação de produto primário do produto |

**Importante**  
Este parâmetro indica o campo da tabela Complemento de Produto (SB5), no qual o usuário indica se determinado produto se refere a produto primário. Essa informação é importante na geração do registro 0200, pois o guia prático do SPED Fiscal determina que o preenchimento do campo 10 – COD\_GEN é obrigatório apenas para produtos primários.  
  
Lembrando que o campo na SB5 em questão deverá ser criado como carácter, e deverá ter as opções N=Não;S=Sim. Se este campo criado manualmente na SB5 estiver com opção igual a S=Sim, então a informação no campo 10 será gerada, caso estiver com opção igual a N=Não, então a informação no campo 10 não será gerada.  
  
III. Conteúdo do campo FT\_POSIPI da Tabela SFT, onde conteúdo pode ser oriundo do Cadastro de Produto(SB1)  Cadastro de NCM;  
  
IV. Caso o campo do Cadastro de produto(SB1)>> B1\_CODISS estiver preenchido  /Para serviço, utilizo sempre "00"  
  
  aAdd (aReg0200[nPos],"00")
