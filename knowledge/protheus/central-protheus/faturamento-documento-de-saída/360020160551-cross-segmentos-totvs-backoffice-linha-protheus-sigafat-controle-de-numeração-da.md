---
article_id: 360020160551
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 75d5b6a71a4bf7a521d06e283b9291b9ea8805cfa6c392120f331db311f6b978
fetched_at: '2026-06-28T22:38:45.066370+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Controle de
  numeração da nota de saída via License Server (MV_TPNRNFS = 2)
type: support-article
updated_at: '2023-08-22T11:00:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020160551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Controle-de-numera%C3%A7%C3%A3o-da-nota-de-sa%C3%ADda-via-License-Server-MV-TPNRNFS-2
---

**Dúvida**

Controle de numeração da nota de saída via License Server (MV\_TPNRNFS = 2).  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Esta opção armazena a próxima numeração disponível, e a seguinte, através do mecanismo do **LS** - **License Server**. Até a versão 11 do Protheus era armazenado nas Tabelas físicas **SXE** e **SXF** no diretório System do ambiente, porém, a partir da versão 12, o controle deve ser somente via License Server (antigo Hardlock). Veja mais informações sobre o License em: **[Controle de Numeração de Tabelas (ALIAS) no Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=235570751).**

**Premissas para correto funcionamento do controle de numeração:**

* Possuir LS - License Server instalado e atualizado para substituição das antigas SXE/SXF
* Se houver necessidade de Séries exclusivas, adeque o ambiente de acordo com o item "**Exclusividade de Séries**" (**[Exclusividade de Séries por Filial](http://tdn.totvs.com/pages/viewpage.action?pageId=329024579#FAT0049ControledeNumera%C3%A7%C3%A3odeDocumentodeSa%C3%ADdanoProtheus-ExclusividadedeS%C3%A9ries)**).  
  (Se não houver necessidade de Séries exclusivas, o sistema irá exibir todas as séries para todas as Filiais, porém, sugerir a numeração atualizada para a Filial que está acionando a Preparação da Nota.)

**Ajuste para sugerir a sequência numérica correta:**

* Verifique o último/maior número de Nota gravada na **SF2** (nota "000009" por exemplo) a partir da qual deseja dar sequência. Atente-se à numeração de acordo com a Filial **F2\_FILIAL**
* Acesse a rotina **APCFG110** - Manutenção SXE/SXF (Caso não localize a rotina em seu Menu, verifique como inserir em **[Controle de Numeração de Tabelas (ALIAS) no Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=235570751)**)
* Localize o registro que precisa ser ajustado.  
  Note que são exibidos registros para **NFF** na coluna ALIAS para o caso de Documento de saída.  
  O campo Chave armazena Série / Filial / Tabela (**SF2**)
* Na seção inferior (antiga **SXF**) - Números em uso/ Números liberados: Exibe a última numeração sugerida
* Na seção superior (antiga **SXE**) - Próximos números: Exibe a numeração seguinte (última sugerida + 1)

**Observação**: A partir da release 12.1.25, o controle por SXE/SXF deixa de existir passando exclusivamente para o controle por license server.

**Saiba mais:**

**[Numeração automática pelo License Server](https://tdn.totvs.com/pages/releaseview.action?pageId=309411140)****[Controle de numeração via Tabelas SXE / SXF (MV\_TPNRNFS = 2)](http://tdn.totvs.com/pages/viewpage.action?pageId=329024579#FAT0049ControledeNumera%C3%A7%C3%A3odeDocumentodeSa%C3%ADdanoProtheus-Controledesequ%C3%AAnciaautom%C3%A1ticadanumera%C3%A7%C3%A3oparaDocumentodeSa%C3%ADda-Faturamento)**
