---
article_id: 40803721522839
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 95e2bd4ccf2e245c667b5500da18235a68ce37bf62dfe45eb35812ab11748bb5
fetched_at: '2026-06-28T22:42:05.179165+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Erro da tabela CF5 ao finalizar a geração dos Tributos Genéricos da LC 224/2025
  (NT 012/2026) no Facilitador
type: support-article
updated_at: '2026-06-02T18:38:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40803721522839-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Erro-da-tabela-CF5-ao-finalizar-a-gera%C3%A7%C3%A3o-dos-Tributos-Gen%C3%A9ricos-da-LC-224-2025-NT-012-2026-no-Facilitador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40803721456535) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Erro da tabela **CF5** ao finalizar a geração dos Tributos Genéricos da **LC 224/2025 (NT 012/2026)** no Facilitador  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803715980567)  
  
**Causa**  
O tamanho do campo **CF5\_NUMDOC** não foi configurado com o **tamanho 44**  
  
**Solução**  
Para correção do incidente siga os seguintes passos:  
  
**1.** Acesse o **Configurador**(**SIGACFG)**em modo Exclusivo. Selecione **Base de Dados > Dicionário > Bases de Dados**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803721463831)**  
  
**1.1** Abra o diretório, selecione **Dicionário de Dados** e clique na **Lupa** para pesquisar a tabela **CF5.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803715982743)  
  
**1.2** Ao clicar em **Buscar**, a tabela aparecerá na direita. Clique no símbolo de **Editar**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803721468311)  
  
**1.3** Abra o diretório e clique em **Campos.** Localize o campo **CF5\_NUMDOC** eclique no símbolo de **Editar**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803721471767)**  
  
**1.4** Ajuste o tamanho do campo para **44** e clique em **Salvar.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803721474583)  
  
**1.5** Clique para **Sair**, depois em **Atualizar Base de Dados** e clique em **Avançar** no *Wizard* até que o ajuste seja finalizado.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803721475095)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803715996311)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803715997207)  
  
**2.** Abra novamente o Protheus **(SIGAMDI),** acesse o **Facilitador** e **reprocesse** a geração dos Tributos Genéricos.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40803721479831)

**Saiba mais**  
[**Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições - Como gerar os Tributos Genéricos da LC 224/2025 (NT 012/2026)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40783586426647-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-os-Tributos-Gen%C3%A9ricos-da-LC-224-2025-NT-012-2026)
