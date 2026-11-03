---
content_hash: b80318282a1379f480a2be3552f3fb687cd8412e10295e5cf10d38e733c2ff41
fetched_at: '2026-06-29T00:09:04.199352+00:00'
page_id: '382559771'
product: rm
source: tdn-rm
title: 3295069 MATESTCNTFTOF01-2853 DT Ajuste no adapter da mensagem Busca Status
  de Solicitação de Compra/Solicitação de Armazém
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382559771
version: 86
---

# CONSULTA STATUS SOLICITAÇÃO DE COMPRA/ARMAZÉM - TRACEABILITYREQUEST\_1.001

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Processos de OS. |
| **Situação/Requisito:** | Ao incluir ou excluir um insumo de uma OS (Ordem de Serviço) no Protheus é apresentada a mensagem informando:  **A cadeia de caracteres de entrada não estava em um formato incorreto.**  A mensagem acima é apresentada pois está sendo enviado na mensagem TraceAbilityRequest um InternalId que já foi excluído da Tabela De-Para de integração. Com isso ao buscar por uma chave inexistente, a mensagem de inconsistência acima é apresentada.  A ocorrência em questão pode ser observada quando o parâmetro MV\_NGMNTAS, Definição de Aglutinação, possui o valor: (2-Não). |
| **Solução/Implementação:** | Realizado o ajuste na mensagem a ser apresentada ao usuário.  A partir de agora, quando não for encontrado o InternalId do movimento que está sendo consultado, a mensagem abaixo será apresentada:  **Não foi encontrado Movimento relacionado ao InternalId XXXX.**  Onde XXXX é a chave que compõem o movimento na integração. |
| **Conversores e Parâmetros:** | Para atualizar o adapter no RM realize os seguintes passos:   1. Acesse RM \ Integração \ Integração \ Mensagem Única \ Integrações. Selecione a integração de Identificador 1001 e abra o Anexo Mapeamento de Entidades. Edite o registro TRACEABILITYREQUEST. Acesse o link do evento e clique em excluir. 2. No anexo Mapeamento de Entidades exclua o registro TRACEABILITYREQUEST. 3. Acesse Integração | Mensagem Única | Transformação. Apagar o item de Transformação para o registro TRACEABILITYREQUEST. 4. Acesse Ferramentas \ Configurar, avance até a etapa Projetos de Integração. Selecione o item **TOTVS Manutenção de Ativos x BackOffice RM** e execute o processo para atualizar o adapter TRACEABILITYREQUEST. |
| **Tickets relacionados:** | 3295069. |
| **Requisito:** | Integração Manutenção de Ativos x BackOffice RM. |

divs
