---
article_id: 19401835302423
category: RH - Soluções para error.log
content_hash: e3ab6b40979d2068a9a93dbb44c02df3e604be984794d0b7551c4cd7d63dc81b
fetched_at: '2026-06-28T22:44:08.939422+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error.log no campo Vara na rotina Processos Opção
  Não disponível no Protheus Função: APT100VARAFILTROCalled By {(Apt100VaraFiltro()
  )}'
type: support-article
updated_at: '2023-11-29T17:06:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19401835302423-RH-Linha-Protheus-GPE-Error-log-no-campo-Vara-na-rotina-Processos-Op%C3%A7%C3%A3o-N%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-APT100VARAFILTROCalled-By-Apt100VaraFiltro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19401844789399) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao clicar no campo Vara na rotina de Processos, sistema gera o error.log Opção Não disponível no Protheus Função: APT100VARAFILTROCalled By {(Apt100VaraFiltro() )}  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19401807472023)  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Filtro errado na consulta padrão RE1.  
  
**Solução**Ajuste a consulta padrão RE1 conforme abaixo, deixando o Filtro vazio:  
No Configurador acesse **>Base de dados >Dicionário >Base de dados >Consulta padrão**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19401815342103)
