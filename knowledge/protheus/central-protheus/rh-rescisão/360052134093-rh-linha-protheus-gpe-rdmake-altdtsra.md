---
article_id: 360052134093
category: RH - Rescisão
content_hash: 329b101d34daa10fdaa492b6af471b8d673e26e57251772919516af1039b95e1
fetched_at: '2026-06-28T22:43:54.380731+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - RDMAKE AltDtSRA
type: support-article
updated_at: '2025-06-16T18:30:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052134093-RH-Linha-Protheus-GPE-RDMAKE-AltDtSRA
---

**Ocorrência**RDMAKE AltDtSRA  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Ocorreu de um funcionário estar afastado, ter uma transferência entre filiais por conta de encerramento da filial, após o retorno do afastamento o funcionário foi desligado, porém a matricula da filial origem continuou ativa e os sistema não permite alterar a data de demissão no cadastro de funcionários.   
  
**Solução**Foi criado um RDMake, AltDtSRA, que deve ser compilado e adicionado ao menu do módulo SIGAGPE.  
  
Essa rotina apresenta os funcionários demitidos (RA\_SITFOLH = D) e permite alterar apenas os campos Data de Demissão (RA\_DEMISSA) e a Situação do Funcionário (RA\_SITFOLH) sem executar nenhuma validação nesses campos.  
  
**Essa rotina não envia nenhum evento para o eSocial.  
  
Atenção  
Só utilize essa rotina em caso de extrema necessidade, pois como as informações não são validadas qualquer alteração pode gerar inconsistência na base de dados.**
