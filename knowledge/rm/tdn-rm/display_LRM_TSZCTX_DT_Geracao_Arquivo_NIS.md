---
content_hash: 8419112705ca5d62131c387394f9d4766ed0a1f6d7f75bc7fcae53b04bf70d92
fetched_at: '2026-06-29T00:06:04.914850+00:00'
page_id: '200912707'
product: rm
source: tdn-rm
title: TSZCTX_DT_Geracao_Arquivo_NIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZCTX_DT_Geracao_Arquivo_NIS
version: 2
---

# GERAÇÃO ARQUIVO NIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Totvs Folha de Pagamento* |
| **Função:** | *Geração Arquivo NIS* |
| **Situação/Requisito:** | *Duplicidade de Registros no Arquivo NIS* |
| **Solução/Implementação:** | Deixamos de utilizar o campo CODMUNICIPIO da tabela PPESSOA por motivo de não haver5 manutenção para o mesmo. Para cada funcionário contido no arquivo será realizado um acesso à base de dados para validação de casos de Municípios de Nascimento ou Endereço do Funcionário, para o mesmo Estado com mesmo NOMEMUNICIPIO na tabela GMUNICIPIO. Para estes casos recuperamos o primeiro município da lista, ordenada pela coluna RECCREATEDON (data de criação) e gerando log de ERRO. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSZCTX* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
