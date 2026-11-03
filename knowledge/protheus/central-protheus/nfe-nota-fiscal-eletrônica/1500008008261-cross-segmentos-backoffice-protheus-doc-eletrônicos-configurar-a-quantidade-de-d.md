---
article_id: 1500008008261
category: NFe - Nota Fiscal Eletrônica
content_hash: dc3acfb860f90b609a6678ef193f79a8153e27a0cfdae7d7ca76680eb3ac77ea
fetched_at: '2026-06-28T22:40:03.625536+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Configurar a quantidade
  de dias retroativos a ser considerado no AUTONFE
type: support-article
updated_at: '2024-12-26T20:47:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008008261-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Configurar-a-quantidade-de-dias-retroativos-a-ser-considerado-no-AUTONFE
---

**Dúvida**Como configurar a quantidade de dias retroativos que será considerado no AUTONFE?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Documentos Eletrônicos Protheus - A partir da versão 12.1.25  
  
**Solução**Para a funcionalidade do **AUTONFE**, foi disponibilizado dois parâmetros numéricos para realizar o controle dos dias retroativos a partir da data de processamento:

* **MV\_QTDTRAN**: este parâmetro será responsável pelo controle dos dias retroativos para o processo de **transmissão** dos documentos (autoNfeTrans).
* **MV\_QTDMON**: este parâmetro será responsável pelo controle dos dias retroativos para o processo de **monitoramento** dos documentos (autoNfeMon).

Ambos os parâmetros estão sendo limitados até 60 dias retroativos. Podendo ser configurado com conteúdo entre 1 e 60.

Como configurar?  
Passo a passo para criação do parâmetro **MV\_QTDTRAN**:  
**1.** Acessar  o módulo **SIGACFG;**

**2.** Acessar ao caminho **Base de Dados** \ **Dicionário** \ **Base de Dados** ou **Ambiente** \ **Cadastros** \ **Parâmetros;**

**3.** Selecionar **Parâmetros**, e em seguida acesse **Incluir;**

**4.** Informar os dados da criação do parâmetro;

Na aba **Informações**, para os campos preencha:  
**Filial:** Pode ser específico por filial ou em branco, para compartilhado.  
**Nome da Var.:** Nome do parâmetro, por exemplo,**MV\_QTDTRAN**.  
**Tipo:** Deve ser **Numérico**.  
**Cont. Por**: Quantidade de dias retroativos para ambiente no idioma português, por exemplo, 30.  
**Cont. Ing**: Quantidade de dias retroativos para ambiente no idioma inglês, por exemplo, 30.  
**Cont. Esp**: Quantidade de dias retroativos para ambiente no idioma espanhol, por exemplo, 30.

Na aba **Descrição**, para os campos preencha:  
**Descrição**: Descrição do parâmetro,   
**Cont. Descriç**: Continuação da descrição, caso necessário.  
**Cont. Descriç**: Continuação da descrição, caso necessário.

Caso necessário, informar a descrição em outros idiomas, possuem os mesmos campos para inglês e espanhol.

**5.** Salve em **Salvar** e pronto.

**Observação:** Para criar o parâmetro **MV\_QTDMON**, basta realizar o mesmo procedimento.
