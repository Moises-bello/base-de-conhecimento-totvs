---
content_hash: 3ff13e3b94ac35db4637d8e81b655b927d466408d1279eba855a821babfbe9b0
fetched_at: '2026-06-29T00:06:08.594194+00:00'
page_id: '201750582'
product: rm
source: tdn-rm
title: TTASTH_DT_Configuracao_Ambiente
type: documentation
url: https://tdn.totvs.com/display/LRM/TTASTH_DT_Configuracao_Ambiente
version: 1
---

# Comparativo Sefip e folha analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamentoi* |
| **Função:** | *Comparativo Sefip folha analítica* |
| **Situação/Requisito:** | Realizando a validação da 12.1.6, no cliente JBS, ocorre erro ao tentar rodar o comparativo de Sefip com Folha Analitica. Mensagem de arquivo não encontrado  Estamos em 3 camadas |
| **Solução/Implementação:** | Configuramos uma pasta no servidor de JOBS, compartilhamos a mesma para todas as pessoas. Incluímos a TAG "FILESERVERPATH" nos arquivos de configuração dos servidores de APP e de JOBS, informamos o caminho da pasta compartilhada ("\\MTZSVMRHJOB1H\relatorios") no parametrizador do labore.    Após estas configurações as rotinas passaram a funcionar corretamente    A tag inserida foi a:  <add key="FileServerPath" value="\\MTZSVMRHJOB1H\relatorios" /> |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTASTH |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
