---
content_hash: df51079a8c9860e8edf3f16ef72547dff094997dc0996d49166860083b14d904
fetched_at: '2026-06-29T00:06:01.974072+00:00'
page_id: '198942334'
product: rm
source: tdn-rm
title: TSURUT_DT_Edicao_Historico_Curto
type: documentation
url: https://tdn.totvs.com/display/LRM/TSURUT_DT_Edicao_Historico_Curto
version: 2
---

# Histórico do Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Cópia de Mensagem para histórico do movimento/item* |
| **Situação/Requisito:** | Ao copiar várias mensagens para o histórico do movimento e clicar em salvar, o sistema exibe uma inconsistência, informando que o tamanho do texto excede o tamanho do campo na  base e fecha a tela. |
| **Solução/Implementação:** | Foi ajustada a cópia de mensagem para o histórico do movimento, o sistema permitia a cópia de mensagens onde o tamanho do texto excedia os 255 caracteres permitidos pelo  histórico curto. A partir de agora, o sistema NÃO realizará a cópia quando, o tamanho da mensagem somado a quantidade de caracteres existentes no histórico ultrapasse o limite. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.7* |
