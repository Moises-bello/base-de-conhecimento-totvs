---
content_hash: bbad84ffbad429e435e349afb607289a918266dac09d789982c21d680797d712
fetched_at: '2026-06-29T00:06:04.996284+00:00'
page_id: '200913066'
product: rm
source: tdn-rm
title: TTBPRN_DT_Geracao_Arquivo_NIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBPRN_DT_Geracao_Arquivo_NIS
version: 2
---

# GERAÇÃO ARQUIVO NIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Geração Arquivo NIS* |
| **Situação/Requisito:** | *Duplicidade de Registros no Arquivo NIS* |
| **Solução/Implementação:** | Deixamos de utilizar o campo CODMUNICIPIO da tabela PPESSOA por motivo de não haver manutenção para o mesmo.  Para cada funcionário contido no arquivo será realizado um acesso à base de dados para validação de casos de Municípios de Nascimento ou Endereço do Funcionário, para o mesmo Estado com mesmo NOMEMUNICIPIO na tabela GMUNICIPIO. Para estes casos recuperamos o primeiro município da lista, ordenada pela coluna RECCREATEDON (data de criação) e gerando log de ERRO. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTBPRN* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
