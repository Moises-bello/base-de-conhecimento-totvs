---
content_hash: a770f2aafbb31bf816076a57970f0821d96f4fd836d1f59555f8e5f581abe079
fetched_at: '2026-06-29T00:09:10.038459+00:00'
page_id: '396371919'
product: rm
source: tdn-rm
title: 3470175 FISCAL01-6148 DT Livro Eletrônico Ato Cotepe - Performance
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=396371919
version: 3
---

# Rotina Estadual Livro Eletrônico

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Rotina Estadual Livro Eletrônico |
| **Situação/Requisito:** | O cliente relatou que está demorando em torno de 5 horas para geração da rotina Livro Eletrônico (Ato Cotepe) e que a rotina deve ser otimizada para geração em menor tempo. |
| **Solução/Implementação:** | Ao gerar a rotina Livro Eletrônico (Ato Cotepe) será criado o arquivo "LRAtoCotepeLog.txt" neste arquivo será detalhado o tempo da Inicialização da Rotina e de cada Bloco 0, A, B, C, D, E e 9.  Os registros “0200, 0220, A300, A310, C550, C555 e E320” sofreram otimização onde cada linha com informações do registro será mantido em memória e no fim do processamento será persistido no arquivo final "LIVRO.TXT".  Nos registros C020, E020, E050 não foi necessário implementar está otimização proposta.  No registro E300, o filho E320 é o registro que sofreu otimização na sua geração, onde foi retirada condição que foi processada com menor custo na Inicialização da Rotina.  Como foi avaliação de performance da rotina: Foi gerado a rotina Livro Eletrônico (Ato Cotepe) no período 06/2018, marcando os registros C020, C550, E020, E050 e E300 na base de dados disponibilizada pelo cliente com a implementação do LOG, Antes e Depois da otimização.  Tempo que a rotina foi executada: A rotina sem otimização foi executada no tempo aproximado a 185 minutos e após a otimização passou a ser executada completamente em 145 minutos.  Foi percebido uma redução no tempo de geração da rotina de 21,6%, ou seja, 40 minutos.    Em uma segunda analise os registros A300, A310, B030 e B035 também foram otimizados através da Issue: FISCAL01-6542. |
| **Requisito:** | FIS000247 |
