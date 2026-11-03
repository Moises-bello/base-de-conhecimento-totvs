---
content_hash: bbd50f3ff29806cff93875fb68285756324e94b7b4aa7d3f59b5eb9d31e5b331
fetched_at: '2026-06-29T00:06:06.171235+00:00'
page_id: '201728892'
product: rm
source: tdn-rm
title: TTCVLU_DT_Avisos_Automaticos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCVLU_DT_Avisos_Automaticos
version: 1
---

# Avisos Automáticos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Totvs Folha de Pagamento* |
| **Função:** | *Avisos Automáticos* |
| **Situação/Requisito:** | *Erro ao enviar Avisos Automáticos agrupados por Seção* |
| **Solução/Implementação:** | Ajuste em tela para selecionar agrupamento por "Funcionário" quando forma de montagem for "Padrão (agrupamento por funcionários)" Ajuste em tela para habilitar campo "Másc. Quebra Seção" quando agrupado por Seção e desabilitar quando agrupado por outro Campos de "E-mail(s) de terceiro(s)", "Másc. Quebra Chefe" e "Másc. Quebra Seção" não são mais limpos quando desabilitado, evitando que valor anterior digitado seja perdido. Adicionado componente de validação de preenchimento obrigatório para os campos "Másc. Quebra Chefe" e "Másc. Quebra Seção" quando habilitados Retirado popup de validação de campos de "Fórmula Cabeçalho", "Fórmula Detalhe" e "Fórmula Rodapé" e incluído componente de validação tooltip com icone de exclamação para preenchimento obrigatório quando habilitado |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTCVLU* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
