---
content_hash: 02727dc034644b27c7320e10925ee985240445215ebeafe251e7f44ee667735b
fetched_at: '2026-06-29T00:06:18.384789+00:00'
page_id: '215484427'
product: rm
source: tdn-rm
title: TTPZTK_DT_ERRO_Candidato_Sem_Permissao_Executor_Web
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPZTK_DT_ERRO_Candidato_Sem_Permissao_Executor_Web
version: 1
---

# EXECUTOR WEB

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Avaliação e Pesquisa* |
| **Função:** | *Executor Web* |
| **Situação/Requisito:** | *Ao iniciar a execução de um avaliação, o sistema está retornando que não havia avaliações para execução.*  *Este erro ocorre, porque o perfil do candidato não possuía permissão nas classificações da avaliação.* |
| **Solução/Implementação:** | *Foi incluído uma validação para verificar a origem da chamada ao método responsável pelo carregamento das informações da avaliação.*  *Esta validação verifica se esta chamada é o Executor Web, e caso positivo, não irá realizar a verificação das permissões nas classificações da avaliação.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *Versão na qual está sendo feita a manutenção deste programa.* |
| **Versão Expedida:** | *Versão em que o programa será oficialmente expedido.* |

divs
