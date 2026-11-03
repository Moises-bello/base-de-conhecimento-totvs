---
content_hash: 203e7d546d103dc6df402412db9942605d60594627a6c87a91e36c0c550c23c7
fetched_at: '2026-06-29T00:06:15.625021+00:00'
page_id: '211059547'
product: rm
source: tdn-rm
title: TTOATX_DT_Atitude_da_Ocorrencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOATX_DT_Atitude_da_Ocorrencia
version: 6
---

# GERAR OCORRÊNCIA MODIFICADA NA ALTERAÇÃO DE ATITUDE DA OCORRÊNCIA COLETADA NO PORTAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Alteração de atitude da ocorrência.* | **Gerar ocorrência modificada na alteração de atitude da ocorrência no portal.** | |
| **Cadastros Iniciais:** | *Acessar a tela de subordinado do portal | Anexos | Alterar Atitude das Ocorrências.* |
| **Parâmetro(s):** | ***Gerar ocorrência modificada na alteração de atitude da ocorrência no portal.*** |
| **Chamados Relacionados** | *TTOATX* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *PPARAMQUIOSQUE, PGRPACESSOQUIOSQUE* |
| **Versões/Release:** | *12.1.8* |

## Descrição

Melhoria de usabilidade na tela de alteração de atitude Web e Parametrizador:

* Criar um novo parâmetro para gerar uma ocorrência modificada correspondente ao valor da ocorrência coletada que está sendo alterada (Parametrizador – RM Portal):  
  Será inserido dentro dos parâmetros iniciais do sistema a opção “Gerar ocorrência modificada na alteração de atitude da ocorrência coletada” que tem como objetivo modificar o comportamento atual da alteração de atitude da ocorrência de forma que uma vez modificada passe sempre a ser considerada.
* Modificar a atitude de uma ocorrência coletada, será gerado uma  correspondente ao valor da alteração da atitude: Com o parâmetro “Gerar ocorrência modificada na alteração de atitude da ocorrência coletada” marcado, o sistema além  de processar a alteração da ocorrência desejada, vai gerar também um registro de modificação de ocorrências correspondente a alteração de atitude do evento.

  Exemplo:

  Ocorrências coletadas:

  Dia 01/01: 00:10 Extras [12:00 12:10] - Compensar

   Ocorrências modificadas: Nenhuma

   Ao executar a alteração de atitude da ocorrência coletada, o sistema vai proceder da seguinte forma:

  Ocorrências coletadas:

  Dia 01/01: 00:10 Extras [12:00 12:10] – Pagar

  Modificações de ocorrência:

  Dia 01/01: 00:10 Extras [12:00 12:10] – Pagar

  Será incluído automaticamente a ocorrência modificada na alteração de atitude com os valores iguais ao da alteração. Dessa forma o cálculo vai passar a interpretar essas alterações de uma forma diferente pois vai considerar as ocorrências modificadas no processamento.
* Considerações do cálculo quando houver essas ocorrências modificadas: Será considerado o novo comportamento do cálculo conforme a especificação abaixo:

  [Modificação de Ocorrências](https://tdn.totvs.com/pages/viewpage.action?pageId=452719212).

## Procedimento para Configuração

*(Estes procedimentos devem ser feitos quando for necessário configurar parâmetros e/ou  rotinas no menu).*

**CONFIGURAÇÃO DE PARÂMETROS**

1. No parametrizador do RM.exe, acessar a opção de parâmetros do portal, selecionar o grupo desejado e marcar o parâmetro "Gerar ocorrência modificada na alteração de atitude da ocorrência coletada".
