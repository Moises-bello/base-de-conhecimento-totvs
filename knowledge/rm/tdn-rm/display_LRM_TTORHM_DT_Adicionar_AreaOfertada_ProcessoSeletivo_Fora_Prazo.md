---
content_hash: 5b20f52f3bc2ee556b64d009746ff79f06e3c07c4483bc285d8cf89f4aa4ca05
fetched_at: '2026-06-29T00:06:22.493506+00:00'
page_id: '223919778'
product: rm
source: tdn-rm
title: TTORHM_DT_Adicionar_AreaOfertada_ProcessoSeletivo_Fora_Prazo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTORHM_DT_Adicionar_AreaOfertada_ProcessoSeletivo_Fora_Prazo
version: 124
---

# CRIAR ÁREAS OFERTADAS DO PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Criar áreas ofertadas do processo seletivo* |
| **Situação/Requisito:** | *O sistema está permitindo utilizar o processo de Criar áreas ofertadas mesmo que o período de inscrição do processo seletivo não esteja mais válido, sendo que o anexo "área ofertada" não permite a criação de áreas quando a data do processo seletivo não é mais válida.* |
| **Solução/Implementação:** | *Foi verificado que ao carregar o anexo "áreas de interesse" é feita uma verificação se o período do processo seletivo é válido, sendo que isto não é feito quando é utilizado o processo de criar áreas ofertadas, foi inserido esta mesma validação ao iniciar o processo para criar áreas, assim sendo, se o processo seletivo não estiver mais válido, é exibida uma mensagem informando que não é permitido criar áreas ofertadas.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | **12.1.10** |

divs
