---
content_hash: ae36b3a717b9c94b5fc62dc9e0abf849c001e22ab91e5b7ca2ad0b943489b2ce
fetched_at: '2026-06-29T00:08:06.029424+00:00'
page_id: '236428345'
product: rm
source: tdn-rm
title: TUOATF_DT_Aviso_Automatico
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOATF_DT_Aviso_Automatico
version: 114
---

# AVISO AUTOMÁTICO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Aviso Automático* |
| **Situação/Requisito:** | - Caso possua uma tabela de cálculo sem vigência processo é executado com sucesso porém não é enviado mensagem; - Caso o Funcionário esteja para entrar de férias na data atual sistema não busca o mesmo; - Chefe externo não recebe e-mail do funcionários da seção; - Caso o Chefe possua mais de uma seção, é disparado vários e-mail ao invés de agrupar e disparar um único e-mail com quebra de linhas; - Caso opte para agrupar por seção não é informado qual a seção dos funcionários; - O processo é concluído com sucesso porém não é enviado ou possui erro; |
| **Solução/Implementação:** | \* Ajuste na rotina para exibir informação de erro ao enviar mensagem quando existir no sistema uma tabela de cálculo sem vigência \* Ajuste na rotina para buscar funcionários que estejam para entrar de férias na data atual sistema \* Ajuste na rotina para envio de e-mail para chefes externos \* Conforme alinhado, atualmente o sistema se comporta como no Delphi, e o impacto dessa melhoria é grande, por este motivo atribuímos a informação da seção para a qual agrupamento foi realizado \* Mensagem padrão (sistema) agora contem seção do funcionário. \* Existem N motivos pelos quais um e-mail não é enviado, sendo assim, o mapeamento será gradual, ou seja, conforme formos identificando. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUOATF |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.44 12.1.11* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
