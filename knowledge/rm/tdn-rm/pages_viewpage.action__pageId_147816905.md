---
content_hash: 57829cd8aec3e7c0a2228ae43f1d5e36ba49b154abd5f708a1d415a35c6123f6
fetched_at: '2026-06-29T00:05:55.921282+00:00'
page_id: '147816905'
product: rm
source: tdn-rm
title: 'Erro na importação de Eventos: Atenção! O número de colunas do arquivo (78)
  é menor que o número de campos da tabela (79)'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=147816905
version: 1
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | Erro na importação de Eventos (Importações -> Importação de dados do RM Labore)  Linha <1> Erro ao realizar importação de Eventos:  Atenção! O número de colunas do arquivo (78) é menor que o número de campos da tabela (79)   Linha <2> Erro ao realizar importação de Eventos:  Atenção! O número de colunas do arquivo (78) é menor que o número de campos da tabela (79) |
| Solução | Devido ao eSocial foi implementado mais um campo no arquivo de importação , porém, esta informação não está no help do sistema, a mesma está sendo implementada através do chamado TPYJLS     Para que o erro não seja apresentado, altere o layout. Será necessário incluir novo campo no layout referente ao eSocial:      DESCRIÇÃO: Inativo (1 – Sim / 0 - Não)     TIPO : Inteiro    TAMANHO: 1    CAMPO: 79       OBS: Cada ponto e vírgula do arquivo representa um campo. |
