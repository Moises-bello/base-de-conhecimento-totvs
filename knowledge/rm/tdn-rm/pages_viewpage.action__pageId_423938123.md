---
content_hash: 09d0ab21a3a2fdf1a73f0d47af6e1879bdacf2dc38070fc7313fd3c089edbc4e
fetched_at: '2026-06-29T00:09:25.347502+00:00'
page_id: '423938123'
product: rm
source: tdn-rm
title: Gerar DACTE em Contingência (CT-e OS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938123
version: 2
---

Caso seja necessário o envio de um CT-e OS em contingência deve-se primeiro parametrizar a filial para essa operação.   
A parametrização pode ser feita através do menu Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | acessar o caminho Integrações | Fiscal | Dados Fiscais.   
Após isso acessar o item Parâmetros por Filial e selecionar a filial que deseja configurar. Ir na aba Ambiente CT-e OS e selecionar a Modalidade de Operação como Contingência Offline FS-DA.  
Para enviar é necessário acessar a visão de CT-e OS no caminho Vendas | Faturamento | Conhecimento de Transporte - Outros Serviços (CT-e OS).   
Então, deve-se acessar Processos | Gerar DACTE em Contingência. É necessário preencher a Filial, o Tipo de Movimento, o Intervalo de Datas de Emissão e também o Intervalo de Números de Movimento que se deseja enviar.   
Após o envio, o registro será salvo com o status de Contingência.  
Esse registro deve-se ser posteriormente enviado à SEFAZ.   
Para isso, selecione o registro com status igual a Contingência e selecione Processos | Enviar CT-e. Informar a Data de Início da Contingência e a Justificativa da contingência  
Após esse Envio, o registro ficará com Status Autorizado.
