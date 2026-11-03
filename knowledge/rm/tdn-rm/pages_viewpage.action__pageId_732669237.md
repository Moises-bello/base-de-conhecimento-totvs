---
content_hash: 04a4ac64e071b1735e159750e97d71882df9b50a8d6ed10c791c008fd31ac9e7
fetched_at: '2026-06-29T00:11:28.608488+00:00'
page_id: '732669237'
product: rm
source: tdn-rm
title: 'Bloco I: Lançamentos Contábeis'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=732669237
version: 10
---

Página em construção.

I001: Abertura do Bloco I

O registro I001 abre o bloco I e indica se há ou não há dados informados no bloco.  
- Gerado automaticamente pelo sistema.

I010: Identificação da Escrituração Contábil

Registro que identifica a escrituração contábil do arquivo.

### Origem dos Dados

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | IND\_ESC | Indicador da forma de escrituração contábil: G - Livro Diário (Completo sem escrituração auxiliar). R - Livro Diário com Escrituração Resumida (com escrituração auxiliar). A - Livro Diário Auxiliar ao Diário com Escrituração Resumida. B - Livro Balancetes Diários e Balanços. Z – Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555). |
| 03 | COD\_VER\_LC | Código da Versão do Leiaute Contábil. Clique para expandir |

I012: Livros Auxiliares ao Diário ou Livro PrincipalI015: Identificação das Contas da Escrituração Resumida a que se Refere a Escrituração AuxiliarI020: Campos AdicionaisI030: Termo de Abertura do LivroI050: Plano de ContasI051: Plano de Contas ReferencialI052: Indicação dos Códigos de AglutinaçãoI053: Subcontas CorrelatasI075: Tabela de Histórico PadronizadoI100: Centro de CustosI150: Saldos Periódicos – Identificação do PeríodoI155: Detalhe dos Saldos PeriódicosI157: Transferência de Saldos de Plano de Contas AnteriorI200: Lançamento ContábilI250: Partidas do LançamentoI300: Balancetes Diários – Identificação da DataI310: Detalhes do Balancete DiárioI350: Saldo das Contas de Resultado Antes do Encerramento – Identificação da DataI355: Detalhes dos Saldos das Contas de Resultado Antes do EncerramentoI500: Parâmetros de Impressão e Visualização do Razão Auxiliar com Leiaute ParametrizávelI510: Definição de Campos do Livro Razão Auxiliar com Leiaute ParametrizávelI550: Detalhes do Livro Razão Auxiliar com Leiaute ParametrizávelI555: Totais no Livro Razão Auxiliar com Leiaute ParametrizávelI990: Encerramento do Bloco I

O registro I990 encerra o bloco I e indica o total de linhas do bloco I. O registro I990 também é considerado no total de linhas do bloco I.  
-Gerado automaticamente pelo sistema.
