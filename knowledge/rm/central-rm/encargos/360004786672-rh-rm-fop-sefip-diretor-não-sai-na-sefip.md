---
article_id: 360004786672
category: Encargos
content_hash: e62ed029baf418d7a5792d40e7b54301d78ed78410013770581a23dd8d0eab77
fetched_at: '2026-06-28T22:46:53.416390+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Diretor não sai na SEFIP'
type: support-article
updated_at: '2025-03-12T10:04:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004786672-RH-RM-FOP-SEFIP-Diretor-n%C3%A3o-sai-na-SEFIP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:50 min****Ocorrência**Ao gerar o arquivo da Sefip e importá-lo no sistema da CEF, os diretores não estão sendo levados.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
A situação ocorre devido a parametrizações incorretas no sistema.  
  
**Solução**Este incidente possui mais de uma solução, pois se trata de parametrizações inexistentes  no ambiente. Veja abaixo:  
  
1. Quando o diretor possuir recolhimento de FGTS, ele deverá estar associado a categoria **5 - Diretor não-empregado com FGTS (empresário)**. Acesse o cadastro do diretor, aba **FGTS / SEFIP** e informe a categoria correta;  
  
2. Quando o diretor estiver parametrizado com a categoria **11 - Diretor não-empregado sem FGTS (empresário)**, ele deve estar alocado em uma seção onde constem funcionários que possuam recolhimento de FGTS ou então deve ser gerado separadamente na modalidade **1 - Declaração ao FGTS e à Previdência**;  
  
3. No evento de pagamento dos diretores deverá constar o **código de cálculo 46**. Verifique o envelope do diretor e verifique se o evento de pagamento possui este código de cálculo. Se não estiver parametrizado com este código de cálculo, altere o código de cálculo e faça a geração da Sefip. Caso não seja possível alterar o evento, cadastre novo evento com este código de cálculo e lance no envelope do diretor.
